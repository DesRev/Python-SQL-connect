import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dash24dash$",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE cars (make VARCHAR(255), model VARCHAR(255))")

sql = "INSERT INTO cars (make, model) VALUES (%s, %s)"
val = ("Toyota", "Rav 4")
mycursor.execute(sql, val)

mydb.commit()


print(mycursor.rowcount, "record inserted.")