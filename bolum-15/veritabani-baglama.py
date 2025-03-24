import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.cursor() # cursor objesi uzerinden sorgulari hazirlariz.

sql = "INSERT INTO genres(name) VALUES('Macera')"
cursor.execute(sql)

connection.commit()

# cursor.execute("select * from customers where city='Oslo'")
# customers = cursor.fetchall()
# customer = cursor.fetchone()
# print(customer)
# for customer in customers:
#     print(customer[1] + " " + customer[2])



connection.close()
print("veritabani baglantisi hazir.")