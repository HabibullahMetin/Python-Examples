from kutuphane import *

print("""--------------------------------------------

Kütüphane Programına Hoşgeldiniz.

İşlemler :

1 - Kitapları Göster 
2 - Kitap Sorgula
3 - Kitap Ekle
4 - Kitap Sil
5 - Baskı Yükselt

Çıkmak için q'ya basın

-----------------------------------------------------
""")

kutuphane = Kutuphane()


while True :
    islem = input("Yapacağınız işlem :")

    if(islem == "q") :
        print("Program sonlandırılıyor.......")
        break
    elif(islem == "1") :
        kutuphane.kitaplari_goster()

    elif(islem == "2") :
        isim = input("Hangi kitabı istiyorsunuz ?")
        print("Kitap Sorgulanıyor...")
        time.sleep(1)

        kutuphane.kitap_sorgula(isim)
    elif(islem == "3") :

        isim = input("İsim :")
        yazar = input("Yazar :")
        yayınevi = input("Yayınevi :")
        tur = input("Tür :")
        baski = int(input("Baskı :"))

        yeni_kitap = Kitap(isim,yazar,yayınevi,tur,baski)
        print("Kitap ekleniyor...")
        time.sleep(1)

        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi.")

    elif(islem == "4") :
        isim = input("Hangi kitabı silmek istiyorsunuz ?")

        cevap = input("Emin misiniz ?")
        if(cevap == "e") :
            print("Kitap siliniyor...")
            time.sleep(1)
            kutuphane.kitap_sil(isim)
            print("Kitap silindi.")

    elif(islem == "5") :
        isim = input("Hangi kitabın baskısını istiyorsunuz ?")
        print("Baskı yükseltiliyor...")
        kutuphane.baski_yukselt(isim)
        print("Baskı yükseltildi.")

    else :
        print("Geçersiz işlem...")





















