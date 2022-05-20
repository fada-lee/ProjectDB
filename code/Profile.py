from tkinter import*
from PIL import Image,ImageTk


from DB import*

class Profileform:
    
    def __init__(self,root,stuid):
        self.root = root
        self.root.title("Edit Profile")
        self.root.geometry("380x780+0+0")
        self.root.option_add('*font', 'Hack 13 bold')

        self.stuid = stuid

        self.bg=ImageTk.PhotoImage(file="Picture\EditPf.png")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        self.root.iconbitmap('Picture\setico.ico')

          # Code color
        f="#403D3D"
        b="#F2EBE3"
        be="#E8DFD4" 
        bmenu = '#F1F1F1'

        # Main frame
        framehead= Frame(self.root,bg = bmenu)
        framehead.place(x=150, y=100,width=210,height=40)

        frametext= Frame(self.root,bg = bmenu)
        frametext.place(x=160, y=160,width=130,height=20)

        frametext2= Frame(self.root,bg = be)
        frametext2.place(x=160, y=200,width=230,height=20)

        frame= Frame(self.root,bg = b)
        frame.place(x=0, y=200,width=400,height=400)

        frame_menu= Frame(self.root,bg = bmenu)
        frame_menu.place(x=0, y=720,width=380,height=200)

        head = Label(self.root, text="Edit Profile",font= ('Hack 17 bold'), fg = "black",bg = "#FFAF5E")
        head.place(x=30,y=15)

        row=DB_connect.name(self.stuid)

        name = Label(framehead,text=(row[1],row[2]),font= ('Hack 15 bold'), fg = 'black',bg = bmenu, bd =0)
        name.place(x=0,y=15)

        id = Label(frametext,text=row[0],font= ('Hack 12 bold'), fg = 'black',bg = bmenu, bd =0)
        id.place(x=0,y=0)

        fname = Label(frame,text= "First name", fg = f,bg = b, bd =0)
        fname.place(x=20,y=20)

        self.textfname=Entry(frame, fg = f,bg = be, bd =0)
        self.textfname.place(x=20,y=45,width=320,height=35)

        lname = Label(frame,text= "Last name", fg = f,bg = b, bd =0)
        lname.place(x=20,y=85)

        self.textlname=Entry(frame, fg = f,bg = be, bd =0)
        self.textlname.place(x=20,y=110,width=320,height=35)

        password = Label(frame,text= "Password", fg = f,bg = b, bd =0)
        password.place(x=20,y=150)

        self.textpass=Entry(frame,show='*', fg = f,bg = be, bd =0)
        self.textpass.place(x=20,y=175,width=320,height=35)

        email = Label(frame,text= "Email", fg = f,bg = b, bd =0)
        email.place(x=20,y=215)

        self.textemail=Entry(frame, fg = f,bg = be, bd =0)
        self.textemail.place(x=20,y=240,width=320,height=35)

        phone = Label(frame,text= "Phone number", fg = f,bg = b, bd =0)
        phone.place(x=20,y=280)

        self.textphone=Entry(frame,font= ("Hack",12,"bold"), fg = f,bg = be, bd =0)
        self.textphone.place(x=20,y=305,width=320,height=35)

        #=============== Variables ===================
        self.textfname.insert(0,row[1])
        self.textlname.insert(0,row[2])
        self.textpass.insert(0,row[3])
        self.textemail.insert(0,row[4])
        self.textphone.insert(0,row[5])

        
        def on_entry_click1(event):
          if self.textfname.get() == row[1] :
              self.textfname.delete(0,END)
              self.textfname.insert(0,'')
        
        def on_entry_click2(event):
          if  self.textlname.get()  == row[2] :
              self.textlname.delete(0,END)
              self.textlname.insert(0,'')

        def on_entry_click3(event):
          if self.textpass.get() == row[3] :
              self.textpass.delete(0,END)
              self.textpass.insert(0,'')
        
        def on_entry_click4(event):
          if  self.textemail.get()  == row[4] :
              self.textemail.delete(0,END)
              self.textemail.insert(0,'')

        def on_entry_click5(event):
          if  self.textphone.get()  == row[5] :
              self.textphone.delete(0,END)
              self.textphone.insert(0,'')

        def on_exit1(event):
          if self.textfname.get()=='':
            self.textfname.insert(0,row[1])

        def on_exit2(event):
          if self.textlname.get()=='':
            self.textlname.insert(0,row[2])

        def on_exit3(event):
          if self.textpass.get()=='':
            self.textpass.insert(0,row[3])

        def on_exit4(event):
          if self.textemail.get()=='':
            self.textemail.insert(0,row[4])
        
        def on_exit5(event):
          if self.textphone.get()=='':
            self.textphone.insert(0,row[5])

        self.textfname.bind('<FocusIn>', on_entry_click1)
        self.textfname.bind('<FocusOut>',on_exit1)
        self.textlname.bind('<FocusIn>', on_entry_click2)
        self.textlname.bind('<FocusOut>',on_exit2)
        self.textpass.bind('<FocusIn>', on_entry_click3)
        self.textpass.bind('<FocusOut>',on_exit3)
        self.textemail.bind('<FocusIn>', on_entry_click4)
        self.textemail.bind('<FocusOut>',on_exit4)
        self.textphone.bind('<FocusIn>', on_entry_click5)
        self.textphone.bind('<FocusOut>',on_exit5)
 



    def updatestudent(self):
      if self.stuid=="" or self.textfname.get()=="" or self.textlname.get()==""\
            or self.textpass.get() =="" or self.textemail.get()=="" or self.textphone.get() =="":
            messagebox.showerror("Error","All field required")
            return -1
      else:
        open_home = messagebox.askyesno('????' ,'Do you want to update the information?')
        if open_home>0:
          self.phoneget=self.textphone.get()
          self.phonenum=self.phoneget[0:3]+self.phoneget[4:7]+self.phoneget[8:12]
          DB_connect.updateprofile(self.stuid,self.textfname.get(),self.textlname.get(),self.textpass.get(),
            self.textemail.get(),self.phonenum) 
          return open_home
        else: 
          if not open_home:
            return -1