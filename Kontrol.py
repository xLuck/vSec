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
        print("GUVENLIK SORGULAMASI TAMAMLANAMADI: USB GUVENLIK KARTI YOK!")

    if(acUser == user ):
        print("GUVENLIK SORGULAMASI TAMAMLANDI: DOGRU!")
        #Hic birsey yapmayarak kullanima izin ver
    else:

        print("GUVENLIK SORGULAMASI TAMAMLANAMADI: GUVENLIK KARTI GECERSIZ, BILDIRILIYOR!!")
        Mailv4.mail(SifreCoz.desifreEt() + '\n' + acUser,1)
        calisanUygulamalar.uygulamalar()

        PCKilit.Kapa()
        time.sleep(15)


def foo(sayiHDD):
    sayHDD = 0
    HDDKont = USBHDDKontrol.detect_devs(sayHDD)

    if sayiHDDx == HDDKont:
        print("GUVENLIK SORGULAMASI TAMAMLANDI: OPTIMUM SEVIYEDE HARICI BELLEKLER VAR!")
        controlUSB()
    else:
        controlUSB()

        print("GUVENLIK SORGULAMASI TAMAMLANAMADI: UYARI HARICI BELLEK TAKILDI VEYA GUVENLIK KARTI CIKARTILDI BILDIRILIYOR!!")
        Mailv4.mail(SifreCoz.desifreEt()+'\n'+acUser,0)

        calisanUygulamalar.uygulamalar()

        PCKilit.Kapa()
        time.sleep(15)
        hddsayi=0
        HDDKont = USBHDDKontrol.detect_devs(hddsayi)

    time.sleep(10)
    foo(sayiHDD)
hddsay=0
sayiHDDx=0
sayiHDDx=USBHDDKontrol.detect_devs(hddsay)
foo(sayiHDDx)
