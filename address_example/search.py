import MySQLdb
import re
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="mjc123456",  # your password
                     db="address")

cursor = db.cursor()


stringPattern=re.compile("[^0-9\-\s]+")
numberPattern=re.compile("[0-9]+")


while True:
    keyword=input("검색어를 입력하세요: ")

    string=stringPattern.findall(keyword)
    number=numberPattern.findall(keyword)

    query="""
    select area_no,sido,sigungu,dong,jibun_main,jibun_sub,d.dong_name
    from detail_address d, zibun_address z,road_address r left outer join meta_address m on r.no=m.no
    where d.road_code=r.road_code
    and r.no=z.no
    and dong like '%%%s%%'
    """%(" ".join(string))

    if len(number)>=1:
        query=query+"and jibun_main=%s "%(number[0])

    if len(number)>=2:
        query=query+"and jibun_sub=%s "%(number[1])
    cursor.execute(query)
    index=1
    for data in cursor.fetchall():
        result="[%d] (%s)%s %s %s %s %s "%(index,data[0],data[1],data[2],data[3],data[4],data[5])
        index=index+1
        print (result)
