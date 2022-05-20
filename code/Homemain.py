from tkinter import*
from PIL import Image,ImageTk
from matplotlib.pyplot import text
from DB import*
from Repair import*
from Home import*
from Setting import*
from Profile import*
from upbook import*
from billshowmonth import*
from billmonth import*
from bills import*
from payment import*
from Booking import*
from Booking2 import*
from Repairhis import*

def mainform():
    win=Tk()
    app = Mainform(win,'62050858')
    win.mainloop()


class Mainform:
    def __init__(self,root,stuid):
        self.root = root
        self.root.geometry("380x780+0+0")
        self.root.option_add('*font', 'Hack 12 bold')
        self.stuid = stuid
        self.root.iconbitmap('Picture\Dormico.ico')

        # Code color
        
        self.f="#403D3D"
        self.b = "#F1F1F1"
        self.be="#F2EBE3"

        global bk_id
        bk_id = DB_connect.bookingid(self.stuid)

        self.homeform()


    #=============================================== Home ======================================================

    def homeform(self):
        self.homepage=Homeform(self.root,stuid=self.stuid)
        #label 4 menu
        self.bk_img=ImageTk.PhotoImage(file="Picture\Bookingbtn.png")
        self.bk_btn=Button(self.root,image=self.bk_img ,bd=0 ,command=self.Bookings )
        self.bk_btn.place(x=10,y=310)

        self.pay_img=ImageTk.PhotoImage(file="Picture\Paymentbtn.png")
        self.pay_btn=Button(self.root, image=self.pay_img ,bd=0, command=self.Bills)
        self.pay_btn.place(x=190,y=310)

        self.rep_img=ImageTk.PhotoImage(file="Picture\Repairbtn.png")
        self.rep_btn=Button(self.root, image=self.rep_img ,bd=0,command=self.Repair)
        self.rep_btn.place(x=10,y=540)

        self.set_img=ImageTk.PhotoImage(file="Picture\Settingsbtn.png")
        self.set_btn=Button(self.root, image=self.set_img ,bd=0,command=self.Setting)
        self.set_btn.place(x=190,y=540)
        self.info()

    def info(self):   
        if bk_id !=None:
            self.billDB= DB_connect.bills(bk_id)
            if self.billDB != ():
                self.btninfo = ImageTk.PhotoImage(file="Picture\info.png")
                info_btn = Button(self.root, bd=0,image=self.btninfo,bg=self.b)
                info_btn.place(x=320,y=475)

    #============================================= Booking ====================================================
    def Bookings(self):
        bk_id = DB_connect.bookingid(self.stuid)
        if bk_id == None:
            self.bookingpage=Bookingform(self.root,stuid=self.stuid)
            self.findroomimg=ImageTk.PhotoImage(file="Picture\Btnfind.png")
            self.findroombtn = Button(self.root,image=self.findroomimg,bd=0 ,bg=self.be,command=self.nextt)
            self.findroombtn.place(x=120,y=210 )
        else :
            self.upbook()    
        self.back()
        self.homeB()
        self.repairB()
        self.bookingO()
        self.menuB()
        self.payB()

    def nextt(self):
        self.fr=Bookingform.findrooms(self)
        print(self.fr)
        if self.fr != 0: 
            self.nextimg = ImageTk.PhotoImage(file="Picture\BtnNext.png")
            self.bknext = Button(self.root, image= self.nextimg, bd=0,bg=self.be ,command=self.booking2)
            self.bknext.place(x=120,y=630 )
        self.back()
        self.homeB()
        self.repairB()
        self.bookingO()
        self.menuB()
        self.payB()
        
    def booking2(self):
        #Bookingform.tobk2()
        self.getvar=Bookingform.varr(self)
        self.buildingname= str(self.getvar[0])
        self.roomtype= str(self.getvar[1])
        self.numroom=str(self.getvar[2])


        self.bookingpage2=Bookingform2(self.root,stuid=self.stuid,bdn=self.buildingname,rt=self.roomtype,nr=self.numroom)

        self.conf_img=ImageTk.PhotoImage(file="Picture\confirmbtn.png")
        self.conf_btt=Button(self.root, image=self.conf_img ,bd=0, bg=self.be,command=self.addbooking)
        self.conf_btt.place(x=120,y=630) 

        self.bk2tobk1()
        self.homeB()
        self.repairB()
        self.bookingO()
        self.menuB()
        self.payB()
    
    def addbooking(self):
        open_home = self.bookingpage2.addbooking()
        if open_home>0:
            self.home()
        else:
            self.upbook()

    def bk2tobk1(self):
        self.btnback = ImageTk.PhotoImage(file="Picture\Back.png")
        back_btn = Button(self.root, bd=0,image=self.btnback,bg="#FFAF5E",
            activebackground="#FFAF5E",command=self.Bookings)
        back_btn.place(x=10,y=20) 

    #============================================= Repair ====================================================

    def Repair(self):
        self.repairpage=Repairform(self.root,stuid=self.stuid)

        self.btnrep = ImageTk.PhotoImage(file="Picture\confirmbtn.png")
        rep_btn = Button(self.root,command=self.rep, bd=0,image=self.btnrep,
            bg=self.be, activebackground=self.be)
        rep_btn.place(x=125,y=630)
        self.back()
        self.homeB()
        self.repairO()
        self.bookingB()
        self.menuB()
        self.payB()
    
    def rep(self):
        open_repair= self.repairpage.recordsrep()
        if open_repair==2:
            return
        else:
            if open_repair>0:
                self.home()
            else:
                self.Repair()



    #===============================================Setting========================================================================
    def Setting(self):
        self.setpage=Settingform(self.root,stuid=self.stuid)

        # Button
        proflie_btn = Button(self.root, bd=0,text= 'Edit profile', font= ('Hack 14 '),bg='#E6C2A2', 
            activebackground= '#E6C2A2', command=self.Profile)
        proflie_btn.place(x=10,y=250)

        update_btn = Button(self.root, bd=0,text= 'Edit room reservation', font= ('Hack 14 '),
            bg=self.be, activebackground=self.be, command=self.upbook)
        update_btn.place(x=10,y=310)

        bill_btn = Button(self.root, bd=0,text= 'Bill payment history', font= ('Hack 14 '),
            bg='#E6C2A2',activebackground='#E6C2A2',command=self.billshis)
        bill_btn.place(x=10,y=375)

        rephis_btn = Button(self.root, bd=0,text= 'Repair history', font= ('Hack 14 '),
            bg=self.be, activebackground=self.be, command=self.rephis)
        rephis_btn.place(x=10,y=435)

        self.back()
        self.homeB()
        self.repairB()
        self.bookingB()
        self.menuO()
        self.payB()

    #--------------------------------Repair history----------------------------------------------------------------------
    def rephis(self):
        self.rephis = RepairHistoryform(self.root,stuid=self.stuid)

        self.backset()
        self.homeB()
        self.repairB()
        self.bookingB()
        self.menuO()
        self.payB()

    #--------------------------------Profile----------------------------------------------------------------------
    def Profile(self):
        self.profilepage=Profileform(self.root,stuid=self.stuid)

        self.btnup = ImageTk.PhotoImage(file="Picture\Btnup.png")
        up_btn = Button(self.root,command=self.updata, bd=0,image=self.btnup,
            bg=self.be,activebackground=self.be)
        up_btn.place(x=125,y=630) 

        self.backset()
        self.homeB()
        self.repairB()
        self.bookingB()
        self.menuO()
        self.payB()

    def updata(self):
        open_admidprofile = self.profilepage.updatestudent()
        if open_admidprofile>0:
            self.Profile()
        else:
            self.Profile()

    #--------------------------------UpBookink----------------------------------------------------------------------
    def upbook(self):
        self.upbkpage = Upbookingform(self.root,stuid=self.stuid)

        self.btnup = ImageTk.PhotoImage(file="Picture\Btnup.png")
        up_btn = Button(self.root, bd=0,image=self.btnup,
            bg=self.be,activebackground=self.be,command=self.upbk)
        up_btn.place(x=30,y=630)

        self.btnout = ImageTk.PhotoImage(file="Picture\Out.png")
        out_btn = Button(self.root, bd=0,image=self.btnout,
            bg=self.be,activebackground=self.be,command=self.checkout)
        out_btn.place(x=200,y=630)
        
        self.backset()
        self.homeB()
        self.repairB()
        self.bookingB()
        self.menuO()
        self.payB()
    
    def upbk(self):
        open_upbk = self.upbkpage.updatebooks()
        if open_upbk>0:
            self.upbook()
        else:
            self.upbook()

    def checkout(self):
        open_upbk = self.upbkpage.Out()
        if open_upbk>0:
            self.Bookings()
        else:
            pass

    #--------------------------------------------------------------------
    def billshis(self):
        self.bilhis = Billhisform(self.root,stuid=self.stuid)
        
        if bk_id != None:
            bill = DB_connect.billmonth(bk_id)
            if bill != None:
                frame= Frame(self.root,bg = "#F2EBE3")
                frame.place(x=20, y=205,width=150,height=400)
                btn=[]
                for i in range(len(bill)):
                    btn.append(Button(frame, text=bill[i], bg="#F2EBE3" , font= ('Hack', 12, 'bold'),
                                        activebackground="#F2EBE3", activeforeground = "white",bd=0,
                                        command=lambda c=i: self.seebill(btn[c].cget("text"))))
                    btn[i].pack(padx=0,pady=1)
        self.backset()
        self.homeB()
        self.repairB()
        self.bookingB()
        self.menuO()
        self.payB()

    def seebill(self,m):
        Billhismonth(self.root,stuid=self.stuid,month=m)
        self.bglimg=ImageTk.PhotoImage(file="Picture\Box.png")
        self.bgllbl =Label(self.root, image=self.bglimg , bg=self.be )
        self.bgllbl.place(x=-10,y=702) 
        
        self.backbill()
        self.homeB()
        self.repairB()
        self.bookingB()
        self.menuO()
        self.payB()


    #======================================================= Bills =====================================================
    def Bills(self):
        if bk_id !=None:
            self.billDB= DB_connect.bills(bk_id) 
            if self.billDB != ():
                self.bill = Billsform(self.root,stuid=self.stuid)
                self.btnext = ImageTk.PhotoImage(file="Picture\BtnNext.png")
                next_btn = Button(self.root, bd=0,image=self.btnext,
                    bg=self.be,activebackground=self.be,command=self.pay)
                next_btn.place(x=120,y=635)
            else:
                self.bglimg=ImageTk.PhotoImage(file="Picture\Bgbk.png")
                bgllbl =Label(self.root, image=self.bglimg , bg="#F2EBE3" )
                bgllbl.place(x=0,y=0)
                head = Label(self.root, text="Bill",font=('Hack', 17 ,'bold'), fg = "black",bg = "#FFAF5E")
                head.place(x=50,y=15) 
                self.paidlbl = Label(self.root, text= "You already paid",   font= ("Hack",16,'bold'), fg = "black",bg = "#F2EBE3")
                self.paidlbl.place(x=107, y=330)
                self.viewlbl = Label(self.root, text= "View your ",   font= ("Hack",10,'bold'), fg = "black",bg = "#F2EBE3")
                self.viewlbl.place(x=120,y=360)
                self.hislbl = Button(self.root, text= "bills history",   font= ("Hack",10,'bold'), fg = "#FFAF5E",
                    bg = "#F2EBE3",activebackground= '#F2EBE3',activeforeground='#FFAF5E',bd=0,command=self.billshis)
                self.hislbl.place(x=190,y=360) 
        else:
            self.bill = Billsform(self.root,stuid=self.stuid)
        self.back()
        self.homeB()
        self.repairB()
        self.bookingB()
        self.menuB()
        self.payO()


    #----------------------------------Payment-------------------------
    #========== Functions Button ==================
    def pay(self):
        self.payments = Payment(self.root,stuid=self.stuid)
        self.nextimg = ImageTk.PhotoImage(file="Picture\confirmbtn.png")
        bknext = Button(self.root, image= self.nextimg,bd=0,bg="#F2EBE3" ,command=self.addpay)
        bknext.place(x=120,y=600 )
        self.backbillpay()
        self.homeB()
        self.repairB()
        self.bookingB()
        self.menuB()
        self.payO()

    def addpay(self):
        open_home = self.payments.addpayment()
        if open_home>0:
                self.home()
        else:
            self.Bills()


    def home(self):
        Mainform(self.root,stuid=self.stuid)

    def back(self):
        self.btnback = ImageTk.PhotoImage(file="Picture\Back.png")
        back_btn = Button(self.root, bd=0,image=self.btnback,bg="#FFAF5E",
            activebackground="#FFAF5E",command=self.home)
        back_btn.place(x=10,y=20) 

    def backset(self):
        self.btnback = ImageTk.PhotoImage(file="Picture\Back.png")
        back_btn = Button(self.root, bd=0,image=self.btnback,bg="#FFAF5E",
            activebackground="#FFAF5E",command=self.Setting)
        back_btn.place(x=10,y=20)

    def backbill(self):
        self.btnback = ImageTk.PhotoImage(file="Picture\Back.png")
        back_btn = Button(self.root, bd=0,image=self.btnback,bg="#FFAF5E",
            activebackground="#FFAF5E",command=self.billshis)
        back_btn.place(x=10,y=20)

    def backbillpay(self):
        self.btnback = ImageTk.PhotoImage(file="Picture\Back.png")
        back_btn = Button(self.root, bd=0,image=self.btnback,bg="#FFAF5E",
            activebackground="#FFAF5E",command=self.Bills)
        back_btn.place(x=10,y=20) 

    def bookingB(self):
        self.btnbk = ImageTk.PhotoImage(file="Picture\doorB.png")
        bk_btn = Button(self.root, bd=0,image=self.btnbk,bg=self.b,command=self.Bookings)
        bk_btn.place(x=0,y=725)

    def bookingO(self):
        self.btnbk = ImageTk.PhotoImage(file="Picture\doorO.png")
        bk_btn = Button(self.root, bd=0,image=self.btnbk,bg=self.b,command=self.Bookings)
        bk_btn.place(x=0,y=725)

    def repairB(self):
        self.btnrepair = ImageTk.PhotoImage(file="Picture\RepB.png")
        re_btn = Button(self.root, bd=0,image=self.btnrepair,bg=self.b,
            command=self.Repair, activebackground=self.b)
        re_btn.place(x=80,y=725)

    def repairO(self):
        self.btnrepair = ImageTk.PhotoImage(file="Picture\RepO.png")
        re_btn = Button(self.root, bd=0,image=self.btnrepair,bg=self.b)
        re_btn.place(x=80,y=725)

    def homeB(self):
        self.btnhome = ImageTk.PhotoImage(file="Picture\homeB.png")
        home_btn = Button(self.root, bd=0,image=self.btnhome,bg=self.b,command=self.home)
        home_btn.place(x=160,y=725) 

    def homeO(self):
        self.btnhome = ImageTk.PhotoImage(file="Picture\homeO.png")
        home_btn = Button(self.root, bd=0,image=self.btnhome,bg=self.b,command=self.home)
        home_btn.place(x=160,y=725) 

    def payB(self):
        self.btnpay = ImageTk.PhotoImage(file="Picture\walletB.png")
        pay_btn = Button(self.root, bd=0,image=self.btnpay,bg=self.b, command=self.Bills)
        pay_btn.place(x=250,y=725)
        if bk_id !=None:
            self.billDB= DB_connect.bills(bk_id)
            if self.billDB != ():
                self.btninfo = ImageTk.PhotoImage(file="Picture\info.png")
                info_btn = Button(self.root, bd=0,image=self.btninfo,bg=self.b)
                info_btn.place(x=285,y=717)

    def payO(self):
        self.btnpay = ImageTk.PhotoImage(file="Picture\walletO.png")
        pay_btn = Button(self.root, bd=0,image=self.btnpay,bg=self.b, command=self.Bills)
        pay_btn.place(x=250,y=725)

    def menuB(self):
        self.btnmenu = ImageTk.PhotoImage(file="Picture\menuB.png")
        menu_btn = Button(self.root, bd=0,image=self.btnmenu,bg=self.b,
            command=self.Setting, activebackground=self.b)
        menu_btn.place(x=320,y=725)

    def menuO(self):
        self.btnmenu = ImageTk.PhotoImage(file="Picture\menuO.png")
        menu_btn = Button(self.root, bd=0,image=self.btnmenu,bg=self.b,
            command=self.Setting, activebackground=self.b)
        menu_btn.place(x=320,y=725)



if __name__ == "__main__" :
    mainform()