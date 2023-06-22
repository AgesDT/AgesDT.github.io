#!C:/Users/Ages/AppData/Local/Programs/Python/Python39/python
import cgi
import sys
import mysql.connector
from login import _IDUSER

print("Content-Type: text/html")
print()
conn = mysql.connector.connect(user='root', password='', host='localhost', database='travelday')
curr = conn.cursor()

form =  cgi.FieldStorage()
trip = "Paket_1"
name = form.getvalue('name')
id = form.getvalue('id')
email = form.getvalue('email')
nat = form.getvalue('nat')
no_telp = form.getvalue('no_telp')
cCode = form.getvalue('cCode')
idUsr = _IDUSER

curr.execute("insert into guest_information values(%s, %s, %s, %s, %s, %s, %s, %s)", (trip, idUsr, name, id, email, nat, cCode, no_telp))
conn.commit()

print("<meta http-equiv='refresh' content='1;url=http://localhost/projects/TravelDay/TravelDay/src/payment.php'>")
print()  

sys.exit()

curr.close()
conn.close()



