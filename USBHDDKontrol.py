

from __future__ import print_function
import glob
import re
import os
#Tamam.
dev_pattern = ['sd.*','mmcblk*']
class USBHDDKontrol:

#Gelistirilecek

    def detect_devs(sayi):

        for device in glob.glob('/sys/block/*'):
            for pattern in dev_pattern:
                if re.compile(pattern).match(os.path.basename(device)):
             #   print('Device:: {0}'.format(device))
                    sayi=sayi+1
        return sayi

