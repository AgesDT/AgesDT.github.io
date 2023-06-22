#!C:/Users/Ages/AppData/Local/Programs/Python/Python39/python
import cgi
import mysql.connector

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

curr.execute("insert into guest_information values(%s, %s, %s, %s, %s, %s, %s)", (trip, name, id, email, nat, cCode, no_telp))
conn.commit()


curr.close()
conn.close()

print("<meta http-equiv='refresh' content='1;url=http://localhost/projects/TravelDay/TravelDay/src/payment.html'>")
print() 





