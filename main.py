from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import ctypes
import sqlite3
import pandas as pd
import tkinter.messagebox as tkMessageBox
import tkinter.scrolledtext as scrolledtext
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import os,PIL,webbrowser,pyperclip

window = Tk()

window.resizable(0,0)

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
lt = [w, h]
a = str(lt[0]//2-446)
b= str(lt[1]//2-383)

window.geometry("892x710+"+a+"+"+b)
window.title('STEALTH')

img = Image.open(r"images/bg.png")
img = ImageTk.PhotoImage(img)
panel = Label(window, image=img)
panel.pack(side="top", fill="both", expand="yes")

canvas = Canvas(window, bg="#297067", height=457, width=888)
canvas.place(x=0,y=249)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

age = IntVar()
gen = StringVar()
cp = IntVar()
rbp = DoubleVar()
chol = DoubleVar()
fbs = StringVar()
res = DoubleVar()
mha = DoubleVar()
eia = StringVar()
st = DoubleVar()
slst = DoubleVar()
mv = IntVar()
tha = IntVar()

age2 = IntVar()
preg = IntVar()
glu = DoubleVar()
bp = DoubleVar()
sti = DoubleVar()
bi = DoubleVar()
ins = DoubleVar()
ped =DoubleVar()

rad = DoubleVar()
ara = DoubleVar()
pere = DoubleVar()
smo = DoubleVar()
tex = DoubleVar()

def database():
    global conn,cursor
    conn=sqlite3.connect("data/doctors.db")
    cursor = conn.cursor()
    q = "Create table if not exists doctor (id integer primary key AUTOINCREMENT,name TEXT,email varchar(150) unique,phone_no TEXT,location TEXT,nearby TEXT,Timing TEXT)"
    cursor.execute(q)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def diab():
    def submit():
        #try:  
        dfx = pd.read_csv('data\\Diabetes_XTrain.csv')
        dfy = pd.read_csv('data\\Diabetes_YTrain.csv')
        X = dfx.values
        Y = dfy.values
        Y = Y.reshape((-1,))


        value = ''
        pregnancies = preg.get()
        glucose = glu.get()
        bloodpressure = bp.get()
        skinthickness = sti.get()
        bmi = bi.get()
        insulin = ins.get()
        pedigree = ped.get()
        age = age2.get()

        user_data = np.array(
                (pregnancies,
                 glucose,
                 bloodpressure,
                 skinthickness,
                 bmi,
                 insulin,
                 pedigree,
                 age)
            ).reshape(1, 8)

        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(X, Y)

        predictions = knn.predict(user_data)

        if int(predictions[0]) == 1:
                warning = Label(canvas, text="Prediction : High Risk Of Diabetes", font=('arial', 12,'bold'), fg="black", bg="#297067", bd=10)
                warning.place(x = 280,y = 290)
                warning.after(4500, lambda: warning.destroy())
               
        elif int(predictions[0]) == 0:
                warning = Label(canvas, text="Prediction : Risk Of Diabetes Are Low", font=('arial', 12,'bold'), fg="black", bg="#297067", bd=10)
                warning.place(x = 280,y = 290)
                warning.after(4500, lambda: warning.destroy())

                
    canvas = Canvas(window, bg="#297067", height=457, width=888)
    canvas.place(x=0,y=249)
                                                                                                                                                                                                
    t = Label(canvas, text=" ____________________________Diabeties Analysis_____________________________", font=('arial', 16,''), fg="white", bg="#297067", bd=10)
    t.place(x = 2,y = 2)

    a = Label(canvas, text="Age :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    a.place(x = 30,y = 52)

    a = Entry(canvas, textvariable=age2, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    a.place(x=465, y=61)

    b = Label(canvas, text="Glucose :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    b.place(x = 30,y = 81)

    c = Entry(canvas, textvariable=glu, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    c.place(x=465, y=90)

    d = Label(canvas, text="Insulin :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    d.place(x = 30,y = 110)

    e = Entry(canvas, textvariable=ins, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    e.place(x=465, y=119)

    f = Label(canvas, text="Pregnancies :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    f.place(x = 30,y = 139)

    g = Entry(canvas, textvariable=preg, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    g.place(x=465, y=148)

    h = Label(canvas, text="Skin Thickness :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    h.place(x = 30,y = 168)

    i = Entry(canvas, textvariable=sti, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    i.place(x=465, y=177)
    
    j = Label(canvas, text="Blood Pressure :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    j.place(x = 30,y = 197)

    k = Entry(canvas, textvariable=bp, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    k.place(x=465, y=206)

    l = Label(canvas, text="Body Mass Index :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    l.place(x = 30,y = 226)

    m = Entry(canvas, textvariable=bi, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    m.place(x=465, y=235)

    n = Label(canvas, text="Diabetes Pedigree Function :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    n.place(x = 30,y = 255)

    o = Entry(canvas, textvariable=ped, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    o.place(x=465, y=264)  

    text = Label(canvas, text='''

ABOUT ALGORITHM USED : k-Nearest Neighbours. It is a supervised learning algorithm. This means that
we train it under supervision. We train it using the labelled data already available to us.''', font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    text.place(x = 30,y = 355)
    
    bh = Button(canvas, text="Analyze", fg="white", bg="#297067", width = 79,
                font=("Calibri", "16",'bold'),command=submit)
    bh.place(x=6, y=340)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def br_cancer():
    def submit():
        try:
                df = pd.read_csv('data/Breast_train.csv')
                data = df.values
                X = data[:, :-1]
                Y = data[:, -1]

                value = ''
                radius = rad.get()
                texture = tex.get()
                perimeter = pere.get()
                area = ara.get()
                smoothness = smo.get()

                rf = RandomForestClassifier(n_estimators=16, criterion='entropy', max_depth=5)
                rf.fit(np.nan_to_num(X), Y)

                user_data = np.array(
                    (radius,
                     texture,
                     perimeter,
                     area,
                     smoothness)
                ).reshape(1, 5)

                predictions = rf.predict(user_data)


                if int(predictions[0]) == 1:

                        warning = Label(canvas, text="Prediction : Risk Of Breast Cancer Is High", font=('arial', 12,'bold'), fg="black", bg="#297067", bd=10)
                        warning.place(x = 265,y = 215)
                        warning.after(4500, lambda: warning.destroy())

                elif int(predictions[0]) == 0:
                    
                        warning = Label(canvas, text="Prediction : Risk Of Breast Cancer Are Low", font=('arial', 12,'bold'), fg="black", bg="#297067", bd=10)
                        warning.place(x = 265,y = 215)
                        warning.after(4500, lambda: warning.destroy())

        except:
                warning = Label(canvas, text="Some Unknown Error Has Occoured Please Try Again", font=('arial', 12,'bold'), fg="yellow", bg="#297067", bd=10)
                warning.place(x = 210,y = 215)
                warning.after(2500, lambda: warning.destroy())
                
    canvas = Canvas(window, bg="#297067", height=457, width=888)
    canvas.place(x=0,y=249)
    
    t = Label(canvas, text=" __________________________Breast Cancer Analysis___________________________", font=('arial', 16,''), fg="white", bg="#297067", bd=10)
    t.place(x = 2,y = 2)

    a = Label(canvas, text="Radius :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    a.place(x = 30,y = 52)

    a = Entry(canvas, textvariable=rad, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    a.place(x=465, y=61)

    b = Label(canvas, text="Area :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    b.place(x = 30,y = 81)

    c = Entry(canvas, textvariable=ara, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    c.place(x=465, y=90)

    d = Label(canvas, text="Perimeter :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    d.place(x = 30,y = 110)

    e = Entry(canvas, textvariable=pere, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    e.place(x=465, y=119)

    f = Label(canvas, text="Texture :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    f.place(x = 30,y = 139)

    g = Entry(canvas, textvariable=tex, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    g.place(x=465, y=148)

    h = Label(canvas, text="Smoothness :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    h.place(x = 30,y = 168)

    i = Entry(canvas, textvariable=smo, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    i.place(x=465, y=177) 

    j = Label(canvas, text='''
ABOUT ALGORITHM USED : Random forests or random decision forests are an ensemble learning method for 
classification, regression and other tasks that operate by constructing a multitude of decision trees at training
time and outputting the class that is the mode of the classes (classification) or mean/average prediction
(regression) of the individual trees. Random decision forests correct for decision trees' habit of overfitting to
their training set. Random forests generally outperform decision trees, but their accuracy is lower than gradient
boosted trees. However, data characteristics can affect their performance.''', font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    j.place(x = 15,y = 290)
    
    bh = Button(canvas, text="Analyze", fg="white", bg="#297067", width = 79,
                font=("Calibri", "16",'bold'),command=submit)
    bh.place(x=6, y=260)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
def heart():
    def submit():
        try:
            x = [3,6,7]
            y = ['male','female']
            z = ['y','n']
            if fbs.get()=='' or gen.get()==''or eia.get()=='':
                
                warning = Label(canvas, text="***Please Fill All The Required Fields***", font=('arial', 12,'bold'), fg="yellow", bg="#297067", bd=10)
                warning.place(x = 30,y = 405)
                warning.after(2500, lambda: warning.destroy())
            elif age.get()<=0 :                        
                warning = Label(canvas, text="***Age Must Not Be Zero***", font=('arial', 12,'bold'), fg="yellow", bg="#297067", bd=10)
                warning.place(x = 30,y = 405)
                warning.after(2500, lambda: warning.destroy())
                
            elif cp.get()<0 or cp.get()>3:                        
                warning = Label(canvas, text="***Chest Pain Level Must Be Between 0 to 3***", font=('arial', 12,'bold'), fg="yellow", bg="#297067", bd=10)
                warning.place(x = 30,y = 405)
                warning.after(2500, lambda: warning.destroy())
            
            elif tha.get() not in x:                        
                warning = Label(canvas, text="***Thalassemia Must Be 3,6 or 7***", font=('arial', 12,'bold'), fg="yellow", bg="#297067", bd=10)
                warning.place(x = 30,y = 405)
                warning.after(2500, lambda: warning.destroy())
            elif (gen.get()).lower() not in y:                        
                warning = Label(canvas, text="***Unidentified input in Gender field***", font=('arial', 12,'bold'), fg="yellow", bg="#297067", bd=10)
                warning.place(x = 30,y = 405)
                warning.after(2500, lambda: warning.destroy())
            elif (fbs.get()).lower() not in z:                        
                warning = Label(canvas, text="Unidentified input in Fasting Blood Pressure field***", font=('arial', 12,'bold'), fg="yellow", bg="#297067", bd=10)
                warning.place(x = 30,y = 405)
                warning.after(2500, lambda: warning.destroy())
            elif (eia.get()).lower() not in z:                        
                warning = Label(canvas, text="Unidentified input in Excercise Indused Angina field***", font=('arial', 12,'bold'), fg="yellow", bg="#297067", bd=10)
                warning.place(x = 30,y = 405)
                warning.after(2500, lambda: warning.destroy())
            else:
                df = pd.read_csv('data/Heart_train.csv')
                data = df.values
                X = data[:, :-1]
                Y = data[:, -1:]
                value = ''
                if (gen.get()).lower()=='male':
                    ge = 1
                elif (gen.get()).lower()=='female':
                    ge = 0
                if (fbs.get()).lower()=='y':
                    fb = 1
                elif (fbs.get()).lower()=='n':
                    fb = 0
                if (eia.get()).lower()=='y':
                    ei = 1
                elif (eia.get()).lower()=='n':
                    ei = 0                              
                ag = age.get()
                sex = ge
                chp = cp.get()
                trestbps = rbp.get()
                chl = chol.get()
                fbos = fb
                restecg = res.get()
                thalach = mha.get()
                exang = ei
                oldpeak = st.get()
                slope = slst.get()
                ca = mv.get()
                thal = tha.get()

                user_data = np.array((ag,sex,chp, trestbps, chl,  fbos, restecg, thalach, exang,oldpeak,slope, ca, thal)).reshape(1, 13)
                rf = RandomForestClassifier(n_estimators=16,criterion='entropy', max_depth=9)
                rf.fit(np.nan_to_num(X), Y.ravel())
                rf.score(np.nan_to_num(X), Y)
                predictions = rf.predict(user_data)

                if int(predictions[0]) == 1:
                        warning = Label(canvas, text="Prediction : Risk Of Heart Disease Is High", font=('arial', 12,'bold'), fg="black", bg="#297067", bd=10)
                        warning.place(x = 30,y = 405)
                        warning.after(4500, lambda: warning.destroy())                       
                elif int(predictions[0]) == 0:
                        warning = Label(canvas, text="Prediction : Risk Of Heart Disease Are Low", font=('arial', 12,'bold'), fg="black", bg="#297067", bd=10)
                        warning.place(x = 30,y = 405)
                        warning.after(4500, lambda: warning.destroy())
                        
        except:
                warning = Label(canvas, text="Some Unknown Error Has Occoured Please Try Again", font=('arial', 12,'bold'), fg="yellow", bg="#297067", bd=10)
                warning.place(x = 30,y = 405)
                warning.after(2500, lambda: warning.destroy())
                
    canvas = Canvas(window, bg="#297067", height=457, width=888)
    canvas.place(x=0,y=249)

    agel = Label(canvas, text="Age :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    agel.place(x = 30,y = 2)

    agee = Entry(canvas, textvariable=age, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    agee.place(x=465, y=11)

    genl = Label(canvas, text="Gender :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    genl.place(x = 30,y = 31)

    gene = Entry(canvas, textvariable=gen, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    gene.place(x=465, y=40)

    cpl = Label(canvas, text="Chest Pain Level (0 to 3) :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    cpl.place(x = 30,y = 60)

    cpe = Entry(canvas, textvariable=cp, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    cpe.place(x=465, y=69)

    rbpl = Label(canvas, text="Resting Blood Pressure(In mm Hg) :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    rbpl.place(x = 30,y = 89)

    rbpe = Entry(canvas, textvariable=rbp, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    rbpe.place(x=465, y=98)

    rbpl = Label(canvas, text="Resting Blood Pressure(In mm Hg) :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    rbpl.place(x = 30,y = 89)

    rbpe = Entry(canvas, textvariable=rbp, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    rbpe.place(x=465, y=98)

    lchol = Label(canvas, text="Cholesterol In mg/dl  :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    lchol.place(x = 30,y = 118)

    echol = Entry(canvas, textvariable=chol, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    echol.place(x=465, y=127)

    lfbs = Label(canvas, text="Fasting Blood Suger>120 mg/dl  (Y/N) :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    lfbs.place(x = 30,y = 147)

    efbs = Entry(canvas, textvariable=fbs, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    efbs.place(x=465, y=156)

    lres = Label(canvas, text="Resting Electrocardiography Result :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    lres.place(x = 30,y = 176)

    eres = Entry(canvas, textvariable=res, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    eres.place(x=465, y=185)

    lmha = Label(canvas, text="Maximum Heart Rate Achived :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    lmha.place(x = 30,y = 205)

    emha = Entry(canvas, textvariable=mha, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    emha.place(x=465, y=214)

    leia = Label(canvas, text="Excercise Indused Angina(Y/N) :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    leia.place(x = 30,y = 234)

    leiae = Entry(canvas, textvariable=eia, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    leiae.place(x=465, y=243)

    stl = Label(canvas, text="ST Depression Induced By Exercise Relative To Rest :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    stl.place(x = 30,y = 263)

    ste = Entry(canvas, textvariable=st, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    ste.place(x=465, y=272)

    sl = Label(canvas, text="The Slope Of The Peak Exercise ST Segment :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    sl.place(x = 30,y = 292)

    se = Entry(canvas, textvariable=slst, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    se.place(x=465, y=301)

    lmv = Label(canvas, text="Number Of Major Vessels Colored By Flourosopy :", font=('arial', 12,'bold'), fg="white", bg="#297067", bd=10)
    lmv.place(x = 30,y = 321)

    lmve = Entry(canvas, textvariable=mv, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    lmve.place(x=465, y=330)

    ltha = Label(canvas, text='A Blood Disorder Called Thalassemia :', font=('arial', 12,'bold'), fg="white", bg="#297067",bd=10)
    ltha.place(x = 30,y = 350)
    ltha = Label(canvas, text='  (3=Normal, 6 = Fixed Defect, 7 = Reversable Defect)',font=('arial', 12,'bold'), fg="white", bg="#297067")
    ltha.place(x = 30,y = 379)
    etha = Entry(canvas, textvariable=tha, font=('arial', 12,'bold'), width=45, bg="white", fg = '#297067')
    etha.place(x=465, y=359)

    bh = Button(canvas, text="Analyze", fg="white", bg="#297067", width = 36,
                font=("Calibri", "16",'bold'),command=submit)
    bh.place(x=467, y=390)

      
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def about():
                canvas = Canvas(window, bg="#297067", height=457, width=888)
                canvas.place(x=0,y=249)
                j = Label(canvas, text='''
STEALTH : HUMAN HEALTH ANALYZER is a software that helps to predict if a person has chances of having
any heart disease, breast cancer or diabetes. STEALTH takes various criterias as input then in the backend
it runs advanvced machine learning algorithms using training data and predict out most accurate results.
Also it have a fully functioning mental health chatbot that guide people regarding mental issues, on top
of that it have a symtoms dignosis function that ask for perticular symptoms and if it is present it tells
the disease name, other system and recommend the doctor they should consult.

About algorithm used :
1. Random forests or random decision forests are an ensemble learning method for 
classification, regression and other tasks that operate by constructing a multitude of decision trees at training
time and outputting the class that is the mode of the classes (classification) or mean/average prediction
(regression) of the individual trees. Random decision forests correct for decision trees' habit of overfitting to
their training set. Random forests generally outperform decision trees, but their accuracy is lower than gradient
boosted trees. However, data characteristics can affect their performance.
2. k-Nearest Neighbours. It is a supervised learning algorithm. This means that we train it under supervision.
We train it using the labelled data already available to us

''', font=('arial', 12), fg="white", bg="#297067", bd=10)
                j.place(x = 50,y = 5)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Exit():
    result = tkMessageBox.askquestion(
        'STEALTH', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        window.destroy()
        exit()

    else:
        tkMessageBox.showinfo(
            'Return', 'You will now return to the main screen')


def healthdig():
	os.system('cmd /k "python healthdig.py"')

def search():

    searchwin=Tk()
    searchwin.title("STEALTH | Search For Doctors")
    searchwin.geometry("780x450")  
    searchwin.resizable(0,0)
    search=StringVar(searchwin)

    searchwin.config(bg="#297067")

    def searchdata():
        treev.delete(*treev.get_children())
        database()
        query ="select id,name,email,phone_no,location,Timing,nearby from doctor"
        cursor.execute(query)
        data = cursor.fetchall()
        for i in range(len(data)):
            if data[i][4]==search.get() or data[i][-1]==search.get():
                treev.insert("",i,text=str(i),values=data[i])

    def searchdataall():
        treev.delete(*treev.get_children())
        database()
        query ="select id,name,email,phone_no,location,Timing from doctor"
        cursor.execute(query)
        data = cursor.fetchall()
        for i in range(len(data)):
            treev.insert("",i,text=str(i),values=data[i])


    h1 = Label(searchwin, text="Search For Doctors",font=("",24,"bold"),bg="#297067",fg="white")
    h1.place(x=230,y=15) 
    h2 = Label(searchwin, text="Location:",font=("",20,"bold"),bg="#297067",fg="white")
    h2.place(x=30,y=100)

    e2 = Entry(searchwin,textvariable=search,font=("",23),width=22,bg="gray10",fg="white")
    e2.place(x=180,y=100)
    b1 = Button(searchwin, text="Search",font=("",15),bd=2,relief="solid",width=15,bg="#297067",fg="white",command=searchdata)
    b1.place(x=559,y=100)
    treev = ttk.Treeview(searchwin, selectmode ='browse')
      
    # Calling pack method w.r.to treeview
    treev.place(x=30,y=170)

    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(searchwin, 
                               orient ="vertical", 
                               command = treev.yview)
      
    # Calling pack method w.r.to verical 
    # scrollbar
    verscrlbar.place(x=30+682+4, y=173, height=200+22)
      
    # Configuring treeview
    treev.configure(xscrollcommand = verscrlbar.set)
      
    # Defining number of columns
    treev["columns"] = ("1", "2", "3","4","5","6")
      
    # Defining heading
    treev['show'] = 'headings'
      
    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width = 80 , anchor ='c')
    treev.column("2", width = 100, anchor ='nw')
    treev.column("3", width = 150, anchor ='nw')
    treev.column("4", width = 152, anchor ='nw')
    treev.column("5", width = 100, anchor ='nw')
    treev.column("6", width = 100, anchor ='nw')

    # Assigning the heading names to the 
    # respective columns
    treev.heading("1", text ="S.no.")
    treev.heading("2", text ="Name")
    treev.heading("3", text ="Email")
    treev.heading("4", text ="Phone No.")
    treev.heading("5", text ="Location")
    treev.heading("6", text ="Timing")
    searchdataall()
    searchwin.mainloop()

def bookamb():
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open_new("tel:+918097585837") 
    pyperclip.copy("tel:+918097585837")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

about()

b1 = Button(window, text="Heart Analysis", fg="white", bg="#297067", width = 15,
            font=("Arial", "14"),command=heart)
b1.place(x=0, y=210)
b2 = Button(window, text="Diabeties Analysis", fg="white", bg="#297028", width = 15,
            font=("Arial", "14"),command=diab)
b2.place(x=175, y=210)
b3 = Button(window, text="Breast Cancer Analysis", fg="white", bg="#297067",
            font=("Arial", "14"),command=br_cancer)
b3.place(x=350, y=210)
b4 = Button(window, text="Health Dignosis", fg="white", bg="#297028",
            font=("Arial", "14"),width=19,command=healthdig)
b4.place(x=563, y=210)

b5 = Button(window, text="Search For Doctors", fg="white", bg="#297000", width = 40,
            font=("Arial", "14"),command=search)
b5.place(x=0, y=170)

b6 = Button(window, text="About", fg="white", bg="#297067", width = 9,
            font=("Arial", "14"),command=about)
b6.place(x=782, y=210)

b7 = Button(window, text="Ambulence Near Me", fg="white", bg="#297000", width = 41,
            font=("Arial", "14"),command=bookamb)
b7.place(x=450, y=170)

window.mainloop()


