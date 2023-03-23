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

### 제약조건
``` sql
create table student(
	no int auto_increment,
	studentno int not null unique,
	name varchar(10) not null default '',
	PRIMARY KEY(no)
);
```
- auto_increment : 이키워드가 붙은 필드는 데이터가 새로 생길때마다 자동증가된다
- not null : 이키워드가 붙은 필드는 null 값을 허용하지않음
- default : 이키워드가 붙은 필드에 값을 넣지않으면 자동으로 default 키워드 뒤에 있는값으로 채워진다
- unique :  이키워드가 붙은 필드는 중복된 값을 허용하지 
- primary key(필드명) : 이키워드로 설정된 필드는 중복을 허용하지 않고 데이터의 기본키가 됨

## MySQL에서 사용가능한 데이터 타입

###  문자형 데이터타입 
|타입|정의|
|---|------|
|CHAR(n)|	고정 길이 데이터 타입(최대 255byte)- 지정된 길이보다 짦은 데이터 입력될 시 나머지 공간 공백으로 채워진다.|
|VARCHAR(n)|	가변 길이 데이터 타입(최대 65535byte)- 지정된 길이보다 짦은 데이터 입력될 시 나머지 공간은 채우지 않는다.|
|TINYTEXT(n)|	문자열 데이터 타입(최대 255byte)|
|TEXT(n)|	문자열 데이터 타입(최대 65535byte)|
|MEDIUMTEXT(n)|	문자열 데이터 타입(최대 16777215byte)|
|LONGTEXT(n)|	문자열 데이터 타입(최대 4294967295byte)|


### 숫자형 데이터 타입
|타입|정의|
|---|------|
|TINYINT(n)|	정수형 데이터 타입(1byte) -128 ~ +127 또는 0 ~ 255수 표현 가능하다.|
|SMALLINT(n)|	정수형 데이터 타입(2byte) -32768 ~ 32767 또는 0 ~ 65536수 표현 가능하다.|
|MEDIUMINT(n)|	정수형 데이터 타입(3byte) -8388608 ~ +8388607 또는 0 ~ 16777215수 표현 가능하다.|
|INT(n)|	정수형 데이터 타입(4byte) -2147483648 ~ +2147483647 또는 0 ~ 4294967295수 표현 가능하다.|
|BIGINT(n)|	정수형 데이터 타입(8byte) - 무제한 수 표현 가능하다.|
|FLOAT(길이,소수)|	부동 소수형 데이터 타입(4byte) -고정 소수점을 사용 형태이다.|
|DECIMAL(길이,소수)|	고정 소수형 데이터 타입고정(길이+1byte) -소수점을 사용 형태이다.|
|DOUBLE(길이,소수)|	부동 소수형 데이터 타입(8byte) -DOUBLE을|

### 날짜형 데이터타입
|타입|정의|
|---|------|
|DATE|	날짜(년도, 월, 일) 형태의 기간 표현 데이터 타입(3byte)|
|TIME|	시간(시, 분, 초) 형태의 기간 표현 데이터 타입(3byte)|
|DATETIME|	날짜와 시간 형태의 기간 표현 데이터 타입(8byte)|
|TIMESTAMP|	날짜와 시간 형태의 기간 표현 데이터 타입(4byte) -시스템 변경 시 자동으로 그 날짜와 시간이 저장된다.|
|YEAR|	년도 표현 데이터 타입(1byte)|

### 이진 데이터타입

|타입|정의|
|---|------|
|BINARY(n) & BYTE(n)|	CHAR의 형태의 이진 데이터 타입 (최대 255byte)|
|VARBINARY(n)|	VARCHAR의 형태의 이진 데이터 타입 (최대 65535byte)|
|TINYBLOB(n)|	이진 데이터 타입 (최대 255byte)|
|BLOB(n)|	이진 데이터 타입 (최대 65535byte)|
|MEDIUMBLOB(n)|	이진 데이터 타입 (최대 16777215byte)|
|LONGBLOB(n)|	이진 데이터 타입 (최대 4294967295byte)|


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
alter table employee
change column title t char(10);
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
delete from employee where name='이수민'
```



### 실습용 데이터 구축
![image](https://github.com/JinYongHwa/database/raw/master/SQL/db.png)

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
	EMPNAME	CHAR(10),
	TITLE	CHAR(10)	DEFAULT '사원',
	MANAGER	INT,
	SALARY INT	,
	DNO	INT DEFAULT 1,
	PRIMARY KEY(EMPNO),
	FOREIGN KEY(MANAGER) REFERENCES EMPLOYEE(EMPNO),
	FOREIGN KEY(DNO) REFERENCES DEPARTMENT(DEPTNO)
);
```
### 외래키 제약조건 (Foreign key constraint)
https://mariadb.com/kb/en/foreign-keys/

https://docs.microsoft.com/ko-kr/sql/relational-databases/tables/primary-and-foreign-key-constraints?view=sql-server-ver15


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

### 이씨성을 가진 사원들의 이름,직급,소속부서번호를 검색하라
``` sql
select EMPNAME,TITLE,DNO
from employee
where EMPNAME like '이%'
```

### 이름에 '민' 이 들어간 사원들의 이름,직급,소속부서번호를 검색하라
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

### 박영권과 같은 직급인 사원의 이름과 직급을 검색해라
``` sql
select empname,title
from employee
where title = (select title 
	       from employee 
	       where dno='박영권')
```

### 영업부나 개발부에 근무하는 사원의 이름을 검색해라
``` sql
select empname
from employee e,department d 
where d.deptno=e.dno and d.deptname in ('영업','개발')
```

``` sql
select empname
from employee
where dno in (select deptno 
	      from department 
	      where deptname in ('영업','개발'))
```

``` sql
select empname
from employee e
where exists (select * 
	      from department d 
	      where d.deptno=e.dno 
	      and deptname in ('영업','개발'))
```

``` sql
select a.empname
from employee a,(select * 
	      from department
	      where deptname in ('영업','개발')) b
where a.dno=b.deptno
```

### 자신의 속한 부서의 평균급여보다 많은 급여를 받는 사원의 이름 부서번호 급여를 검색해라
``` sql
select empname,dno,salary from employee e
where salary> (select avg(salary) 
		from employee d 
                where d.dno=e.dno)
```
### 사원의 이름과 자신의 급여보다 많은사원의 수를 검색하라
``` sql
select empname,(
select count(*) from employee b
where a.salary<b.salary
) count
from employee a
```
