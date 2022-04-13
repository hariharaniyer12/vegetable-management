from tkinter import *
vegitablelist=[]
vegitablequantity=[]
vegitableid=[]
username=[]
userpassword=[]
adminname=[]
adminpassword=[]
end=-1
adminend=-1
userend=-1
temp=1
def login():
    def choice(value):
        global temp
        if value==1:
            temp=1
        else:
            temp=2
    def signuppp():
        insert.destroy()
        signup()
    def loginn():
        global adminend
        global userend
        global username
        global adminname
        global userpassword
        global adminpassword
        global temp
        if(temp==1):
            for i in range (userend+1):
                if(username[i]==n.get() and userpassword[i]==p.get()):
                    print("login successful")
                else:
                    Label(insert,text="Either password or login is wrong").pack()
        else:
            for i in range (adminend+1):
                if(adminname[i]==n.get() and adminpassword[i]==p.get()):
                    insert.destroy()
                    Adminlogin()
                else:
                    Label(insert,text="Either password or login is wrong").pack()
                
    insert=Tk()
    insert.title("LOGIN")
    insert.geometry("300x200")
    Label(insert, text="Enter the following details").pack()
    Label(insert ,text="Username:").pack()
    n=Entry(insert ,width="40")
    n.pack()
    Label(insert ,text="Password:").pack()
    p=Entry(insert,width="40")
    p.pack()
    s=IntVar()
    #s.set(1)
    Radiobutton(insert,text="User account",variable=s,value=1,command=lambda:choice(s.get())).pack()
    Radiobutton(insert,text="Admin account",variable=s,value=2,command=lambda:choice(s.get())).pack()
    Button(insert,text="Login",command=loginn).pack()
    Button(insert,text="Signup",command=signuppp).pack()
    insert.mainloop()
def signup():
    def choice(value):
        global temp
        if value==1:
            temp=1
        else:
            temp=2
    def loginnn():
        insert.destroy()
        login()
    def signupp():
        global adminend
        global userend
        global username
        global adminname
        global userpassword
        global adminpassword
        global temp
        if(temp==1):
            for i in range (userend+1):
                if username[i]==n.get():
                    Label(insert,text="this Username already exists").pack()
                    return
                
            username.append(n.get())
            userpassword.append(p.get())
            Label(insert,text="Account created").pack()
            userend=userend+1
        else:
            for i in range (adminend+1):
                if adminname[i]==n.get():
                    Label(insert,text="this Username already exists").pack()
                    return
                
            adminname.append(n.get())
            adminpassword.append(p.get())
            Label(insert,text="Account created").pack()
            adminend=adminend+1
                
    insert=Tk()
    insert.title("SIGN UP")
    insert.geometry("300x200")
    Label(insert, text="Enter the following details").pack()
    Label(insert ,text="Username:").pack()
    n=Entry(insert ,width="40")
    n.pack()
    Label(insert ,text="Password:").pack()
    p=Entry(insert,width="40")
    p.pack()
    r=IntVar()
    #r.set(1)
    Radiobutton(insert,text="User account",variable=r,value=1,command=lambda:choice(r.get())).pack()
    Radiobutton(insert,text="Admin account",variable=r,value=2,command=lambda:choice(r.get())).pack()
    Button(insert,text="Create account",command=signupp).pack()
    Button(insert,text="go to login page",command=loginnn).pack()
    insert.mainloop()
def Adminlogin():
    def insertelement():
        def insertt():
            global end
            global vegitablelist
            global vegitablequantity
            global vegitableid
            for i in range (end+1):
                if(vegitableid[i]==int(ui.get())):
                    Label(insert, text="id already exists").pack()
                    return
            end=end+1
            vegitablelist.append(u.get())
            vegitablequantity.append(int(q.get()))
            vegitableid.append(int(ui.get()))
            Lb.insert(END,"id:  "+ui.get()+"      name:  "+u.get()+"      Available:  "+q.get()+"kg")
        insert=Tk()
        insert.title("ADD VEGETABLE")
        insert.geometry("300x200")
        Label(insert, text="ADD VEGETABLE").pack()
        Label(insert ,text="VEGETABLE ID:").pack()
        ui=Entry(insert ,width="40")
        ui.pack()
        Label(insert ,text="VEGETABLE NAME:").pack()
        u=Entry(insert,width="40")
        u.pack()
        Label(insert ,text="QUANTITY:").pack()
        q=Entry(insert,width="40")
        q.pack()
        Button(insert ,text="ADD VEGETABLE",command=insertt).pack()
        insert.mainloop()
    def delete():
        global vegitablelist
        global vegitablequantity
        global vegitableid
        for item in Lb.curselection():
            del vegitablelist[item]
            del vegitableid[item]
            del vegitablequantity[item]
        Lb.delete(ANCHOR)
    def update():
        def updatee():
            global vegitablelist
            global vegitablequantity
            global vegitableid
            for item in Lb.curselection():
                if(u.get()!=""):
                    vegitablelist[item]=u.get()
                if(ui.get()!=""):
                    for i in range (end+1):
                        if(vegitableid[i]==int(ui.get())):
                            Label(insert,text="id already exists").pack()
                            return
                    vegitableid[item]=int(ui.get())
                if(q.get()!=""):
                    vegitablequantity[item]=int(q.get())
                Lb.insert(item,"id:  "+str(vegitableid[item])+"      name:  "+vegitablelist[item]+"      Available:  "+str(vegitablequantity[item])+"kg")
            Lb.delete(ANCHOR)
            insert.destroy()
                
        insert=Tk()
        insert.title("ADD VEGETABLE")
        insert.geometry("300x300")
        Label(insert ,text="UPDATE").pack()
        Label(insert, text="Selected item: "+Lb.get(ANCHOR)).pack()
        Label(insert ,text="VEGETABLE ID:").pack()
        ui=Entry(insert ,width="40")
        ui.pack()
        Label(insert ,text="VEGETABLE NAME:").pack()
        u=Entry(insert,width="40")
        u.pack()
        Label(insert ,text="QUANTITY:").pack()
        q=Entry(insert,width="40")
        q.pack()
        Button(insert ,text="UPDATE",command=updatee).pack()
        insert.mainloop()
    alogin=Tk()
    alogin.title("ADMIN")
    alogin.geometry("600x600")
    Lb=Listbox(alogin,width=50,height=20)
    Lb.pack()
    for i in range (end+1):
            Lb.insert(END,"id:  "+vegitableid[i]+"      name:  "+vegitablelist[i]+"      Available:  "+vegitablequantity[i]+"kg")
    Button(alogin,text="ADD VEGETABLES",command=insertelement).pack()
    Button(alogin,text="REMOVE VEGETABLES",command=delete).pack()
    Button(alogin,text="UPDATE VEGETABLES",command=update).pack()
    alogin.mainloop()
login()
