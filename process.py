#! C:\Users\pawel\AppData\Local\Programs\Python\Python312\python.exe
import cgi
import smtplib
import os
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import mysql.connector



print("Content-Type: text/html\n")

form = cgi.FieldStorage()

if os.environ["REQUEST_METHOD"] == "POST":
    imie = form.getvalue("Imie")
    nazwisko = form.getvalue("Nazwisko")
    email = form.getvalue("Email")
    numer = form.getvalue("Numer")
    wiadomosc = form.getvalue("Wiadomosc")

    html = """\
<html>

<head>
<style>
body {margin:0;padding:0}
@import url('https://fonts.googleapis.com/css2?family=Oswald&display=swap');
#naglowek {
	width:500px;
	background-color:#fff3cc;
	margin:0;
	padding:0;
	}
#srodek {
	width:500px;
	background-color:#ebc034;
	}
#firma{
	font-family: 'Oswald', sans-serif;
	}
#dane{
	text-align:left;
	margin-left:10px;
	margin-bottom:0px;
	margin-top:0px;
	}
</style>
</head>
<body>
<center>
<div id="naglowek">
<center><h1 id="firma">Lublinieckie Biuro Projektowe</h1></center>
</div>
</center>
<center>
<div id="srodek">
<h3 id="dane">Nadawca: """ + imie + """ """ + nazwisko + """ </h3>
<h3 id="dane">Email: """ + email + """</h3>
<h3 id="dane">Numer: """ + numer + """</h3>
</div>
</center>
<center>
<div id="naglowek">
</br>
<center><h3 id="dane">""" + wiadomosc + """</h3></center>
</div>
</center>
<center>
<div id="srodek">
<h3 id="dane"></h3>
</div>
</center>
</body>
</html>
"""

    part2 = MIMEText(html, 'html')




regex = '^([_a-z0-9-.]+)@([_a-z0-9-.]+)(.[a-z]{2,3})$'

def check(email):
    if(re.search(regex, email)):
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("kochamtruskawki998@gmail.com", "paweldlubala")
        server.sendmail("kochamtruskawki998@gmail.com", "kochamtruskawki998@gmail.com", part2.as_string())
        print(json.dumps({'status': True, 'content': """<div style="background-color:#1aff1a; width:100%; height:20%;"><center><b><p style="color:white;">Dziękujemy za wysłanie formularza. Postaramy się odpowiedzieć drogą mailową lub telefoniczną najszybciej jak bedzie to możliwe.</p><b></center></div>"""}))

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
        
        

    else:
        print(json.dumps({'status': False, 'error': ["""<div style="background-color:red; width:100%; height:20%;"><center><b><a style="color:white;">Twoja wiadomość nie została wysłana. Sprawdz poprawność formularza.<a><b></center></div>"""]}))
        
check(email)
