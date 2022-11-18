import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="userpass",
    database="UserData")

cursor = mydb.cursor();

cursor.execute("ALTER TABLE Users RENAME COLUMN middlename TO lastname");

mydb.commit()