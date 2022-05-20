from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from turtle import rt
from PIL import Image,ImageTk
from datetime import*

from click import command
from DB import*
#from Home import mainhome

def mainbooking():
    win=Tk()
    app = Bookingform(win,'62050052')
    win.mainloop()

class Bookingform:
    def __init__(self,root,stuid):
        self.root = root
        self.root.title("Booking")
        self.root.geometry("380x780+0+0")
        self.root.configure(background='#F2EBE3')
        self.stuid = stuid        
        self.Numroom = StringVar()
        # Code color
        global b ,f ,be
        f="#403D3D" #สีเทาๆๆ ฟอนต์
        b = "#F2EBE3" #ส้มอ่อน
        be = "#F1F1F1" #พื้นหลังเทาอ่อน ให้กรอก



        #BG HOME        
        self.bg=ImageTk.PhotoImage(file="Picture\Bgbk.png")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        self.root.iconbitmap('Picture\Bookingico.ico')

        #Frame
        #h=highlightbackground='red',highlightthickness=3
        self.framehead=Frame(self.root,bg = "#FFAF5E")
        self.framehead.place(x=0, y=0,width=380,height=60)
        self.frame2=Frame(self.root,bg=b)
        self.frame2.place(x=0, y=80,width=380,height=130)
        self.frame3=Frame(self.root,bg=b)
        self.frame3.place(x=0, y=210,width=380)
        self.frame4=Frame(self.root,bg=b)     
        self.frame4.place(x=10, y=280,width=360,height=200)

        #Label
        self.titlelbl1 = Label(self.framehead, text="Booking",font= ("Hack",17,"bold"), fg = "black",bg = "#FFAF5E")
        self.titlelbl1.place(x=50,y=15)

        # the following alters the Combobox entry field

        ebg = "#FFAF5E"
        fg = 'black'
        style = ttk.Style()
        style.theme_use('alt')

        style.map('TCombobox', fieldbackground=[('readonly', ebg)] , selectbackground=[('readonly', ebg)] ,selectforeground=[('readonly', fg)]
                        , background=[('readonly', ebg)] , foreground=[('readonly', fg)])

        #Combobox

        global dormname

        def building(*args):
            global buildingname
            build_name = DB_connect.getbuilding(self.dormstrv.get(),typestrv.get())
            build_name2=["Select Building"]

            for i in range(len(build_name)):
                build_name2.append(build_name[i])
            buildingname=ttk.Combobox(self.frame2,font=("Hack",13,"bold") ,width=35, state='readonly',value=build_name2)
            buildingname.current(0)
            buildingname.place(x=22,y=90)


        def defroomtype(*args):
            global roomtype,typestrv
            typestrv = StringVar()
            room_type = DB_connect.getroomtype(self.dormstrv.get())
            room_type2=["Select Room Type"]
            for i in range(len(room_type)):
                room_type2.append(room_type[i])
            roomtype=ttk.Combobox(self.frame2,font=("Hack",13,"bold"),textvariable=typestrv,width=35,state='readonly',value=room_type2)
            roomtype.current(0)        
            roomtype.place(x=22,y=48)
            typestrv.trace('w', building)



        self.dormstrv = StringVar()
        dorm_name = DB_connect.getdorm()
        self.dorm_name2=["Select Dormitory"]
        for i in range(len(dorm_name)):
            self.dorm_name2.append(dorm_name[i])
        dormname=ttk.Combobox(self.frame2,font=("Hack",13,"bold") ,textvariable=self.dormstrv,width=35, state='readonly',value=self.dorm_name2)
        dormname.current(0)
        dormname.pack(padx=10,pady=5)
        self.dormstrv.trace('w', defroomtype)   

        self.room_type2=["Select Room Type"]
        roomtype=ttk.Combobox(self.frame2,font=("Hack",13,"bold"),width=35,state='readonly',value=self.room_type2)
        roomtype.current(0)        
        roomtype.place(x=22,y=48)

        build_name2=["Select Building"]
        buildingname=ttk.Combobox(self.frame2,font=("Hack",13,"bold") ,width=35, state='readonly',value=build_name2)
        buildingname.current(0)
        buildingname.place(x=22,y=90)

        #self.rt.trace('w',self.building) textvariable=self.rt


        #self.findbd=ImageTk.PhotoImage(file="Picture\Find.png")
        #self.btnbd = Button(self.frame2,bd=0 ,image=self.findbd,bg=b,command=self.building)
        #self.btnbd.pack(padx=5,pady=1)


        
        
    def findrooms(self):
        
        self.findr_img = ImageTk.PhotoImage(file="Picture\Bgroom.png")
        if dormname.get()=="Select Dormitory" or roomtype.get()=="Select Room Type" or buildingname.get()=="Select Building":
            messagebox.showerror("Error","All field required") 
        else:
            global froom
            froom = DB_connect.findroom(dormname.get(),roomtype.get(),str(dormname.get()+buildingname.get()))

            #print(froom)
            if len(froom) == 0:
                textvar =Label(self.root,text= "No room available", fg ='black',bg = b, bd =0)
                textvar.place(x=120,y=430)
                return 0

            else:  
            
                # froom_bg = Label(self.root,image = self.findr_img)
                # froom_bg.place(x=15,y=300)#FFB97B
                self.frnumroom=Frame(self.root,bg="#F4CBA6")
                self.frnumroom.place(x=25, y=300,width=325,height=90)
                froomlbl=Label(self.frnumroom,text="Please choose a room number",  font= ("Hack",12,'bold'), fg = "black",bg="#F4CBA6")
                froomlbl.pack(pady=10)
                #====
                scframe = VerticalScrolledFrame(self.root)
                scframe.place(x=25, y=350)
                #======          

                global btn
                btn=[]
                r,c=0,0
                width=5
                for i in range(len(froom)): 
                    #btn.append(Button(self.frame4, text=froom[i],command=se))
                    btn.append(Button(scframe.interior, text=froom[i], bg='white' ,width=4,height=2,bd=2,font=("Hack",10),relief=GROOVE, activebackground="#FFAF5E",
                                        activeforeground = "white",command=lambda c=i: se(btn[c].cget("text"))))        
                    btn[i].grid(row=r, column=c,padx=10,pady=5, sticky=N+S+E+W)
                    c+=1
                    if c==width:
                        r+=1
                        c=0


            def se(r):
                global numroom
                numroom=r
                rnlbl = Label(self.root, text="You choose room number: "+ str(numroom)+"    |    Floor : "+ str(numroom[0]) ,  font= ("Hack",10,'bold'), fg = "black",bg="#F4CBA6")
                rnlbl.place(x=40,y=312)


    def varr(self):
        self.bd=str(dormname.get()+buildingname.get())
        self.rt=roomtype.get()
        self.nr=numroom
        return self.bd,self.rt,self.nr


class VerticalScrolledFrame(Frame):
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)            

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,bg='#FFB97B',
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas,bg='#FFB97B')
        interior_id = canvas.create_window(0, 0, window=interior, anchor=NW)
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        # def _configure_canvas(event):
        #     if interior.winfo_reqwidth() != canvas.winfo_width():
        #         # update the inner frame's width to fill the canvas
        #         canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        # canvas.bind('<Configure>', _configure_canvas)
        






if __name__ == "__main__" :
    mainbooking()
