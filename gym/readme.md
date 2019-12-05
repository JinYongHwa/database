> 헬스장의 회원 관리 시스템을 구축하려고한다
헬스장의 회원은 회원번호,이름,성별,키 의 회원정보를 받아 가입시키며 회원번호로 각 회원을 식별할 수 있다.
``` sql
create table `member`(
  number int auto_increment primary key,
  name char(20),
  gender char(1),
  trainerId char(20),
  foreign key (trainerId) references trainer(phone)
)
```

> 회원은 매달 몸무게 체지방량을 기록하여 트레이너가 관리할수 있게 해야한다. 
회원 한명당 한명의 담당 트레이너가 있어 담당트레이너에게 관리 받을수있다. 
``` sql
create table weightHistory(
  weight double,
  fatRatio double,
  memberId int,
  foreign key(memberId) references `member`(number)
)
```

> 트레이너의 정보는 이름 핸드폰번호 생년월일의 정보를 받으며 핸드폰번호로 식별한다. 
트레이너한명은 여러 회원을 담당하여 관리하게된다.
``` sql
create table trainer(
  name char(20),
  phone char(20) primary key,
  birthday date
)
```

> 회원은 담당트레이너에게 날짜와 시간을 정해 PT예약을 할수있다. 
트레이너의 PT예약은 날짜와 시간이 중복되어 예약할 수 없다.
``` sql
create table schedule(
  trainerId char(20),
  memberId int,
  date char(6),
  time char(2)
  foreign key(trainerId) references trainer(phone),
  foreign key(memberId) references member(id),
  primary key(trainerId,date,time)
)
```
