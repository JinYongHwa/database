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
  `no` INT NOT NULL,
  `name` CHAR(20) NULL,
  `title` CHAR(20) NULL,
  `manager` INT NULL,
  `salary` INT NULL,
  `dno` INT NULL
);
DEFAULT CHARACTER SET = utf8;
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
  insert into employee(`no`,`name`,`title`,`manager`,`salary`,`dno`)
  values(2106,'김창섭','대리',1001,250000,2);
```

``` sql
insert into employee(`no`,`name`,`title`,`manager`,`salary`,`dno`)
  values (3426,'박영권','과장',4377,3000000,1),
  (3011,'이수민','부장',4377,4000000,3),
  (1003,'조민희','과장',4377,3000000,2),
  (3427,'최종철','사원',3011,1500000,3),
  (1365,'김상원','사원',2426,1500000,1),
  (2106,'이성래','사장',null,5000000,2)
  
```

### select 문
``` sql
select * from employee;
```

``` sql
select name,title from employee;
```

``` sql
select * from employee where salary >=3000000;
```

### update 문
``` sql
update employee set title='대리' where name='최종철'
```

### delete 문
``` sql
delete employee where name='이수민'
```
