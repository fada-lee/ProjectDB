from tkinter import*
from PIL import Image,ImageTk
from datetime import datetime
from DB import*
import random

def mainProfile():
    win=Tk()
    app = Homeform(win,'62050052')
    win.mainloop()
class Homeform:
    def __init__(self,root,stuid):
        self.root = root
        self.root.title("HOME")
        self.root.option_add('*font', 'Hack 12 bold')
        self.root.geometry("380x780+0+0")

        self.stuid = stuid

        # Code color
        
        self.f="#403D3D"
        self.b = "#F1F1F1"
        self.be="#F1F1F1"

        #BG HOME        
        self.bg=ImageTk.PhotoImage(file="Picture\Home.png")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        #Frame
        frameText=Frame(self.root,bg=self.b)
        frameText.place(x=10,y=130)

        frame_time=Frame(root, bg= self.b)
        frame_time.place(x=0,y=180, height=400,width=400)

        frame_menu=Frame(root, bg= self.b)
        frame_menu.place(x=0,y=310, height=500,width=400)

        # label
        row = DB_connect.name(self.stuid)
        self.name_lbl = Label(frameText, text= (row[1],row[2]),  
            font= ("Hack",15,"bold"), fg = self.f,bg=self.b)
        self.name_lbl.pack(side=LEFT)

        self.datetime = datetime.today()
        timehours =int(self.datetime.strftime("%H"))*60
        timesd =int(self.datetime.strftime("%M"))
        tm= (timehours+timesd)/60
        if tm < 12:
            self.tm_img=ImageTk.PhotoImage(file="Picture\mor.png")
            self.tm_lbl=Label(frame_time, image=self.tm_img ,bd=0)
            self.tm_lbl.place(x=30,y=0)
        elif tm < 18 :
            self.tm_img=ImageTk.PhotoImage(file="Picture\Aft.png")
            self.tm_lbl=Label(frame_time, image=self.tm_img ,bd=0)
            self.tm_lbl.place(x=10,y=0)
        elif tm < 23:
            self.tm_img=ImageTk.PhotoImage(file="Picture\eve.png")
            self.tm_lbl=Label(frame_time, image=self.tm_img ,bd=0)
            self.tm_lbl.place(x=20,y=0)
        else:
            self.tm_img=ImageTk.PhotoImage(file="Picture\GN.png")
            self.tm_lbl=Label(frame_time, image=self.tm_img ,bd=0)
            self.tm_lbl.place(x=10,y=0)
        
        

if __name__ == "__main__" :
    mainProfile()
