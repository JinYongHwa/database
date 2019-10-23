

``` sql
create table road_address(
	no char(25) not null primary key,
    road_code char(12) not null,
    dong_code char(2) not null,
    ground char(1) not null,
    building_main char(5) not null,
    building_sub char(5) not null,
    area_no char(5) not null,
    modify_code char(2) not null,
    publish_date char(8) null,
    before_road_code char(25) null,
    detail_address char(1) not null
)
```

``` sql
create table zibun_address(
	no char(25) not null,
    subno char(3) not null,
    dong_code char(10),
    sido char(20),
    sigungu char(20),
    dong char(20),
    lee char(20),
    mountin char(1),
    zibun_main int,
    zibun_sub int,
    is_main char(1),
    primary key(no,subno)
)
```

``` sql
create table meta_address(
	no char(25) not null primary key,
    dong_code char(10) not null,
    dong_name char(20) not null,
    zipcode char(5) not null,
    zipcode_sub char(3) null,
    multi_address char(40) null,
    building_name char(40) null,
    gu_building_name char(40) null,
    public_house char(1) null
)
```

``` sql
create table detail_address(
	gu_code char(5),
    dong_no int,
    floor_no int not null default 0,
    ho_no int not null default 0,
    ho_prefix_no int not null default 0,
    dong_name char(50),
    floor_name char(50),
    ho_name char(50),
    ho_prefix_name char(10),
    underground char(1),
    building_code char(25),
    dong_code char(10),
    underground_key char(1),
    building_main int,
    building_sub int,
    primary key(gu_code,dong_no,floor_no,ho_no,ho_prefix_no)
)
```
