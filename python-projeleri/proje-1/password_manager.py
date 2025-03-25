import sqlite3
import hashlib
import os #?

def veritabaniniSil():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS users")  # Eski tabloyu sil
    conn.commit()
    conn.close()
    print("📌 Eski 'users' tablosu silindi.")


def veritabaniOlustur():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
          )
    ''')
    connection.commit()
    connection.close()
    print("veritabani olusturuldu")

# sifreleme icin sha-256 kullanilir.
def hashlenmis_sifreler(password):
    return hashlib.sha256(password.encode()).hexdigest()

def kayit():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    username = input("Kullanici Adi: ")
    password = input("Parola: ")

    hash_password = hashlenmis_sifreler(password)

    try:
        cursor.execute("INSERT INTO users (username,password) VALUES (?,?)", (username, hash_password))
        connection.commit()
        print("Kayit olundu")
    except:
        print("Kullanici adi zaten alinmis")

    connection.close()

def login():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    username = input("Kullanici Adi: ")
    password = input("Parola: ")
    hash_password = hashlenmis_sifreler(password)

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",(username,hash_password))
    user = cursor.fetchone()

    if user:
        print("Hos geldin, ", username)
    else:
        print("gecersiz...")

    connection.close()

def main():
    veritabaniOlustur()

    while True:
        secim = input("Seciniz: \n1. Kayit Ol\n2. Giris \n3. Cikis")
        if secim == "1":
            kayit()
        elif secim == "2":
            login()
        elif secim == "3":
            print("cikis yapiliyor")
            break
        else:
            print("tekrar dene")

if __name__ == "__main__":
    main()