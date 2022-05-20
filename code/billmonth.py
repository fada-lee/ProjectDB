from tkinter import*
from tkinter import ttk
from turtle import width

from PIL import Image,ImageTk
from DB import*


def mainBillhis():
    win=Tk()
    app = Billhismonth(win,'62050052','January 2022')
    win.mainloop()


class Billhismonth:
    def __init__(self,root,stuid,month):
        self.root = root
        self.root.title("Bill")
        self.root.geometry("380x780+0+0")
        self.root.option_add('*font', 'Hack 12 bold')
        self.stuid = stuid
        self.month = month
        self.var_rep = StringVar()


        # Code color
        global b ,f
        f="#403D3D" #สีเทาๆๆ ฟอนต์
        b = "#F2EBE3" #ส้มอ่อน
        be = "#F1F1F1" #พื้นหลังเทาอ่อน ให้กรอก

        self.bglimg=ImageTk.PhotoImage(file="Picture\Bills.png")
        self.bgllbl =Label(self.root, image=self.bglimg , bg=b )
        self.bgllbl.place(x=0,y=0) 

        self.root.iconbitmap('Picture\Billico.ico')

        #Frame
        #h=highlightbackground='red',highlightthickness=3
        framehead=Frame(self.root,bg = "#FFAF5E")
        framehead.place(x=0, y=0,width=380,height=70)

        frameinvoice=Frame(self.root,bg=b)
        frameinvoice.place(x=0, y=80,width=380,height=75)

        frametext=Frame(self.root,bg=b)
        frametext.place(x=0, y=155,width=380,height=240)

        frame4=Frame(self.root,bg=b)     
        frame4.place(x=0, y=380,width=380,height=50)

        frame5=Frame(self.root, bg=b)     
        frame5.place(x=0, y=410,width=380,height=180)

        head = Label(framehead, text="Bill payment history",font=('Hack', 17 ,'bold'), fg = "black",bg = "#FFAF5E")
        head.place(x=30,y=15)

        #============ดึงข้อมูลลลลล==============
        
        bk_id = DB_connect.bookingid(self.stuid)
        
        if bk_id != None :
            repair = DB_connect.repairhistory(self.month)
            self.billDB = DB_connect.billhistory(bk_id,self.month)
            dormDB=DB_connect.dormdata(bk_id) #(Bank, Bank_no, dormitory_name, Location, Tel, Water_p_u, Power_p_u, Bank_name)
            userinfo = DB_connect.name(self.stuid) #fname, lname, room_floor, room_number , room_price
            roominfo  = DB_connect.room(bk_id)

            # #frame Invoice
            titlelbl2 = Label(frameinvoice, text="Invoice", fg = "black",bg = b)
            titlelbl2.pack(padx=10,pady=0)

            billno = Label(frameinvoice, text="Bill No "+ str(self.billDB[0][0]), fg = "black",bg = b)
            billno.pack(padx=10,pady=0)

            billmounth = Label(frameinvoice, text=str(self.billDB[0][1]), fg = "black",bg = b)
            billmounth.pack(padx=10,pady=0)

            #frametext
            dormnamelbl = Label(frametext, text=("Dormitory: %3s\t\tBuilding: %s " %(dormDB[0][2],dormDB[0][8])), fg = "black",bg = b)
            dormnamelbl.place(x=15,y=10)

            roomlbl = Label(frametext, text=("Floor: %3s \t\t\tRoom: %3s " %(roominfo[0],roominfo[1])), fg = "black",bg = b)
            roomlbl.place(x=15,y=35)
            
            Lolbl = Message(frametext, text=  str(dormDB[0][3]), width=280, 
                relief=FLAT,  fg = "black",bg = b)
            Lolbl.place(x=50,y=70)

            self.locaimg=ImageTk.PhotoImage(file="Picture\loc.png")
            localbl =Label(frametext, image=self.locaimg , bg=b )
            localbl.img = self.locaimg
            localbl.place(x=7,y=70)

            tellbl = Label(frametext, text= dormDB[0][4], fg = "black",bg = b)
            tellbl.place(x=260,y=120)

            self.phone_img=ImageTk.PhotoImage(file="Picture\phone.png")
            self.phone_lbl=Label(frametext, image=self.phone_img ,bd=0, bg=b)
            self.phone_lbl.img = self.phone_img
            self.phone_lbl.place(x=230,y=120)

            emplbl = Label(frametext, text=self.billDB[0][7] ,fg = "black",bg = b)
            emplbl.place(x=50,y=122)

            if self.billDB[0][8] == 'male' or self.billDB[0][8] == 'm':
                self.empimg=ImageTk.PhotoImage(file="Picture\M.png")
            else: 
                self.empimg=ImageTk.PhotoImage(file="Picture\F.png")

            emplbl =Label(frametext, image=self.empimg , bg=b )
            emplbl.img = self.empimg
            emplbl.place(x=15,y=120) 

            banknolbl = Label(frametext, text="Bank No:  "+ dormDB[0][1],fg = "black",bg = b)
            banknolbl.place(x=15,y=175)

            banklbl = Label(frametext, text="Bank :  "+ dormDB[0][0],  fg = "black",bg = b)
            banklbl.place(x=15,y=155) 

            banknamelbl = Label(frametext, text="Bank Name:  "+ dormDB[0][7], fg = "black",bg = b)
            banknamelbl.place(x=15,y=195)

            #frame4
            namelbl =Label(frame4, text= userinfo[1]+ ' '+ userinfo[2] , fg = "black",bg = b)
            namelbl.place(x=15,y=0)

            sttlbl =Label(frame4, text="Status: "+ self.billDB[0][6], fg = "black",bg = "#FFAF5E")
            sttlbl.place(x=250,y=0)

            style = ttk.Style(root)
            style.theme_use("default")
            style.configure("Treeview",  background=b,foreground="black",font= ("Hack",10,'bold'), fieldbackground=b)
            style.configure('Treeview.Heading', font= ("Hack",10,'bold'), background="#FFAF5E")
            style.configure('.',borderwidth = 1) 

            displaybill= ttk.Treeview(frame5, columns= ('Desc', 'U_price', 'U_used', 'Am'))  
            #tv = ttk.Treeview(ws, columns=(1, 2, 3), show='headings', height=8)
            displaybill.column("#0", width=0,  stretch=NO)
            displaybill.column("Desc", width=110)
            displaybill.column("U_price",anchor=CENTER,width=80)
            displaybill.column("U_used",anchor=CENTER,width=80)
            displaybill.column("Am",anchor=CENTER,width=70)
            displaybill.heading("#0",text="")
            displaybill.heading("Desc",text="Description")
            displaybill.heading("U_price",text="Unit price")
            displaybill.heading("U_used",text="Unit of used")
            displaybill.heading("Am",text="Amount")
            displaybill.insert(parent='',index='end',iid=0,text='', 
                values=('Room ',str(roominfo[2]),'1', str(roominfo[2])),tags = ('a',))
            displaybill.insert(parent='',index='end',iid=1,text='', 
                values=('Electricity bills', str(dormDB[0][6]), str(self.billDB[0][5]-self.billDB[0][4]),
                (self.billDB[0][5]-self.billDB[0][4])*dormDB[0][6]))
            displaybill.insert(parent='',index='end',iid=2,text='', 
                values=(' Previous: ' +str(self.billDB[0][4]),'',''))
            displaybill.insert(parent='',index='end',iid=3,text='', 
                values=(' Latest: ' +str(self.billDB[0][5]) ,'',''))
            displaybill.insert(parent='',index='end',iid=4,text='', 
                values=('Water bills', str(dormDB[0][5]), str(self.billDB[0][3]-self.billDB[0][2]),
                (self.billDB[0][3]-self.billDB[0][2])*dormDB[0][5]))
            displaybill.insert(parent='',index='end',iid=5,text='', 
                values=(' Previous: ' +str(self.billDB[0][2]),'',''))
            displaybill.insert(parent='',index='end',iid=6,text='', 
                values=(' Latest: ' +str(self.billDB[0][3]) ,'',''))
            if repair[0][0] != None:
                displaybill.insert(parent='',index='end',iid=7,text='', 
                values=('Repair ','' ,'',repair[0][0]))
        else: pass            
        displaybill.tag_configure('a', background=b)
        displaybill.pack(padx=20)

        if repair[0][0] !=None:
            total = (roominfo[2])+((self.billDB[0][5]-self.billDB[0][4])*dormDB[0][6])+(self.billDB[0][3]-self.billDB[0][2])*dormDB[0][5] + repair[0][0]
            self.sttlbl =Label(self.root, text="Total amount due:  "+ str(total) ,font= ("Hack",12,'bold'), fg = "black",bg = b)
            self.sttlbl.place(x=150,y=600)
        else:
            # global total
            total = (roominfo[2])+((self.billDB[0][5]-self.billDB[0][4])*dormDB[0][6])+(self.billDB[0][3]-self.billDB[0][2])*dormDB[0][5]
            self.sttlbl =Label(self.root, text="Total amount due:  "+ str(total) ,font= ("Hack",12,'bold'), fg = "black",bg = b)
            self.sttlbl.place(x=150,y=600)


if __name__ == "__main__" :
    mainBillhis()
