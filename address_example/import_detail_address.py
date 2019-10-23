import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="mjc123456",  # your password
                     db="address")

cursor = db.cursor()

file=open("adrdc_seoul.txt",mode="rt",encoding="euc-kr")
for line in file:
    splitedLine=line.replace("'","''").replace("\n","").split("|")
    insertQuery=f'insert into detail_address values(\'{splitedLine[0]}\',\'{splitedLine[1]}\',\'{splitedLine[2]}\',\'{splitedLine[3]}\',\'{splitedLine[4]}\',\'{splitedLine[5]}\',\'{splitedLine[6]}\',\'{splitedLine[7]}\',\'{splitedLine[8]}\',\'{splitedLine[9]}\',\'{splitedLine[10]}\',\'{splitedLine[11]}\',\'{splitedLine[12]}\',\'{splitedLine[13]}\',\'{splitedLine[14]}\',\'{splitedLine[15]}\')'
    cursor.execute(insertQuery)
    db.commit()

db.close()
