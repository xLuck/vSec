import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

gmail_user = "developerxLuck@gmail.com"
gmail_pwd = "123123xX"

baslik = "UYARI!!!!!"
icerik = "BILGI HIRSIZLIGI TESPIT EDILDI..","KIMLIK BELIRLENEMEDI: KIMLIK  KARTI CIKARTILDI VEYA TAKILMADI! "
ek = "screenshot.jpg"
ek2="/tmp/uygulamalar.log"
yonetici = "vedatcetin07@hotmail.com"
class Mailv4:
    def mail(bilgiler,icerikSecici):
        msg = MIMEMultipart()
        Mesaj=icerik[icerikSecici] +'\n'+ "Kullanici Bilgileri: "+bilgiler
        msg['From'] = gmail_user
        msg['To'] = yonetici
        msg['Subject'] = baslik

        msg.attach(MIMEText(Mesaj))

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(ek, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(ek))
        msg.attach(part)
        #msg.attach(MIMEText(Mesaj))

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(ek2, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(ek2))
        msg.attach(part)

        mailServer = smtplib.SMTP("smtp.gmail.com", 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmail_user, gmail_pwd)
        mailServer.sendmail(gmail_user, yonetici, msg.as_string())

        mailServer.close()


