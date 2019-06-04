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
            
        root = Tk()
        root.title('Admin')
        root.configure(background = '#fcf594')
        root.geometry('300x50')
        graphButton = Button(root, text = 'Show Graph', command = DisplayGraph,)
        graphButton.grid(row = 0, column = 1, sticky = W)
        #graphButton.pack()
        usersButton = Button(root, text = 'Users', command = display_users)
        usersButton.grid(row = 0, column = 2, sticky = W)
        #usersButton.pack()
        userdataButton = Button(root, text = 'User Data', command = display_userdata)
        userdataButton.grid(row = 0, column = 3, sticky = W)
        #userdataButton.pack()
        exitButton = Button(root, text = 'Exit', command = root.destroy)
        exitButton.grid(row = 0, column = 4, columnspan = 3, sticky = W)
        #exitButton.pack()
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

        root = Tk()
        root.title('Login Page')
        root.configure(background = "#fcf594")
        root.geometry('300x180')
        friendname = Label(root, text="Friend's name:  ",bg ="#fcf594")
        friendname.grid(row = 1, column = 0)
        rating = Label(root, text='Scale of Friendship (0 - 10):  ',bg ="#fcf594")
        rating.grid(row = 2, column = 0)
        #friendname.pack()
        #rating.pack() 
     
        friendnameInput = Entry(root)
        friendnameInput.grid(row = 1, column = 1)
        ratingInput = Entry(root)
        ratingInput.grid(row = 2, column = 1)
        #friendnameInput.pack()
        #ratingInput.pack() 
        addfriendbutton = Button(root, text='Add Friend', width = 10, command = add_friend)
        addfriendbutton.grid(row = 3, column = 1)
        #addfriendbutton.pack()

        pathto = Label(root, text = "Path to (Friend's name): ",bg ="#fcf594")
        pathto.grid(row = 4, column = 0, sticky = W)
        #pathto.pack()

        pathtoInput = Entry(root)
        pathtoInput.grid(row = 4, column = 1)
        #pathtoInput.pack()
        pathtobutton = Button(root, text = 'Find path to: ', width = 10, command = findPath)
        pathtobutton.grid(row = 6, column = 1)
        #pathtobutton.pack()

        exitbutton = Button(root, text = 'EXIT', width = 5, command = root.destroy)
        exitbutton.grid(row =8, column = 1)
        #exitbutton.pack()

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



r = Tk()
r.title('ConnectME')
r.geometry('300x300')
r.configure(bg = '#fcf594')
intruction = Label(r, text='SIGN UP',bg ="#fcf594")
intruction.grid(row = 0, column = 1)
#intruction.pack()
nameL = Label(r, text='New Username: ',bg ="#fcf594")
nameL.grid(row = 1) 
passwordL = Label(r, text='New Password: ',bg ="#fcf594")
passwordL.grid(row = 2)
#nameL.pack()
#passwordL.pack() 
 
nameE = Entry(r)
nameE.grid(row = 1, column = 1)
passwordE = Entry(r, show='*')
passwordE.grid(row = 2, column = 1)
#nameE.pack()
#passwordE.pack() 
signupButton = Button(r, text='Signup', width = 5, command = register)
signupButton.grid(row =3)
#signupButton.pack()



loginInstruction = Label(r, text='LOG IN \n',bg ="#fcf594")
loginInstruction.grid(row = 4, column = 1, columnspan = 2, sticky = S)
#loginInstruction.pack()
nameL = Label(r, text='Username: ',bg ="#fcf594")
nameL.grid(row = 5)
pwordL = Label(r, text='Password: ',bg ="#fcf594")
pwordL.grid(row = 6)
#nameL.pack() 
#pwordL.pack() 
 
nameLogin = Entry()
nameLogin.grid(row = 5, column = 1)
pwordLogin = Entry(r, show='*')
pwordLogin.grid(row = 6, column = 1)
#nameLogin.pack()
#pwordLogin.pack() 
 
loginButton = Button(r, text='Login', width = 5, command = afterLogin)
loginButton.grid(row = 7)
#loginButton.pack()

def endingFunction():
    # save user_data
    with open("user_pass_data_3.txt","wb") as fp:
        pickle.dump(user_data,fp)
        
    li=[(u,v,d) for (u,v,d) in G.edges(data=True)]
    #save list
    with open("weight_data_3.txt","wb") as fp:
        pickle.dump(li,fp)
  
    r.destroy()
    
EB = Button(r,text='EXIT',width =5,command=endingFunction)
EB.grid(row = 8)
#EB.pack()


    
r.mainloop()



