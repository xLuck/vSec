

from __future__ import print_function
import glob
import re
import os

dev_pattern = ['sd.*','mmcblk*']
#Gelistirilecek
def detect_devs():
    for device in glob.glob('/sys/block/*'):
        for pattern in dev_pattern:
            if re.compile(pattern).match(os.path.basename(device)):
                print('Device:: {0}'.format(device))

if __name__=='__main__':
    detect_devs()