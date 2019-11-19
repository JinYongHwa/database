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



> 하나의 메뉴항목을 준비하는 데는 양도 다르고 종류도 다른 재료가 한가지 이상 필요하다. 
이러한 재료들은 그 이름으로 식별되고, 
커피자바는 각각의 재료마다 킬로그램, 리터, 파운드 같은 주문단위를 기록하며, 양으로 재주문한다.
``` sql
create table material(
  name char(20) primary key,
  unit char(10)
)
```

> 하나의 재료는 하나 또는 그 이상의 메뉴항목에서 사용될 수 있고, 
하나의 메뉴항목은 하나 또는 그 이상의 재료로 구성될 수 있다. 
고슬링 요리장은 특별 메뉴 항목에 사용되는 재료가 얼마나 되는지를 파악하고 있어야 한다.
``` sql
create table menu_material(
  menuId int,
  materialName char(20),
  usage int,
  foreign key(menuId) references menu(id),
  foreign key(materialName) references material(name)
)
```

 
> 제임스씨는 다양한 재료를 제공하는 공급업체 목록을 관리해야
한다. 이들 공급업체들은 그들의 공급업체 번호로 식별되고, 공급업체 이름과 주소를 가진다. 
``` sql
create table supplier(
  id char(20) primary key,
  name char(50),
  address char(50)
)
```

> 재료의 가격은 공급업체마다 다르며, 공급업체의 납기도 음식재료마다 다르다.
``` sql
create table supplier_material(
  supplierId char(20),
  materialName char(20),
  dueDate datetime,
  price int,
  foreign key(supplierId) references supplier(id),
  foreign key(materialName) references material(name)
)
```
