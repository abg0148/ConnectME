import networkx as nx
import matplotlib.pyplot as plt
G=nx.DiGraph()

users=['admin']
user_data={'admin':'abhinav'}

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

def register(username,password):
    if(str(username) not in users):
        add_user(username)
        user_data[str(username)]=str(password)
        return 1
    else:
        return 0

def login(username,password):
    if(str(username) in users):
        if(user_data.get(str(username))==str(password)):
            return 1
        else:
            print('INCORRECT PASSWORD')
            return 0
    else:
        print('INCORRECT USERNAME')
        return 0

def afterLogin(username,password):
    if(username=='admin' and login(username,password)):
        def show():
            DisplayGraph()
        ex=0
        while(ex!=1):
            print('1. Show Graph')
            print('2. Users')
            print('3. User Data')
            print('4. exit')
            k=int(input())
            if(k==1):
                show()
            if(k==2):
                print(users)
            if(k==3):
                print(user_data)
            if(k==4):
                ex=1
            
            
    elif(login(username,password)):
        def add_friend(b,c):
            add_path(b,str(username),c)

        def findPath(b):
            showShortestPath(str(username),b)

        ex=0
        
        while(ex!=1):
            print('what do you wanna do?')
            print('1. Add Friend')
            print('2. Find Path')
            print('3. Logout')
            k=int(input())
            if(k==1):
                print('enter friend name')
                b=str(input())
                print('enter how close your friendship is on a scale of 1-10')
                c=10-int(input())
                add_friend(b,c)
            if(k==2):
                print('enter the username of person you want to find')
                b=str(input())
                findPath(b)
            if(k==3):
                ex=1
        
            


        
    
    
    



    
    
    
    
        
