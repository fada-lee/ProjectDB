from lib2to3.pgen2.grammar import opmap
from tkinter import*
from tkinter import ttk

from PIL import Image,ImageTk
from DB import*



def mainBillhis():
    win=Tk()
    app = Billhisform(win,'62050052')
    win.mainloop()


class Billhisform:
    
    def __init__(self,root,stuid):
        self.root = root
        self.root.title("Edit Profile")
        self.root.geometry("380x780+0+0")
        self.root.option_add('*font', 'Hack 13 bold')

        self.stuid = stuid

        self.bg=ImageTk.PhotoImage(file="Picture\EditPf.png")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        self.root.iconbitmap('Picture\Billico.ico')

          # Code color
        f="#403D3D"
        b="#F2EBE3"
        be="#E8DFD4" 
        bmenu = '#F1F1F1'

        # Main frame
        framehead= Frame(self.root,bg = bmenu)
        framehead.place(x=150, y=100,width=210,height=40)

        frametext= Frame(self.root,bg = bmenu)
        frametext.place(x=160, y=160,width=130,height=20)

        frame_menu= Frame(self.root,bg = bmenu)
        frame_menu.place(x=0, y=720,width=30,height=200)

        frame= Frame(self.root,bg = "#F2EBE3")
        frame.place(x=20, y=205,width=150,height=400)

        head = Label(self.root, text="Bill payment history",font= ('Hack 17 bold'), fg = "black",bg = "#FFAF5E")
        head.place(x=30,y=15)

        row=DB_connect.name(self.stuid)

        name = Label(framehead,text=(row[1],row[2]),font= ('Hack 15 bold'), fg = 'black',bg = bmenu, bd =0)
        name.place(x=0,y=15)

        id = Label(frametext,text=row[0],font= ('Hack 12 bold'), fg = 'black',bg = bmenu, bd =0)
        id.place(x=0,y=0)


        


if __name__ == "__main__" :
    mainBillhis()
