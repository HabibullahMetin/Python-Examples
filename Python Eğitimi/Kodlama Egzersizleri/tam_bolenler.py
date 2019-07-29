def tamBolenleriBulma(sayi) :
    tamBolenler = []

    for i in range(2,sayi) :
        if(sayi % i == 0) :
            tamBolenler.append(i)
    return tamBolenler

while True :
    sayi = input("Sayı :")
    if(sayi == "q") :
        break
    else :
        sayi = int(sayi)
        print("Tam Bölenler :",tamBolenleriBulma(sayi))