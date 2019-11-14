> 고객은 고객 이름으로 식별되고, 주소와 휴대폰번호를 가진다.
``` sql
create table customer(
  name char(20) primary key,
  address char(100),
  phone char(20)
)
```


하나의 주문은 주문 날짜와 계산을 한 고객으로 식별된다. 그리고
하나의 주문에는 현금, 신용카드, 수표 등의 지불방식을 기록해야
한다.
``` sql
create table `order`(
  method int,
  customerName char(20),
  date datetime,
  foreign key(customerName) references customer(name)
  primary key(customerName,date)
)
```



> 메뉴 항목은 항목번호로 식별되고, 메뉴항목의
이름과 가격, 그리고 커피, 차, 음료, 제과, 상품, 세트 메뉴, 상품권,
무선인터넷 같은 분류를 가진다.
``` sql
create table menu(
  id int auto_increment primary key,
  name char(20),
  price int,
  category char(10)
)
```

> 각각의 주문은 하나 또는 그 이상의 메뉴항목으로
구성된다.
주문은 각각의 메뉴 항목 단위로 이루어지고, 주문
수량도 기록된다.
``` sql
create table order_menu(
  orderDate datetime,
  orderCustomerName char(20),
  menuId int,
  foreign key(orderCustomerName,orderDate) references `order`(customerName,date),
  foreign key(menuId) references menu(id)
)
```
