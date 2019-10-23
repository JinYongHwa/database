import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="mjc123456",  # your password
                     db="address")

cursor = db.cursor()

file=open("주소_서울특별시.txt",mode="rt",encoding="euc-kr")
for line in file:
    splitedLine=line.split("|")
    insertQuery=f'insert into road_address values(\'{splitedLine[0]}\',\'{splitedLine[1]}\',\'{splitedLine[2]}\',\'{splitedLine[3]}\',\'{splitedLine[4]}\',\'{splitedLine[5]}\',\'{splitedLine[6]}\',\'{splitedLine[7]}\',\'{splitedLine[8]}\',\'{splitedLine[9]}\',\'{splitedLine[10]}\')'
    cursor.execute(insertQuery)
    db.commit()

db.close()
