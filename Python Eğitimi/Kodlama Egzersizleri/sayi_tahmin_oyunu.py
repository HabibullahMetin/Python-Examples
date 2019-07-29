import random
import time

print("""Sayı Tahmin Oyunu

1 ila 40 arasında sayıyı tahmin edin.

""")

rastgeleSayi = random.randint(1,40)
tahminHakki = 7

while True :

    tahmin = int(input("Tahmininiz :"))

    if(tahmin < rastgeleSayi) :
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Çık")
        tahminHakki -= 1

    elif(tahmin > rastgeleSayi) :
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("İn")
        tahminHakki -= 1

    else :
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler doğru bildiniz !")
        break

    if(tahminHakki == 0) :
        print("Tahmin hakkınız bitti.")
        print("Sayı :",rastgeleSayi)
        break