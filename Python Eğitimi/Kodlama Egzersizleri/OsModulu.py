import os
from datetime import datetime


""""
print(dir(os))
print(os.getcwd())

os.chdir("C:/Users/hp/Desktop")

for i in os.listdir() :
    print(i)

os.mkdir("Deneme1")
os.makedirs("Deneme2/Deneme3")
os.rmdir("Deneme2/Deneme3")
os.removedirs("Deneme2/Deneme3")
os.rename("test.txt","test2.txt")
print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime))
print(os.walk("C:/Users/hp/Desktop"))

for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk("C:/Users/hp/Desktop") :
    print("Klasör yolu",klasor_yolu)
    print("Klasör İsimleri :",klasor_isimleri)
    print("Dosya isimleri :",dosya_isimleri)
    print("---------------------------------------")


"""


for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk("C:/Users/hp/Desktop") :
    for i in dosya_isimleri :
        if(i.endswith(".txt")) :
            print(i)










