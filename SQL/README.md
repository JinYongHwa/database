## MYSQL 기본 명령어

### 전체 데이터베이스 보기
``` sql
show databases;
```

### 데이터베이스 생성
``` sql
create database [데이터베이스명];
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
  `dno` INT NULL,
  PRIMARY KEY (`no`)
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
