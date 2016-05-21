#Sistemde calışan uygulamalar hakkında bilgi edinmek için sınıf
#Ilk arastirma
import os,sys
import subprocess
import platform
import shutil

class calisanUygulamalar:

    def uygulamalar():
        os.system("top -b -n1 > /tmp/uygulamalar.log")
        os.system("scrot screenshot.jpg")

