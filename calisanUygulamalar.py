#Sistemde calışan uygulamalar hakkında bilgi edinmek için sınıf
#Ilk arastirma
class calisanUygulamalar
  import os
  def uygulamalariListele()

    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

    for pid in pids:
        try:
            uygulamalar = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
            return uygulamar
        except IOError: # proc has already terminated
            continue
