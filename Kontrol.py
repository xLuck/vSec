# -*- coding: utf-8
import shutil
import getpass
import time, threading
from Mailv4 import *
from PCKilit import *
from USBHDDKontrol import *
from Sifreleme import *
from calisanUygulamalar import *
from SifreCoz import *

#Problem: Tum USB Kullanicilari icin cozum bulunmali A84A-7167!
#Vize de programin calismamasi cozuldu
try:
    shutil.copy2("/media/"+getpass.getuser()+"/A84A-7167/information.vsec", 'new')
    dosya = open("new")
    acUser = dosya.readline()
    dosya.close()
except FileNotFoundError:
    acUser = "x"

def controlUSB():
    try:
        dosya = open("/media/"+getpass.getuser()+"/A84A-7167/information.vsec","r")
        user = dosya.readline()
    except FileNotFoundError:
        user = "NULL"
        print("Dosya yok")

    if(acUser == user ):
        print("dogru")
        #Hic birsey yapmayarak kullanima izin ver
    else:

        print("yanlisUSB")
        #Mail.mailyolla()
        #calisanUygulamalari = calisanUygulamalar.uygulamalariListele()
        #Mail.mailyolla(Sifreleme.desifre(user),calisanUygulamalar)
       # PCKilit.Kapa()
        time.sleep(30)


def foo(sayiHDD):
    sayHDD = 0
    HDDKont = USBHDDKontrol.detect_devs(sayHDD)

    if sayiHDDx == HDDKont:
        print("dogru")
        controlUSB()
    else:
        print("yanlis")
        Mailv4.mail(SifreCoz.desifreEt()+'\n'+acUser)
        calisanUygulamalar.uygulamalar()
        #Mail.mailyolla(Sifreleme.desifre(acUser),calisanUygulamalar)
        #PCKilit.Kapa()
        time.sleep(30)
        hddsayi=0
        HDDKont = USBHDDKontrol.detect_devs(hddsayi)

    time.sleep(10)
    foo(sayiHDD)
hddsay=0
sayiHDDx=0
sayiHDDx=USBHDDKontrol.detect_devs(hddsay)
foo(sayiHDDx)
