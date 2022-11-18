import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="userpass",
    database="UserData")

cursor = mydb.cursor();

cursor.execute("SELECT * FROM Users ORDER BY marks DESC");

records = cursor.fetchall()

print(records)
sum = 0

for marks in records:
    sum = sum + int(marks[1]);

avg = sum/len(records);
print(f"Average marks : {avg}")