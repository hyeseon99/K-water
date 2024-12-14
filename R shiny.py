if (!require("shiny")) install.packages("shiny")
if (!require("shinydashboard")) install.packages("shinydashboard")
if (!require("shinythemes")) install.packages("shinythemes")
if (!require("leaflet")) install.packages("leaflet")
if (!require("dplyr")) install.packages("dplyr")
if (!require("plotly")) install.packages("plotly")
if (!require("randomForest")) install.packages("randomForest")
if (!require("caret")) install.packages("caret")
if (!require("DT")) install.packages("DT")
if (!require("here")) install.packages("here")

# 필요한 라이브러리 불러오기
library(shiny)
library(shinydashboard)
library(shinythemes)
library(leaflet)
library(dplyr)
library(plotly)
library(randomForest)
library(caret)
library(tidyr)
library(DT)
library(here)

# 현재 디렉토리 설정
current_dir <- here::here()

# 댐 데이터 불러오기
dam_data <- read.csv(file.path(current_dir, "data", "dam_loc.csv"), header = TRUE, stringsAsFactors = FALSE, fileEncoding = 'euc-kr')

# SPI 데이터 불러오기 및 전처리
spi <- read.csv(file.path(current_dir, "data", "spi유효.csv"), header = TRUE, stringsAsFactors = TRUE, fileEncoding = 'euc-kr')
spi <- na.omit(spi)
spi <- spi[,-c(6,7)]

# 훈련 및 테스트 데이터 분할
set.seed(24)
train_indx <- createDataPartition(spi$가뭄, p = 0.9, list = FALSE)
spi_train <- spi[train_indx, ]
spi_test <- spi[-train_indx, ]

# 정규화 및 표준화 함수
normalize <- function(x, min_x, max_x) {
  return ((x - min_x) / (max_x - min_x))
}

standard <- function(x, mean_x, sd_x) {
  return ((x - mean_x) / sd_x)
}

# 훈련 데이터 통계
train_min_가조시간 <- min(spi_train$가조시간)
train_max_가조시간 <- max(spi_train$가조시간)
train_min_평균기온 <- min(spi_train$평균기온)
train_max_평균기온 <- max(spi_train$평균기온)
train_mean_저수량 <- mean(spi_train$저수량)
train_sd_저수량 <- sd(spi_train$저수량)
train_mean_누적강수량 <- mean(spi_train$누적강수량)
train_sd_누적강수량 <- sd(spi_train$누적강수량)
train_mean_유효저수량 <- mean(spi_train$유효저수량)
train_sd_유효저수량 <- sd(spi_train$유효저수량)

# 훈련 데이터 정규화 및 표준화
spi_train$가조시간 <- normalize(spi_train$가조시간, train_min_가조시간, train_max_가조시간)
spi_train$평균기온 <- normalize(spi_train$평균기온, train_min_평균기온, train_max_평균기온)
spi_train$저수량 <- standard(spi_train$저수량, train_mean_저수량, train_sd_저수량)
spi_train$누적강수량 <- standard(spi_train$누적강수량, train_mean_누적강수량, train_sd_누적강수량)

# 테스트 데이터 정규화 및 표준화
spi_test$가조시간 <- normalize(spi_test$가조시간, train_min_가조시간, train_max_가조시간)
spi_test$평균기온 <- normalize(spi_test$평균기온, train_min_평균기온, train_max_평균기온)
spi_test$저수량 <- standard(spi_test$저수량, train_mean_저수량, train_sd_저수량)
spi_test$누적강수량 <- standard(spi_test$누적강수량, train_mean_누적강수량, train_sd_누적강수량)


# 랜덤 포레스트 모델 훈련
rf_model <- randomForest(가뭄 ~ ., data = spi_train, ntree = 97)

# UI 정의
ui <- dashboardPage(
  skin = "black",
  dashboardHeader(title = "SPI Dashboard"),
  dashboardSidebar(
    sidebarMenu(
      menuItem("SPI 예측", tabName = "dam_info", icon = icon("tint")),
      selectInput("region", "유역 선택", choices = c("전체", unique(dam_data$유역))),
      uiOutput("dam_ui"),
      sliderInput("accum_precip", "누적강수량", min = 70, max = 2149, value = 70),
      sliderInput("precip_time", "가조시간", min = 9, max = 16, value = 9),
      sliderInput("storage", "저수량", min = 0, max = 3000, value = 0),
      sliderInput("avg_standard", "평균기온", min = -20, max = 35, value = -20),
      numericInput("eff_storage", "유효저수량", value = 0, min = 0, max = 5000, step = 1),
      actionButton("predict_btn", "예측하기", class = "btn btn-primary")
    )
  ),
  dashboardBody(
    fluidRow(
      valueBoxOutput("dam_eff_storage"),
      valueBoxOutput("dam_total_storage"),
      valueBoxOutput("dam_height")
    ),
    fluidRow(
      box(width = 6, leafletOutput("map")),
      box(width = 6,
          plotlyOutput("predictionPlot"),
          box(
            title = "예측된 가뭄 상태",
            status = "primary",
            solidHeader = TRUE,
            textOutput("prediction_result"),
            collapsible = TRUE,
            width = 12
          ),
          dataTableOutput("spi_table")
      )
    )
  )
)

# 서버 로직 정의
server <- function(input, output, session) {
  
  # 유역 선택에 따른 댐 목록 업데이트
  output$dam_ui <- renderUI({
    dams <- if (input$region == "전체") {
      unique(dam_data$name)
    } else {
      unique(dam_data$name[dam_data$유역 == input$region])
    }
    selectInput("dam", "댐 선택", choices = c("전체", dams))
  })
  
  # 선택된 댐의 정보 표시 및 유효저수량 고정
  output$dam_eff_storage <- renderValueBox({
    dam_info <- dam_data %>% filter(name == input$dam)
    valueBox(dam_info$유효저수량, "유효저수량 (톤)", icon = icon("tint", lib = "font-awesome", style = "font-size: 24px;"), color = "blue")
  })
  
  output$dam_total_storage <- renderValueBox({
    dam_info <- dam_data %>% filter(name == input$dam)
    valueBox(dam_info$총저수용량, "총저수용량 (톤)", icon = icon("database", lib = "font-awesome", style = "font-size: 24px;"), color = "green")
  })
  
  output$dam_height <- renderValueBox({
    dam_info <- dam_data %>% filter(name == input$dam)
    valueBox(dam_info$높이, "높이 (m)", icon = icon("arrows-alt-v", lib = "font-awesome", style = "font-size: 24px;"), color = "orange")
  })
  
  # 지도 렌더링
  output$map <- renderLeaflet({
    leaflet() %>%
      addTiles()
  })
  # 지도 업데이트 및 마커 추가
  observe({
    req(input$region, input$dam)
    
    if (input$region == "전체" && input$dam == "전체") {
      leafletProxy("map") %>%
        clearMarkers() %>%
        addMarkers(data = dam_data, ~경도, ~위도, 
                   popup = ~paste(name, "<br>", "유역:", 유역, "<br>", "유효저수량:", 유효저수량, "톤", "<br>", "총저수용량:", 총저수용량, "톤", "<br>", "높이:", 높이, "m")) %>%
        setView(lng = 127.8, lat = 35.8, zoom = 7)
    } else if (input$region != "전체" && input$dam == "전체") {
      region_data <- dam_data %>% filter(유역 == input$region)
      leafletProxy("map") %>%
        clearMarkers() %>%
        addMarkers(data = region_data, ~경도, ~위도, 
                   popup = ~paste(name, "<br>", "유역:", 유역, "<br>", "유효저수량:", 유효저수량, "톤", "<br>", "총저용량:", 총저수용량, "톤", "<br>", "높이:", 높이, "m")) %>%
        setView(lng = mean(region_data$경도), lat = mean(region_data$위도), zoom = 8)
    } else if (input$dam != "전체") {
      dam_info <- dam_data %>% filter(name == input$dam)
      if (nrow(dam_info) > 0) {
        lat <- dam_info$위도
        lng <- dam_info$경도
        updateNumericInput(session, "eff_storage", value = dam_info$유효저수량, max = 5000)  # 유효저수량 자동 설정
        leafletProxy("map") %>%
          setView(lng = lng, lat = lat, zoom = 12) %>%
          clearMarkers() %>%
          addMarkers(lng = lng, lat = lat, popup = paste(dam_info$name, "<br>", "유역:", dam_info$유역, "<br>", "유효저수량:", dam_info$유효저수량, "톤", "<br>", "총저수용량:", dam_info$총저수용량, "톤", "<br>", "높이:", dam_info$높이, "m"))
      }
    }
  })
  
  observeEvent(input$predict_btn, {
    # 유효저수량은 선택된 댐에 따라 자동 설정됨
    eff_storage_value <- input$eff_storage
    
    # Normalize and standardize input data
    norm_precip_time <- normalize(input$precip_time, train_min_가조시간, train_max_가조시간)
    norm_avg_standard <- normalize(input$avg_standard, train_min_평균기온, train_max_평균기온)
    std_storage <- standard(input$storage, train_mean_저수량, train_sd_저수량)
    std_accum_precip <- standard(input$accum_precip, train_mean_누적강수량, train_sd_누적강수량)
    std_eff_storage <- standard(eff_storage_value, train_mean_유효저수량, train_sd_유효저수량)
    
    # Create a new data frame for prediction
    new_data <- data.frame(
      가조시간 = norm_precip_time,
      평균기온 = norm_avg_standard,
      저수량 = std_storage,
      누적강수량 = std_accum_precip,
      유효저수량 = std_eff_storage
    )
    
    # Make prediction
    prediction <- predict(rf_model, new_data, type = 'prob')
    
    # Convert results to dataframe
    result_df <- as.data.frame(t(prediction))
    result_df$Category <- rownames(result_df)
    colnames(result_df)[1] <- "Probability"
    
    # Create bar plot with highlight effect
    output$predictionPlot <- renderPlotly({
      plot_ly(result_df, x = ~Category, y = ~Probability, type = 'bar', 
              marker = list(color = 'rgba(158,202,225,0.8)', # 색깔 변경
                            line = list(color = 'rgba(8,48,107,1.0)', width = 1.5))) %>%
        layout(title = "Prediction Probabilities",
               xaxis = list(title = "Category"),
               yaxis = list(title = "Probability")) %>%
        config(displayModeBar = FALSE) %>%  # Hide mode bar for cleaner look
        highlight("plotly_hover", opacityDim = 0.6) %>%
        highlight("plotly_click", selected = attrs_selected(marker = list(color = 'rgba(255,127,14,1.0)', opacity = 0.8)))
    })
    
    output$prediction_result <- renderText({
      pred_class <- rownames(result_df)[which.max(result_df$Probability)]
      paste("예측된 가뭄 상태: ", pred_class)
    })
  })
  # SPI6 기준표 출력
  output$spi_table <- renderDataTable({
    datatable(data.frame(
      상태 = c("심한 습윤", "보통 습윤", "정상", "약한 가뭄", "보통 가뭄", "심한 가뭄"),
      기준 = c("SPI6 > 1.5", "1.5 > SPI6 > 1", "1 > SPI6 > -1", "-1 > SPI6 > -1.5", "-1.5 > SPI6 > -2", "SPI6 < -2")
    ), options = list(dom = 't', paging = FALSE, searching = FALSE, ordering = FALSE))
  })
}

# Run the application 
shinyApp(ui = ui, server = server, options = list(port = 8080))

