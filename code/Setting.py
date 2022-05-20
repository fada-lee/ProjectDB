from tkinter import*
from PIL import Image,ImageTk
from Profile import*

from DB import*


class Settingform:
    
    def __init__(self,root,stuid):
      self.root = root
      self.root.title("Setting")
      self.root.geometry("380x780+0+0")
      self.root.option_add('*font', 'Hack 12 bold')

      self.stuid = stuid

        # Code color
      f="#403D3D"
      b="#F2EBE3"
      be="#F1F1F1"        

      #BG SETTING        
      self.bg=ImageTk.PhotoImage(file="Picture\Other.png")
      lbl_bg = Label(self.root, image=self.bg)
      lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

      self.root.iconbitmap('Picture\setico.ico')

      # Main frame
      frame= Frame(self.root,bg = be)
      frame.place(x=150, y=90,width=300,height=70)

      frametext= Frame(self.root,bg = be)
      frametext.place(x=160, y=170,width=230,height=20)

      frametext2= Frame(self.root,bg = be)
      frametext2.place(x=160, y=200,width=230,height=20)


      Setting = Label(self.root, text="Setting", font= ("Hack",17,"bold"), fg = "black",bg = "#FFAF5E")
      Setting.place(x=30,y=15)

      row = DB_connect.name(self.stuid)

      name = Label(frame, text=(row[1],row[2]), font= ("Hack",14,"bold"), fg = "black",bg = be)
      name.place(x=0,y=20)

      texstuid = Label(frame, text=self.stuid, fg = "black",bg = be)
      texstuid.place(x=0,y=50)

      textvar = Label(frametext, text=('Dormitory   Floor   Room'), fg='black',bg = be)
      textvar.place(x=0,y=0)

      bk_id = DB_connect.bookingid(self.stuid)
        
      if bk_id != None:
        textdata = DB_connect.dormitory(bk_id)

        if textdata != None:

          textdorm = Label(frametext2, text=(textdata[0]), fg='black',bg =be)
          textdorm.place(x=15,y=0)
    
          textfloor = Label(frametext2, text=(textdata[2]), fg='black',bg = be)
          textfloor.place(x=95,y=0)
    
          textroom = Label(frametext2, text=(textdata[3]), fg='black',bg = be)
          textroom.place(x=150,y=0)


