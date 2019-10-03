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



### 실습용 데이터 구축
``` sql
CREATE TABLE DEPARTMENT (
	DEPTNO	INT	NOT NULL,
	DEPTNAME	CHAR(10),
	FLOOR		INT,
	PRIMARY KEY(DEPTNO)
);
```

``` sql
INSERT INTO DEPARTMENT VALUES(1, '영업', 8);
INSERT INTO DEPARTMENT VALUES(2, '기획', 10);
INSERT INTO DEPARTMENT VALUES(3, '개발', 9);
INSERT INTO DEPARTMENT VALUES(4, '총무', 7);
```

``` sql
CREATE TABLE EMPLOYEE (
	EMPNO	INT	NOT NULL,
	EMPNAME	CHAR(10)	UNIQUE,
	TITLE	CHAR(10)	DEFAULT '사원',
	MANAGER	INT,
	SALARY INT	CHECK (SALARY < 6000000),
	DNO	INT DEFAULT 1 CHECK (DNO IN (1,2,3,4)),
	PRIMARY KEY(EMPNO),
	FOREIGN KEY(MANAGER) REFERENCES EMPLOYEE(EMPNO),
	FOREIGN KEY(DNO) REFERENCES DEPARTMENT(DEPTNO) ON DELETE CASCADE
);
```

``` sql
INSERT INTO EMPLOYEE VALUES(4377, '이성래', '사장', NULL, 5000000, 2);
INSERT INTO EMPLOYEE VALUES(3426, '박영권', '과장', 4377, 3000000, 1);
INSERT INTO EMPLOYEE VALUES(3011, '이수민', '부장', 4377, 4000000, 3);
INSERT INTO EMPLOYEE VALUES(3427, '최종철', '사원', 3011, 1500000, 3);
INSERT INTO EMPLOYEE VALUES(1003, '조민희', '과장', 4377, 3000000, 2);
INSERT INTO EMPLOYEE VALUES(2106, '김창섭', '대리', 1003, 2500000, 2);
INSERT INTO EMPLOYEE VALUES(1365, '김상원', '사원', 3426, 1500000, 1);
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
### 1번부서나 3번부서의 사람들에 관한 모든 정보를 검색해라
``` sql
select * from employee
where dno in (1,3)
```

### 직급이 과장인 사원들에 대하여 이름과 급여가 10%인상되었을때의 값을 검색해라
``` sql
select empname,salary,salary*1.1 as newsalary
from employee
where title='과장'
```

### 매니저가 없는사람을 검색 해라
```
select empno,empname,manager from employee
where manager is null
```

### 2번부서에 근무하는사람들의 급여 직급 이름을 검색하여 오름차순으로 정렬하라
``` sql
select salary,title,empname
from employee
where dno=2
order by salary asc
```

### 전체 사원의 평균 급여와 최대급여를 검색해라
``` sql
select avg(salary) as salary_average,max(salary) as salary_max
from employee;
```

### 모든 사원들에 대해서 사원들이 속한 부서번호에 대해 그룹화 하고 각 부서마다 부서번호,평균급여,최대급여를 검색하라
``` sql
select dno,avg(salary) as salary_avg, max(salary) as salary_max
from employee
group by dno
```

### 평균급여가 250만원이 넘는 부서의  부서번호,평균급여,최대급여를 검색하라
``` sql
select dno,avg(salary) as salary_avg, max(salary) as salary_max
from employee
group by dno
having salary_avg>=2500000
```

### 김창섭이 속한 부서거나 개발부서인 부서번호를 검색하라
``` sql
select dno
from employee
where empname='김창섭'
union
select deptno
from department
where deptname='개발'
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

