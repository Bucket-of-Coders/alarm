import os
from os import path
import time
import subprocess

Jalan = True
def countdown(t):
    Jalan = False
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer) 
        time.sleep(1) 
        t -= 1
        
    Jalan = True
    self_path=os.path.dirname(os.path.realpath(__file__))
    subprocess.call(["python",r"{}\compare.py".format(self_path)])

def timer():
    t = 10
    while Jalan:
        countdown(int(t)) 
        
        
