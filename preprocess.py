--1. 년도별 용수댐 통합 코드(저수량, 강우량, 방류량)
create table dam2
as
select * from dam2_2018
union all
select * from dam2_2019
union all
select * from dam2_2020
union all
select * from dam2_2021
union all
select * from dam2_2022;



--2. 년도별 다목적댐 통합 코드(저수량, 강우량, 방류량)
create table dam1
as
select * from dam1_2018
union all
select * from dam1_2019
union all
select * from dam1_2020
union all
select * from dam1_2021
union all
select * from dam1_2022;

3. 용수댐의 컬럼 추가 코드
alter table dam1
add 광동 number(10,5);
alter table dam1
add 달방 number(10,5);
alter table dam1
add 영천 number(10,5);
alter table dam1
add 안계 number(10,5);
alter table dam1
add 감포 number(10,5);
alter table dam1
add 운문 number(10,5);
alter table dam1
add 대곡 number(10,5);
alter table dam1
add 사연 number(10,5);
alter table dam1
add 대암 number(10,5);
alter table dam1
add 선암 number(10,5);
alter table dam1
add 연초 number(10,5);
alter table dam1
add 구천 number(10,5);
alter table dam1
add 수어 number(10,5);
alter table dam1
add 평림 number(10,5);




--4. 용수댐 데이터 추가 코드
merge into dam1 d1
using dam2 d2
on (d1.일시 = d2.일시)
when matched then
update set d1.광동 = d2.광동;
merge into dam1 d1
using dam2 d2
on (d1.일시 = d2.일시)
when matched then
update set d1.달방 = d2.달방;
merge into dam1 d1
using dam2 d2
on (d1.일시 = d2.일시)
when matched then
update set d1.영천 = d2.영천;
merge into dam1 d1
using dam2 d2
on (d1.일시 = d2.일시)
when matched then
update set d1.안계 = d2.안계;
merge into dam1 d1
using dam2 d2
on (d1.일시 = d2.일시)
when matched then
update set d1.감포 = d2.감포;
merge into dam1 d1
using dam2 d2
on (d1.일시 = d2.일시)
when matched then
update set d1.운문 = d2.운문;
merge into dam1 d1
using dam2 d2
on (d1.일시 = d2.일시)
when matched then
update set d1.대곡 = d2.대곡;
merge into dam1 d1
using dam2 d2
on (d1.일시 = d2.일시)
when matched then
update set d1.사연 = d2.사연;
merge into dam1 d1
using dam2 d2
on (d1.일시 = d2.일시)
when matched then
update set d1.대암 = d2.대암;
merge into dam1 d1
using dam2 d2
on (d1.일시 = d2.일시)
when matched then
update set d1.선암 = d2.선암;
merge into dam1 d1
using dam2 d2
on (d1.일시 = d2.일시)
when matched then
update set d1.연초 = d2.연초;
merge into dam1 d1
using dam2 d2
on (d1.일시 = d2.일시)
when matched then
update set d1.구천 = d2.구천;
merge into dam1 d1
using dam2 d2
on (d1.일시 = d2.일시)
when matched then
update set d1.수어 = d2.수어;
merge into dam1 d1
using dam2 d2
on (d1.일시 = d2.일시)
when matched then
update set d1.평림 = d2.평림;




--5. 댐 통합 코드
create table dam11
as
select * from dam1
unpivot (저수량 for 댐 in (소양강, 충주,횡성,안동,임하,합천,남강,밀양,군위,김천부항,
                        영주,성덕,보현산,용담,대청,섬진강,주암본,주암조,보령,장흥,
                        광동,달방,영천,안계,감포,운문,대곡,사연,대암,선암,연초,구천,
                        수어,평림,부안) );
                        
select * from dam11;
              



--6. 강 유역 추가 코드                        
alter table dam11
    add 강 varchar2(100);
    


--7. 강 데이터 추가 코드    
update dam11
    set 강 = '한강'
    where 댐 in ('소양강','충주','횡성','광동','달방');

update dam11
    set 강 = '금강'
    where 댐 in ('용담','대청','보령');

update dam11
    set 강 = '낙동강'
    where 댐 in ('안동','임하','합천','남강','밀양','군위','김천부항','영주','성덕','보현산',
                '영천','안계','감포','운문','대곡','사연','대암','선암','연초','구천');

update dam11
    set 강 = '영섬'
    where 댐 in ('섬진강','주암본','주암조','장흥','수어','평림','부안');
    
    



--8. 합계 삭제 코드    
alter table dam11
drop column 계;







--9. 유효저수량 컬럼 추가 코드
alter table dam11
    add 유효저수량 number(10,2);
    





--10. 유효저수량 데이터 추가 코드    
update dam11
    set 유효저수량 = 1900
    where 댐 = '소양강';
update dam11
    set 유효저수량 = 1789
    where 댐 = '충주';
update dam11
    set 유효저수량 = 73.4
    where 댐 = '횡성';
update dam11
    set 유효저수량 = 1000
    where 댐 = '안동';
update dam11
    set 유효저수량 = 424
    where 댐 = '임하';
update dam11
    set 유효저수량 = 560
    where 댐 = '합천';
update dam11
    set 유효저수량 = 299.7
    where 댐 = '남강';
update dam11
    set 유효저수량 = 69.8
    where 댐 = '밀양';
update dam11
    set 유효저수량 = 40.1
    where 댐 = '군위';
update dam11
    set 유효저수량 = 42.6
    where 댐 = '김천부항';
update dam11
    set 유효저수량 = 138
    where 댐 = '영주';
update dam11
    set 유효저수량 = 24.8
    where 댐 = '성덕';
update dam11
    set 유효저수량 = 17.9
    where 댐 = '보현산';
update dam11
    set 유효저수량 = 672.5
    where 댐 = '용담';
update dam11
    set 유효저수량 = 790
    where 댐 = '대청';
update dam11
    set 유효저수량 = 429
    where 댐 = '섬진강';
update dam11
    set 유효저수량 = 352
    where 댐 = '주암본';
update dam11
    set 유효저수량 = 210
    where 댐 = '주암조';
update dam11
    set 유효저수량 = 108.7
    where 댐 = '보령';
update dam11
    set 유효저수량 = 171
    where 댐 = '장흥';
update dam11
    set 유효저수량 = 8
    where 댐 = '광동';
update dam11
    set 유효저수량 = 7.5
    where 댐 = '달방';
update dam11
    set 유효저수량 = 81.4
    where 댐 = '영천';
update dam11
    set 유효저수량 = 13
    where 댐 = '안계';
update dam11
    set 유효저수량 = 2.2
    where 댐 = '감포';
update dam11
    set 유효저수량 = 126.2
    where 댐 = '운문';
update dam11
    set 유효저수량 = 27.8
    where 댐 = '대곡';
update dam11
    set 유효저수량 = 20
    where 댐 = '사연';
update dam11
    set 유효저수량 = 5
    where 댐 = '대암';
update dam11
    set 유효저수량 = 1.5
    where 댐 = '선암';
update dam11
    set 유효저수량 = 4.6
    where 댐 = '연초';
update dam11
    set 유효저수량 = 9.3
    where 댐 = '구천';
update dam11
    set 유효저수량 = 22.2
    where 댐 = '수어';
update dam11
    set 유효저수량 = 8.1
    where 댐 = '평림';
update dam11
    set 유효저수량 = 35.6
    where 댐 = '부안';
    
    




--11. 총저수량 컬럼 추가 코드
alter table dam11
    add 총저수량 number(10,2);





--12. 총저수량 데이터 추가 코드    
update dam11
    set 총저수량 = 2900
    where 댐 = '소양강';
update dam11
    set 총저수량 = 2750
    where 댐 = '충주';
update dam11
    set 총저수량 = 86.9
    where 댐 = '횡성';
update dam11
    set 총저수량 = 1248
    where 댐 = '안동';
update dam11
    set 총저수량 = 595
    where 댐 = '임하';
update dam11
    set 총저수량 = 790
    where 댐 = '합천';
update dam11
    set 총저수량 = 309.2
    where 댐 = '남강';
update dam11
    set 총저수량 = 73.6
    where 댐 = '밀양';
update dam11
    set 총저수량 = 48.7
    where 댐 = '군위';
update dam11
    set 총저수량 = 54.3
    where 댐 = '김천부항';
update dam11
    set 총저수량 = 181.1
    where 댐 = '영주';
update dam11
    set 총저수량 = 27.9
    where 댐 = '성덕';
update dam11
    set 총저수량 = 22.11
    where 댐 = '보현산';
update dam11
    set 총저수량 = 815
    where 댐 = '용담';
update dam11
    set 총저수량 = 1490
    where 댐 = '대청';
update dam11
    set 총저수량 = 466
    where 댐 = '섬진강';
update dam11
    set 총저수량 = 457
    where 댐 = '주암본';
update dam11
    set 총저수량 = 250
    where 댐 = '주암조';
update dam11
    set 총저수량 = 116.9
    where 댐 = '보령';
update dam11
    set 총저수량 = 191
    where 댐 = '장흥';
update dam11
    set 총저수량 = 13.13
    where 댐 = '광동';
update dam11
    set 총저수량 = 8.75
    where 댐 = '달방';
update dam11
    set 총저수량 = 103.21
    where 댐 = '영천';
update dam11
    set 총저수량 = 18.46
    where 댐 = '안계';
update dam11
    set 총저수량 = 2.64
    where 댐 = '감포';
update dam11
    set 총저수량 = 160.25
    where 댐 = '운문';
update dam11
    set 총저수량 = 36.16
    where 댐 = '대곡';
update dam11
    set 총저수량 = 30.34
    where 댐 = '사연';
update dam11
    set 총저수량 = 13.14
    where 댐 = '대암';
update dam11
    set 총저수량 = 2.02
    where 댐 = '선암';
update dam11
    set 총저수량 = 5.22
    where 댐 = '연초';
update dam11
    set 총저수량 = 10.02
    where 댐 = '구천';
update dam11
    set 총저수량 = 31.27
    where 댐 = '수어';
update dam11
    set 총저수량 = 10.26
    where 댐 = '평림';
update dam11
    set 총저수량 = 50.3
    where 댐 = '부안';






--13. 강우량, 저수량, 방류량 댐 조인 코드
create table dam
as
select d.일시 as 날짜, d.댐, d. 저수량, d.강, d.유효저수량, 
a.저수량 as 강우량, m.총저수량, m.방류량
    from dam11 d, dam22 a, dam33 m
    where d.일시 = a.일시 and d.일시 = m.일시 and d.댐 = a.댐 and d.댐 = m.댐
    order by d.일시 asc;






--14. 계절, 지점, 행정구역 컬럼 추가 코드
alter table dam
add 계절 varchar2(100);

alter table dam
add 지점 varchar2(100);

alter table dam
add 행정구역 varchar2(100);






--15. 계절 데이터 추가 코드
update dam
set 계절 = '겨울'
where 날짜 between to_date('19/01/01','RRRR/MM/DD')
and to_date('19/02/22','RRRR/MM/DD');
update dam
set 계절 = '봄'
where 날짜 between to_date('19/02/23','RRRR/MM/DD')
and to_date('19/06/12','RRRR/MM/DD');
update dam
set 계절 = '여름'
where 날짜 between to_date('19/06/13','RRRR/MM/DD')
and to_date('19/10/04','RRRR/MM/DD');
update dam
set 계절 = '가을'
where 날짜 between to_date('19/10/05','RRRR/MM/DD')
and to_date('19/11/24','RRRR/MM/DD');
update dam
set 계절 = '겨울'
where 날짜 between to_date('19/11/25','RRRR/MM/DD')
and to_date('20/02/24','RRRR/MM/DD');
update dam
set 계절 = '봄'
where 날짜 between to_date('20/02/25','RRRR/MM/DD')
and to_date('20/05/29','RRRR/MM/DD');
update dam
set 계절 = '여름'
where 날짜 between to_date('20/05/30','RRRR/MM/DD')
and to_date('20/09/17','RRRR/MM/DD');
update dam
set 계절 = '가을'
where 날짜 between to_date('20/09/18','RRRR/MM/DD')
and to_date('20/11/22','RRRR/MM/DD');
update dam
set 계절 = '겨울'
where 날짜 between to_date('20/11/23','RRRR/MM/DD')
and to_date('21/02/26','RRRR/MM/DD');
update dam
set 계절 = '봄'
where 날짜 between to_date('21/02/27','RRRR/MM/DD')
and to_date('21/06/04','RRRR/MM/DD');
update dam
set 계절 = '여름'
where 날짜 between to_date('21/06/05','RRRR/MM/DD')
and to_date('21/10/10','RRRR/MM/DD');
update dam
set 계절 = '가을'
where 날짜 between to_date('21/10/11','RRRR/MM/DD')
and to_date('21/11/30','RRRR/MM/DD');
update dam
set 계절 = '겨울'
where 날짜 between to_date('21/12/01','RRRR/MM/DD')
and to_date('22/03/07','RRRR/MM/DD');
update dam
set 계절 = '봄'
where 날짜 between to_date('22/03/08','RRRR/MM/DD')
and to_date('22/05/27','RRRR/MM/DD');
update dam
set 계절 = '여름'
where 날짜 between to_date('22/05/28','RRRR/MM/DD')
and to_date('22/09/19','RRRR/MM/DD');
update dam
set 계절 = '가을'
where 날짜 between to_date('22/09/20','RRRR/MM/DD')
and to_date('22/11/29','RRRR/MM/DD');
update dam
set 계절 = '겨울'
where 날짜 between to_date('22/11/30','RRRR/MM/DD')
and to_date('22/12/31','RRRR/MM/DD');









--16. 행정구역 추가 코드
update dam
    set 행정구역= '대구광역시'
    where 댐 in ('군위');
    
update dam
    set 행정구역= '강원도'
    where 댐 in ('소양강','횡성','광동','달방');

update dam
    set 행정구역= '경상북도'
    where 댐 in ('안동','임하','영주','성덕','보현산','영천','안계','감포',
							   '운문','김천부항');
							      
update dam
    set 행정구역= '경상남도'
    where 댐 in ('남강','밀양','연초','구천','합천');

update dam
    set 행정구역= '울산광역시'
    where 댐 in ('대곡','사연','대암','선암');

update dam
    set 행정구역= '전라남도'
    where 댐 in ('주암본','주암조','장흥','수어','평림');   

update dam
    set 행정구역= '전라북도'
    where 댐 in ('섬진강','용담','부안');   
    
update dam
    set 행정구역= '충청남도'
    where 댐 in ('보령');
    
update dam
    set 행정구역= '충청북도'
    where 댐 in ('충주','대청');









--17. 지점 추가 코드
update dam
	set 지점 = '거제'
	where 댐 in ('연초','구천');
	
update dam
	set 지점 = '경주시'
	where 댐 in ('안계','감포','운문');
	
update dam
	set 지점 = '광주'
	where 댐 = '평림';
	
update dam
	set 지점 = '구미'
	where 댐 = '김천부항';
	
update dam
	set 지점 = '대구'
	where 댐 = '군위';
	
update dam
	set 지점 = '동해'
	where 댐 in ('광동','달방');
	
update dam
	set 지점 = '밀양'
	where 댐 = '밀양';
	
update dam
	set 지점 = '보령'
	where 댐 = '보령';
	
update dam
	set 지점 = '부안'
	where 댐 = '부안';
	
update dam
	set 지점 = '순천'
	where 댐 in ('주암조','주암본','수어');
	
update dam
	set 지점 = '안동'
	where 댐 in ('안동','임하');
	
update dam
	set 지점 = '영주'
	where 댐 = '영주';
	
update dam
	set 지점 = '영천'
	where 댐 in ('보현산','영천');
	
update dam
	set 지점 = '울산'
	where 댐 in ('대곡','사연','대암','선암');
	
update dam
	set 지점 = '임실'
	where 댐 = '섬진강';
	
update dam
	set 지점 = '장수'
	where 댐 = '용담' ;
	
update dam
	set 지점 = '장흥'
	where 댐 = '장흥';
	
update dam
	set 지점 = '진주'
	where 댐 = '남강';
	
update dam
	set 지점 = '청송군'
	where 댐 = '성덕';
	
update dam
	set 지점 = '청주'
	where 댐 = '대청';
	
update dam
	set 지점 = '춘천'
	where 댐 = '소양강';
	
update dam
	set 지점 = '충주'
	where 댐 = '충주';
	
update dam
	set 지점 = '합천'
	where 댐 = '합천';
	
update dam
	set 지점 = '홍천'
	where 댐 = '횡성';
	




--18. SPI, 강수량 컬럼 추가 코드
alter table dam
add SPI number(10,4);

alter table dam
add 강수량 number(10,3);
	




--19. SPI 데이터 추가 코드
merge into dam d
using SPI s
on (d.날짜 = s.일시 and d.지점 = s.지점명)
when matched then
update set d.SPI = s.SPI6;





--20. 강수량 데이터 추가 코드
merge into dam d
using 강수 s
on (d.날짜 = s.일시 and d.지점 = s.지점명)
when matched then
update set d.강수량 = s.일강수량;





--21. 컬럼 삭제 코드
alter table water_day drop column 지점;
alter table water_day drop column 강수계속시간;
alter table water_day drop column 최다강수량10m;
alter table water_day drop column 최다강수량시각10m;
alter table water_day drop column 최다강수량1h;
alter table water_day drop column 최다강수량시각1h;




--22. 섬지역 제외 코드
DELETE from water_day where 지점명 in ('서귀포', '성산','울릉도','제주','고산','백령도','흑산도');




--23. 빈 날짜 채워넣기 코드

insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='속초')   select  '속초',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='북춘천') select  '북춘천',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='철원')	  select  '철원',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='동두천') select  '동두천',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='파주')	  select  '파주',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='대관령') select  '대관령',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='춘천')	  select  '춘천',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='북강릉') select '북강릉',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='강릉')	  select  '강릉',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='동해')	  select  '동해',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='서울')	  select  '서울',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='인천')	  select  '인천',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='원주')	  select  '원주',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='수원')	  select  '수원',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='영월')	  select  '영월',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='충주')	  select  '충주',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='서산')	  select  '서산',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='울진')	  select  '울진',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='청주')	  select  '청주',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='대전')	  select  '대전',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='추풍령') select  '추풍령',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='안동')   select '안동',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='상주')   select '상주',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='포항')   select '포항',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='군산')   select '군산',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='대구')   select '대구',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='전주')   select '전주',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='울산')   select '울산',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='진주')   select '진주',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='부여')   select '부여',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='강화')   select '강화',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='홍천')   select '홍천',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='금산')   select '금산',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='제천')   select '제천',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='보은')   select '보은',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='태백')   select '태백',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='양평')   select '양평',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='임실')   select '임실',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='천안')   select '천안',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='세종')   select '세종',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='이천')   select '이천',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='정선군') select '정선군',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='보령')   select '보령',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='인제')   select '인제',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='목포')   select '목포',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='고창')   select '고창',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='순천')   select '순천',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='창원')   select '창원',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='여수')   select '여수',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='광주')	  select  '광주',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='진도(첨찰산)') select  '진도(첨찰산)',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='홍성')   select '홍성',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='부산')	  select  '부산',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='완도')	  select  '완도',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='통영')	  select  '통영',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='광양시') select  '광양시',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='밀양')	  select  '밀양',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='진도군') select  '진도군',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='청송군') select  '청송군',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='영천')	  select  '영천',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='산청')	  select  '산청',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='영덕')	  select  '영덕',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='경주시') select  '경주시',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='봉화')	  select  '봉화',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='남해')	  select  '남해',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='의성')	  select  '의성',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='거창')	  select  '거창',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='거제')	  select  '거제',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='영주')	  select  '영주',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='문경')	  select  '문경',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='구미')	  select  '구미',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='합천')	  select  '합천',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='고창군') select '고창군',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='영광군') select  '영광군',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='양산시') select  '양산시',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='정읍')	  select  '정읍',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='보성군') select  '보성군',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='해남')	  select  '해남',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='남원')	  select  '남원',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='김해시') select  '김해시',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='고흥')	  select  '고흥',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='강진군') select  '강진군',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='순창군') select  '순창군',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='의령군') select  '의령군',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='장흥')	  select  '장흥',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='장수')	  select  '장수',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='북창원') select  '북창원',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='함양군') select  '함양군',일시,0 from plus;
insert into water_day(지점명,일시,일강수량) with plus as (select to_date('2013/06/30','RRRR/MM/DD') + level as 일시 from dual connect by level <= 3836 minus select 일시 from water_day where 지점명 ='부안') select  '부안',일시,0 from plus;
commit;



--24. 강유역 컬럼 생성 및 업데이트 코드
alter table water_day add 강유역 varchar2(20);

-- 한강
update water_day
    set 강유역 ='한강'
    where 지점명 in ('속초','북춘천','철원','동두천','파주','대관령','춘천','백령도',
                    '북강릉','강릉','동해','서울','인천','원주','수원','영월','충주',
                    '홍천','강화','태백','양평','이천','정선군','제천','인제','홍성');
-- 금강
update water_day
    set 강유역 ='금강'
    where 지점명 in ('서산','청주','대전','추풍령','군산','보령','정읍','부여','금산',
                    '세종','보은','천안','고창','서청주','고창군');
                    
-- 낙동강
update water_day
    set 강유역 ='낙동강'
    where 지점명 in ('울진','안동','상주','포항','대구','울산','창원','진주','부산',
                    '경주시','밀양','산청','청송군','거제','영덕','남해','봉화','의성',
                    '영주','거창','북부산','구미','문경','합천','영천','영광군','양산시',
                    '해남','김해시','의령군','함양군','북창원');

-- 영섬
update water_day
    set 강유역 ='영섬'
    where 지점명 in ('전주','남원','임실','통영','완도','목포','여수','순천','광주',
                    '흑산도','진도(첨찰산)','진도군','고흥','보성군','강진군',
                    '장수','순창군','장흥','광양시','부안');




--25. 행정구역 컬럼 부여 코드
alter table water_day add 행정구역 varchar2(30);
update water_day
    set 행정구역 = '서울특별시'
    where 지점명 in ('서울');
    
update water_day
    set 행정구역 = '인천광역시'
    where 지점명 in ('강화','인천');
    
update water_day
    set 행정구역 = '광주광역시'
    where 지점명 in ('광주');
    
update water_day
    set 행정구역 = '대구광역시'
    where 지점명 in ('대구');
    
update water_day
    set 행정구역 = '대전광역시'
    where 지점명 in ('대전');
    
update water_day
    set 행정구역 = '세종특별자치시'
    where 지점명 in ('세종');
    
update water_day
    set 행정구역 = '울산광역시'
    where 지점명 in ('울산');
    
update water_day
    set 행정구역 = '부산광역시'
    where 지점명 in ('부산');
    
update water_day
    set 행정구역 = '경기도'
    where 지점명 in ('파주','동두천','양평','이천','수원');
    
update water_day
    set 행정구역 = '충청남도'
    where 지점명 in ('보령','부여','천안','홍성','금산','서산');
    
update water_day
    set 행정구역 = '충청북도'
    where 지점명 in ('충주','제천','추풍령','청주','보은');
    
update water_day
    set 행정구역 = '경상남도'
    where 지점명 in ('김해시','진주','통영','함양군','남해','의령군','거창','밀양','창원','합천','거제','산청','북창원','양산시');

update water_day
    set 행정구역 = '경상북도'
    where 지점명 in ('안동','영주','문경','포항','봉화','상주','영덕','영천','청송군','경주시','구미','울진','의성');

update water_day
    set 행정구역 = '전라남도'
    where 지점명 in ('목포','여수','보성군','완도','영광군','해남','강진군','고흥','광양시','순천','장흥','진도군','진도(첨찰산)');

update water_day
    set 행정구역 = '전라북도'
    where 지점명 in ('전주','군산','고창','부안','임실','정읍','남원','장수','고창군','순창군');

update water_day
    set 행정구역 = '강원도'
    where 지점명 in ('속초','철원','대관령','춘천','북강릉','강릉','동해','원주','영월','인제','홍천','태백','정선군','북춘천');
commit;





--26. 계절 컬럼 부여 코드
alter table water_day add 계절 varchar2(20);  
update water_day
    set 계절 = '겨울'
    where 일시 between to_date('19/01/01','RRRR/MM/DD')
        and to_date('19/02/22','RRRR/MM/DD');
update water_day
    set 계절 = '봄'
    where 일시 between to_date('19/02/23','RRRR/MM/DD')
        and to_date('19/06/12','RRRR/MM/DD');
update water_day
    set 계절 = '여름'
    where 일시 between to_date('19/06/13','RRRR/MM/DD')
        and to_date('19/10/04','RRRR/MM/DD');
update water_day
    set 계절 = '가을'
    where 일시 between to_date('19/10/05','RRRR/MM/DD')
        and to_date('19/11/24','RRRR/MM/DD');
update water_day
    set 계절 = '겨울'
    where 일시 between to_date('19/11/25','RRRR/MM/DD')
        and to_date('20/02/24','RRRR/MM/DD');
update water_day
    set 계절 = '봄'
    where 일시 between to_date('20/02/25','RRRR/MM/DD')
        and to_date('20/05/29','RRRR/MM/DD');
update water_day
    set 계절 = '여름'
    where 일시 between to_date('20/05/30','RRRR/MM/DD')
        and to_date('20/09/17','RRRR/MM/DD');
update water_day
    set 계절 = '가을'
    where 일시 between to_date('20/09/18','RRRR/MM/DD')
        and to_date('20/11/22','RRRR/MM/DD');
update water_day
    set 계절 = '겨울'
    where 일시 between to_date('20/11/23','RRRR/MM/DD')
        and to_date('21/02/26','RRRR/MM/DD');
update water_day
    set 계절 = '봄'
    where 일시 between to_date('21/02/27','RRRR/MM/DD')
        and to_date('21/06/04','RRRR/MM/DD');
update water_day
    set 계절 = '여름'
    where 일시 between to_date('21/06/05','RRRR/MM/DD')
        and to_date('21/10/10','RRRR/MM/DD');
update water_day
    set 계절 = '가을'
    where 일시 between to_date('21/10/11','RRRR/MM/DD')
        and to_date('21/11/30','RRRR/MM/DD');
update water_day
    set 계절 = '겨울'
    where 일시 between to_date('21/12/01','RRRR/MM/DD')
        and to_date('22/03/07','RRRR/MM/DD');
update water_day
    set 계절 = '봄'
    where 일시 between to_date('22/03/08','RRRR/MM/DD')
        and to_date('22/05/27','RRRR/MM/DD');
update water_day
    set 계절 = '여름'
    where 일시 between to_date('22/05/28','RRRR/MM/DD')
        and to_date('22/09/19','RRRR/MM/DD');
update water_day
    set 계절 = '가을'
    where 일시 between to_date('22/09/20','RRRR/MM/DD')
        and to_date('22/11/29','RRRR/MM/DD');
update water_day
    set 계절 = '겨울'
    where 일시 between to_date('22/11/30','RRRR/MM/DD')
        and to_date('22/12/31','RRRR/MM/DD');
commit;







--27. 누적 강수량 계산 코드
create index water_지점명 on water(지점명);
create index water_일시 on water(일시);
CREATE INDEX idx_water_일시3 ON water(TO_DATE(일시,'YYYY/MM/DD'));
create index water_일시2 on water(add_months(to_date(일시,'YYYY/MM/DD'),-6));
update water_day w
    set w.누적강수량 = (select sum(일강수량)
                        from water_day w2
                        where w.지점명 = w2.지점명 
                        and to_date(w2.일시,'RRRR/MM/DD') between add_months(to_date(w.일시,'RRRR/MM/DD'), -6)
                        and to_date(w.일시,'RRRR/MM/DD'));





--28. 컬럼 삭제 코드
alter table drought drop column 지점;




--29. 섬지역 제외 코드
DELETE from drought where 지점명 in ('서귀포', '성산','울릉도','제주','고산','흑산도','백령도');




--30. 비어 있는 지점명 찾기 코드
select w.지점명,d.지점명
    from water_day w,drought d
    where w.지점명 = d.지점명(+)
    group by w.지점명,d.지점명;







--31. 비어있는 날짜 찾아서 주변 평균낸 spi6 삽입 코드 (철원,안동,창원,장수,태백,봉화)
with plus as
(select to_date('2017/12/31','RRRR/MM/DD') + level as 일시
    from dual
    connect by level <= 1826
 minus
 select 일시
    from drought
    where 지점명 = '속초')
select '속초',(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '속초'
    group by (p.전날1 + 1);

insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '속초') select '속초'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '속초' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '철원') select '철원'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '철원' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '대관령') select '대관령' ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '대관령' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '춘천') select '춘천'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '춘천' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '서울') select '서울'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '서울' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '강릉') select '강릉'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '강릉' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '인천') select '인천'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '인천' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '수원') select '수원'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '수원' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '원주') select '원주'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '원주' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '충주') select '충주'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '충주' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '서산') select '서산'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '서산' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '울진') select '울진'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '울진' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '청주') select '청주'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '청주' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '대전') select '대전'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '대전' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '추풍령') select '추풍령' ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '추풍령' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '안동') select '안동'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '안동' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '포항') select '포항'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '포항' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '여수') select '여수'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '여수' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '완도') select '완도'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '완도' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '강화') select '강화'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '강화' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '양평') select '양평'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '양평' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '진주') select '진주'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '진주' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '전주') select '전주'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '전주' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '광주') select '광주'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '광주' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '군산') select '군산'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '군산' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '통영') select '통영'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '통영' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '울산') select '울산'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '울산' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '부산') select '부산'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '부산' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '대구') select '대구'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '대구' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '목포') select '목포'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '목포' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '창원') select '창원'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '창원' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '임실') select '임실'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '임실' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '금산') select '금산'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '금산' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '장수') select '장수'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '장수' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '정읍') select '정읍'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '정읍' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '해남') select '해남'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '해남' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '고흥') select '고흥'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '고흥' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '남원') select '남원'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '남원' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '장흥') select '장흥'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '장흥' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '홍천') select '홍천'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '홍천' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '보은') select '보은'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '보은' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '이천') select '이천'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '이천' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '보령') select '보령'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '보령' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '태백') select '태백'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '태백' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '천안') select '천안'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '천안' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '인제') select '인제'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '인제' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '부여') select '부여'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '부여' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '제천') select '제천'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '제천' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '거제') select '거제'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '거제' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '밀양') select '밀양'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '밀양' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '남해') select '남해'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '남해' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '산청') select '산청'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '산청' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '문경') select '문경'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '문경' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '구미') select '구미'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '구미' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '봉화') select '봉화'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '봉화' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '거창') select '거창'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '거창' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '영덕') select '영덕'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '영덕' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '영천') select '영천'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '영천' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '영주') select '영주'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '영주' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '합천') select '합천'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '합천' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '의성') select '의성'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '의성' group by (전날1+1);
insert into drought(지점명,일시,spi6) with plus as (select to_date('2017/12/31','RRRR/MM/DD') + level as 일시 from dual connect by level <= 1826 minus select 일시 from drought where 지점명 = '부안') select '부안'	  ,(p.전날1 + 1),round(avg(case when d.일시 in(p.전날2,p.전날1,p.다음날1,p.다음날2) then d.spi6 else null end),3)
    from drought d,(select (일시 - 2) as "전날2",(일시 - 1) as "전날1", (일시 + 1) as "다음날1",(일시 + 2) as "다음날2"
                    from plus) p
    where d.일시 in (p.전날2,p.전날1,p.다음날1,p.다음날2) and 지점명 = '부안' group by (전날1+1);
commit;







--32. 빈 지점 주변 평균값 입력 코드
insert into drought(지점명,일시,spi6)
select '북춘천',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('춘천')
    group by 일시;  
    
insert into drought(지점명,일시,spi6)
select '동두천',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('철원', '춘천')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '파주',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('동두천','서울','강화')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '북강릉',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('강릉')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '영월',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('제천','태백')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '정선군',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('영월','대관령','태백')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '동해',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('강릉','정선군')
    group by 일시;  

insert into drought(지점명,일시,spi6)
select '상주',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('문경','추풍령','구미','보은','의성')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '경주시',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('포항','영천')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '순창군',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('남원','임실','정읍')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '세종',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('청주','천안','대전')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '홍성',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('서산','보령')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '함양군',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('산청','거창')
    group by 일시;  
    
insert into drought(지점명,일시,spi6)
select '의령군',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('합천','진주')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '북창원',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('창원')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '김해시',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('창원','밀양','부산')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '양산시',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('김해시','밀양','울산','부산')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '청송군',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('안동','의성','영덕')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '고창군',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('부안','정읍')
    group by 일시;  
    
insert into drought(지점명,일시,spi6)
select '고창',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('고창군')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '영광군',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('고창군','광주')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '진도군',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('해남')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '진도(첨찰산)',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('진도군')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '강진군',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('해남','장흥')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '보성군',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('장흥','고흥')
    group by 일시;  
    
insert into drought(지점명,일시,spi6)
select '광양시',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('여수','남해')
    group by 일시;
    
insert into drought(지점명,일시,spi6)
select '순천',일시,round(avg(spi6),3)
    from drought
    where 지점명 in ('보성군','여수','광양시')
    group by 일시;
commit;






--33. 행정구역 컬럼 추가 코드
alter table drought add 행정구역 varchar2(30);
update drought
    set 행정구역 = '서울특별시'
    where 지점명 in ('서울');
    
update drought
    set 행정구역 = '인천광역시'
    where 지점명 in ('강화','인천');
    
update drought
    set 행정구역 = '광주광역시'
    where 지점명 in ('광주');
    
update drought
    set 행정구역 = '대구광역시'
    where 지점명 in ('대구');
    
update drought
    set 행정구역 = '대전광역시'
    where 지점명 in ('대전');
    
update drought
    set 행정구역 = '세종특별자치시'
    where 지점명 in ('세종');
    
update drought
    set 행정구역 = '울산광역시'
    where 지점명 in ('울산');
    
update drought
    set 행정구역 = '부산광역시'
    where 지점명 in ('부산');
    
update drought
    set 행정구역 = '경기도'
    where 지점명 in ('파주','동두천','양평','이천','수원');
    
update drought
    set 행정구역 = '충청남도'
    where 지점명 in ('보령','부여','천안','홍성','금산','서산');
    
update drought
    set 행정구역 = '충청북도'
    where 지점명 in ('충주','제천','추풍령','청주','보은');
    
update drought
    set 행정구역 = '경상남도'
    where 지점명 in ('김해시','진주','통영','함양군','남해','의령군','거창','밀양','창원','합천','거제','산청','북창원','양산시');

update drought
    set 행정구역 = '경상북도'
    where 지점명 in ('안동','영주','문경','포항','봉화','상주','영덕','영천','청송군','경주시','구미','울진','의성');

update drought
    set 행정구역 = '전라남도'
    where 지점명 in ('목포','여수','보성군','완도','영광군','해남','강진군','고흥','광양시','순천','장흥','진도군','진도(첨찰산)');

update drought
    set 행정구역 = '전라북도'
    where 지점명 in ('전주','군산','고창','부안','임실','정읍','남원','장수','고창군','순창군');

update drought
    set 행정구역 = '강원도'
    where 지점명 in ('속초','철원','대관령','춘천','북강릉','강릉','동해','원주','영월','인제','홍천','태백','정선군','북춘천');
commit;






--34. 계절 컬럼 부여 코드
alter table drought add 계절 varchar2(20);  
update drought
    set 계절 = '겨울'
    where 일시 between to_date('19/01/01','RRRR/MM/DD')
        and to_date('19/02/22','RRRR/MM/DD');
update drought
    set 계절 = '봄'
    where 일시 between to_date('19/02/23','RRRR/MM/DD')
        and to_date('19/06/12','RRRR/MM/DD');
update drought
    set 계절 = '여름'
    where 일시 between to_date('19/06/13','RRRR/MM/DD')
        and to_date('19/10/04','RRRR/MM/DD');
update drought
    set 계절 = '가을'
    where 일시 between to_date('19/10/05','RRRR/MM/DD')
        and to_date('19/11/24','RRRR/MM/DD');
update drought
    set 계절 = '겨울'
    where 일시 between to_date('19/11/25','RRRR/MM/DD')
        and to_date('20/02/24','RRRR/MM/DD');
update drought
    set 계절 = '봄'
    where 일시 between to_date('20/02/25','RRRR/MM/DD')
        and to_date('20/05/29','RRRR/MM/DD');
update drought
    set 계절 = '여름'
    where 일시 between to_date('20/05/30','RRRR/MM/DD')
        and to_date('20/09/17','RRRR/MM/DD');
update drought
    set 계절 = '가을'
    where 일시 between to_date('20/09/18','RRRR/MM/DD')
        and to_date('20/11/22','RRRR/MM/DD');
update drought
    set 계절 = '겨울'
    where 일시 between to_date('20/11/23','RRRR/MM/DD')
        and to_date('21/02/26','RRRR/MM/DD');
update drought
    set 계절 = '봄'
    where 일시 between to_date('21/02/27','RRRR/MM/DD')
        and to_date('21/06/04','RRRR/MM/DD');
update drought
    set 계절 = '여름'
    where 일시 between to_date('21/06/05','RRRR/MM/DD')
        and to_date('21/10/10','RRRR/MM/DD');
update drought
    set 계절 = '가을'
    where 일시 between to_date('21/10/11','RRRR/MM/DD')
        and to_date('21/11/30','RRRR/MM/DD');
update drought
    set 계절 = '겨울'
    where 일시 between to_date('21/12/01','RRRR/MM/DD')
        and to_date('22/03/07','RRRR/MM/DD');
update drought
    set 계절 = '봄'
    where 일시 between to_date('22/03/08','RRRR/MM/DD')
        and to_date('22/05/27','RRRR/MM/DD');
update drought
    set 계절 = '여름'
    where 일시 between to_date('22/05/28','RRRR/MM/DD')
        and to_date('22/09/19','RRRR/MM/DD');
update drought
    set 계절 = '가을'
    where 일시 between to_date('22/09/20','RRRR/MM/DD')
        and to_date('22/11/29','RRRR/MM/DD');
update drought
    set 계절 = '겨울'
    where 일시 between to_date('22/11/30','RRRR/MM/DD')
        and to_date('22/12/31','RRRR/MM/DD');
commit;







--35. 유역 컬럼 부여 코드
alter table drought add 강유역 varchar2(20);

-- 한강
update drought
    set 강유역 ='한강'
    where 지점명 in ('속초','북춘천','철원','동두천','파주','대관령','춘천','백령도',
                    '북강릉','강릉','동해','서울','인천','원주','수원','영월','충주',
                    '홍천','강화','태백','양평','이천','정선군','제천','인제','홍성');
-- 금강
update drought
    set 강유역 ='금강'
    where 지점명 in ('서산','청주','대전','추풍령','군산','보령','정읍','부여','금산',
                    '세종','보은','천안','고창','서청주','고창군');
                    
-- 낙동강
update drought
    set 강유역 ='낙동강'
    where 지점명 in ('울진','안동','상주','포항','대구','울산','창원','진주','부산',
                    '경주시','밀양','산청','청송군','거제','영덕','남해','봉화','의성',
                    '영주','거창','북부산','구미','문경','합천','영천','영광군','양산시',
                    '해남','김해시','의령군','함양군','북창원');

-- 영섬
update drought
    set 강유역 ='영섬'
    where 지점명 in ('전주','남원','임실','통영','완도','목포','여수','순천','광주',
                    '흑산도','진도(첨찰산)','진도군','고흥','보성군','강진군',
                    '장수','순창군','장흥','광양시','부안');
commit;







--36. 1차 머신러닝 생성 코드

drop table w; 
create table w
as
select rownum as id,s.spi6,d.누적강수량,
w.최대풍속,
w.최대풍속풍향,
w.최다풍향,
w.최소상대습도,
w.평균상대습도,
w.평균증기압,
w.평균현지기압,
w.최고해면기압,
w.평균해면기압,
w.가조시간,
w.합계일조시간,
w.평균전운량,
w.평균중하층운량,
w.평균지면온도,
w.최저초상온도,
w.합계소형증발량,
w.최고기온,
w.최대순간풍속,
a.저수량,
a.유효저수량,
a.총저수량,
a.방류량
    from weather w,drought s, water_day d, dam a
    where s.일시 = w.일시 and s.지점명 = w.지점명 and s.일시 = d.일시 and s.지점명 = d.지점명
     and a.날짜 = s.일시 and a.지점 = s.지점명;

delete from  w where 최대순간풍속시각 is null;
delete from  w where 최대풍속 is null;
delete from  w where 최대풍속풍향 is null;
delete from  w where 최대풍속시각 is null;
delete from  w where 평균풍속 is null;
delete from  w where 풍정합 is null;
delete from  w where 최다풍향 is null;
delete from  w where 평균이슬점온도 is null;
delete from  w where 최소상대습도 is null;
delete from  w where 최소상대습도시각 is null;
delete from  w where 평균상대습도 is null;
delete from  w where 평균증기압 is null;
delete from  w where 평균현지기압 is null;
delete from  w where 최고해면기압 is null;
delete from  w where 최고해면기압시각 is null;
delete from  w where 최저해면기압 is null;
delete from  w where 최저해면기압시각 is null;
delete from  w where 평균해면기압 is null;
delete from  w where 가조시간 is null;
delete from  w where 합계일조시간 is null;
delete from  w where 최다일사시각1H is null;
delete from  w where 최다일사량1H is null;
delete from  w where 합계일사량 is null;
delete from  w where 일최심신적설 is null;
delete from  w where 일최심신적설시각 is null;
delete from  w where 일최심적설 is null;
delete from  w where 일최심적설시각 is null;
delete from  w where 합계3시간신적설 is null;
delete from  w where 평균전운량 is null;
delete from  w where 평균중하층운량 is null;
delete from  w where 평균지면온도 is null;
delete from  w where 최저초상온도 is null;
delete from  w where 평균5CM지중온도 is null;
delete from  w where 평균10CM지중온도 is null;
delete from  w where 평균20CM지중온도 is null;
delete from  w where 평균30CM지중온도 is null;
delete from  w where 지중온도0_5 is null;
delete from  w where 지중온도1 is null;
delete from  w where 지중온도1_5 is null;
delete from  w where 지중온도3 is null;
delete from  w where 지중온도5 is null;
delete from  w where 합계대형증발량 is null;
delete from  w where 합계소형증발량 is null;
delete from  w where 강수99 is null;
delete from  w where 안개계속시간 is null;
delete from  w where 평균기온 is null;
delete from  w where 최저기온 is null;
delete from  w where 최저기온시각 is null;
delete from  w where 최고기온 is null;
delete from  w where 최고기온시각 is null;
delete from  w where 강수계속시간 is null;
delete from  w where 최다강수량10 is null;
delete from  w where 최다강수량시각10 is null;
delete from  w where 최다강수량1H is null;
delete from  w where 최다강수량시각1H is null;
delete from  w where 일강수량 is null;
delete from  w where 최대순간풍속 is null;
delete from  w where 최대순간풍속풍향 is null;

alter table w add 가뭄 varchar2(20);  
update w
    set 가뭄 = '심한습윤'
    where spi6 >= 1.50;
update w
    set 가뭄 = '보통습윤'
    where spi6 >= 1.00 and spi6 < 1.50;
update w
    set 가뭄 = '정상'
    where spi6 > -1.00 and spi6 < 1.00;
update w
    set 가뭄 = '약한가뭄'
    where spi6 > -1.50 and spi6 <= -1.00;
update w
    set 가뭄 = '보통가뭄'
    where spi6 > -2.00 and spi6 <= -1.50;
update w
    set 가뭄 = '심한가뭄'
    where spi6 <= -2.00;

alter table w
drop column spi6;

commit;






--37. 1차 머신러닝 코드
drop table w_train;
create table w_train
as
select *
    from w
    where id < 16524;
drop table w_test;
create table w_test
as
select *
    from w
    where id >= 16524;
select count(*) from w_train;
select count(*) from w_test;
select * from w_test;

DROP TABLE SETTINGS_GLM;

CREATE TABLE SETTINGS_GLM
AS
SELECT *
     FROM TABLE (DBMS_DATA_MINING.GET_DEFAULT_SETTINGS)
    WHERE SETTING_NAME LIKE '%GLM%';

BEGIN

   INSERT INTO SETTINGS_GLM
        VALUES (DBMS_DATA_MINING.ALGO_NAME, 'ALGO_RANDOM_FOREST');

   INSERT INTO SETTINGS_GLM
        VALUES (DBMS_DATA_MINING.PREP_AUTO, 'ON');

   INSERT INTO SETTINGS_GLM
        VALUES (
                  DBMS_DATA_MINING.GLMS_REFERENCE_CLASS_NAME,
                  'GLMS_RIDGE_REG_DISABLE');

   COMMIT;
END;
/


-- 3. 머신러닝 모델을 삭제합니다.

BEGIN
   DBMS_DATA_MINING.DROP_MODEL( 'MD_CLASSIFICATION_MODEL4');
END;
/


-- 4. 머신러닝 모델을 생성합니다. 

BEGIN 
   DBMS_DATA_MINING.CREATE_MODEL(
      model_name         => 'MD_CLASSIFICATION_MODEL4',
      mining_function       =>  DBMS_DATA_MINING.CLASSIFICATION,
      data_table_name       => 'W_train',
      case_id_column_name   => 'ID',
      target_column_name    =>  '가뭄',
      settings_table_name   => 'SETTINGS_GLM');
END;
/

-- 5. 머신러닝 모델을 확인합니다.

SELECT MODEL_NAME,
       ALGORITHM,
       MINING_FUNCTION
  FROM ALL_MINING_MODELS
 WHERE MODEL_NAME = 'MD_CLASSIFICATION_MODEL4';


-- 6. 머신러닝 모델 설정 정보를 확인합니다. 

SELECT SETTING_NAME, SETTING_VALUE
FROM ALL_MINING_MODEL_SETTINGS
WHERE MODEL_NAME = 'MD_CLASSIFICATION_MODEL4';

-- 7. 모델이 예측한 결과를 확인합니다. 

SELECT id,가뭄,
 PREDICTION (MD_CLASSIFICATION_MODEL4 USING *) MODEL_PREDICT_RESPONSE
FROM w_test
order by id;

-- 8. 정확도를 출력합니다. 
SELECT round(sum(decode(실제값,예측값,1,0)) / count(*) * 100,3) || '%' as 정확도
    from (SELECT id,가뭄 실제값,PREDICTION (MD_CLASSIFICATION_MODEL4 USING *) 예측값
            FROM w_test
            order by id);
