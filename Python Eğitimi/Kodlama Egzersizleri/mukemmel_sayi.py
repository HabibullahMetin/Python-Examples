toplam = 0

sayi = int(input("Sayı giriniz :"))


for i in range(1,sayi) :
    if(sayi % i == 0) :
        toplam += i

print(toplam)

if(toplam == sayi) :
    print(sayi,"sayısı mükemmeldir")
else :
    print(sayi,"sayısı mükemmel değildir")