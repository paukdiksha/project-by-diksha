import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
mycursor=mydb.cursor()
mycursor.execute("Create database Emp_Man")
print("Database created successfully")


import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Emp_man"
)
mycursor=mydb.cursor()
mycursor.execute("create table emp_table(id int(2) primary key auto_increment,name varchar(120),address varchar(120),phone varchar(10),mail varchar(100),department varchar(100))")
print("Table created successfully")


import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Emp_man"
)
mycursor=mydb.cursor()
sql="insert into emp_table(id,name,address,phone,mail,department) values(%s,%s,%s,%s,%s,%s)"
val=[
    ("","Mr.DAS","Kolkata","621922810","das220@gmail.com","sales"),
    ("","Mrs.Adhikari","Darjeeling","72990177771","adhi22@gmail.com","accounts"),
    ("","Mr.sen","kurseong","9336622190","sen_221@gmail.com","purchase")
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"row/s insented")
sql="select * from emp_table"
mycursor.execute(sql)
myresult= mycursor.fetchall()
for u in myresult:
    print(u)
sql="update emp_table set name=%s where name=%s"
val=("Mrs.DAS","Mrs.Das")
mycursor.execute(sql,val)
print(mycursor.rowcount,"row\s affected")
mydb.commit()