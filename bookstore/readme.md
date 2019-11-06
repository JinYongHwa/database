### 회원 테이블
``` sql
create table member(
	number int not null auto_increment primary key,
    password varchar(200) not null
);
```

### 회원 - 카드 테이블
``` sql
create table card(
	number char(12) not null primary key,
    validity char(4) not null,
    type char(8),
    memberNumber int,
    foreign key(memberNumber) references member(number)
);
```

### 회원 - 배송지 테이블
``` sql
create table address(
	id int auto_increment primary key,
	zipcode char(6) not null,
    address varchar(200) not null,
    address_detail varchar(200) null,
    memberNumber int,
    foreign key(memberNumber) references member(number)
);
```

### 장바구니 테이블
``` sql
create table basket(
	number int auto_increment primary key,
    createDate date,
    memberNumber int,
    foreign key(memberNumber) references member(number)
);
```

### 도서 테이블
``` sql
create table book(
	number int auto_increment primary key,
    title varchar(30),
    inventory int,
    price double
);
```

### 주문 테이블
``` sql
create table `order`(
	orderNumber int auto_increment primary key,
	orderDate datetime,
    orderPrice double,
    cardNumber char(12),
    cardValidity char(4),
    cardType char(8),
    zipcode char(6),
    address char(200),
    address_detail char(200),
    memberNumber int,
    foreign key(memberNumber) references member(number)
);
```

### 장바구니-책 테이블
``` sql
create table basket_book(
	basketNumber int,
    bookNumber int,
    count int,
	foreign key (basketNumber) references basket(number),
    foreign key (bookNumber) references book(number),
	primary key(basketNumber,bookNumber)
);
```
### 주문-책 테이블
``` sql
create table order_book(
	orderNumber int,
    bookNumber int,
    foreign key (orderNumber) references `order`(orderNumber),
    foreign key (bookNumber) references book(number),
    primary key(orderNumber,bookNumber)
);
```
