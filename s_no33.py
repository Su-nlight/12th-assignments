import mysql.connector
mydb = mysql.connector.connect(
	host="localhost",
	user="user",
	password="userpass",
	database="UserData")
	
cursor = mydb.cursor()

name = input("Enter name : ")
email = input("Enter email : ")
password = input("Enter password:")
phone = input("Enter phone : ")
location = input("Enter location :")

cursor.execute("INSERT INTO Users(name,email,password,phone,location) VALUES('{name}','{email}','{password}','{phone}','{location}';)".format(name,email,password,phone,location))

mydb.commit()

print("Record Added.")