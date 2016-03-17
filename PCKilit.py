#PC Kontorulunu Engelleme
import subprocess
import os


class PCKilit:
    def Kapa():
        #Kilitleme Islemi Gelistirilecek
        os.system("pkill -9 -u whix")

