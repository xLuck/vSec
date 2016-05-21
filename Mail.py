import smtplib
#Mail Yollama Gelistirilecek!
#Kisi Bilgileri Yolanmali Mesaj Olarak

class Mail:
    def mailyolla():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
#Next, log in to the server
        server.login("developerxLuck", "123123xX")

#Send the mail
        msg = "\nUYARI!" # GONDERILECEK MESAJ

        server.sendmail("SistemUyari", "vedatcetin07@hotmail.com", msg)
        server.close()
        
    def mailyolla2(kullaniciBilgi,calisanBilgileri):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
#Next, log in to the server
        server.login("developerxLuck", "123123xX")

#Send the mail
        msg = "\nUYARI!\n Kullancı Bilgileri\n"+ kullaniciBilgi +"\n Calısan Program Bilgileri \n"+ calisanBilgileri  # GONDERILECEK MESAJ
        server.sendmail("SistemUyari", "vedatcetin07@hotmail.com", msg,)
        server.close()

Mail.mailyolla()