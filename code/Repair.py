from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql
import random
from DB import*
from datetime import datetime


def mainform():
    global win,app
    win=Tk()
    app = Repairform(win,'62050052')
    win.mainloop()

class Repairform:    
    def __init__(self,root,stuid):
        self.root = root
        self.root.title("Repair")
        self.root.geometry("380x780+0+0")
        self.root.option_add('*font', 'Hack 12 bold')
        self.stuid = stuid

        self.root.iconbitmap('Picture\Repairico.ico')
        

         # Code color
        f="#403D3D"
        b="#F2EBE3"
        be="#F1F1F1"

        #BG SETTING        
        self.bg=ImageTk.PhotoImage(file="Picture\Repair.png")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        # Main frame

        frame =Frame(self.root,bg = b)
        frame.place(x=0, y=0,width=380,height=580)

        framehead= Frame(self.root,bg = "#FFAF5E")
        framehead.place(x=0, y=0,width=380,height=70)

        framebody1 = Frame(self.root,bg = b)
        framebody1.place(x=0, y=90,width=380,height=200)

        framebody2 = Frame(self.root,bg = b)
        framebody2.place(x=0, y=470,width=380,height=200)

        #label
        Repairhead = Label(framehead, text="Repair",  font= ("Hack",17,"bold"), fg = "black",bg = "#FFAF5E")
        Repairhead.place(x=30,y=15) 

        # Text 
        global bk_id
        bk_id = DB_connect.bookingid(self.stuid)
        if bk_id != None:
            row = DB_connect.dormitory(bk_id)
            if row != None:
            # Repairid
                Re_No = random.randint(10000,99999)
                self.Repair_id =(str(Re_No))

                self.box_img=ImageTk.PhotoImage(file="Picture\Repno.png")
                self.repno_lbl=Label(framebody1, image=self.box_img ,bd=0, bg=b)
                self.repno_lbl.place(x=80,y=0) 

                lbl_Rep_No =Label(framebody1, text=("Repair No "+self.Repair_id), font= ("Hack",12,"bold"), fg = "black",bg = "white", bd =0)
                lbl_Rep_No.place(x=115,y=10)

                textdor = Label(framebody1, text=(row[0]), fg = "black",bg = b, )
                textdor.place(x=30,y=110)

                textbuil = Label(framebody1, text=(row[1]), fg = "black",bg = b, )
                textbuil.place(x=160,y=110)

                textfloor = Label(framebody1, text=(row[2]), fg = "black",bg = b, )
                textfloor.place(x=230,y=110)

                textroom = Label(framebody1, text=(row[3]), fg = "black",bg = b, )
                textroom.place(x=290,y=110)

        textvar = Label(framebody1, text='Dormitory      Building     Floor       Room', fg = "black",bg = b)
        textvar.place(x=30,y=60)

        self.line_img=ImageTk.PhotoImage(file="Picture\Line.png")
        self.line_lbl=Label(framebody1, image=self.line_img ,bd=0, bg=b)
        self.line_lbl.place(x=-10,y=90) 

        # DATE
        self.date_img=ImageTk.PhotoImage(file="Picture\date.png")
        self.date_lbl=Label(self.root, image=self.date_img ,bd=0, bg=b)
        self.date_lbl.place(x=50,y=300) 

        self.date_Re = datetime.today()
        date_month =Label(self.date_lbl,text=self.date_Re.strftime("%m"), font= ("Hack",14,"bold"), fg = f,bg= '#E6E6E6')
        date_month.place(x=100,y=60)
        date_Day =Label(self.date_lbl,text=self.date_Re.strftime("%d"), font= ("Hack",14,"bold"), fg = f,bg="#E6E6E6")
        date_Day.place(x=150,y=60)
        date_year =Label(self.date_lbl,text=self.date_Re.strftime("%Y"), font= ("Hack",14,"bold"), fg = f, bg="#E6E6E6")
        date_year.place(x=195,y=60)

        # Entry Repair
        Repair_name = Label(framebody2,text= "Items to be repaired", fg = "black",bg = b)
        Repair_name.place(x=10,y=0)
        
        self.textrep=Entry(framebody2, fg = "black",bg = "#D8D3D3", bd =0)
        self.textrep.place(x=30,y=40,width=300,height=100)

        # self.menu_img=ImageTk.PhotoImage(file="Picture\Box.png")
        # self.menu_lbl=Label(frame_menu, image=self.menu_img ,bd=0, bg=b)
        # self.menu_lbl.place(x=-10,y=0) 

    def recordsrep(self):
        open_home = DB_connect.insertrepair(bk_id,self.Repair_id,self.textrep.get(),self.date_Re)
        return open_home

if __name__ == "__main__" :
    mainform()


