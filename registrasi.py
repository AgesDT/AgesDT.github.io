#!C:/Users/Ages/AppData/Local/Programs/Python/Python39/python
import cgi
import sys
import mysql.connector
import uuid

print("Content-Type: text/html")
print()
conn = mysql.connector.connect(user='root', password='', host='localhost', database='travelday')
curr = conn.cursor()

form =  cgi.FieldStorage()
id = uuid.uuid4()
idStr = str(id)
email = form.getvalue('email')
password = form.getvalue('password')
noTelp = form.getvalue('noTelp')

curr.execute("insert into registrasi_user values(%s, %s, %s, %s)", (idStr, noTelp, email, password))
conn.commit()

print("<meta http-equiv='refresh' content='1;url=http://localhost/projects/TravelDay/TravelDay/index.php'>")
print()  

sys.exit()

curr.close()
conn.close()



