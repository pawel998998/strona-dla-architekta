import mysql.connector


for i in range(100):
  imie = 'awdawd'
  nazwisko = 'awdawd'
  email = 'awdawd@gmail.com'
  numer = '123-123-123'
  wiadomosc = 'awdawd'


  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
  )

  mycursor = mydb.cursor()
  sql = "INSERT INTO dane (imie, nazwisko, email, numer, wiadomosc) VALUES (%s, %s, %s, %s, %s)"
  val = (f"{imie}", f"{nazwisko}", f"{email}", f"{numer}", f"{wiadomosc}")
  mycursor.execute(sql, val)
  mydb.commit()