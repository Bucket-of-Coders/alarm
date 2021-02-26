#!/usr/bin/python3
#change​ Tkinter to tkinter 
import tkinter as tk
win = tk.Tk()
win.title("SP-ONE ALERT")
win.configure(bg='blue')

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
        
app=FullScreenApp(win)
#add​ label
mylabel=tk.Label(win,text="WARNING !!",font=("ubuntu",40,"bold"), fg = "yellow", bg='blue')
mylabe2=tk.Label(win,text="An attempt of intrusion has been detected. There is nothing to do actually except verifying the activity of the network.",font=("ubuntu",40,"bold"), fg = "yellow", bg='blue', wraplength=1200)
mylabe3=tk.Label(win,text="THANK YOU",font=("ubuntu",40,"bold"), fg = "yellow", bg='blue')
mylabel.pack()
mylabe2.pack()
mylabe3.pack()
win.mainloop()