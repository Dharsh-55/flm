import matplotlib.pyplot as mc
import numpy as n
import mysql.connector as m
import tkinter as tk
from tabulate import tabulate
from PIL import ImageTk,Image
x=m.connect(host='localhost',user='root',passwd='sd55',database='preml')
y=x.cursor() 

def ts():
    #print('helllo') 
    j=i.get()
    if j==1:
        p=ImageTk.PhotoImage(Image.open("team names.png"))
        l2=tk.Label(f2,text='TEAM NAMES',bg='#311432',font=('lucida handwriting',15),fg='red',image=p,compound='bottom')
        l2.place(x=20,y=0)
        p1=ImageTk.PhotoImage(Image.open("graph1.png"))
        l=tk.Label(f2,text='LINE GRAPH',bg='#311432',font=('lucida handwriting',15),fg='red',image=p1,compound='bottom')
        l.place(x=290,y=0)
        p2=ImageTk.PhotoImage(Image.open("graph 2.png"))
        l1=tk.Label(f2,text='BAR GRAPH',bg='#311432',font=('lucida handwriting',15),fg='red',image=p2,compound='bottom')
        l1.place(x=260,y=235)
        x=m.connect(host='localhost',user='root',passwd='sd55',database='preml')
        y=x.cursor() 
        y.execute('select * from teamstats order by Points desc')
        z=y.fetchall()
        pt=z[0][5]
        maxp=z[0]
        print()
        print(maxp[0],'are the Premier League champions!!! of 2020-21')
        print(maxp[0],'finishes with',pt,'points')
        print('Win percentage :',(maxp[2]/38)*100,'%')
        print('goals scored :',maxp[6])
        print('current ranking in world club football :', maxp[9])  
        x=m.connect(host='localhost',user='root',passwd='sd55',database='preml')
        y=x.cursor() 
        y.execute('select Team,Points from teamstats order by Points desc')
        z=y.fetchall()
        print('''
TOP 5 TEAMS:''')
        print(tabulate(z[0:5],headers=['Team','Points']))
        print('''
Teams entering into Champions League''')
        print(tabulate(z[0:4],headers=['Team','Points']))
        print('''
Teams relegated''')
        print(tabulate(z[17:20],headers=['Team','Points']))
        
        w1=tk.Tk()                                  
        w1.geometry('300x300')
        w1.title('Team Statistics')
        l1=tk.Label(w1,text='Team Stats!!!',font=(7))
        l1.place(x=100,y=6)
        f=tk.Frame(w1,width=300,height=300,bg='light blue')
        f.place(x=0,y=30)
        l2=tk.Label(f,text='''TEAMS STATISTICS ARE DISPLAYED
    in the form of:''',font=('Lucida handwriting',11),bg='light blue',fg='black')
        l2.place(x=15,y=40)
        l2=tk.Label(f,text='''   LINE GRAPH
   BAR GRAPH''',font=('ariel',12),bg='light blue',fg='brown')
        l2.place(x=30,y=140)
        w1.mainloop()
        
    elif j==2:
        for widget in f2.winfo_children():
            widget.destroy()
        p=ImageTk.PhotoImage(Image.open("graph 3.png"))
        l2=tk.Label(f2,text='BAR GRAPH',bg='#311432',font=('lucida handwriting',15),fg='red',image=p,compound='bottom')
        l2.place(x=20,y=0)
        p1=ImageTk.PhotoImage(Image.open("st names.jpeg"))
        l=tk.Label(f2,text='STRIKER NAMES',bg='#311432',font=('lucida handwriting',15),fg='red',image=p1,compound='bottom')
        l.place(x=350,y=0)
        p2=ImageTk.PhotoImage(Image.open("graph 4.png"))
        l1=tk.Label(f2,text='LINE GRAPH',bg='#311432',font=('lucida handwriting',15),fg='red',image=p2,compound='bottom')
        l1.place(x=180,y=270)
        w2 = tk.Tk()                               #refer Window-2
        w2.geometry('500x400')
        w2.title('strkr stat option')
        w2.configure(bg='LightYellow3')
        l1= tk.Label(w2,text = '''STRIKER STATISTICS
  is represented as:''',font =('Times New Roman',23),fg='black',bg='LightYellow3').pack()
        f3=tk.Frame(w2,width = 500,height = 380,bg='PeachPuff4')
        f3.place(x=0,y=70)  
        l2= tk.Label(f3,text = '''LINE GRAPH
BAR GRAPH''',font =('Times New Roman',28),fg='black',bg='LightYellow3')
        l2.place(x=20,y=100)
        w2.mainloop()
    
    elif j==3:
        for widget in f2.winfo_children():
            widget.destroy()
        p=ImageTk.PhotoImage(Image.open("gk names.jpeg"))
        l2=tk.Label(f2,text='GOALKEEPER NAMES',bg='#311432',font=('lucida handwriting',15),fg='red',image=p,compound='bottom')
        l2.place(x=40,y=0)
        p1=ImageTk.PhotoImage(Image.open("chart 1.png"))
        l3=tk.Label(f2,text='GOALKEEPER STATS',bg='#311432',font=('lucida handwriting',15),fg='red',image=p1,compound='bottom')
        l3.place(x=240,y=100)
        x=m.connect(host='localhost',user='root',passwd='sd55',database='preml')
        y=x.cursor()
        def tp():
            y.execute('select * from defenderstats')
            z=y.fetchall()
            for k in range(10):
                print(k+1,'.',z[k][0])
            a=int(input('''Enter the no. of the Defender you want to get statistics
'''))
            k=a-1
            print('Selected Defender:',z[k][0])
            print('Team:',z[k][1])
            print('Tackles:',z[k][2])
            print('Interceptions:',z[k][3])
            a2=input('''
Do you want more statistics? y/n''')
            if a2=='y':                           #refer Console-5
                print('''Defenders with tackles more than 90:
''')
                y.execute("select Player,Team,Tackles from defenderstats where tackles>=90")
                z2=y.fetchall()
                print(tabulate(z2,headers=['Player','Team','Tacklles']))
                print('''
Defenders with Interceptions more than 55:
''')            
                y.execute("select Player,Team,Interceptions from defenderstats where Interceptions>55")
                z3=y.fetchall()
                print(tabulate(z3,headers=['Player','Team','Interceptions']))
                y.execute('select Player,Team,Tackles,Interceptions from defenderstats order by Tackles desc,Interceptions desc')
                z4=y.fetchmany(5)
                print('''
Top 5 defenders:''')
                print(tabulate(z4,headers=['Player','Team','Tackles','Interceptions']))
            def stp():
                j2=tl.get()
                x=m.connect(host='localhost',user='root',passwd='sd55',database='preml')
                y=x.cursor()
                
                y.execute('select * from strikerstats')
                z=y.fetchall()
                l,a,b=[],[[],[]],[]
                for k in range(10):
                    l.append(z[k][1])
                for k in range(10):
                    if j2==z[k][1]:
                        print('')
                        print('Striker',z[k][0],'of',z[k][1],'has scored',z[k][2],'goals and provided',z[k][3],'assists!')
                        a[0].append(z[k][2])
                        a[1].append(z[k][3])
                        b.append(z[k][0])
                    elif j2 not in l:
                        print('Your team has none of its strikers in top 10:(')
                        break
                for k in range(10):
                    if j2==z[k][1]:
                        c=n.arange(1,len(a[0])+1)
                        mc.ylim(1,30)
                        mc.xticks(c,b)
                        mc.bar(c,a[0],color='m',width=0.2,label='Goals')
                        mc.bar(c+0.2,a[1],color='olive',width=0.2,label='Assists')
                        mc.title('Team-Striker stats')
                        mc.xlabel('player name')
                        mc.ylabel('goals and assists')
                        mc.legend(loc='upper left')
                            
            w4=tk.Tk()                         #refer Window-4
            w4.geometry('500x500')
            w4.title('Team-Striker statistics')
            w4.configure(bg='IndianRed1')
            l=['Arsenal','Aston Villa','Brighton','Burnley','Chelsea','Crystal Palace','Everton','Fulham',
    'Leeds United','Leicester City','Liverpool','Manchester City','Manchester United','Newcastle United',
    'Southampton','Sheffield United','Tottenham Hotspur','West Brom','West Ham United','Wolves']
            l1=tk.Label(w4,text='Enter Team name',bg='IndianRed1',font=(30))
            l1.place(x=50,y=50)
            tl=tk.StringVar()
            e1=tk.OptionMenu(w4,tl,*l)
            e1.place(x=250,y=40)
            b=tk.Button(w4,text='submit',font=(40),command=stp)
            b.place(x=190,y=200)
            w4.mainloop()
            
        
        w3=tk.Tk()                                    #refer Window-3
        w3.geometry('600x600')
        w3.configure(bg='light green')
        w3.title('Team-Player Statistics')
        l1=tk.Label(w3,text='Want to know more about your team players!?',font=('ariel',20),fg='black',bg='light green').pack()
        f=tk.Frame(w3,width=700,height=700,bg='light blue')
        f.place(x=0,y=60)
        l2=tk.Label(f,text='Select category of players:',font=('lucida',20),bg='light blue')
        l2.place(x=30,y=120)
        r1=tk.Button(f,text='Click to select the Team of your striker',font=(22),bg='blue',fg='white',command=tp)
        r2=tk.Label(f,text='Defender stats can be seen in the console!',font=(22),bg='black',fg='white')
        r3=tk.Label(f,text='Goalkeeper stats can be seen here-->',font=(22),bg='black',fg='white')
        r1.place(x=30,y=180)
        r2.place(x=30,y=240)
        r3.place(x=30,y=300)
        #b=tk.Button(f,text='submit',bg='black',fg='white',font=(20),command=w.destroy)
        #b.place(x=320,y=340)
        w3.mainloop()
        
    elif j==4:
        for widget in f2.winfo_children():
            widget.destroy()
        x=m.connect(host='localhost',user='root',passwd='sd55',database='preml')
        y=x.cursor() 
        y.execute('select * from teamstats')
        z=y.fetchall()
        def gd():
            g=v.get()
            l=[]
            h=[]
            #graph
            for k in range(20):                #refer Graph-6
                h.append(z[k][8])              #refer Console-7
                print(k+1,'.',z[k][0],end='\n')
            X  = n.arange(1,21)
            mc.title('GD of each team')
            mc.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
            mc.bar(X,h,color ='green', width=0.4)
            mc.xlabel('team no.')
            mc.ylabel('goal dif.')
            #pyconsole
            for k in range(20):
                l.append(z[k][0])
                if g in l:
                    print(g,':')
                    print('Goals scored: ',z[k][6])
                    print('Goals conceded: ',z[k][7])
                    print('Goal Difference: ',z[k][8])
                    break
        p=ImageTk.PhotoImage(Image.open("team names.png"))
        l2=tk.Label(f2,text='TEAM NAMES',bg='#311432',font=('lucida handwriting',15),fg='red',image=p,compound='bottom')
        l2.place(x=40,y=0)
        p1=ImageTk.PhotoImage(Image.open("graph 6.png"))
        l3=tk.Label(f2,text='TEAM NAMES',bg='#311432',font=('lucida handwriting',15),fg='red',image=p1,compound='bottom')
        l3.place(x=270,y=280)
        w = tk.Tk()                           #refer Window-5
        w.title('GD Calc.')
        w.geometry('500x500')
        w.configure(bg='#eedc82')
        v=tk.Entry(w,width=40)
        l1 = tk.Label(w,text = 'Enter Team Name',font =('Times New Roman',18),fg='#8b4000',bg='#eedc82')
        l1.place(x = 20,y=70) 
        v.place(x =235,y =78)
        b=tk.Button(w,text='submit',bg='red',fg='white',command=gd)
        b.place(x=40,y=150)
        w.mainloop()
        
#     elif j==5:
#         for widget in f2.winfo_children():
#             widget.destroy()
#         x=m.connect(host='localhost',user='root',passwd='sd55',database='preml')
#         y=x.cursor() 
#         y.execute('select * from teamstats order by Points desc')
#         z=y.fetchmany(5)
#         l = ['Manchester City', 'Manchester United', 'Liverpool', 'Chelsea', 'Leicester City']
#         print('''Top 5 Teams of the Season 2020-21:
# ''')
#         for k in range(5):
#             print(k+1,'.',l[k])
#         a1 = input('Enter the team you want to know about from the top 5')
#         for k in range(5):
#             if l[k]==a1:
#                 ab=k
#                 print('''
# Team Selected:''',a1)
#                 print('Matches Won:',z[ab][2])
#                 print('Points Scored:',z[ab][5])
#                 print('Goals Scored:',z[ab][6])
#                 print('World Ranking:',z[ab][9])
#                 break
            
w=tk.Tk()                                       #refer Window-6
w.title('Award ceremony')
w.geometry('1150x1150')
w.configure(bg='#311432')
f1=tk.Frame(w,height=1150,width=600,bg='#997950')
f1.place(x=0,y=0)
f2=tk.Frame(w,height=1150,width=550,bg='#311432')
f2.place(x=480,y=0)
l=tk.Label(w,text='Select the menu you want to know:',font=('ariel',20),bg='#997950',fg='#FFF200')
l.place(x=25,y=30)
i=tk.IntVar()
r1=tk.Radiobutton(f1,text='TEAM STATS',bg='black',fg='white',value=1,variable=i)
r2=tk.Radiobutton(f1,text='STRIKER STATS',bg='black',fg='white',value=2,variable=i)
r3=tk.Radiobutton(f1,text='TEAM-PLAYER STATS',bg='black',fg='white',value=3,variable=i)
r4=tk.Radiobutton(f1,text="GOAL DIF CALC",bg='black',fg='white',value=4,variable=i)
#r5=tk.Radiobutton(f1,text="TOP 5 TEAM INFO",bg='black',fg='white',value=5,variable=i)
#r6=tk.Radiobutton(f1,text="TOP 5 TEAMS",bg='black',fg='white',value=6,variable=i)
r1.place(x=70,y=100)
r2.place(x=70,y=150)
r3.place(x=70,y=200)
r4.place(x=70,y=250)
#r5.place(x=70,y=300)
#r6.place(x=70,y=350)
b=tk.Button(w,text='submit',bg='white',fg='black',command=ts)
b.place(x=50,y=480)
w.mainloop()
