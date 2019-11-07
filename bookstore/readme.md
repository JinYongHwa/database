### 회원 테이블
``` sql
create table member(
  id int not null auto_increment primary key,
  password varchar(200) not null
);
```

### 회원 - 카드 테이블
``` sql
create table card(
  id char(12) not null primary key,
  validity char(4) not null,
  type char(8),
  memberId int,
  foreign key(memberId) references member(id)
);
```

### 회원 - 배송지 테이블
``` sql
create table address(
  id int auto_increment primary key,
  zipcode char(6) not null,
  address varchar(200) not null,
  address_detail varchar(200) null,
  memberId int,
  foreign key(memberId) references member(id)
);
```

### 장바구니 테이블
``` sql
create table basket(
  id int auto_increment primary key,
  createDate datetime,
  memberId int,
  foreign key(memberId) references member(id)
);
```

### 도서 테이블
``` sql
create table book(
  id int auto_increment primary key,
  title varchar(30),
  inventory int,
  price double
);
```

### 주문 테이블
``` sql
create table `order`(
  id int auto_increment primary key,
  orderDate datetime,
  orderPrice double,
  cardNumber char(12),
  cardValidity char(4),
  cardType char(8),
  zipcode char(6),
  address char(200),
  address_detail char(200),
  memberId int,
  foreign key(memberId) references member(id)
);
```

### 장바구니-책 테이블
``` sql
create table basket_book(
  basketId int,
  bookId int,
  count int,
  foreign key (basketId) references basket(id),
  foreign key (bookId) references book(id),
  primary key(basketId,bookId)
);
```
### 주문-책 테이블
``` sql
create table order_book(
  orderId int,
  bookId int,
  foreign key (orderId) references `order`(id),
  foreign key (bookId) references book(id),
  primary key(orderId,bookId)
);
```
