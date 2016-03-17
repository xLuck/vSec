# -*- coding: utf-8
import shutil
import getpass
import time, threading
from Mail import *
from PCKilit import *
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

    if(acUser == user):
        print("dogru")
        #Hic birsey yapmayarak kullanima izin ver
    else:

        print("yanlis")
       # Mail.mailyolla()
        PCKilit.Kapa()
        time.sleep(60)

        #PCKilit() islemi yapalicak

def foo():
   controlUSB()
   threading.Timer(10, foo).start()

foo()
