import os
import subprocess
from os import path
from red_alarm import red_alarm
from selection import filter

Alarm=False

def comparator(file, file2):
    # source_code_awal = open("{0}".format(file), encoding="latin1")
    # source_code_pembanding = open("{0}".format(file2), encoding="latin1")
    global Alarm
    
    source_code_awal = open(r"C:\Users\User\Documents\PROJECT\SPONE\PYTHON\{0}".format(file))
    source_code_pembanding = open(r"C:\Users\User\Documents\PROJECT\SPONE\{0}".format(file2))
    

    file_awal = [c for c in source_code_awal.readlines()]
    file_pembanding = [c for c in source_code_pembanding.readlines()]
    cnt = 1

    if(len(file_awal) == len(file_pembanding)):
        while file_awal:
            if(file_awal == file_pembanding):
                break
            else:
                Alarm = True
                break
        cnt += 1
    else:
        Alarm = True


        
folderOri = filter(path=r'C:\Users\User\Documents\PROJECT\SPONE\PYTHON\FILE', master_folder='FILE')[1]
folderLain = filter(path=r'C:\Users\User\Documents\PROJECT\SPONE\FILE', master_folder='FILE')[1]

        
if (len(folderOri) == len(folderLain)):
    count = 0
    while folderOri:
        comparator(folderOri[count], folderLain[count])
        count += 1
        if(count>= len(folderOri)):
            break
else:
    Alarm = True
    


print(Alarm)
self_path=os.path.dirname(os.path.realpath(__file__))
if Alarm:
    subprocess.call(["python",r"{}\red_alarm\red_alarm.py".format(self_path)])

