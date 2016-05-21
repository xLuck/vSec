import getpass
import shutil

from Sifreleme import *
#Problem : Tum USB ler icin duzeltilmeli A84A-7167!
#Çözüm: Bir Db içinde bulunan USB bilgileri ve kullanıcı bilgileri karsılaştırma işlemi yapılabilir
class SifreCoz:
    def desifreEt():
        sifrelenmiscikti = ""

        dosya = open("new")
        acUser = dosya.readline()

        sifrelenmiscikti = Sifreleme.desifre(acUser)
        return (sifrelenmiscikti)
