import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="userpass",
    database="UserData")

cursor = mydb.cursor()

username = input("enter username : ")
password = input("enter password : ")

cursor.execute(f"SELECT * FROM Users WHERE username='{username}'")

records = cursor.fetchall()

if(len(records)==0):
    print("Username does not exist");
else:
    if(records[0][1]!=password):
        print("Password does not match")
    else:
        print("Login successful")
