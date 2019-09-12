## MYSQL 기본 명령어

### 전체 데이터베이스 보기
> show databases;

### 데이터베이스 선택하기
> use [데이터베이스명];

### 데이터베이스 내 전체 테이블 목록확인하기
> show tables;

### 테이블의 스키마 확인하기
> desc [테이블명];

## DDL (데이터 정의어)

### create table
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

### alter table 
> * 새롭게 추가된 컬럼은 테이블의 마지막 컬럼이 되며 컬럼의 위치를 지정할 수는 없다.


``` sql
alter table `test`.`employee`
add age int;
```

