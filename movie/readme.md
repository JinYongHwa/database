> 각 고객은 고객#로 식별되며 이름, 전화# 및 주소를 가진다
개인고객의 경우는 신용카드#가 필요하며, 소매고객의 경우는 사업자등록#와 FAX#가 요구된다

``` sql
create table customer(
  id int auto_increment primary key,
  name char(20),
  phone char(14),
  address char(100),
  type int,
  cardNumber char(16),
  registrationNumber char(10),
  fax char(14)
)
```

> SDV사는 현재 테이프가 들어와 있거나 곧 들어올 모든 영화에 대해 제목, 감독, 판매가격, 대여료 등의 정보를 유지한다
한 영화에 대해 대여용 테이프가 여러 개인 경우는 테이프마다 일련번호를 붙여서 관리하며, 각 테이프마다 테이프 형식을 기록한다
소매점 고객이 테이프를 구매할 때는 구매일, 지불양식, 또 각 영화 당 구매수량 등이 기록된다

``` sql
create table movie(
  id int auto_increment primary key,
  title char(100),
  director char(20),
  sellPrice double,
  rentPrice double
)
```


``` sql
create table tape(
  id int auto_increment primary key,
  type int,
  movieId int,
  foreign key(movieId) references movie(id)
)
```


> SDV사의 고객이 되기 위해서는 적어도 한번은 SDV사로부터 비디오 테이프를 대여했거나 구입했어야 한다
고객은 한번에 여러 개의 테이프를 대여할 수 있으나 대여일로부터 3일 이내에 반납하지 않으면 한 개당 일일 1,000원의 벌금을 지불해야 한다
반납만기일까지 빌린 테이프를 다 보지 못한 경우, 어떤 고객은 무더기 벌금을 피하기 위해 다 본 테이프들은 반납하고 나머지만 하루, 이틀 더 본 뒤 벌금과 함께 반납하기도 한다
``` sql
create table customer_tape(
  customerId int,
  tapeId int,
  type int,
  rentDate date,
  dueDate date,
  foreign key(customerId) references customer(id),
  foreign key(tapeId) references tape(id)
)
```
 



  
> SDV사는 최근 고객들이 영화를 고를 때 특정 영화배우가 출연했거나 대종상에 출연배우가 후보로 지명된 영화들을 선호하는 현상을 보고,
 고객서비스 차원에서 대종상연기부문 정보(연두, 부문, 상금, 후보영화, 후보배우 등)와 영화배우 정보(이름, 주소, 출연영화 등)를 갖춰 고객의 영화선정을 도울 계획이다
 
``` sql
 create table actor(
   id int auto_increment primary key,
   name char(20),
   address char(100)
 )
```
  
``` sql
 create table prize(
  id int auto_increment primary key,
  category char(10),
  price int
 )
```

``` sql
 create table prize_movie(
  prizeId int,
  movieId int,
  foreign key(prizeId) references prize(id),
  foreign key(movieId) references movie(id)
 )
```

``` sql
 create table prize_actor(
  prizeId int,
  actorId int,
  foreign key(prizeId) references prize(id),
  foreign key(actorId) references actor(id)
 )
```


 
