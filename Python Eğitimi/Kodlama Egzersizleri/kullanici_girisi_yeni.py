print("Kullanıcı Girişi Programına Hoşgeldiniz")

sys_kullanici_adi = "habib"
sys_parola = "123"

girisHakki = 3

while True :
    kullanici_adi = input("Kullanıcı Adı :")
    parola = input("Parola :")
    if (kullanici_adi != sys_kullanici_adi and parola == sys_parola):
        print("Kullanıcı Adı hatalı")
        girisHakki -= 1
    elif (kullanici_adi == sys_kullanici_adi and parola != sys_parola):
        print("Parola hatalı")
        girisHakki -= 1
    elif (kullanici_adi != sys_kullanici_adi and parola != sys_parola):
        print("Kullanıcı adı ve parola hatalı")
        girisHakki -= 1
    else :
        print("Sisteme başarıyla giriş yapıldı.")
        break
    if(girisHakki == 0) :
        print("Giriş hakkınız bitti")
        break
