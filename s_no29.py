import mysql.connector
mydb = mysql.connector.connect(
	host="localhost",
	user="user",
	password="userpass",
	database="UserData")
	
cursor = mydb.cursor()
#ordering records

cursor.execute("SELECT * FROM Users ORDER BY userid ASC;")

records = cursor.fetchall()

print(records)
#deleting last record

if(len(records)>0):
	lastrec = records[len(records)-1]
	last_userid = lastrec[0];
	cursor.execute(f"DELETE FROM Users WHERE userid='{last_userid}';")
	mydb.commit()
	print("Record deleted")
else:
	print("No record")