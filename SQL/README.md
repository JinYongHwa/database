## MYSQL 기본 명령어

### 전체 데이터베이스 보기
``` sql
show databases;
```

### 데이터베이스 생성
``` sql
create database [데이터베이스명];
```
``` sql
create database [데이터베이스명] default character set [인코딩];
```

### 데이터베이스 삭제
``` sql
drop database [데이터베이스명];
```

### 데이터베이스 선택하기
``` sql
use [데이터베이스명];
```

### 데이터베이스 내 전체 테이블 목록확인하기
``` sql
show tables;
```



### 테이블의 스키마 확인하기
> desc [테이블명];

## DDL (데이터 정의어)

### create table
> 테이블 생성
``` sql
CREATE TABLE `데이터베이스명`.`테이블명` (
  `필드명1` 타입명 속성,
  `필드명2` 타입명 속성
)
```


``` sql
CREATE TABLE `test`.`employee` (
  `EMPNO` INT NOT NULL,
  `EMPNAME` CHAR(20) NULL,
  `TITLE` CHAR(20) NULL,
  `MANAGER` INT NULL,
  `SALARY` INT NULL,
  `DNO` INT NULL
);
```

``` sql
CREATE TABLE department(
  DEPTNO INT NOT NULL,
  DEPTNAME char(20) null,
  FLOOR int null
)
```

### drop table
> 테이블 삭제
``` sql
drop table `데이터베이스명`.`테이블명`
```

### alter table 
> * 새롭게 추가된 컬럼은 테이블의 마지막 컬럼이 되며 컬럼의 위치를 지정할 수는 없다.


> alter add
``` sql
alter table `test`.`employee`
add age int;
```

> alter modify 
``` sql
alter table `test`.`employee`
modify age char(10);
```

> alter drop
``` sql
alter table `test`.`employee`
drop age
```

> alter rename column
``` sql
alter table `test`.`employee`
rename column 
```

## DML(데이터 조작어)

### insert 문
``` sql
  insert into employee(`EMPNO`,`EMPNAME`,`TITLE`,`MANAGER`,`SALARY`,`DNO`)
  values(2106,'김창섭','대리',1001,250000,2);
```

``` sql
insert into employee(`EMPNO`,`EMPNAME`,`TITLE`,`MANAGER`,`SALARY`,`DNO`)
  values (2106,'김창섭','대리',1001,250000,2),
  (3426,'박영권','과장',4377,3000000,1),
  (3011,'이수민','부장',4377,4000000,3),
  (1003,'조민희','과장',4377,3000000,2),
  (3427,'최종철','사원',3011,1500000,3),
  (1365,'김상원','사원',2426,1500000,1),
  (2106,'이성래','사장',null,5000000,2)
  
```

``` sql
insert into department
values(1,'영업',8),
(2,'기획',10),
(3,'개발',9),
(4,'총무',7)
```

### select 문
``` sql
select * 
from employee;
```

``` sql
select name,title 
from employee;
```

``` sql
select * 
from employee 
where salary >=3000000;
```

### update 문
``` sql
update employee 
set title='대리' where name='최종철'
```

### delete 문
``` sql
delete employee where name='이수민'
```



### 중복제거
``` sql
select title 
from employee 
```

``` sql
select distinct title 
from employee
```

### 2번 부서에 근무하는 사원들에 관한 모든 정보를 검색하라
``` sql
 select *
 from employee
 where dno=2
```

### 이씨성을 가진 사원들의 이름,직금,소속부서번호를 검색하라
``` sql
select EMPNAME,TITLE,DNO
from employee
where EMPNAME like '이%'
```

### 이름에 '민' 이 들어간 사원들의 이름,직금,소속부서번호를 검색하라
``` sql
select EMPNAME,TITLE,DNO
from employee
where EMPNAME like '%민%'
```

### 직급이 과장이면서 1번부서에 근무하는 사원들의 이름과 급여를 검색하라
``` sql
select EMPNAME,SALARY
from employee
where title='과장' and dno=1
```

### 직급이 과장이면서 1번부서에 속하지 않은 사원들의 이름과 급여를 검색하라
``` sql
select EMPNAME,SALARY
from employee
where title='과장' and dno=1
```

### 급여가 3000000원 이상이고 4500000원 이하인 사원들의 이름,직급,급여를 검색하라
``` sql
select EMPNAME,TITLE,SALARY
from employee
where salary between 3000000 and 4500000
```

``` sql
select EMPNAME,TITLE,SALARY
from employee
where salary >=3000000 and salary <=4500000
```


### 김창섭 또는 최종철이 속한 부서이면서 기획 부서의 부서번호를 검색하라
``` sql
select dno
from employee
where name='김창섭' or name='최종철'
```

``` sql
select no 
from department 
where name='기획';
```

``` sql
select dno 
from employee
where name='김창섭' or name='최종철' 
and dno=(select no from department where name='기획')
```

### 소속된 직원이 한 명도 없는 부서의 부서번호를 검색하라.

``` sql
select DEPTNO 
from department
```

``` sql
select distinct DNO 
from employee
```

``` sql
select DEPTNO 
from department 
where DEPTNO not in (select distinct DNO from employee)
```


### 동등 조인
``` sql
select * 
from department as dep join employee as emp
where dep.DEPTNO=emp.DNO
```

### 자연 조인
``` sql
select * 
from employee natural join (select  DEPTNO as DNO,DEPTNAME,FLOOR from department) as dept
```

### 모든 사원들의 급여의 평균이 얼마인가?

``` sql
select avg(salary) as average_salary 
from employee
```

### 각 부서별 사원들의 급여의 평균이 얼마인가?
``` sql
select department.DEPTNAME, avg(salary) as salary 
from employee join department
where employee.DNO=department.DEPTNO
group by employee.dno
```

