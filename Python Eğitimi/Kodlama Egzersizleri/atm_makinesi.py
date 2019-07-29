print("-------------Atm Makinesi---------------")
print(""" 

1 -) Bakiye Sorgulama

2 -) Para Yatırma

3 -) Para Çekme

Programdan çıkmak için q'ya basın.

""")

bakiye = 1000

while True :
    islem = input("İşlemi seçin : ")

    if(islem == "q") :
        print("Yine bekleriz")
        break
    elif(islem == "1") :
        print("Bakiyeniz {} tldir".format(bakiye))

    elif(islem == "2"):
        miktar = int(input("Miktarı giriniz :"))
        bakiye += miktar
    elif(islem == "3"):
        miktar = int(input("Miktarı giriniz :"))
        if(bakiye - miktar < 0) :
            print("Böyle bi miktar çekemezsiniz")
            continue
        bakiye -= miktar
    else :
        print("Geçersiz işlem")