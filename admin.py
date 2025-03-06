#! C:/Users/pawel/AppData/Local/Programs/Python/Python310/python.exe
#-- coding: utf-8 --
import cgi
import smtplib
import os
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import mysql.connector
import math

PageLimit = 5

print("Content-Type: text/html\n")

form = cgi.FieldStorage()




page = form.getvalue("page")



if page == None:
    page = 1


#print(form['page'])




page = int(page)

page = page - 1



na_stronie = page*PageLimit



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)


mycursor = mydb.cursor()
mycursor.execute("SELECT COUNT(id) FROM dane LIMIT 1")
result = mycursor.fetchall()



total = result[0]






mycursor.execute(f"SELECT * FROM dane ORDER BY `id` DESC LIMIT {na_stronie},{PageLimit}")



result = mycursor.fetchall()



ostatnia = total[0]/5




ostatnia = (int(math.ceil(ostatnia)))

    

back = page - 1
next_1 = page + 1

if page < 2:
    back = 1

if page < ostatnia:
    next_1 = ostatnia






print("""
<center>
<!DOCTYPE html>
<html>
<head>
<style>
.pagination {
  display: inline-block;
}

.pagination a {
  color: black;
  float: left;
  padding: 8px 16px;
  text-decoration: none;
}

.pagination a.active {
  background-color: #4CAF50;
  color: white;
}

.pagination a:hover:not(.active) {background-color: #ddd;}
</style>
</head>
<body style="margin:0;padding:0;">""" + f"""



<div class="pagination">
  <a href="/strona/admin.py?page={back}">wczesniej</a>
  <a href="/strona/admin.py?page=1">1</a>
  <a>...</a> 

  """)





akutalna = page + 1



def pokaz_wszystko():
    global page
    if page < 1:
        page = akutalna
        print(f"""<a class="active" href="/strona/admin.py?page={page}">{page}</a>""")

        page = page + 1
        print(f"""<a href="/strona/admin.py?page={page}">{page}</a>""")
        page = akutalna

        page = page + 2
        print(f"""<a href="/strona/admin.py?page={page}">{page}</a>""")
        page = akutalna

        page = page + 3
        print(f"""<a href="/strona/admin.py?page={page}">{page}</a>""")
        page = akutalna

        page = page + 4
        print(f"""<a href="/strona/admin.py?page={page}">{page}</a>""")
        page = akutalna
    else:
        if page < 2:
            page = akutalna
            page = page - 1
            print(f"""<a href="/strona/admin.py?page={page}">{page}</a>""")

            page = akutalna
            print(f"""<a class="active" href="/strona/admin.py?page={page}">{page}</a>""")
            

            page = page + 1
            print(f"""<a href="/strona/admin.py?page={page}">{page}</a>""")
            page = akutalna

            page = page + 2
            print(f"""<a href="/strona/admin.py?page={page}">{page}</a>""")
            page = akutalna

            page = page + 3
            print(f"""<a href="/strona/admin.py?page={page}">{page}</a>""")
            page = akutalna

        else:
            page = akutalna
            page = page - 2
            print(f"""<a href="/strona/admin.py?page={page}">{page}</a>""")
            page = akutalna

            page = page - 1
            print(f"""<a href="/strona/admin.py?page={page}">{page}</a>""")
            page = akutalna


            
            page = akutalna
            print(f"""<a class="active" href="/strona/admin.py?page={page}">{page}</a>""")


            page = page + 1
            print(f"""<a href="/strona/admin.py?page={page}">{page}</a>""")
            page = akutalna

            page = page + 2
            print(f"""<a href="/strona/admin.py?page={page}">{page}</a>""")
            page = akutalna

page = akutalna - 1

if page == 1:
    q = (""" class="active" """)
else:
    q = (" ")

    
if page == 2:
    w = (""" class="active" """)
else:
    w = (" ")

    
if page == 3:
    e = (""" class="active" """)
else:
    e = (" ")

    
if page == 4:
    r = (""" class="active" """)
else:
    r = (" ")
    



def pokaz_1():
    page = akutalna
    print(f"""<a {q} href="/strona/admin.py?page=1">1</a>""")

def pokaz_1i2():
    page = akutalna
    print(f"""<a {q} href="/strona/admin.py?page=1">1</a>""")
    page = akutalna
    print(f"""<a {w} href="/strona/admin.py?page=2">2</a>""")

def pokaz_1i2i3():
    page = akutalna
    print(f"""<a {q} href="/strona/admin.py?page=1">1</a>""")
    page = akutalna
    print(f"""<a {w} href="/strona/admin.py?page=2">2</a>""")
    page = akutalna
    print(f"""<a {e} href="/strona/admin.py?page=3">3</a>""")

def pokaz_1i2i3i4():
    page = akutalna
    print(f"""<a {q} href="/strona/admin.py?page=1">1</a>""")
    page = akutalna
    print(f"""<a {w} href="/strona/admin.py?page=2">2</a>""")
    page = akutalna
    print(f"""<a {e} href="/strona/admin.py?page=3">3</a>""")
    page = akutalna
    print(f"""<a {r} href="/strona/admin.py?page=4">4</a>""")



def pokaz_to_samo_1():
    
    print(f"""<a href="/strona/admin.py?page={ostatnia-4}">{ostatnia-4}</a>""")
    
    print(f"""<a href="/strona/admin.py?page={ostatnia-3}">{ostatnia-3}</a>""")
    
    print(f"""<a href="/strona/admin.py?page={ostatnia-2}">{ostatnia-2}</a>""")
    
    print(f"""<a class="active" href="/strona/admin.py?page={ostatnia-1}">{ostatnia-1}</a>""")
    
    print(f"""<a href="/strona/admin.py?page={ostatnia}">{ostatnia}</a>""")
    

def pokaz_to_samo_2():
    
    print(f"""<a href="/strona/admin.py?page={ostatnia-4}">{ostatnia-4}</a>""")
    
    print(f"""<a href="/strona/admin.py?page={ostatnia-3}">{ostatnia-3}</a>""")
    
    print(f"""<a href="/strona/admin.py?page={ostatnia-2}">{ostatnia-2}</a>""")
    
    print(f"""<a  href="/strona/admin.py?page={ostatnia-1}">{ostatnia-1}</a>""")
    
    print(f"""<a class="active" href="/strona/admin.py?page={ostatnia}">{ostatnia}</a>""") 
    
















if ostatnia == 1:
    pokaz_1()
elif ostatnia == 2:
    pokaz_1i2()
elif ostatnia == 3:
    pokaz_1i2i3()
elif ostatnia == 4:
    pokaz_1i2i3i4()
elif akutalna == ostatnia - 1:
    pokaz_to_samo_1()
elif akutalna == ostatnia:
    pokaz_to_samo_2()
else:
    pokaz_wszystko()





























    
    




        




print(f"""
  <a href="/strona/admin.py?page=6">...</a>
  <a href="/strona/admin.py?page={ostatnia}">{ostatnia}</a>
  <a href="/strona/admin.py?page={next_1}">nastepna</a>
</div>

</body>
</html>
</center>
"""
)





p = []

tbl = """<tr><td style="border: 1px solid;">ID</td><td style="border: 1px solid;">Imie</td><td style="border: 1px solid;">Nazwisko</td><td style="border: 1px solid;">Email</td><td style="border: 1px solid;">Numer</td><td style="border: 1px solid;">Wiadomosc</td></tr>"""
p.append(tbl)

for row in result:
    a = """<tr><td style="border: 1px solid;">%s</td>"""%row[0]
    p.append(a)
    b = """<td style="border: 1px solid;">%s</td>"""%row[1]
    p.append(b)
    c = """<td style="border: 1px solid;">%s</td>"""%row[2]
    p.append(c)
    d = """<td style="border: 1px solid;">%s</td>"""%row[3]
    p.append(d)
    e = """<td style="border: 1px solid;">%s</td>"""%row[4]
    p.append(e)
    f = """<td style="border: 1px solid;word-wrap:break-word; max-width:800px;">%s</td>"""%row[5]
    p.append(f)





contents = f'''
<html>
<head>
<title>admin</title>
</head>
<body style="margin:0;padding:0">
<center><table style="border: 1px solid;border-collapse: collapse;margin-top:10px;">
'''

p = "".join(p)
contents = contents + p

contents = contents + '''</table></center>
</body>
</html>
'''

print(contents)







