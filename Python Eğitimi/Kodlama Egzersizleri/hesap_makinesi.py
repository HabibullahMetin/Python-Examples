print("Hesap Makinesi Programı"
      "İşlemler"
      "1. Toplama"
      "2. Çıkarma"
      "3. Çaprma"
      "4. Bölme")

a = int(input("Sayı1 : "))
b = int(input("Sayı2 : "))

islem = input("İşlemi giriniz")
if islem == "1" :
    print("{} ile {} in toplamı {} dir".format(a,b,a+b))
elif islem == "2" :
    print("{} ile {} in farkı {} dir".format(a,b,a-b))
elif islem == "3" :
    print("{} ile {} in çarpımı {} dir".format(a,b,a*b))
elif  islem == "4" :
    print("{} ile {} in bölümü {} dir".format(a,b,a/b))
else :
    print("Geçersiz işlem")