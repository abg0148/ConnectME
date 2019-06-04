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
            G.add_edge(str(x),str(y),weight=int(w))
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
    pos=nx.spring_layout(G)
    nx.draw(G,pos, with_labels=True)
    plt.draw()
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
        root.geometry('500x500')
        graphButton = Button(root, text = 'Show Graph', command = DisplayGraph)
        graphButton.pack()
        usersButton = Button(root, text = 'Users', command = display_users)
        usersButton.pack()
        userdataButton = Button(root, text = 'User Data', command = display_userdata)
        userdataButton.pack()
        exitButton = Button(root, text = 'Exit', command = root.destroy)
        exitButton.pack()
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
        root.title('People Graph')
        root.geometry('500x500')
        friendname = Label(root, text="Friend's name:  ") 
        rating = Label(root, text='Scale of Friendship:  ')
        friendname.pack()
        rating.pack() 
     
        friendnameInput = Entry(root)
        ratingInput = Entry(root) 
        friendnameInput.pack()
        ratingInput.pack() 
        addfriendbutton = Button(root, text='Add Friend', width = 10, command = add_friend)
        addfriendbutton.pack()

        pathto = Label(root, text = 'Path to: ')
        pathto.pack()

        pathtoInput = Entry(root)
        pathtoInput.insert(0, "Friend's name")
        pathtoInput.pack()
        pathtobutton = Button(root, text = 'Find path to: ', width = 10, command = findPath)
        pathtobutton.pack()

        exitbutton = Button(root, text = 'EXIT', width = 5, command = root.destroy)
        exitbutton.pack()

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
    with open("user_pass_data.txt","rb") as fp:
        user_pass_data=pickle.load(fp)
except Exception:
    print('no data to read')
    

try:
    with open("weight_data.txt","rb") as fp:
        weight_data=pickle.load(fp)
except Exception:
    print('no data to read')
    
for i in user_pass_data:
    add_user(str(i))
    user_data[str(i)]=user_pass_data[str(i)]

for k in weight_data:
    add_path(k[0],k[1],k[2])



r = Tk()
r.title('People Graph')
r.geometry('300x300')
intruction = Label(r, text='SIGN UP')
intruction.pack()
nameL = Label(r, text='New Username: ') 
passwordL = Label(r, text='New Password: ')
nameL.pack()
passwordL.pack() 
 
nameE = Entry(r)
passwordE = Entry(r, show='*') 
nameE.pack()
passwordE.pack() 
signupButton = Button(r, text='Signup', width = 5, command = register)
signupButton.pack()



loginInstruction = Label(r, text='Please enter your login details\n')
loginInstruction.pack()
nameL = Label(r, text='Username: ') 
pwordL = Label(r, text='Password: ')
nameL.pack() 
pwordL.pack() 
 
nameLogin = Entry(r) 
pwordLogin = Entry(r, show='*') 
nameLogin.pack()
pwordLogin.pack() 
 
loginButton = Button(r, text='Login', width = 5, command = afterLogin)
loginButton.pack()

def endingFunction():
    # save user_data
    with open("user_pass_data.txt","wb") as fp:
        pickle.dump(user_data,fp)
        
    li=[(u,v,d) for (u,v,d) in G.edges(data=True)]
    #save list
    with open("weight_data.txt","wb") as fp:
        pickle.dump(li,fp)
  
    r.destroy()
    
EB = Button(r,text='EXIT',width =5,command=endingFunction)
EB.pack()


    
r.mainloop()



