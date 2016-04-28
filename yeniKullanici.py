#/usr/bin/env python
# -*- coding: utf-8
import getpass
from Sifreleme import *
#Problem : Tum USB ler icin duzeltilmeli A84A-7167!
sifrelenmiscikti = ""
dosya = open("/media/"+getpass.getuser()+"/A84A-7167/information.vsec","w")
user = input("Kullanici Adi Giriniz:")
password = input("Sifre Giriniz:")
sifrelenmiscikti = Sifreleme.sifrele(user+"*"+password)
dosya.write(sifrelenmiscikti)
dosya.close()