print("Kullanıcı Girişi")

sys_kullanici_adi = "habib"
sys_parola = "123"

kullanici_adi = input("Kullanıcı Adı :")
parola = input("Parola :")

if (kullanici_adi == sys_kullanici_adi and parola != sys_parola) :
    print("Parola hatalı")
elif (kullanici_adi != sys_kullanici_adi and parola == sys_parola) :
    print("Kullanıcı Adı hatalı")
elif (kullanici_adi != sys_kullanici_adi and parola != sys_parola) :
    print("Kullanıcı adı ve parola hatalı")
else :
    print("Başarıyla giriş yaptınız")
