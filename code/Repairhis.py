from tkinter import*
from tkinter import ttk
from turtle import width

from PIL import Image,ImageTk
from DB import*


def mainBillhis():
    win=Tk()
    app = RepairHistoryform(win,'62050858')
    win.mainloop()


class RepairHistoryform:
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
        self.bg=ImageTk.PhotoImage(file="Picture\EditPF.png")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        self.root.iconbitmap('Picture\setico.ico')

        # Main frame
        frame= Frame(self.root,bg = be)
        frame.place(x=110, y=80,width=300,height=50)

        frametext= Frame(self.root,bg = be)
        frametext.place(x=110, y=125,width=250,height=20)

        frametext2= Frame(self.root,bg = be)
        frametext2.place(x=110, y=160,width=230,height=20)


        Setting = Label(self.root, text="Repair History", font= ("Hack",17,"bold"), fg = "black",bg = "#FFAF5E")
        Setting.place(x=30,y=15)

        row = DB_connect.name(self.stuid)

        name = Label(frame, text=(row[1],row[2]), font= ("Hack",14,"bold"), fg = "black",bg = be)
        name.place(x=0,y=0)

        texstuid = Label(frame, text=self.stuid, font='Hack 10 bold',fg = "black",bg = be)
        texstuid.place(x=0,y=25)

        textvar = Label(frametext, text=('Dormitory\tFloor\tRoom'),font='Hack 11 bold', fg='black',bg = be)
        textvar.place(x=0,y=0)

        bk_id = DB_connect.bookingid(self.stuid)
        
        if bk_id != None:
            textdata = DB_connect.dormitory(bk_id)

            if textdata != None:
                textdorm = Label(frametext2, text=("%s %20s %15s "%(textdata[0]+' '+textdata[1],textdata[2],textdata[3])),
                font='Hack 11 bold', fg='black',bg =be)
                textdorm.place(x=0,y=0)


                style = ttk.Style(root)
                style.theme_use("default")
                style.configure("Treeview",  background=b,foreground="black",font= ("Hack",10,'bold'), fieldbackground=b)
                style.configure('Treeview.Heading', font= ("Hack",10,'bold'), background="#FFAF5E")
                style.configure('.',borderwidth = 1) 
                displaybill= ttk.Treeview(self.root, columns= ('Date', 'Name', 'Price', 'Status'))  
                #tv = ttk.Treeview(ws, columns=(1, 2, 3), show='headings', height=8)
                displaybill.column("#0", width=0,  stretch=NO)
                displaybill.column("Date", width=80)
                displaybill.column("Name",anchor=CENTER,width=100)
                displaybill.column("Price",anchor=CENTER,width=80)
                displaybill.column("Status",anchor=CENTER,width=70)
                displaybill.heading("#0",text="")
                displaybill.heading("Date",text="Date")
                displaybill.heading("Name",text="Name")
                displaybill.heading("Price",text="Price")
                displaybill.heading("Status",text="Status")

                repair = DB_connect.showRepair(bk_id)
                if repair != ():
                    for i in range(len(repair)): 
                        displaybill.insert(parent='',index='end',iid=i,text='', 
                        values=(repair[i][0],repair[i][1],repair[i][2],repair[i][3]))          
                displaybill.tag_configure('a', background=b)
                displaybill.pack(padx=20,pady=220)


if __name__ == "__main__" :
    mainBillhis()