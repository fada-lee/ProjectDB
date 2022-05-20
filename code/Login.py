from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from DB import*
from Homemain import*


def mainlogin():
    global win,app
    win=Tk()
    app = Loginform(win)
    win.mainloop()

class Loginform:
    
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("380x780+0+0")
        self.root.option_add('*font', 'Hack 12 bold')
        self.root.iconbitmap('Picture\Dormico.ico')

        # Code color

        f="#403D3D"
        b = "#F1F1F1"
        be = "#E6E6E6"

        self.bg=ImageTk.PhotoImage(file="Picture\Login.png")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        self.root.configure(background='#F1F1F1')

        # Main frame

        frame = Frame(self.root,bg = "#F1F1F1")
        frame.place(x=10, y=370,width=360,height=330)

        #label

        studentid = Label(frame, text="StudentID", fg = f,bg = b)
        studentid.place(x=15,y=0)

        self.stuid=Entry(frame,font= ("Hack",12,"bold"), fg = f,bg = be, bd =0)
        self.stuid.place(x=15,y=30,width=320,height=40)

        password = Label(frame, text="Password", fg = f,bg = b)
        password.place(x=15,y=80)

        self.textpass=Entry(frame, show="*", fg = f,bg =be,bd=0)
        self.textpass.place(x=15,y=110,width=320,height=40)

        # Login Button
        
        self.btnsignin = ImageTk.PhotoImage(file="Picture\ButtonLogin.png")
        login_btn = Button(frame,command=self.signin, bd=0,image=self.btnsignin)
        login_btn.place(x=130,y=200)      

        # Register Button
        register_btn = Button(frame,command=self.Register_win,text="SIGNUP", 
            bd=0, font= ("Hack",10,"bold"),fg = "#ff9900", bg = b, 
            activeforeground="#ff9900",activebackground=b)
        register_btn.place(x=200,y=280)

        register_lbl = Label(frame,text="NEW USER?", font= ("Hack",10,"bold"), fg=f,bg = b )
        register_lbl.place(x=120,y=281)

        # Forgetpass Button
        forgetpass_btn = Button(frame,text="FORGET PASSWORD?",
            command=self.forgot_password, bd=0,
             font= ("Hack",8,"bold"), fg = f,bg = "#F1F1F1", 
             activeforeground=f,activebackground="#F1F1F1")
        forgetpass_btn.place(x=220,y=155)

    def signin(self):
        if self.stuid.get()=="" or self.textpass.get() == "":
            messagebox.showerror("Error","All field required")
        else:
            row = DB_connect.Login(self.stuid.get(),self.textpass.get())
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                self.Home()
            
    def Home(self):
        self.app=Mainform(self.root,stuid=self.stuid.get())

    def Register_win(self):
        self.app=Registerform(self.root)
        pass

    def forgot_password(self):
        if self.stuid.get() =="" :
            messagebox.showerror("Error","Please Enter the Email address to reset password ")
        else:
            row = DB_connect.forgot_pass(self.stuid.get())
            print("StudentId: "+ row[0]) 
            print("Name: "+ row[1]+" "+ row[2])
            print("Password: "+ row[3])
        


#============================ Register ====================================

class Registerform:
    def __init__ (self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("380x780+0+0")
        self.root.option_add('*font', 'Hack 12 bold')
        self.root.iconbitmap('Picture\Dormico.ico')

        #=============== Variables ===================
        self.var_student_id = StringVar()
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_password = StringVar()
        self.var_repassword = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()

        # Code color

        f="#403D3D"
        b = "#F1F1F1"
        be = "#E6E6E6"

        self.bg=ImageTk.PhotoImage(file="Picture\Reg.png")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        # Main frame
        frame = Frame(self.root,bg = "#F1F1F1")
        frame.place(x=10, y=300,width=360,height=450)


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

        self.textpass=Entry(frame, textvariable=self.var_password,show='*', fg = f,bg = be, bd =0)
        self.textpass.place(x=130,y=120,width=400,height=30)

        repassword = Label(frame,text= "Repassword", fg = f,bg = b, bd =0)
        repassword.place(x=10,y=165)

        self.textrepass=Entry(frame, textvariable=self.var_repassword,show='*', fg = f,bg = be, bd =0)
        self.textrepass.place(x=130,y=160,width=400,height=30)

        email = Label(frame,text= "Email", fg = f,bg = b, bd =0)
        email.place(x=10,y=205)

        self.textemail=Entry(frame, textvariable=self.var_email, fg = f,bg = be, bd =0)
        self.textemail.place(x=130,y=200,width=400,height=30)

        phone = Label(frame,text= "Phone number", fg = f,bg = b, bd =0)
        phone.place(x=10,y=245)

        self.textphone=Entry(frame,textvariable=self.var_phone, fg = f,bg = be, bd =0)
        self.textphone.place(x=130,y=240,width=400,height=30)

        #================= Checkbuttons ====================
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check,
            text= "I Agree The Terms & Conditions",
            font= ("Hack",8,"bold"), fg = f,bg = b, onvalue=1, offvalue=0, 
            activebackground=b,activeforeground=f)
        checkbtn.place(x=150,y=290)


        #=================== Register Button ===================
        self.btnsignup = ImageTk.PhotoImage(file="Picture\ButtonReg.png")
        register_btn = Button(frame,text="Register", 
            command=self.register_data,bd=0,image=self.btnsignup,bg =b)
        register_btn.place(x=130,y=320)

        textlogin = Label(frame,text= "ALREADY HAVE AN ACCOUNT?",
            font= ("Hack",10,"bold"), fg = f,bg =b, bd =0)
        textlogin.place(x=50,y=393)

        login_btn = Button(frame,text="SIGN IN",command=self.Login_win, 
            bd=0, font= ("Hack",10,"bold"),fg = "#ff9900",bg = b,
            activeforeground="#ff9900",activebackground=b)
        login_btn.place(x=250,y=390)



    def register_data(self):
        if self.var_student_id.get()=="" or self.var_fname.get()=="" or self.var_lname.get()==""\
            or self.var_password.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="":
            messagebox.showerror("Error","All field required")

        elif len(self.var_student_id.get()) !=8 or len(self.var_phone.get()) !=10:
            messagebox.showerror("Error","Please check the student_id or phone again.\n whether the lack or excess")

        elif self.var_password.get() != self.var_repassword.get():
            messagebox.showerror("Error","Please check your passwords do not match.")

        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")

        else:
            DB_connect.Register( self.var_student_id.get(),self.var_fname.get(),
            self.var_lname.get(), self.var_password.get(),self.var_email.get(),self.var_phone.get())
            open_home = messagebox.askyesno("Success","Register Successfully\nDo you want to log in?")
            if open_home>0:
                self.Home()
            else:
                self.Login_win()

    def Login_win(self):
        self.app=Loginform(self.root)

    def Home(self):
        self.app=Mainform(self.root,stuid=self.var_student_id.get())

if __name__ == "__main__" :
    mainlogin()