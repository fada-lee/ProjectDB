from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import pymysql
from DB import*
from tkinter import filedialog
import random
from tkinter import messagebox 


def mainBillhis():
    win=Tk()
    app = Payment(win,'62050052')
    win.mainloop()

class Payment:
    def __init__(self,root,stuid):
        self.root = root
        self.root.title("Payment")
        self.root.geometry("380x780+0+0")
        self.root.option_add('*font', 'Hack 12 bold')
        self.root.configure(background='#F2EBE3')
        self.stuid = stuid
                # Code color
        global b ,f
        f="#403D3D" #สีเทาๆๆ ฟอนต์
        b = "#F2EBE3" #ส้มอ่อน
        be = "#F1F1F1" #พื้นหลังเทาอ่อน ให้กรอก

        self.bglimg=ImageTk.PhotoImage(file="Picture\Booking.png")
        bgllbl =Label(self.root, image=self.bglimg , bg=b )
        bgllbl.place(x=0,y=0) 

        self.root.iconbitmap('Picture\payico.ico')

        #Frame
        #h=highlightbackground='red',highlightthickness=3
        framehead=Frame(self.root,bg = "#FFAF5E")
        framehead.place(x=0, y=0,width=380,height=60)

        frame2=Frame(self.root,bg=b)
        frame2.place(x=0, y=60,width=380,height=90)

        frame3=Frame(self.root,bg=b)
        frame3.place(x=0, y=130,width=380,height=300)

        frame4=Frame(self.root,bg=b)     
        frame4.place(x=0, y=410,width=380,height=200)

        #self.frame5=Frame(self.root, bg=b)

        

        #============ดึงข้อมูลลลลล==============
        bk_id = DB_connect.bookingid(self.stuid)

        if bk_id != None:
            roominfo  = DB_connect.room(bk_id)
            self.billDB= DB_connect.bills(bk_id)
            if self.billDB != ():

                #Bill_No, date_format(Bill_date, '%%M %%Y'), Water_old, Water_new, Power_old, Power_new, Bill_status,Repair_price
                dormDB=DB_connect.dormdata(bk_id) #(Bank, Bank_no, dormitory_name, Location, Tel, Water_p_u, Power_p_u, Bank_name)
                userinfo = DB_connect.name(stuid) #fname, lname, room_floor, room_number , room_price
                self.repairid = DB_connect.repairid(stuid)
                if self.repairid !=():
                    self.repair = DB_connect.repair(stuid)
                    self.total = (roominfo[2])+((self.billDB[0][3]-self.billDB[0][2])*dormDB[0][5])+(self.billDB[0][5]-self.billDB[0][4])*dormDB[0][6]+self.repair[0][0]
                else: 
                    self.total = (roominfo[2])+((self.billDB[0][3]-self.billDB[0][2])*dormDB[0][5])+(self.billDB[0][5]-self.billDB[0][4])*dormDB[0][6]

                #Label
                titlelbl1 = Label(framehead, text="Payment",  font= ("Hack",17,'bold'), fg = "black",bg = "#FFAF5E")
                titlelbl1.place(x=30,y=15)

                innolbl = Label(frame2, text="Invoice No. " + self.billDB[0][0], fg = "black",bg = b)
                innolbl.place(x=10,y=10)

                namelbl =Label(frame2, text="Name: "+ userinfo[1]+ ' '+ userinfo[2] , fg = "black",bg = b)
                namelbl.place(x=10,y=40)

                self.totalimg=ImageTk.PhotoImage(file="Picture\Bgtotal.png")
                ttimglbl =Label(frame3, image=self.totalimg,bg= b )
                ttimglbl.pack(pady=30)

                totallbl =Label(frame3, text="Total Amount Due " ,  font= ("Hack",14,'bold'), fg = "black",bg = '#FFAF5E')
                totallbl.place(x=100,y=50)

                totallbl =Label(frame3, text=  self.total ,  font= ("Hack",20,'bold'), fg = "black",bg = '#FFAF5E')
                totallbl.place(x=160,y=80)


                #uploads
                self.bguplimg=ImageTk.PhotoImage(file="Picture\BGupload.png")
                bgupllbl =Button(frame3, image=self.bguplimg , bg=b,command = lambda:upload_file() ,bd=0)
                bgupllbl.pack(pady=0) 

                namelbl =Label(frame3, text="Attach proof of payment " ,  font= ("Hack",12,'bold'), fg = "black",bg = '#C7C7C7')
                namelbl.place(x=50,y=190)      



                def upload_file(): # Image upload and display
                    global filename,img
                    f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
                    filename = filedialog.askopenfilename(filetypes=f_types)
                    #img = ImageTk.PhotoImage(file=filename)
                    #b2 =Button(self.frame3,image=img) # using Button 
                    #b2.place(x=30,y=240)#display uploaded photo
                    self.namelbl =Label(frame3, text="Uploaded successfully              " ,  
                        font= ("Hack",12,'bold'), fg = "black",bg = '#C7C7C7')
                    self.namelbl.place(x=50,y=190) 
   

                self.dateimg=ImageTk.PhotoImage(file="Picture\date.png")
                self.date_lbl=Label(frame4, image=self.dateimg , bg=b)
                self.date_lbl.pack(pady=30)

                self.date_pay = datetime.today()
                date_month =Label(self.date_lbl,text=self.date_pay.strftime("%m"), font= ("Hack",14,"bold"), fg = f,bg= '#E6E6E6')
                date_month.place(x=100,y=60)
                date_Day =Label(self.date_lbl,text=self.date_pay.strftime("%d"), font= ("Hack",14,"bold"), fg = f,bg="#E6E6E6")
                date_Day.place(x=150,y=60)
                date_year =Label(self.date_lbl,text=self.date_pay.strftime("%Y"), font= ("Hack",14,"bold"), fg = f, bg="#E6E6E6")
                date_year.place(x=195,y=60)

        
    def addpayment(self): 
        payid=random.randint(10000,99999)

        if self.repairid !=():
            
            open_home = DB_connect.insertpaymemt(payid,self.date_pay,self.stuid,self.billDB[0][0],filename,self.total,self.repairid)
            return open_home
        else:
            open_home = DB_connect.insertpaymemt(payid,self.date_pay,self.stuid,self.billDB[0][0],filename,self.total,())
            return open_home
        
            

if __name__ == "__main__" :
    mainBillhis()
