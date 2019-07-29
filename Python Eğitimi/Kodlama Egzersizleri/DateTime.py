from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL,"")

""""
şu_an = datetime.now()

print(şu_an.year)
print((şu_an.month))
print(şu_an.microsecond)
print(şu_an.hour)

şu_an = datetime.now()
print(datetime.ctime(şu_an))

print(datetime.strftime(şu_an,"%y"))
print(datetime.strftime(şu_an,"%b"))
print(datetime.strftime(şu_an,"%d"))
print(datetime.strftime(şu_an,"%y %d %b"))

su_an = datetime.now()

saniye = datetime.timestamp(su_an)

print(saniye)

su_an2 = datetime.fromtimestamp(saniye)

print(su_an2)

su_an = datetime.fromtimestamp(0)

print(su_an)

"""

tarih = datetime(2019,12,1)

su_an = datetime.now()

print(tarih-su_an)

