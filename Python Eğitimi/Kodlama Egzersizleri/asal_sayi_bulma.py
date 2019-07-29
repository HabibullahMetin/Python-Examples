def asalmi(sayi) :
    if(sayi == 1) :
        return False
    elif(sayi == 2) :
        return True
    else :
        for i in range(2,sayi) :
            if(sayi % i == 0) :
                return False
            return True

while True :
    number = input("Sayı :")
    if(number == "q") :
        break
    else :
        number = int(number)
        if(asalmi(number)) :
            print(number,"asal bir sayıdır")
        else :
            print(number,"asal bir sayı değildir.")