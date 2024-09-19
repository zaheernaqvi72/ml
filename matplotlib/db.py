import mysql.connector as mc

mydb = mc.connect(
  host="localhost",
  user="root",
  password="",
  database="employee_management_system"
)

mycursor = mydb.cursor()
mycursor.execute("DESC leaves;")
print(mycursor.fetchall())