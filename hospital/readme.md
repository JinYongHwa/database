
> 각 환자에 대해서는 이름, 주소, 성별, 주민등록번호, 보험코드 등을 알 수 있어야 하고 각 부서에 대해서는 부서명, 위치, 책임자, 병상의 수, 사용중인 병상의 수를 저장한다.
각 부서에는 여러 명의 의사들과 간호사가 있으며 의사중 한 명이 책임자가 된다.
각 입원 환자에는 담당 의사와 간호사가 있으며 각 의사는 여러 명의 입원 환자를 담당한다.

``` sql
create table patient(
  name char(20),
  address char(100),
  gender char(1),
  registrationNumber char(13) primary key,
  code char(20),
  chargeDoctor char(10),
  foreign key(chargeDoctor) references doctor(number)
)

```

``` sql
create table patient_nurse(
  patientNumber char(13),
  nurseNumber char(10),
  foreign key(patientNumber) references patient(registrationNumber),
  foreign key(nurseNumber) references nurse(number),
  primary key(patientNumber, nurseNumber)
)
```

``` sql
create table department(
  id int auto_increment primary key,
  name char(20),
  location char(20),
  officer char(20),
  badCount int,
  usedBadCount int
)
```

> 각 의사와 간호사에 대해서는 사원번호, 이름, 주민등록번호, 재직년수 등의 정보가
있다.

``` sql
create table doctor(
  number char(10) primary key,
  name char(20),
  registrationNumber char(13),
  enrollYear int,
  departmentId int,
  foreign key(departmentId) references department(id)
);
```
``` sql
create table nurse(
  number char(10) primary key,
  name char(20),
  registrationNumber char(13),
  enrollYear int,
  departmentId int,
  foreign key(departmentId) references department(id)
)
```

> 각 환자들은 지정된 날짜에 입, 퇴원하며 입원기간 동안 여러번의 치료를 받는다. 치료에 대해서는 치료명, 기간, 환자가 보일 수 있는 반응 등을 저장한다.

``` sql
create table admit(
  id int auto_increment primary key,
  startDate date,
  endDate date,
  patientNumber char(13),
  foreign key(patientNumber) references patient(registrationNumber)
)
```


``` sql
create table cure(
  name char(20),
  startDate date,
  endDate date,
  reaction char(100),
  admitId int,
  foreign key(admitId) references admit(id)
)
```
