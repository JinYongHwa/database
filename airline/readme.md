> 비행기에 대한 기종, 엔진 종류, 생산연도, 좌석 수에 대한 정보가 있다.
``` sql
create table airline(
  id int auto_increment primary key,
  model char(30),
  engine char(20),
  year int,
  seat int
)
```


> 스케줄이 잡힌 각 비행기에 대해, 출발지와 도착지 및 일시를 알 수 있다.
비행기에 대해서는 중간 기착지 없이 하나의 출발지와 도착지에 연결되는 것으로 가정한다.
``` sql
create table schedule(
  id int auto_increment primary key,
  startAirportId char(4),
  arriveAirportId char(4),
  startTime datetime,
  arriveTime datetime,
  airlineId int,
  foriegn key(startAirportId) refrences airport(id),
  foriegn key(arriveAirportId) refrences airport(id),
  foriegn key(airlineId) refrences airline(id),
)
```



> 출발지와 도착지는 공항 이름, 국가, 도시이름, 인구에 대한
정보가 있다
``` sql
create table airport(
  id char(4) primary key,
  country char(20),
  city char(20),
  population int,
)
```


> 각 승객은 이름, 성별, 전화번호 및 좌석, 흡연 여부,
마일리지를 알 수 있다
``` sql
create table passenger(
  id int auto_increment primary key,
  name char(20),
  gender char(1),
  phone char(20),
  smoking char(1),
  mileage int
)
```

> 각 승객은 복수 예약이 가능하다.
``` sql
create table schedule_passenger(
  scheduleId int,
  passengerId int,
  seat char(5),
  foreign key(scheduleId) reference schedule(id),
  foreign key(passengerId) reference passenger(id),
  primary key(scheduleId,passengerId)
)
```
