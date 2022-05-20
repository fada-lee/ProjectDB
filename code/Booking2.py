
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from datetime import*
import random
from DB import*
#from Home import mainhome

def mainform():
    win=Tk()
    app = Bookingform2(win,'62050052','kmitla','air','102')
    win.mainloop()

class Bookingform2:
    def __init__(self,root,stuid,bdn,rt,nr):
        self.root = root
        self.root.title("Booking2")
        self.root.geometry("380x780+0+0")
        self.root.option_add('*font', 'Hack 12 bold')
        self.stuid = stuid
        self.root.configure(background='#F2EBE3')
        self.buildingget=bdn
        self.roomtypeget=rt
        self.numroom=nr
        #BG         
        self.bg=ImageTk.PhotoImage(file="Picture\Booking2.png")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        self.root.iconbitmap('Picture\Bookingico.ico')

        global b ,f
        f="#403D3D" #สีเทาๆๆ ฟอนต์
        b = "#F2EBE3" #ส้มอ่อน
        be = "#F1F1F1" #พื้นหลังเทาอ่อน ให้กรอก

        #FRAME
        self.framehead=Frame(self.root,bg = "#FFAF5E")
        self.framehead.place(x=0, y=0,width=380,height=60)
        self.frame2=Frame(self.root,bg=be)
        self.frame2.place(x=130, y=80,width=300,height=70)
        self.frame3=Frame(self.root,bg=be)
        self.frame3.place(x=0, y=165,width=380,height=27)
        self.frame4=Frame(self.root,bg=be)
        self.frame4.place(x=0, y=200,width=380,height=30)
        self.frameloca=Frame(self.root,bg=b)
        self.frameloca.place(x=90, y=250,width=165,height=100)



        # self.box_img=ImageTk.PhotoImage(file="Picture\Rect.png")
        # self.repno_lbl=Label(self.frame3, image=self.box_img ,bd=0, bg=b)
        # self.repno_lbl.place(x=0,y=0) 

        #=============== Variables ===================
        self.var_student_id = StringVar()
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var=StringVar()

    #     #--FRAME 1
        self.titlelbl1 = Label(self.framehead, text="Booking",  
            font= ("Hack",17,'bold'), fg = "black",bg = "#FFAF5E")
        self.titlelbl1.place(x=50,y=15)
        #--FRAME 2
        namedis = DB_connect.name(self.stuid)

        fname2 = Label(self.frame2,text= ( namedis[1],namedis[2]) , fg =f ,bg=be)
        fname2.place(x=0,y=10)
        fsid2 = Label(self.frame2,text= ( namedis[0]) , fg = f,bg=be)
        fsid2.place(x=0,y=40)

        fstel = Label(self.frame2,text= str(namedis[5]) , fg = f,bg=be)
        fstel.place(x=120,y=40)

        self.phone_img=ImageTk.PhotoImage(file="Picture\phone.png")
        self.phone_lbl=Label(self.frame2, image=self.phone_img ,bd=0, bg=be)
        self.phone_lbl.place(x=100,y=40)

        # self.linelbl = Label(self.frame3, text='-'*70 ,  font= ("Hack",12), fg = "black",bg='#D6D6D6')
        # self.linelbl.place(x=10,y=20)
        textvar = Label(self.frame3, text=('%15s %15s %15s %15s' %('Building','Type','Floor','Room')),fg = "black",bg = be)
        textvar.place(x=0,y=5)

        self.dnlbl = Label(self.frame4, text= ('%12s %20s %15s %22s' 
            %(self.buildingget,self.roomtypeget,str(self.numroom[0]),str(self.numroom) )), fg = f,bg=be)
        self.dnlbl.place(x=0,y=0)

        location = DB_connect.location(self.buildingget)

        Lolbl = Message(self.frameloca, text=  str(location[0][0]), width=165, font= ('Hack 11 bold'),fg = "black",bg = b)
        Lolbl.place(x=0,y=10)


      
        pricepowwat = DB_connect.dataroom(self.buildingget,self.roomtypeget) 

        textwater = Label(self.root, text='Water', fg = f,bg = b )
        textwater.place(x=290,y=270)

        water = Label(self.root, text=(pricepowwat[0][2]),font=('Hack', 15 ,'bold') , fg = f,bg = "#E8DFD4"  )
        water.place(x=290,y=320)
        
        textpower = Label(self.root, text='Power', fg = f,bg = b )
        textpower.place(x=275,y=390)

        power = Label(self.root, text= (pricepowwat[0][1]),font=('Hack', 15 ,'bold'), fg = f,bg = "#E8DFD4"  )
        power.place(x=295,y=440)

        textprice = Label(self.root, text='Price', fg = f,bg = b )
        textprice.place(x=280,y=510)

        price = Label(self.root, text=(pricepowwat[0][0]),font=('Hack', 15 ,'bold'), fg = f,bg = "#E8DFD4"  )
        price.place(x=280,y=555)

          

        # self.prlbl = Label(self.root, text= ('Price:%60s Bath' %str(pricepowwat[0][0])) , fg = "black" ,bg=b)
        # self.prlbl.place(x=10,y=260)
        # self.pwlbl = Label(self.frame4, text= 'Power/p/u:%53s Bath' %str(pricepowwat[0][1]), fg = "black" ,bg=b)
        # self.pwlbl.place(x=10,y=30)
        # self.wtlbl = Label(self.frame4, text= 'Water/p/u:%54s Bath' %str(pricepowwat[0][2]), fg = "black" ,bg=b)
        # self.wtlbl.place(x=10,y=50)

 

        chI = Label(self.root,text= " Check In" , fg = "black",bg=b)
        chI.place(x=30,y=333) 

        self.dateimg=ImageTk.PhotoImage(file="Picture\dateb.png")

        self.checkIn_lbl=Label(self.root, image=self.dateimg ,bd=0)
        self.checkIn_lbl.place(x=20,y=360)

        self.dateMIN = Entry(self.checkIn_lbl,font= ("Hack",12,"bold"), fg = f ,bg = "#E6E6E6", relief=FLAT)
        self.dateMIN.place(x=73,y=40,width=25,height=30)

        self.dateDIN = Entry(self.checkIn_lbl,font= ("Hack",12,"bold"), fg = f ,bg = "#E6E6E6", relief=FLAT)
        self.dateDIN.place(x=110,y=40,width=25,height=30)

        self.dateYIN = Entry(self.checkIn_lbl,font= ("Hack",12,"bold"), fg = f ,bg = "#E6E6E6", relief=FLAT)
        self.dateYIN.place(x=150,y=40,width=40,height=30)
        #self.chIdate=



        chO = Label(self.root,text= " Check Out" , fg = "black",bg=b)
        chO.place(x=30,y=483) 

        self.checkout_lbl=Label(self.root, image=self.dateimg ,bd=0)
        self.checkout_lbl.place(x=20,y=510)

        self.dateMOUT = Entry(self.checkout_lbl, fg = f ,bg = "#E6E6E6", relief=FLAT)
        self.dateMOUT.place(x=73,y=40,width=25,height=30)

        self.dateDOUT = Entry(self.checkout_lbl, fg = f ,bg = "#E6E6E6", relief=FLAT)
        self.dateDOUT.place(x=110,y=40,width=25,height=30)

        self.dateYOUT = Entry(self.checkout_lbl, fg = f ,bg = "#E6E6E6", relief=FLAT)
        self.dateYOUT.place(x=150,y=40,width=40,height=30)

        self.date_Re = datetime.today()
        date_month =self.date_Re.strftime("%m")
        date_Day = self.date_Re.strftime("%d")
        date_year =self.date_Re.strftime("%Y")
        date_yearout =int(self.date_Re.strftime("%Y")) +4

        self.dateDIN.insert(0,date_Day)
        self.dateMIN.insert(0,date_month)
        self.dateYIN.insert(0,date_year)

        self.dateDOUT.insert(0,date_Day)
        self.dateMOUT.insert(0,date_month)
        self.dateYOUT.insert(0,date_yearout)

        def on_exit1(event):
          if self.dateDIN.get()=='':
             self.dateDIN.insert(0,date_Day)

        def on_exit2(event):
          if self.dateMIN.get()=='':
             self.dateMIN.insert(0,date_month)
        def on_exit3(event):
          if self.dateYIN.get()=='':
             self.dateYIN.insert(0,date_year)

        def on_exit4(event):
          if self.dateDOUT.get()=='':
             self.dateDOUT.insert(0,date_Day)

        def on_exit5(event):
          if self.dateMOUT.get()=='':
             self.dateMOUT.insert(0,date_month)

        def on_exit6(event):
          if self.dateYOUT.get()=='':
             self.dateYOUT.insert(0,date_yearout)

        self.dateDIN.bind('<FocusOut>',on_exit1)
        self.dateMIN.bind('<FocusOut>',on_exit2)
        self.dateYIN.bind('<FocusOut>',on_exit3)
        self.dateDOUT.bind('<FocusOut>',on_exit4)
        self.dateMOUT.bind('<FocusOut>',on_exit5)
        self.dateYOUT.bind('<FocusOut>',on_exit6)
 

    def addbooking(self):

        #Booking_id, Booking_date, CheckIn, CheckOut, Student_id, Dormitory_name, room_number
        bkid = random.randint(00000,99999)
        date_booking = datetime.today()
        checkIN = (str(self.dateYIN.get())+'-'+(str(self.dateMIN.get()))+'-'+(str(self.dateDIN.get())))
        checkOut = (str(self.dateYOUT.get())+'-'+(str(self.dateMOUT.get()))+'-'+(str(self.dateDOUT.get())))

        DB_connect.insertbookings(bkid,date_booking,checkIN,checkOut,self.stuid,self.buildingget,self.numroom)
        open_home = messagebox.askyesno('SUCCESS' ,'Report a successful booking.\nGo back home?')
        return open_home
if __name__ == "__main__" :
    mainform()