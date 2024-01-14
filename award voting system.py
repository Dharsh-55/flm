#import matplotlib.pyplot as mc
#import numpy as n
import mysql.connector as m
import tkinter as tk
#from tabulate import tabulate
from PIL import ImageTk,Image 

def vp():
    j3=i3.get()
    x=m.connect(host='localhost',user='root',passwd='sd55',database='preml')
    y=x.cursor() 
    y.execute("select * from votes")
    z=y.fetchall()
    l=[]
    l2=[]
    for k in range(15):
        l.append(z[k][3])
        l2.append(z[k][2])
    if j3==1:
        h=max(l2[0:3])
        f=l2.index(h)
        print(z[f][1],f)
        if f==0:
            for widget in f2.winfo_children():
                widget.destroy()
            p=ImageTk.PhotoImage(Image.open("hk.jpg"))
            l2=tk.Label(f2,text='''Harry Kane is voted as the Favorite Striker''',bg='#8B1A1A',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
            l2.place(x=0,y=0)
            w.mainloop()
        elif f==1:
            for widget in f2.winfo_children():
                widget.destroy()
            p=ImageTk.PhotoImage(Image.open("msw.jpeg"))
            l2=tk.Label(f2,text='''Mohamed Salah is voted as the favorite striker''',bg='#8B1A1A',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
            l2.place(x=0,y=0)
            w.mainloop()
        elif f==2:
            for widget in f2.winfo_children():
                widget.destroy()
            p=ImageTk.PhotoImage(Image.open("bfw.jpeg"))
            l2=tk.Label(f2,text='''Bruno fernandes is voted as the favorite striker''',bg='#8B1A1A',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
            l2.place(x=0,y=0)
            w.mainloop()
                
    elif j3==2:
        h=max(l2[3:6])
        f=l2.index(h)
        print(z[f][1],f)
        if f==3:
            for widget in f2.winfo_children():
                widget.destroy()
            p=ImageTk.PhotoImage(Image.open("law.jpeg"))
            l2=tk.Label(f2,text='''Luke Ayling is voted as the Favorite defender''',bg='#8B1A1A',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
            l2.place(x=0,y=0)
            w.mainloop()
        elif f==4:
            for widget in f2.winfo_children():
                widget.destroy()
            p=ImageTk.PhotoImage(Image.open("ybw.jpeg"))
            l2=tk.Label(f2,text='''Yves Bissouma is voted as the favorite defender''',bg='#8B1A1A',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
            l2.place(x=0,y=0)
            w.mainloop()
        elif f==5:
            for widget in f2.winfo_children():
                widget.destroy()
            p=ImageTk.PhotoImage(Image.open("wnw.jpeg"))
            l2=tk.Label(f2,text='''Wilfred Ndidi is voted as the favorite defender''',bg='#8B1A1A',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
            l2.place(x=0,y=0)
            w.mainloop()
            
    elif j3==3:
        h=max(l2[6:9])
        f=l2.index(h)
        print(z[f][1],f)
        if f==6:
            for widget in f2.winfo_children():
                widget.destroy()
            p=ImageTk.PhotoImage(Image.open("emw.jpeg"))
            l2=tk.Label(f2,text='''Emiliano is voted as the Favorite goalkeeper''',bg='#8B1A1A',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
            l2.place(x=0,y=0)
            w.mainloop()
        elif f==7:
            for widget in f2.winfo_children():
                widget.destroy()
            p=ImageTk.PhotoImage(Image.open("hlw.jpeg"))
            l2=tk.Label(f2,text='''Hugo Lloris is voted as the favorite goalkeeper''',bg='#8B1A1A',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
            l2.place(x=0,y=0)
            w.mainloop()
        elif f==8:
            for widget in f2.winfo_children():
                widget.destroy()
            p=ImageTk.PhotoImage(Image.open("edw.jpeg"))
            l2=tk.Label(f2,text='''Ederson is voted as the favorite goalkeeper''',bg='#8B1A1A',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
            l2.place(x=0,y=0)
            w.mainloop()
            
    elif j3==4:
        h=max(l2[9:12])
        f=l2.index(h)
        print(z[f][1],f)
        if f==9:
            for widget in f2.winfo_children():
                widget.destroy()
            p=ImageTk.PhotoImage(Image.open("kdbw.jpeg"))
            l2=tk.Label(f2,text='''Kevin De Bruyne is voted as the Favorite Playmaker''',bg='#8B1A1A',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
            l2.place(x=0,y=0)
            w.mainloop()
        elif f==10:
            for widget in f2.winfo_children():
                widget.destroy()
            p=ImageTk.PhotoImage(Image.open("shmw.jpeg"))
            l2=tk.Label(f2,text='''Son Heung-Min is voted as the favorite playmaker''',bg='#8B1A1A',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
            l2.place(x=0,y=0)
            w.mainloop()
        elif f==11:
            for widget in f2.winfo_children():
                widget.destroy()
            p=ImageTk.PhotoImage(Image.open("jvw.jpeg"))
            l2=tk.Label(f2,text='''Jamie Vardy is voted as the favorite playmaker''',bg='#8B1A1A',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
            l2.place(x=0,y=0)
            w.mainloop()
        
    elif j3==5:
        h=max(l2[12:15])
        f=l2.index(h)
        print(z[f][1],f)
        if f==12:
            for widget in f2.winfo_children():
                widget.destroy()
            p=ImageTk.PhotoImage(Image.open("pgw.jpeg"))
            l2=tk.Label(f2,text='''Pep Guardiola is voted as the Favorite Manager''',bg='#8B1A1A',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
            l2.place(x=0,y=0)
            w.mainloop()
        elif f==13:
            for widget in f2.winfo_children():
                widget.destroy()
            p=ImageTk.PhotoImage(Image.open("ogw.jpeg"))
            l2=tk.Label(f2,text='''Ole Gunnar is voted as the favorite manager''',bg="#8B1A1A",font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
            l2.place(x=0,y=0)
            w.mainloop()
        elif f==14:
            for widget in f2.winfo_children():
                widget.destroy()
            p=ImageTk.PhotoImage(Image.open("jkw.jpeg"))
            l2=tk.Label(f2,text='''Jurgen Klopp is voted as the favorite manager''',bg='#8B1A1A',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
            l2.place(x=0,y=0)
            w.mainloop()
def award(): 
    def v():
        j2=i2.get()
        x=m.connect(host='localhost',user='root',passwd='sd55',database='preml')
        y=x.cursor()     
        y.execute('select * from votes')
        z=y.fetchall()
        if j2==1:
            y.execute("update votes set Votes=Votes+1 where SNo=1")
            x.commit()
        elif j2==2:
            y.execute("update votes set Votes=Votes+1 where SNo=2")
            x.commit()
        elif j2==3:
            y.execute("update votes set Votes=Votes+1 where SNo=3")
            x.commit()
        elif j2==4:
            y.execute("update votes set Votes=Votes+1 where SNo=4")
            x.commit()
        elif j2==5:
            y.execute("update votes set Votes=Votes+1 where SNo=5")
            x.commit()
        elif j2==6:
            y.execute("update votes set Votes=Votes+1 where SNo=6")
            x.commit()
        elif j2==7:
            y.execute("update votes set Votes=Votes+1 where SNo=7")
            x.commit()
        elif j2==8:
            y.execute("update votes set Votes=Votes+1 where SNo=8")
            x.commit()
        elif j2==9:
            y.execute("update votes set Votes=Votes+1 where SNo=9")
            x.commit()
        elif j2==10:
            y.execute("update votes set Votes=Votes+1 where SNo=10")
            x.commit()
        elif j2==11:
            y.execute("update votes set Votes=Votes+1 where SNo=11")
            x.commit()
        elif j2==12:
            y.execute("update votes set Votes=Votes+1 where SNo=12")
            x.commit()
        elif j2==13:
            y.execute("update votes set Votes=Votes+1 where SNo=13")
            x.commit()
        elif j2==14:
            y.execute("update votes set Votes=Votes+1 where SNo=14")
            x.commit()
        elif j2==15:
            y.execute("update votes set Votes=Votes+1 where SNo=15")
            x.commit()
            
                     #refer Window-7
    j=i.get()
    if j==1:
        for widget in f2.winfo_children():
            widget.destroy()
        p=ImageTk.PhotoImage(Image.open("hkv.jpeg"))
        l2=tk.Label(f2,text='''Harry Kane''',bg='#311432',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
        l2.place(x=0,y=0)
        b=tk.Radiobutton(f2,text='Vote',value=1,variable=i2,fg='white',bg='black',command=v)
        b.place(x=100,y=220)
        l=['23 Goals','14 Assists','53 ShotsOnTarget']
        t=tk.StringVar()
        e=tk.OptionMenu(f2,t,*l)
        e.place(x=0,y=220)
        
        p1=ImageTk.PhotoImage(Image.open("msv.jpeg"))
        l3=tk.Label(f2,text='''Salah''',bg='#311432',font=('lucida handwriting',15),fg='white',image=p1,compound='bottom')
        l3.place(x=300,y=0)
        b1=tk.Radiobutton(f2,text='Vote',value=2,variable=i2,fg='white',bg='black',command=v)
        b1.place(x=400,y=220)
        l1=['22 Goals','5 Assists','52 ShotsOnTarget']
        t1=tk.StringVar()
        e1=tk.OptionMenu(f2,t1,*l1)
        e1.place(x=300,y=220)

        p2=ImageTk.PhotoImage(Image.open("bfv.jpeg"))
        l4=tk.Label(f2,text='''Bruno Fernandes''',bg='#311432',font=('lucida handwriting',15),fg='white',image=p2,compound='bottom')
        l4.place(x=200,y=250)
        b2=tk.Radiobutton(f2,text='Vote',value=3,variable=i2,fg='white',bg='black',command=v)
        b2.place(x=320,y=450)
        l2=['18 Goals','12 Assists','51 ShotsOnTarget']
        t2=tk.StringVar()
        e2=tk.OptionMenu(f2,t2,*l2)
        e2.place(x=220,y=450)
        w.mainloop()
    elif j==2:
        for widget in f2.winfo_children():
            widget.destroy()
        p=ImageTk.PhotoImage(Image.open("lav.jpeg"))
        l2=tk.Label(f2,text='''Luke Ayling''',bg='#311432',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
        l2.place(x=0,y=0)
        b=tk.Radiobutton(f2,text='Vote',value=4,variable=i2,fg='white',bg='black',command=v)
        b.place(x=100,y=240)
        l=['108 Tackles','58 Interceptions']
        t=tk.StringVar()
        e=tk.OptionMenu(f2,t,*l)
        e.place(x=0,y=240)
        
        p1=ImageTk.PhotoImage(Image.open("ybv.jpeg"))
        l3=tk.Label(f2,text='''Yves Bissouma''',bg='#311432',font=('lucida handwriting',15),fg='white',image=p1,compound='bottom')
        l3.place(x=300,y=0)
        b1=tk.Radiobutton(f2,text='Vote',value=5,variable=i2,fg='white',bg='black',command=v)
        b1.place(x=400,y=220)
        l1=['104 Tackles','64 Interceptions']
        t1=tk.StringVar()
        e1=tk.OptionMenu(f2,t1,*l1)
        e1.place(x=300,y=220)

        p2=ImageTk.PhotoImage(Image.open("wnv.jpeg"))
        l4=tk.Label(f2,text='''Wilfred Ndidi''',font=('lucida handwriting',15),bg='#311432',fg='white',image=p2,compound='bottom')
        l4.place(x=200,y=250)
        b2=tk.Radiobutton(f2,text='Vote',value=6,variable=i2,fg='white',bg='black',command=v)
        b2.place(x=320,y=470)
        l2=['96 Tackles','61 Interceptions']
        t2=tk.StringVar()
        e2=tk.OptionMenu(f2,t2,*l2)
        e2.place(x=220,y=470)
        w.mainloop()
    elif j==3:
        for widget in f2.winfo_children():
            widget.destroy()
        p=ImageTk.PhotoImage(Image.open("ev.jpeg"))
        l2=tk.Label(f2,text='''Emiliano''',bg='#311432',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
        l2.place(x=0,y=0)
        b=tk.Radiobutton(f2,text='Vote',value=7,variable=i2,fg='white',bg='black',command=v)
        b.place(x=100,y=230)
        l=['142 Saves','15 CleanSheets']
        t=tk.StringVar()
        e=tk.OptionMenu(f2,t,*l)
        e.place(x=0,y=230)
        
        p1=ImageTk.PhotoImage(Image.open("hlv.jpeg"))
        l3=tk.Label(f2,text='''Hugo Lloris''',bg='#311432',font=('lucida handwriting',15),fg='white',image=p1,compound='bottom')
        l3.place(x=300,y=0)
        b1=tk.Radiobutton(f2,text='Vote',value=8,variable=i2,fg='white',bg='black',command=v)
        b1.place(x=400,y=210)
        l1=['114 Saves','12 CleanSheets']
        t1=tk.StringVar()
        e1=tk.OptionMenu(f2,t1,*l1)
        e1.place(x=300,y=210)

        p2=ImageTk.PhotoImage(Image.open("edv.jpeg"))
        l4=tk.Label(f2,text='''Ederson''',bg='#311432',font=('lucida handwriting',15),fg='white',image=p2,compound='bottom')
        l4.place(x=200,y=270)
        b2=tk.Radiobutton(f2,text='Vote',value=9,variable=i2,fg='white',bg='black',command=v)
        b2.place(x=320,y=480)
        l2=['66 Saves','19 CleanSheets']
        t2=tk.StringVar()
        e2=tk.OptionMenu(f2,t2,*l2)
        e2.place(x=220,y=480)
        w.mainloop()
    elif j==4:
        for widget in f2.winfo_children():
            widget.destroy()
        p=ImageTk.PhotoImage(Image.open("kdbv.jpeg"))
        l2=tk.Label(f2,text='''Kevin De Bruyne''',bg='#311432',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
        l2.place(x=0,y=0)
        b=tk.Radiobutton(f2,text='Vote',value=10,variable=i2,fg='white',bg='black',command=v)
        b.place(x=100,y=240)
        l=['12 Assists','31 Shots']
        t=tk.StringVar()
        e=tk.OptionMenu(f2,t,*l)
        e.place(x=0,y=240)
        
        p1=ImageTk.PhotoImage(Image.open("shmv.jpeg"))
        l3=tk.Label(f2,text='''Son Heung-Min''',bg='#311432',font=('lucida handwriting',15),fg='white',image=p1,compound='bottom')
        l3.place(x=300,y=0)
        b1=tk.Radiobutton(f2,text='Vote',value=11,variable=i2,fg='white',bg='black',command=v)
        b1.place(x=400,y=230)
        l1=['10 Assists','36 Shots']
        t1=tk.StringVar()
        e1=tk.OptionMenu(f2,t1,*l1)
        e1.place(x=300,y=230)

        p2=ImageTk.PhotoImage(Image.open("jvv.jpeg"))
        l4=tk.Label(f2,text='''Jamie Vardy''',bg='#311432',font=('lucida handwriting',15),fg='white',image=p2,compound='bottom')
        l4.place(x=200,y=260)
        b2=tk.Radiobutton(f2,text='Vote',value=12,variable=i2,fg='white',bg='black',command=v)
        b2.place(x=320,y=470)
        l2=['9 Assists','38 Shots']
        t2=tk.StringVar()
        e2=tk.OptionMenu(f2,t2,*l2)
        e2.place(x=220,y=470)
        w.mainloop()
    elif j==5:
        for widget in f2.winfo_children():
            widget.destroy()
        p=ImageTk.PhotoImage(Image.open("pgv.jpeg"))
        l2=tk.Label(f2,text='''Pep Guardiola''',bg='#311432',font=('lucida handwriting',15),fg='white',image=p,compound='bottom')
        l2.place(x=0,y=0)
        b=tk.Radiobutton(f2,text='Vote',value=13,variable=i2,fg='white',bg='black',command=v)
        b.place(x=100,y=220)
        l=['27 Wins','86 Points']
        t=tk.StringVar()
        e=tk.OptionMenu(f2,t,*l)
        e.place(x=0,y=220)
        
        p1=ImageTk.PhotoImage(Image.open("ogv.jpeg"))
        l3=tk.Label(f2,text='''Ole Gunnar''',bg='#311432',font=('lucida handwriting',15),fg='white',image=p1,compound='bottom')
        l3.place(x=300,y=0)
        b1=tk.Radiobutton(f2,text='Vote',value=14,variable=i2,fg='white',bg='black',command=v)
        b1.place(x=400,y=210)
        l1=['21 Wins','74 Points']
        t1=tk.StringVar()
        e1=tk.OptionMenu(f2,t1,*l1)
        e1.place(x=300,y=210)

        p2=ImageTk.PhotoImage(Image.open("jkv.jpeg"))
        l4=tk.Label(f2,text='''Jurgen Klopp''',bg='#311432',font=('lucida handwriting',15),fg='white',image=p2,compound='bottom')
        l4.place(x=200,y=250)
        b2=tk.Radiobutton(f2,text='Vote',value=15,variable=i2,fg='white',bg='black',command=v)
        b2.place(x=320,y=470)
        l2=['20 Wins','69 Points']
        t2=tk.StringVar()
        e2=tk.OptionMenu(f2,t2,*l2)
        e2.place(x=220,y=470)
        w.mainloop()
        
    
w=tk.Tk()                                       #refer Window-6
w.title('Award ceremony')
w.geometry('1150x1150')
w.configure(bg='#8B1A1A')
f1=tk.Frame(w,height=575,width=450,bg='#FFB90F')
f1.place(x=0,y=0)
f2=tk.Frame(w,height=1150,width=700,bg='#8B1A1A')
f2.place(x=500,y=0)
f3=tk.Frame(w,height=575,width=450,bg='black')
f3.place(x=500,y=575)
l=tk.Label(w,text='VOTE NOW!!!',font=('ariel',20),bg='#997950',fg='#FFF200')
l.place(x=130,y=30)
i2=tk.IntVar()
i=tk.IntVar()
r1=tk.Radiobutton(f1,text='FAVORITE STRIKER',bg='black',fg='white',value=1,variable=i)
r2=tk.Radiobutton(f1,text='FAVORITE DEFENDER',bg='black',fg='white',value=2,variable=i)
r3=tk.Radiobutton(f1,text="FAVORITE GOALKEEPER",bg='black',fg='white',value=3,variable=i)
r4=tk.Radiobutton(f1,text="FAVORITE PLAYMAKER",bg='black',fg='white',value=4,variable=i)
r5=tk.Radiobutton(f1,text="FAVORITE MANAGER",bg='black',fg='white',value=5,variable=i)
r1.place(x=40,y=100)
r2.place(x=230,y=100)               
r3.place(x=40,y=150)
r4.place(x=230,y=150)
r5.place(x=140,y=200)
l2=tk.Label(w,text='KNOW THE WINNERS!!!',font=('ariel',20),bg='#997950',fg='#FFF200')
l2.place(x=70,y=270)
i3=tk.IntVar()
r6=tk.Radiobutton(f1,text='STRIKER',bg='black',fg='white',value=1,variable=i3)
r7=tk.Radiobutton(f1,text=' DEFENDER',bg='black',fg='white',value=2,variable=i3)
r8=tk.Radiobutton(f1,text=" GOALKEEPER",bg='black',fg='white',value=3,variable=i3)
r9=tk.Radiobutton(f1,text=" PLAYMAKER",bg='black',fg='white',value=4,variable=i3)
r0=tk.Radiobutton(f1,text=" MANAGER",bg='black',fg='white',value=5,variable=i3)
r6.place(x=40,y=320)
r7.place(x=230,y=320)               
r8.place(x=40,y=370)
r9.place(x=230,y=370)
r0.place(x=140,y=420)
b=tk.Button(w,text='submit',bg='white',fg='black',command=award)
b.place(x=190,y=240)
b1=tk.Button(w,text='submit',bg='white',fg='black',command=vp)
b1.place(x=190,y=460)
w.mainloop()









