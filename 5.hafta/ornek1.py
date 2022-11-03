'''
-- veri isimli bir klasör oluştur
-- zip dosyasını veri klasörüne çıkartın
-- zip dosyası içindeki cv dosyalarının tüç içeriğini tek bir csv dosyasında birleştirin
-- volume olmasın
-- b kayıtların tamamını sqlite veritabanına bir tablo oluşturarak yükleyin
-- kullanıcının belirlediği paritenin belirlediği aralığının kullanıcının belirlerdiği değerin grafiğini çizdirin
'''
import os
import zipfile
import pandas as pd
import sqlite3



if not os.path.exists("veri"):
    os.mkdir("veri")

arsiv = zipfile.ZipFile('pariteler_cikti_1hour_2022_2022.zip')
arsiv.extractall("veri/")

tum_dosyalar=os.listdir("veri")
pandas_csv_listesi=[]
for csv_dosya in tum_dosyalar:
    veri=pd.read_csv("veri/" + csv_dosya)
    del veri["volume"]
    pandas_csv_listesi.append(veri)

birlesmis_csv_ler = pd.concat(pandas_csv_listesi)
birlesmis_csv_ler.to_csv('hepsi.csv', index=False)



bag=sqlite3.connect("kripto.vt")

cursor=bag.cursor()
cursor.execute("CREATE TABLE parite (otime DATETIME, open FLOAT, high FLOAT, low FLOAT, close FLOAT)")

bag.commit()
bag.close()
kayitlar = pd.read_csv("hepsi.csv")


