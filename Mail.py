import smtplib

def mailyolla():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
#Next, log in to the server
    server.login("developerxLuck", "123123xX")

#Send the mail
    msg = "\nHello!" # GONDERILECEK MESAJ
    server.sendmail("SistemUyari", "vedatcetin07@hotmail.com", msg)