#/usr/bin/env python3
# -*- coding: utf-8
import getpass
from Sifreleme import *
#Problem : Tum USB ler icin duzeltilmeli A84A-7167!
#Çözüm: Bir Db içinde bulunan USB bilgileri ve kullanıcı bilgileri karsılaştırma işlemi yapılabilir
sifrelenmiscikti = ""
dosya = open("/media/"+getpass.getuser()+"/A84A-7167/information.vsec","w")
user = input("Kullanici Adi Giriniz:")

sifrelenmiscikti = Sifreleme.sifrele(user)
dosya.write(sifrelenmiscikti)
dosya.close()
