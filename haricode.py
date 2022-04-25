from tkinter import *
vegitablelist=[]
vegitablequantity=[]
vegitableid=[]
username=[]
userpassword=[]
adminname=[]
adminpassword=[]
cart=[]
end=-1
adminend=-1
userend=-1
temp=1
cartend=-1
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
                    insert.destroy()
                    Userlogin()
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
    global end
    global vegitablelist
    global vegitablequantity
    global vegitableid
    def insertelement():
        global end
        global vegitablelist
        global vegitablequantity
        global vegitableid
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
    def logoutt():
        alogin.destroy()
        login()
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
    Button(alogin,text="LOGOUT",command=logoutt).pack()
    alogin.mainloop()
def Userlogin():
    global end
    global vegitablelist
    global vegitablequantity
    global vegitableid
    def shoppingcartt():
        ulogin.destroy()
        shoppingcart()
    def logoutt():
        ulogin.destroy()
        login()
    def addtocart():
        global end
        global vegitablelist
        global vegitablequantity
        global vegitableid
        def addtocartt():
            global end
            global vegitablelist
            global vegitablequantity
            global vegitableid
            global cart
            global cartend
            global temp
            for item in Lb.curselection():
                temp=item
                if vegitablequantity[temp]>int(q.get()):
                    for i in range(cartend+1):
                        if(cart[i][0]==vegitableid[item]):
                            Label(aoc,text="this item is already in cart").pack()
                            return
                    temp1=[vegitableid[item],vegitablelist[item],int(q.get())]
                    cart.append(temp1)
                    cartend=cartend+1
                    aoc.destroy()
                else:
                    Label(aoc,text="your requirement exceeds the maximum quantity").pack()
        aoc=Tk()
        aoc.title("add to cart")
        Label(aoc,text="Enter the quantity you want to buy").pack()
        q=Entry(aoc)
        q.pack()
        Button(aoc,text="Add",command=addtocartt).pack()
        aoc.mainloop()
    ulogin=Tk()
    ulogin.title("USER")
    ulogin.geometry("600x600")
    Lb=Listbox(ulogin,width=50,height=20)
    Lb.pack()
    for i in range (end+1):
            Lb.insert(END,"id:  "+str(vegitableid[i])+"      name:  "+vegitablelist[i]+"      Available:  "+str(vegitablequantity[i])+"kg")
    Button(ulogin,text="ADD TO CART",command=addtocart).pack()
    Button(ulogin,text="GO TO CART",command=shoppingcartt).pack()
    Button(ulogin,text="LOGOUT",command=logoutt).pack()
    ulogin.mainloop()
def shoppingcart():
    global end
    global vegitablelist
    global vegitablequantity
    global vegitableid
    global cart
    global cartend
    global temp
    def continueshopping():
        scart.destroy()
        Userlogin()
    def removecart():
        global cart
        global cartend
        global temp
        del cart[temp]
        cartend=cartend-1
        Lb.delete(ANCHOR)
    def buyallitems():
        global end
        global vegitablelist
        global vegitablequantity
        global vegitableid
        global cart
        global cartend
        for i in range(cartend+1):
            for j in range(end+1):
                if(cart[i][0]==vegitableid[j]):
                    if(cart[i][2]<vegitablequantity[j]):
                        vegitablequantity[j]=vegitablequantity[j]-cart[i][2]
                        Lb.delete(0,END)
                        cart.clear()
                        cartend=-1
                    else:
                        Label(scart,text="Some item in your cart exceeds the maximum quantity available")
    scart=Tk()
    scart.title("SHOPPING CART")
    scart.geometry("600x600")
    Lb=Listbox(scart,width=50,height=20)
    Lb.pack()
    for item in Lb.curselection():
        temp=item
    for i in range (cartend+1):
            Lb.insert(END,"id:  "+str(cart[i][0])+"      name:  "+cart[i][1]+"      Available:  "+str(cart[i][2])+"kg")
    Button(scart,text="REMOVE FROM CART",command=removecart).pack()
    Button(scart,text="BUY ALL ITEMS",command=buyallitems).pack()
    Button(scart,text="CONTINUE SHOPPING",command=continueshopping).pack()
    scart.mainloop()
login()
