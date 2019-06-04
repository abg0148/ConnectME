import networkx as nx
import matplotlib.pyplot as plt
import os
from tkinter import *
import pandas as pd
import pickle
 
G=nx.DiGraph()

def add_path(x,y,w):
    if(str(x) in users):
        if(str(y) in users):
            G.add_edge(str(x),str(y),weight=int(str(w)))
        else:
            print(y,'not present in users')
    else:
        print(x,'not present in users')
        
def add_user(x):
    if(str(x) not in users):
        users.append(str(x))
        G.add_node(str(x))

def display_users():
    a=str(users)
    messagebox.showinfo('USERS',a)

def display_userdata():
    a=str(user_data)
    messagebox.showinfo('USER_DATA',a)


def remove_user(x):
    if(str(x) in users):
        G.remove_node(str(x))

def isPresent(x):
    if(str(x) in users):
        return True
    else:
        return False
    
def showShortestPath(x,y):
    if(str(x) in users):
        if(str(y) in users):
            try:
                print(nx.dijkstra_path(G,str(x),str(y)))
            except Exception:
                print('no path found')
        else:
            print(y,'not present in users')
    else:
        print(x,'not present in users')

def DisplayGraph():
    pos=nx.circular_layout(G)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    nx.draw(G,pos, with_labels=True)
    plt.suptitle('USER GRAPH')
    plt.show()
    

def register():
    if(str(nameE.get()) not in users):
        add_user(nameE.get())
        user_data[str(nameE.get())]=str(passwordE.get())
        return 1
    else:
        messagebox.showinfo('ERROR!!','User Already Exists. Try a different Username')
        return 0

def login(username,password):
    if(str(username) in users):
        if(user_data.get(str(username))==str(password)):
            return 1
        else:
            messagebox.showinfo('ERROR!!','INCORRECT CREDENTIALS')
            return 0
    else:
        messagebox.showinfo('ERROR!!','INCORRECT CREDENTIALS')
        return 0

def afterLogin():
    if(nameLogin.get()=='admin' and login(nameLogin.get(),pwordLogin.get())):
##        r.destroy()

        def show():
            DisplayGraph()
            
        root=Tk()
        root.title('Admin')
        fr00=Frame(root,bg="lightgoldenrod")

        fr00.pack()

        
        graphButton=Button(fr00,text="DISPLAY GRAPH",bg="green2",fg="white", font="Courier 12 bold", command= DisplayGraph)
        graphButton.configure(width=30,height=1)
        graphButton.pack()

        usersButton=Button(fr00,text="USERS",bg="green2",fg="white", font="Courier 12 bold", command= display_users)
        usersButton.configure(width=30,height=1)
        usersButton.pack()

        userdataButton=Button(fr00,text="USER DATA",bg="green2",fg="white", font="Courier 12 bold", command= display_userdata)
        userdataButton.configure(width=30,height=1)
        userdataButton.pack()

        exitButton=Button(fr00,text="LOGOUT",bg="indian red",fg="white", font="Courier 12 bold", command= root.destroy)
        exitButton.configure(width=30,height=1)
        exitButton.pack()

        root.resizable(0,0)
        root.mainloop()

        
        
##        ex=0
##        while(ex!=1):
##            print('1. Show Graph')
##            print('2. Users')
##            print('3. User Data')
##            print('4. exit')
##            k=int(input())
##            if(k==1):
##                show()
##            if(k==2):
##                print(users)
##            if(k==3):
##                print(user_data)
##            if(k==4):
##                ex=1
##            
            
    elif(login(nameLogin.get(),pwordLogin.get())):

        def add_friend():
            add_path(friendnameInput.get(),str(nameLogin.get()),ratingInput.get())

        def findPath():
            showShortestPath(str(nameLogin.get()),pathtoInput.get())
        
##        r.destroy()

        root=Tk()
        root.title('USER')
        kfr00=Frame(root,bg="lightgoldenrod")
        kfr0l=Frame(kfr00,bg="light goldenrod")
        kfr0r=Frame(kfr00,bg="white")
        #left frames
        kfr1=Frame(kfr0l,bg="white")
        kfr2=Frame(kfr0l,bg="azure3")

        kfr20=Frame(kfr2,bg="azure3")
        kfr21=Frame(kfr2,bg="azure3")
        kfr22=Frame(kfr2,bg="azure3")
        kfr23=Frame(kfr2,bg="azure3")
        kfr24=Frame(kfr2,bg="azure3")

        kfr00.pack()

        kfr0l.pack(side=LEFT)
        kfr0r.pack(side=LEFT)

        kfr1.pack()
        kfr2.pack()

        kfr20.pack()
        kfr21.pack()
        kfr22.pack()
        kfr23.pack()
        kfr24.pack()

        #right frames
        krfr1=Frame(kfr0r,bg="white")
        krfr2=Frame(kfr0r,bg="azure3")

        krfr20=Frame(krfr2,bg="azure3")
        krfr21=Frame(krfr2,bg="azure3")
        krfr22=Frame(krfr2,bg="azure3")
        krfr23=Frame(krfr2,bg="azure3")
        krfr24=Frame(krfr2,bg="azure3")

        krfr1.pack()
        krfr2.pack()

        krfr20.pack()
        krfr21.pack()
        krfr22.pack()
        krfr23.pack()
        krfr24.pack()


        #rate a friend
        klabel1=Label(kfr1,text="RATE A FRIEND", bg='powder blue', fg='white', font="Courier 20 bold")
        klabel1.config(height=2,width=30)
        keL1=Label(kfr20,text="",bg="azure3")
        keL1.config(height=1,width=40)
        friendname=Label(kfr21,text="Friend's name:",bg="azure3")
        friendname.config(height=3,width=25)
        rating=Label(kfr22,text="Scale of Friendship (0 - 10):",bg="azure3")
        rating.config(height=3,width=25)
        friendnameInput=Entry(kfr21,bg="white")
        friendnameInput.config(width=15)
        ratingInput=Entry(kfr22,bg="white",fg="green")
        ratingInput.config(width=15)
        addfriendbutton=Button(kfr23,text="RATE",bg="green2",fg="white", font="Courier 12 bold", command= add_friend)
        addfriendbutton.configure(width=10,height=1)
        keL2=Label(kfr24,text="",bg="azure3")
        keL2.config(height=1,width=40)

        klabel1.pack()
        keL1.pack()
        friendname.pack(side=LEFT)
        friendnameInput.pack(side=LEFT)
        rating.pack(side=LEFT)
        ratingInput.pack(side=LEFT)
        addfriendbutton.pack()
        keL2.pack()

        #find path
        krlabel1=Label(krfr1,text="FIND PATH", bg='pale turquoise', fg='white', font="Courier 20 bold")
        krlabel1.config(height=2,width=30)
        kreL1=Label(krfr20,text="",bg="azure3")
        kreL1.config(height=1,width=40)
        pathto=Label(krfr21,text="Path to (Friend's name):",bg="azure3")
        pathto.config(height=3,width=25)

        pathtoInput=Entry(krfr21,bg="white")
        pathtoInput.config(width=15)

        el3=Label(krfr22,text="",bg="azure3")
        el3.config(height=3)
        
        pathtobutton=Button(krfr23,text="Find Path To:",bg="DarkOliveGreen4",fg="white", font="Courier 12 bold", command= findPath)
        pathtobutton.configure(width=25,height=1)
        kreL2=Label(krfr24,text="",bg="azure3")
        kreL2.config(height=1,width=40)

        krlabel1.pack()
        kreL1.pack()
        pathto.pack(side=LEFT)
        pathtoInput.pack(side=LEFT)
        el3.pack()
        pathtobutton.pack()
        kreL2.pack()


            
        exitbutton = Button(root,text='LOGOUT',width =5, bg="indian red", fg="white", font="Courier 12 bold" , command=root.destroy)
        exitbutton.configure(width=10,height=1)
        kexitLabel=Label(root,text="", font="Courier 8 bold")
        exitbutton.configure(height=1)

        exitbutton.pack(side=RIGHT)

        kexitLabel.pack(side=LEFT,fill=X)
        #EB.pack()


        root.resizable(0,0)    
        root.mainloop()

        
        

        ex=0
        
##        while(ex!=1):
##            print('what do you wanna do?')
##            print('1. Add Friend')
##            print('2. Find Path')
##            print('3. Logout')
##            k=int(input())
##            if(k==1):
##                print('enter friend name')
##                b=str(input())
##                print('enter how close your friendship is on a scale of 1-10')
##                c=10-int(input())
##                add_friend(b,c)
##            if(k==2):
##                print('enter the username of person you want to find')
##                b=str(input())
##                findPath(b)
##            if(k==3):
##                ex=1
user_pass_data=[]
weight_data=[]
users=['admin']
user_data={'admin':'a'}

try:
    with open("user_pass_data_3.txt","rb") as fp:
        user_pass_data=pickle.load(fp)
except Exception:
    print('no data to read')
    

try:
    with open("weight_data_3.txt","rb") as fp:
        weight_data=pickle.load(fp)
except Exception:
    print('no data to read')
    
for i in user_pass_data:
    add_user(str(i))
    user_data[str(i)]=user_pass_data[str(i)]

for k in weight_data:
    add_path(k[0],k[1],k[2]['weight'])



r=Tk()
r.title('ConnectME')
fr00=Frame(r,bg="lightgoldenrod")
fr0l=Frame(fr00,bg="light goldenrod")
fr0r=Frame(fr00,bg="white")
#left frames
fr1=Frame(fr0l,bg="white")
fr2=Frame(fr0l,bg="azure3")

fr20=Frame(fr2,bg="azure3")
fr21=Frame(fr2,bg="azure3")
fr22=Frame(fr2,bg="azure3")
fr23=Frame(fr2,bg="azure3")
fr24=Frame(fr2,bg="azure3")

fr00.pack()

fr0l.pack(side=LEFT)
fr0r.pack(side=LEFT)

fr1.pack()
fr2.pack()

fr20.pack()
fr21.pack()
fr22.pack()
fr23.pack()
fr24.pack()

#right frames
rfr1=Frame(fr0r,bg="white")
rfr2=Frame(fr0r,bg="azure3")

rfr20=Frame(rfr2,bg="azure3")
rfr21=Frame(rfr2,bg="azure3")
rfr22=Frame(rfr2,bg="azure3")
rfr23=Frame(rfr2,bg="azure3")
rfr24=Frame(rfr2,bg="azure3")

rfr1.pack()
rfr2.pack()

rfr20.pack()
rfr21.pack()
rfr22.pack()
rfr23.pack()
rfr24.pack()


#signup
label1=Label(fr1,text="SIGN UP", bg='blue', fg='white', font="Courier 20 bold")
label1.config(height=3,width=30)
eL1=Label(fr20,text="",bg="azure3")
eL1.config(height=1,width=23)
userLabel=Label(fr21,text="Username",bg="azure3")
userLabel.config(height=3,width=8)
passLabel=Label(fr22,text="Password",bg="azure3")
passLabel.config(height=3,width=8)
nameE=Entry(fr21,bg="white")
nameE.config(width=15)
passwordE=Entry(fr22,bg="white",fg="green")
passwordE.config(width=15)
signupButton=Button(fr23,text="REGISTER",bg="green2",fg="white", font="Courier 12 bold", command= register)
signupButton.configure(width=10,height=1)
eL2=Label(fr24,text="",bg="azure3")
eL2.config(height=1,width=23)

label1.pack()
eL1.pack()
userLabel.pack(side=LEFT)
nameE.pack(side=LEFT)
passLabel.pack(side=LEFT)
passwordE.pack(side=LEFT)
signupButton.pack()
eL2.pack()

#signin
rlabel1=Label(rfr1,text="SIGN IN", bg='black', fg='white', font="Courier 20 bold")
rlabel1.config(height=3,width=30)
reL1=Label(rfr20,text="",bg="azure3")
reL1.config(height=1,width=23)
ruserLabel=Label(rfr21,text="Username",bg="azure3")
ruserLabel.config(height=3,width=8)
rpassLabel=Label(rfr22,text="Password",bg="azure3")
rpassLabel.config(height=3,width=8)
nameLogin=Entry(rfr21,bg="white")
nameLogin.config(width=15)
pwordLogin=Entry(rfr22,bg="white",fg="green", show='*')
pwordLogin.config(width=15)
loginButton=Button(rfr23,text="LOGIN",bg="DarkOliveGreen4",fg="white", font="Courier 12 bold", command= afterLogin)
loginButton.configure(width=10,height=1)
reL2=Label(rfr24,text="",bg="azure3")
reL2.config(height=1,width=23)

rlabel1.pack()
reL1.pack()
ruserLabel.pack(side=LEFT)
nameLogin.pack(side=LEFT)
rpassLabel.pack(side=LEFT)
pwordLogin.pack(side=LEFT)
loginButton.pack()
reL2.pack()




def endingFunction():
    # save user_data
    with open("user_pass_data_3.txt","wb") as fp:
        pickle.dump(user_data,fp)
        
    li=[(u,v,d) for (u,v,d) in G.edges(data=True)]
    #save list
    with open("weight_data_3.txt","wb") as fp:
        pickle.dump(li,fp)
  
    r.destroy()
    
EB = Button(r,text='EXIT',width =5, bg="indian red", fg="white", font="Courier 12 bold" , command=endingFunction)
EB.configure(width=10,height=1)
exitLabel=Label(r,text="Created By: ABHINAV GUPTA & ABHINAV CHOUDHARY", font="Courier 8 bold")
EB.configure(height=1)

EB.pack(side=RIGHT)

exitLabel.pack(side=LEFT,fill=X)
#EB.pack()


r.resizable(0,0)    
r.mainloop()



