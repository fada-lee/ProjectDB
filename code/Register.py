from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from DB import*




class Registerform:
    def __init__ (self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("380x780+0+0")
        self.root.option_add('*font', 'Hack 12 bold')


        f="#403D3D"
        b = "#F1F1F1"
        be = "#E6E6E6"

        #=============== Variables ===================
        self.var_student_id = StringVar()
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_password = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()

        self.bg=ImageTk.PhotoImage(file="Picture\Reg.png")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        # Main frame
        frame = Frame(self.root,bg = "#F1F1F1")
        frame.place(x=10, y=300,width=360,height=400)


        # Label and Entry
        student_id = Label(frame,text= "StudentId", fg =f,bg = b, bd =0)
        student_id.place(x=10,y=5)

        self.textstuid=Entry(frame,textvariable = self.var_student_id, fg = f,bg = be, bd =0)
        self.textstuid.place(x=130,y=0,width=400,height=30)

        fname = Label(frame,text= "First name", fg = f,bg = b, bd =0)
        fname.place(x=10,y=45)

        self.textfname=Entry(frame, textvariable=self.var_fname, fg = f,bg = be, bd =0)
        self.textfname.place(x=130,y=40,width=400,height=30)

        lname = Label(frame,text= "Last name", fg = f,bg = b, bd =0)
        lname.place(x=10,y=85)

        self.textlname=Entry(frame, textvariable=self.var_lname, fg = f,bg = be, bd =0)
        self.textlname.place(x=130,y=80,width=400,height=30)

        password = Label(frame,text= "Password", fg = f,bg = b, bd =0)
        password.place(x=10,y=125)

        self.textpass=Entry(frame, textvariable=self.var_password, fg = f,bg = be, bd =0)
        self.textpass.place(x=130,y=120,width=400,height=30)

        email = Label(frame,text= "Email", fg = f,bg = b, bd =0)
        email.place(x=10,y=165)

        self.textemail=Entry(frame, textvariable=self.var_email, fg = f,bg = be, bd =0)
        self.textemail.place(x=130,y=160,width=400,height=30)

        phone = Label(frame,text= "Phone number", fg = f,bg = b, bd =0)
        phone.place(x=10,y=205)

        self.textphone=Entry(frame,textvariable=self.var_phone, fg = f,bg = be, bd =0)
        self.textphone.place(x=130,y=200,width=400,height=30)

        #================= Checkbuttons ====================
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check,
            text= "I Agree The Terms & Conditions",
            font= ("Hack",8,"bold"), fg = f,bg = b, onvalue=1, offvalue=0, 
            activebackground=b,activeforeground=f)
        checkbtn.place(x=150,y=280)


        #=================== Register Button ===================
        self.btnsignup = ImageTk.PhotoImage(file="Picture\ButtonReg.png")
        register_btn = Button(frame,text="Register", 
            command=self.register_data,bd=0,image=self.btnsignup,bg =b)
        register_btn.place(x=130,y=320)

        textlogin = Label(frame,text= "ALREADY HAVE AN ACCOUNT?",
            font= ("Hack",10,"bold"), fg = f,bg =b, bd =0)
        textlogin.place(x=50,y=373)


    def register_data(self):
        DB_connect.Register( self.var_student_id,self.var_fname,
            self.var_lname, self.var_password,
            self.var_email,self.var_phone,self.var_check )
