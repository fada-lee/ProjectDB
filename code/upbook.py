from tkinter import*
from turtle import update
from PIL import Image,ImageTk
from datetime import datetime
from DB import*


def mainform():
    global win,app
    win=Tk()
    app = Upbookingform(win,'62050052')
    win.mainloop()

class Upbookingform:
    def __init__(self,root,stuid):
        self.root = root
        self.root.title("Booking")
        self.root.option_add('*font', 'Hack 12 bold')
        self.root.geometry("380x780+0+0")
        self.root.iconbitmap('Picture\Bookingico.ico')

        self.stuid = stuid

        # Code color
        f="#403D3D"
        b="#F2EBE3"
        be="#E8DFD4" 
        bmenu = '#F1F1F1'

        #BG HOME        
        self.bg=ImageTk.PhotoImage(file="Picture\EditBook.png")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        #Frame
        frametext= Frame(self.root,bg = bmenu)
        frametext.place(x=150, y=100,width=210,height=70)

        frametext2= Frame(self.root,bg = bmenu)
        frametext2.place(x=130, y=170,width=230,height=20)

        frametext3= Frame(self.root,bg = bmenu)
        frametext3.place(x=130, y=200,width=230,height=20)

        frame_menu= Frame(self.root,bg = bmenu)
        frame_menu.place(x=0, y=720,width=380,height=200)

        Setting = Label(self.root, text="Edit Booking", 
          font= ("Hack",17,"bold"), fg = "black",bg = "#FFAF5E")
        Setting.place(x=30,y=15)

        # label
        row = DB_connect.name(self.stuid)
        name = Label(frametext,text=(row[1],row[2]),
          font= ('Hack 15 bold'), fg = 'black',bg = bmenu, bd =0)
        name.place(x=0,y=0)

        id = Label(frametext,text=row[0],fg = 'black',bg = bmenu, bd =0)
        id.place(x=0,y=30)

        global bk_id

        bk_id = DB_connect.bookingid(self.stuid)

        if bk_id != None:
          room = DB_connect.room(bk_id)
          self.room = room[1]
          dorm = DB_connect.dormitory(bk_id)

          if dorm != None:

            self.dorm = str(dorm[0]+dorm[1])
            textdor = Label(frametext3, text=(dorm[0]), fg = "black",bg = bmenu)
            textdor.place(x=0,y=0)

            textbuil = Label(frametext3, text=(dorm[1]), fg = "black",bg = bmenu,)
            textbuil.place(x=130,y=0)

          textvar = Label(frametext2, text='Dormitory      Building', fg = "black",bg = bmenu)
          textvar.place(x=0,y=0)

          textin = Label(self.root, text='CheckIN', fg = f,bg = b )
          textin.place(x=25,y=300)

          textout = Label(self.root, text='CheckOut', fg = f,bg = b )
          textout.place(x=25,y=470)

        
          textbkid = Label(self.root, text='BookingID '+str(bk_id[0]), fg = f,bg = '#C2C2C2' )
          textbkid.place(x=50,y=265)

          floor = Label(self.root, text=room[0],font=('Hack', 15 ,'bold') , fg = f,bg = be )
          floor.place(x=290,y=320)

          roomnumber = Label(self.root, text=room[1],font=('Hack', 15 ,'bold'), fg = f,bg = be )
          roomnumber.place(x=282,y=440)

          price = Label(self.root, text=room[2],font=('Hack', 15 ,'bold'), fg = f,bg = be )
          price.place(x=280,y=555)

          

        textfloor = Label(self.root, text='Floor', fg = f,bg = b )
        textfloor.place(x=275,y=270)


        textroom = Label(self.root, text='Room', fg = f,bg = b )
        textroom.place(x=275,y=390)


        textprice = Label(self.root, text='Price', fg = f,bg = b )
        textprice.place(x=280,y=510)


        self.dateDIN = Entry(self.root, fg = f,bg = '#E6E6E6', bd =0)
        self.dateDIN.place(x=95,y=385,width=30,height=27)

        self.dateMIN = Entry(self.root, fg = f,bg = '#E6E6E6', bd =0)
        self.dateMIN.place(x=133,y=385,width=30,height=27)

        self.dateYIN = Entry(self.root, fg = f,bg = '#E6E6E6', bd =0)
        self.dateYIN.place(x=172,y=385,width=50,height=27)

        self.dateDOUT = Entry(self.root, fg = f,bg = '#E6E6E6', bd =0)
        self.dateDOUT.place(x=95,y=556,width=30,height=27)

        self.dateMOUT = Entry(self.root, fg = f,bg = '#E6E6E6', bd =0)
        self.dateMOUT.place(x=133,y=556,width=30,height=27)

        self.dateYOUT = Entry(self.root, fg = f,bg = '#E6E6E6', bd =0)
        self.dateYOUT.place(x=172,y=556,width=50,height=27)

        if bk_id != None:
          date = DB_connect.showbookdate(bk_id)
          if date !=None:
            self.dateDIN.insert(0,date[0])
            self.dateMIN.insert(0,date[1])
            self.dateYIN.insert(0,date[2])
            self.dateDOUT.insert(0,date[3])
            self.dateMOUT.insert(0,date[4])
            self.dateYOUT.insert(0,date[5])

            def on_exit1(event):
              if self.dateDIN.get()=='':
                 self.dateDIN.insert(0,date[0])

            def on_exit2(event):
              if self.dateMIN.get()=='':
                 self.dateMIN.insert(0,date[1])

            def on_exit3(event):
              if self.dateYIN.get()=='':
                 self.dateYIN.insert(0,date[2])

            def on_exit4(event):
              if self.dateDOUT.get()=='':
                 self.dateDOUT.insert(0,date[3])

            def on_exit5(event):
              if self.dateMOUT.get()=='':
                 self.dateMOUT.insert(0,date[4])

            def on_exit6(event):
              if self.dateYOUT.get()=='':
                 self.dateYOUT.insert(0,date[5])

            self.dateDIN.bind('<FocusOut>',on_exit1)
            self.dateMIN.bind('<FocusOut>',on_exit2)
            self.dateYIN.bind('<FocusOut>',on_exit3)
            self.dateDOUT.bind('<FocusOut>',on_exit4)
            self.dateMOUT.bind('<FocusOut>',on_exit5)
            self.dateYOUT.bind('<FocusOut>',on_exit6)


    def Out(self):
      open_home = messagebox.askyesno('CHECK OUT' ,'Do you want to check out, right?')
      if open_home>0:
        DB_connect.checkOut(self.dorm,self.room,bk_id)
        return open_home
      else: 
        if not open_home:
          return -1
      

    def updatebooks(self):
      open_home = messagebox.askyesno('????' ,'Do you want to update the information?')
      if open_home>0:
        self.checkin = (str(self.dateYIN.get())+'-'+(str(self.dateMIN.get()))+'-'+(str(self.dateDIN.get())))
        self.checkout = (str(self.dateYOUT.get())+'-'+(str(self.dateMOUT.get()))+'-'+(str(self.dateDOUT.get())))
        DB_connect.updatebooking(self.checkin,self.checkout,bk_id) 
        return open_home
      else: 
        if not open_home:
          return -1
        
  



if __name__ == "__main__" :
    mainform()