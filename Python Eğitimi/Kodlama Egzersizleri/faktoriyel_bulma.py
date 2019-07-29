print("""Faktoriyel Programı
Çıkmak için q'ya basın.
""")

while True :
    sayi = input("Sayı :")
    if(sayi == "q") :
        break
    else :
        sayi = int(sayi)

        faktoriyel = 1

        for i in range(2,sayi+1) :
            faktoriyel *= i
        print("Faktoriyel",faktoriyel)

