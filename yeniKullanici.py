#/usr/bin/env python
# -*- coding: utf-8
import getpass

#Problem : Tum USB ler icin duzeltilmeli
sifrelenmiscikti = ""
dosya = open("/media/"+getpass.getuser()+"/A84A-7167/information.vsec","w")
user = input("Kullanici Adi Giriniz:")
password = input("Sifre Giriniz:")
# Sifreleme Eklenecek
# Sifreleme()Sinifi
dosya.write(sifrelenmiscikti)
dosya.close()