# -*- coding: utf-8
import shutil
import getpass
import time, threading
from Mail import *
from PCKilit import *
from USBHDDKontrol import *
#Problem: Tum USB Kullanicilari icin cozum bulunmali
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
       # PCKilit.Kapa()
        time.sleep(30)


def foo(sayiHDD):
    sayHDD = 0
    HDDKont = USBHDDKontrol.detect_devs(sayHDD)

    if sayiHDD == HDDKont:
        print("dogru")
        controlUSB()
    else:
        print("yanlis")
        #Mail.mailyolla()
       # PCKilit.Kapa()
        time.sleep(30)
        hddsayi=0
        sayiHDD = USBHDDKontrol.detect_devs(hddsayi)


    threading.Timer(10, foo(sayiHDD)).start()
hddsay=0
sayiHDD=0
sayiHDD=USBHDDKontrol.detect_devs(hddsay)
foo(sayiHDD)
