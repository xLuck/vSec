# -*- coding: utf-8
import shutil
import getpass
import time, threading

#Problem: Tum USB Kullanicilari icin cozum bulunmali
shutil.copy2("/media/"+getpass.getuser()+"/A84A-7167/information.vsec", 'new')
dosya = open("new")
acUser = dosya.readline()
dosya.close()

def controlUSB():
    dosya = open("/media/"+getpass.getuser()+"/A84A-7167/information.vsec","r")
    user = dosya.readline()

    if(acUser == user):
        print("dogru")
        #Hic birsey yapmayarak kullanima izin ver
    else:
        print("yanlis")
        #Mail() atilacak
        #PCKilit() islemi yapalicak

def foo():
   controlUSB()
   threading.Timer(10, foo).start()

foo()
