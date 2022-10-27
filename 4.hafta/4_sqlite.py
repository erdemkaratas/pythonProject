import sqlite3

bag=sqlite3.connect("a.vt")

cursor=bag.cursor()
cursor.execute("CREATE TABLE IF NOT EXIST kitap (isim TEXT, yazar TEXT, yayinevi TEXT, sayfa)")

bag.close()



