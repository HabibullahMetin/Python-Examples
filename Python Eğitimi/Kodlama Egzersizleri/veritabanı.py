import sqlite3

con = sqlite3.connect("library.db")

cursor = con.cursor()
def tablo_olustur() :
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()

def veri_ekle() :
    cursor.execute("INSERT INTO kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()

def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı) :
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()

def verileri_al() :
    cursor.execute("SELECT * FROM kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık tablosunun Bilgileri")
    for i in liste :
        print(i)

def verileri_al2() :
    cursor.execute("SELECT İsim,Yazar FROM kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık tablosunun Bilgileri")
    for i in liste :
        print(i)

def verileri_al3(yayınevi) :
    cursor.execute("SELECT * FROM kitaplık WHERE Yayınevi = ?",(yayınevi,))
    liste = cursor.fetchall()
    print("Kitaplık tablosunun Bilgileri")
    for i in liste :
        print(i)

def verileri_guncelle(eski_yayınevi,yeni_yayınevi) :
    cursor.execute("UPDATE kitaplık SET Yayınevi = ? WHERE Yayınevi = ?",(yeni_yayınevi,eski_yayınevi))
    con.commit()

def verileriSil(yazar) :
    cursor.execute("DELETE FROM kitaplık WHERE Yazar = ?",(yazar,))
    con.commit()

    
    
    

#isim = input("İsim :")
#yazar = input("Yazar :")
#yayınevi = input("Yayınevi :")
#sayfa_sayısı = int(input("Sayfa sayısı :"))
#veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı)
#verileri_al()
#verileri_al3("Everest")
#verileri_guncelle("Doğan Kitap","Everest")
#verileriSil("Ahmet Ümit")

con.close()
