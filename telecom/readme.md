가입자
주민등록번호,주소,가입날짜
``` sql
create table member(
  id int auto_increment primary key,
  jumin char(13) not null,
  address char(100)
)
```

전화번호
국, 번호
가입자 1:N 전화번호
``` sql
create table phone(
  id int auto_increment primary key,
  area char(4),
  number char(4),
  memberId int,
  foreign key(memberId) references member(id)
)
```

통신사
이름
``` sql
create table telecom(
  id int auto_increment primary key,
  name char(20)
)
```



부가서비스
서비스이름,한달이용료
통신사 1:N 부가서비스
``` sql
create table service(
  id int auto_increment primary key,
  name char(20),
  price double,
  telecomId int,
  foreign key(telecomId) references telecom(id)
)
```



전화번호 N:M 부가서비스
      가입날자
``` sql
create table phone_service(
  phoneId int,
  serviceId int,
  joinDate datetime,
  foreign key(phoneId) references phone(id),
  foreign key(serviceId) references service(id),
  primary key(phoneId,serviceId)
)
```
