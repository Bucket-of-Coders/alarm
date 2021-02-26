#!/usr/bin/python3
#change​ Tkinter to tkinter 
import tkinter as tk
win = tk.Tk()
win.title("SP-ONE ALERT")
win.configure(bg='black')

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
mylabel=tk.Label(win,text="THIS IS SERIOUS ALARM",font=("ubuntu",40,"bold"), fg = "red", bg='black')
mylabe2=tk.Label(win,text="Although the system is not in danger, intrusion has been detected",font=("ubuntu",35,"bold"), fg = "red", bg='black' ,wraplength=1200)
mylabe3=tk.Label(win,text="WHAT TO DO",font=("ubuntu",40,"bold"), fg = "red", bg='black')
mylabe4=tk.Label(win,text="Please switch off the power during 15 second and disconnect internet. Then: ",justify='left',font=("ubuntu",35,"bold"), fg = "red", bg='black' ,wraplength=1200)
mylabe5=tk.Label(win,text="=> Switch on power <=",font=("ubuntu",30,"bold"), fg = "red", bg='black')
mylabe6=tk.Label(win,text="=> Change the password <=",font=("ubuntu",30,"bold"), fg = "red", bg='black')
mylabe7=tk.Label(win,text="=> Connect internet if needed <=",font=("ubuntu",30,"bold"), fg = "red", bg='black')
mylabe8=tk.Label(win,text="If there is any other questions, please contact customer services PT. SYDECO",font=("ubuntu",40,"bold"), fg = "red", bg='black', wraplength=1000)
mylabel.pack()
mylabe2.pack()
mylabe3.pack()
mylabe4.pack()
mylabe5.pack()
mylabe6.pack()
mylabe7.pack()
mylabe8.pack()
win.mainloop()