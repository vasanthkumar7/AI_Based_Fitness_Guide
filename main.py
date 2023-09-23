
from tkinter import *
from tkinter import ttk 
from PIL import ImageTk, Image
from click import edit
from cryptography.fernet import Fernet
import cv2
import numpy as np
import face_recognition
import webbrowser

from tkinter import messagebox

#gym
from jumpingjacks import jumpingJacks
from abdominalcrunches_ import abdominalcrunchesf
from mountainclimbers_ import mountainclimbersf
from legraises_ import legraisesf
from plank_ import plankf
from cobrastrech_ import cobrastrechf
from armraises_ import armraisesf
from tricepdips_ import tricepdipsf
from pushups_ import pushupsf
from squats_ import squatsf
from sideleglif_left_ import sideleglift_leftf
from sideleglif_right import sideleglift_rightf
from backwardlunge_ import backwardlungef
from donkeykickleft_ import donkeykickleftf
from donkeykickright_ import donkeykickrightf
from kneepushups_ import kneepushupsf
from inclinepushups_ import inclinepushupsf


#yoga

from chairpose_ import chairposef
from downwarddog_ import downwarddogf
from warriorII_ import warriorIIf
from treepose_ import treeposef
from triangularpose_ import triangularf
from puppyonchair_ import puppyonchairf
from warriorI_ import warriorIf
from camelpose_ import camelposef
from sideplank_ import sideplankf


import os
import random


root=Tk()
root.title("AI BASED SPORTS TRAINER AND FITNESS GUIDE")  #title


#global variables

glb_name=""
glb_fileName=""
glb_key=""
glb_height=""
glb_weight=""
glb_age=""
glb_gender=""
glb_ns=""
glb_ne=""
glb_cb=""
glb_yoga=""
glb_min=""
glb_camera=""
glb_whatToUpdate=""
glb_previouspage=""


glb_morning={100:("idli","1"), 120:("dosa","1"),250:("masala dosa","1"),150:("sambar","1cup"),160:("cereal or oats","1bowl"),75:("egg","1"),80:("boiled egg","1"),140:("milk","1cup"),45:("butter","1ts"),110:("banana","1")}

glb_mq=["1","1","1","1cup","1Cup","1","1","1cup","1ts","1"]
glb_mc=[100,120,250,150,160,75,80,140,45,110]

glb_lunch={200:("vegetable rice","1plate"),120:("Boiled rice","1plate"),150:("Sambar","1plate"),20:("raita","1serving"),100:("salad","1plate"),100:("curd","1cup"),155:("cheese","50g"),45:("butter","1ts"),120:("omelette","1"),75:("egg","1"),85:("boiled egg","1")}
glb_lq=["1plate","1cup","1cup","1serving","1plate","1cup","50g","1ts","1","1","1"]
glb_lc=[200,120,150,20,100,110,155,45,120,75,85]

glb_evening={150:("milk","1cup"),250:("sandwidch","1"),70:("vada","1"),140:("samosa","1"),110:("banana","1"),10:("watermelon","1slice"),25:("straberries","1bowl"),60:("cherries","1bowl"),65:("grapes","1bowl")}
glb_eq=["1cup","1","1","1","1","1slice","1bowl","1bowl","1bowl"]
glb_ec=[150,250,70,140,110,10,60,65]

glb_dinner={100:("idli","1"), 120:("dosa","1"),250:("masala dosa","1"),150:("sambar","1cup"),90:("salad","1plate"),110:("curd","1cup"),155:("cheese","50g"),45:("butter","1ts"),120:("omelette","1"),75:("egg","1"),85:("boiled egg","1")}
glb_dq=["1","1","1","1cup","1plate","1cup","50g","1ts","1","1","1"]
glb_dc=[100,120,250,150,90,110,155,45,120,75,85]

sets_or_time="sets"

#functions 

def profile_visit():
    global nam,hei,wei,ag,gen,cb,sd,ed,yd,ms,welcomePage,profilePage
    global glb_name,glb_filename,glb_key,glb_height,glb_weight,glb_age,glb_gender,glb_ns,glb_ne,glb_cb,glb_yoga,glb_min,glb_camera
    nam.config(text="Name : "+glb_name)
    hei.config(text="Height(in Cm) : "+glb_height)
    wei.config(text="Weight(in Kg) : "+glb_weight)
    ag.config(text="Age : "+glb_age)
    gen.config(text="Gender : "+glb_gender)
    cb.config(text="Calories Burned : "+glb_cb)
    sd.config(text="Number Of Sets Done : "+glb_ns)
    ed.config(text="Number Of Excersices Done : "+glb_ne)
    yd.config(text="Number Of Yogasanam's Done : "+glb_yoga)
    ms.config(text="Number of Minutes Spent : "+glb_min)
    navigate(welcomePage,profilePage)
    
def profile_visit1():
    global nam,hei,wei,ag,gen,cb,sd,ed,yd,ms,welcomePage,profilePage
    global glb_name,glb_filename,glb_key,glb_height,glb_weight,glb_age,glb_gender,glb_ns,glb_ne,glb_cb,glb_yoga,glb_min,glb_camera
    nam.config(text="Name : "+glb_name)
    hei.config(text="Height(in Cm) : "+glb_height)
    wei.config(text="Weight(in Kg) : "+glb_weight)
    ag.config(text="Age : "+glb_age)
    gen.config(text="Gender : "+glb_gender)
    cb.config(text="Calories Burned : "+glb_cb)
    sd.config(text="Number Of Sets Done : "+glb_ns)
    ed.config(text="Number Of Excersices Done : "+glb_ne)
    yd.config(text="Number Of Yogasanam's Done : "+glb_yoga)
    ms.config(text="Number of Minutes Spent : "+glb_min)

def mainImageFunction(ratio,imageinfo):
    stimg=Image.open(imageinfo)
    width,height=stimg.size
    owidth,oheight=int(width/ratio),int(height/ratio)
    myimg=ImageTk.PhotoImage(stimg.resize((owidth,oheight),Image.ANTIALIAS))
    return myimg




def list_tostring(a):
    l=""
    for i in a:
        l+=str(i)+" "
    return l

def save_faces():
    messagebox.showinfo("Information", "Press 's' to capture ")
    cap = cv2.VideoCapture(0)
    while True:
        img = cap.read()
        img = np.array(img[1], dtype=np.uint8)
        img2=np.array(img[1], dtype=np.uint8)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('img', img)
        if cv2.waitKey(1)& 0xFF == ord('s'):
            cv2.imwrite('test1.jpg',img)
            break
    cap.release()
    cv2.destroyAllWindows()


## signup functions

def signupPannuga():
    global startingPage,signupPage
    startingPage.grid_forget()
    save_faces()
    signupPage.grid(row=0,column=1)

def signupPannitanga():
    global nameSignUp , startingPage,signupPage,gender,heightSignUp,weightSignUp,ageSignUp
    if nameSignUp.get()=="" or heightSignUp.get()=="" or weightSignUp.get()=="" or ageSignUp.get()=="" :
        messagebox.showinfo("information", "Enter Your Name!!")
        return
    known_image = face_recognition.load_image_file("test1.jpg")
    biden_encoding = face_recognition.face_encodings(known_image)[0]
    ass=list_tostring(list(biden_encoding))
    biden_encoding=list(map(float,ass.split()))
    biden_encoding=np.array(biden_encoding)
    f=open("users.txt","a")
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encMessage = fernet.encrypt(ass.encode())
    enname=nameSignUp.get()
    encMessage1= fernet.encrypt(enname.encode())

    enheight=heightSignUp.get()
    encMessage2= fernet.encrypt(enheight.encode())

    enweight=weightSignUp.get()
    encMessage3= fernet.encrypt(enweight.encode())

    enage=ageSignUp.get()
    encMessage4= fernet.encrypt(enage.encode())

    engender=gender.get()
    encMessage5= fernet.encrypt(engender.encode())

    encMessage6=fernet.encrypt("0".encode())
    f.write(str(key)+" "+str(encMessage)+" "+str(encMessage1)+" \n")

    ff=open("nothing/"+str(encMessage1)+".txt","a")

    ff.write(str(encMessage1)+" \n"+str(encMessage2)+" \n"+
    str(encMessage3)+" \n"+str(encMessage4)+" \n"+str(encMessage5)+" \n"+str(encMessage6)+" \n"+str(encMessage6)
    +" \n"+str(encMessage6)+" \n"+str(encMessage6)+" \n"+str(encMessage6)+" \n"+str(encMessage6))

    signupPage.grid_forget()
    startingPage.grid(row=0,column=0)

def navigate(startingpage,destpage):
    global glb_previouspage
    glb_previouspage=startingpage

   
    startingpage.grid_forget()
    destpage.grid(row=0,column=0)


def spnavigate(startingpage):
    global glb_previouspage

    startingpage.grid_forget()

    glb_previouspage.grid(row=0,column=0)


def navigate1(startingpage,destpage,rows,columns):
    startingpage.grid_forget()
    destpage.grid(row=rows,column=columns)

def exnavigate(fir,sec,color,what):
    global sets_or_time
    sets_or_time=what
    fir.config(bg="black",fg=color)
    sec.config(bg=color,fg="black")

## setting function

def go_to_settings():
    global whichCamera,cameras,glb_camera
    whichCamera.set(cameras[int(glb_camera)])
    navigate(welcomePage,settingsPage)

def settings_save():
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)
    for i in ff[:10]:
        fg.write(i+" \n")
    if whichCamera.get()=="Primary":
        glb_camera="0"
        fg.write(str(fernet.encrypt("0".encode()))+" \n")
    else:
        glb_camera="1"
        fg.write(str(fernet.encrypt("1".encode()))+" \n")

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")
    

## diet function


def diet_page():
    global whatType,weightGainMsg,weightLossMsg,glb_height,glb_weight,welcomePage,dietPage
    colors=["red","yellow","green"]
    msgs=["NOT RECOMMENDED","OPTIONAL","HIGHLY RECOMMENDED"]
    bmi=(int(glb_weight)/(( int(glb_height)**2)/10000))
    if bmi<18.5:
        whatType.config(text="Your body type : UNDER WEIGHT")
        weightLossMsg.config(text=msgs[0],fg=colors[0])
        weightGainMsg.config(text=msgs[2],fg=colors[2])

    elif bmi>=18.5 and bmi<25:
        whatType.config(text="Your body type : MODERATE")
        weightLossMsg.config(text=msgs[1],fg=colors[1])
        weightGainMsg.config(text=msgs[1],fg=colors[1])

    elif bmi>=25 and bmi<30:
        whatType.config(text="Your body type : OVER WEIGHT")
        weightLossMsg.config(text=msgs[2],fg=colors[2])
        weightGainMsg.config(text=msgs[0],fg=colors[0])
        
    elif bmi>=30:
        whatType.config(text="Your body type : OBESITY")
        weightLossMsg.config(text=msgs[2],fg=colors[2])
        weightGainMsg.config(text=msgs[0],fg=colors[0])

    navigate(welcomePage,dietPage)


#weightloss page function
def find_dupes(l,combo):
    k=[]
    count=[]
    for i in l:
        if i not in k:
            k.append(i)
            count.append(l.count(i))
    combo.append((k,count))

def unique_combination(l, sums, K, local, A,combo):
    if (sums == K):
        find_dupes(local,combo)
        return 
    for i in range(l, len(A), 1):
        if (sums + A[i] > K):
            break
       
        local.append(A[i])
        unique_combination(i , sums + A[i],K, local, A,combo)
 
        local.remove(local[len(local) - 1])


 
def Combination(A, K,combo):
 
    A.sort(reverse=False)
 
    local = []
 
    unique_combination(0, 0, K, local, A,combo)


def weight_gain_page():
    global glb_name,glb_filename,glb_key,glb_height,glb_weight,glb_age,glb_gender,glb_ns,glb_ne,glb_cb,glb_yoga,glb_min,glb_camera
    global weightLossPage_right_report1,dietPage,weightLossPage,weightLossPage_right_wte
    global weightGainPage_right_report1,dietPage,weightGainPage,weightGainPage_right_wte
    global glb_mc,glb_mq,glb_morning,glb_lc,glb_lq,glb_lunch,glb_ec,glb_eq,glb_evening,glb_dc,glb_dq,glb_dinner

    calorie_expence=0
    report=""

    if glb_gender=="male":
        calorie_expence=66+(6.2*(2.2*int(glb_weight)))+(12.7*(int(glb_height)*0.393701))-(6.76*int(glb_age))
    else:
        calorie_expence=655.1+(4.35*(2.2*int(glb_weight)))+(4.7*(int(glb_height)*0.393701))-(4.7*int(glb_age))


    bmi=(int(glb_weight)/((int(glb_height)**2)/10000))

    if bmi<18.5:
        report="Based on your BMI your body type is UNDER WEIGHT . So weight loss is not recommended but if you want to lose weight here is the diet report . To maintain same weight you must eat atleast "+str(int(1.2*calorie_expence))+" calories . To gain weight you must eat "+str(int(1.2*calorie_expence))+" calories and burn "+str(int(1.2*calorie_expence)-500)+" calories . By this you can gain 0.5 kg a week."
    elif bmi>=18.5 and bmi<25:
        report="Based on your BMI you body type is Moderate . So weight loss is optional for You . If you want to lose weight here is your diet report . . To maintain same weight you must eat atleast "+str(int(1.2*calorie_expence))+" calories . To gain weight you must eat "+str(int(1.2*calorie_expence))+" calories and burn "+str(int(1.2*calorie_expence)-500)+" calories . By this you can gain 0.5 kg a week."
    elif bmi>=25:
        report="Based on your BMI your body type is OVER WEIGHT / OBESE . So weight loss highly recommended for you . Here is the diet report . To maintain same weight you must eat atleast "+str(int(1.2*calorie_expence))+" calories . To gain weight you must eat "+str(int(1.2*calorie_expence))+" calories and burn "+str(int(1.2*calorie_expence)-500)+" calories . By this you can gain 0.5 kg a week."
    for item in weightGainPage_right_wte.get_children():
      weightGainPage_right_wte.delete(item)



    newReport=""
    counts=0

    report=report.split()
    for i in report:
        if counts+len(i)>50:
            newReport+=" "*(50-counts)+i+" "
            counts=0
        else:
            newReport+=i+" "
        counts+=len(i)+1

    report=newReport
    weightGainPage_right_report1 .config(state= NORMAL)

    weightGainPage_right_report1.delete("1.0","end")
    weightGainPage_right_report1.insert(END,report)
    weightGainPage_right_report1 .config(state= DISABLED)

    calories_split=int((1.2*calorie_expence)/3)
    morning=calories_split-(calories_split%10)
    lunch=int(calories_split/2)-(int(calories_split/2)%10)
    evening=int(calories_split/2)-(int(calories_split/2)%10)
    night=calories_split-(calories_split%10)


    morning_combo=[]
    Combination(glb_mc, morning,morning_combo)
    lunch_combo=[]
    Combination(glb_lc,lunch,lunch_combo)
    evening_combo=[]
    Combination(glb_ec,evening,evening_combo)
    dinner_combo=[]
    Combination(glb_dc,night,dinner_combo)

    morning_combo=morning_combo[random.randint(0,len(morning_combo)-1)]
    lunch_combo=lunch_combo[random.randint(0,len(lunch_combo)-1)]
    evening_combo=evening_combo[random.randint(0,len(evening_combo)-1)]
    dinner_combo=dinner_combo[random.randint(0,len(dinner_combo)-1)]


    counts=0
    for j,i in enumerate(morning_combo[0]):
        print(glb_mq,glb_mc.index(i))
        weightGainPage_right_wte.insert(parent='', index=counts, iid=counts, values=(glb_morning[i][0],glb_morning[i][1]+" X "+str(morning_combo[1][j]), "9.00 AM"))
        counts+=1

    for j,i in enumerate(lunch_combo[0]):
        weightGainPage_right_wte.insert(parent='', index=counts, iid=counts, values=(glb_lunch[i][0], glb_lunch[i][1]+" X "+str(lunch_combo[1][j]), "1.00 PM"))
        counts+=1

    for j,i in enumerate(evening_combo[0]):
        weightGainPage_right_wte.insert(parent='', index=counts, iid=counts, values=(glb_evening[i][0], glb_evening[i][1]+" X "+str(evening_combo[1][j]), "4.00 PM"))
        counts+=1

    for j,i in enumerate(dinner_combo[0]):
        weightGainPage_right_wte.insert(parent='', index=counts, iid=counts, values=(glb_dinner[i][0], glb_dinner[i][1]+" X "+str(dinner_combo[1][j]), "8.30 PM"))
        counts+=1
    

    navigate(dietPage,weightGainPage)

def weight_loss_page():
    global glb_name,glb_filename,glb_key,glb_height,glb_weight,glb_age,glb_gender,glb_ns,glb_ne,glb_cb,glb_yoga,glb_min,glb_camera
    global weightLossPage_right_report1,dietPage,weightLossPage,weightLossPage_right_wte
    global glb_mc,glb_mq,glb_morning,glb_lc,glb_lq,glb_lunch,glb_ec,glb_eq,glb_evening,glb_dc,glb_dq,glb_dinner

    calorie_expence=0
    report=""

    if glb_gender=="male":
        calorie_expence=66+(6.2*(2.2*int(glb_weight)))+(12.7*(int(glb_height)*0.393701))-(6.76*int(glb_age))
    else:
        calorie_expence=655.1+(4.35*(2.2*int(glb_weight)))+(4.7*(int(glb_height)*0.393701))-(4.7*int(glb_age))


    bmi=(int(glb_weight)/((int(glb_height)**2)/10000))

    if bmi<18.5:
        report="Based on your BMI your body type is UNDER WEIGHT . So weight loss is not recommended but if you want to lose weight here is the diet report . To maintain same weight you must eat atleast "+str(int(1.2*calorie_expence))+" calories . To reduce weight you must eat "+str(int(1.2*calorie_expence))+" calories and burn "+str(int(1.2*calorie_expence)+500)+" calories . By this you can lose 0.5 kg a week."
    elif bmi>=18.5 and bmi<25:
        report="Based on your BMI you body type is Moderate . So weight loss is optional for You . If you want to lose weight here is your diet report . . To maintain same weight you must eat atleast "+str(int(1.2*calorie_expence))+" calories . To reduce weight you must eat "+str(int(1.2*calorie_expence))+" calories and burn "+str(int(1.2*calorie_expence)+500)+" calories . By this you can lose 0.5 kg a week."
    elif bmi>=25:
        report="Based on your BMI your body type is OVER WEIGHT / OBESE . So weight loss highly recommended for you . Here is the diet report . To maintain same weight you must eat atleast "+str(int(1.2*calorie_expence))+" calories . To reduce weight you must eat "+str(int(1.2*calorie_expence))+" calories and burn "+str(int(1.2*calorie_expence)+500)+" calories . By this you can lose 0.5 kg a week."

    for item in weightLossPage_right_wte.get_children():
      weightLossPage_right_wte.delete(item)
    weightLossPage_right_report1 .config(state= NORMAL)


    counts=0

    newReport=""

    report=report.split()
    for i in report:
        if counts+len(i)>50:
            newReport+=" "*(50-counts)+i+" "
            counts=0
        else:
            newReport+=i+" "
        counts+=len(i)+1

    report=newReport


    weightLossPage_right_report1.delete("1.0","end")
    weightLossPage_right_report1.insert(END,report)
    weightLossPage_right_report1 .config(state= DISABLED)

    calories_split=int((1.2*calorie_expence)/3)
    morning=calories_split-(calories_split%10)
    lunch=int(calories_split/2)-(int(calories_split/2)%10)
    evening=int(calories_split/2)-(int(calories_split/2)%10)
    night=calories_split-(calories_split%10)


    morning_combo=[]
    Combination(glb_mc, morning,morning_combo)
    lunch_combo=[]
    Combination(glb_lc,lunch,lunch_combo)
    evening_combo=[]
    Combination(glb_ec,evening,evening_combo)
    dinner_combo=[]
    Combination(glb_dc,night,dinner_combo)

    morning_combo=morning_combo[random.randint(0,len(morning_combo)-1)]
    lunch_combo=lunch_combo[random.randint(0,len(lunch_combo)-1)]
    evening_combo=evening_combo[random.randint(0,len(evening_combo)-1)]
    dinner_combo=dinner_combo[random.randint(0,len(dinner_combo)-1)]


    counts=0
    for j,i in enumerate(morning_combo[0]):
        print(glb_mq,glb_mc.index(i))
        weightLossPage_right_wte.insert(parent='', index=counts, iid=counts, values=(glb_morning[i][0],glb_morning[i][1]+" X "+str(morning_combo[1][j]), "9.00 AM"))
        counts+=1

    for j,i in enumerate(lunch_combo[0]):
        weightLossPage_right_wte.insert(parent='', index=counts, iid=counts, values=(glb_lunch[i][0], glb_lunch[i][1]+" X "+str(lunch_combo[1][j]), "1.00 PM"))
        counts+=1

    for j,i in enumerate(evening_combo[0]):
        weightLossPage_right_wte.insert(parent='', index=counts, iid=counts, values=(glb_evening[i][0], glb_evening[i][1]+" X "+str(evening_combo[1][j]), "4.00 PM"))
        counts+=1

    for j,i in enumerate(dinner_combo[0]):
        weightLossPage_right_wte.insert(parent='', index=counts, iid=counts, values=(glb_dinner[i][0], glb_dinner[i][1]+" X "+str(dinner_combo[1][j]), "8.30 PM"))
        counts+=1
    
    navigate(dietPage,weightLossPage)




##update functions





    
    


## login functions

def check_facematch():
    global glb_name,glb_filename,glb_key,glb_height,glb_weight,glb_age,glb_gender,glb_ns,glb_ne,glb_cb,glb_yoga,glb_min,glb_camera
    messagebox.showinfo("information", "Press 's' to capture ")
    flag=0
    cap = cv2.VideoCapture(0)
    while True:
        img = cap.read()
        img = np.array(img[1], dtype=np.uint8)
        cv2.imshow('img', img)
        if cv2.waitKey(1)& 0xFF == ord('s'):
            cv2.imwrite('test1.jpg',img)
            break
    cap.release()
    cv2.destroyAllWindows() 
    f=open("users.txt","r")
    ff=f.read().split("\n")
    for i in ff:
        j=i.split()
        if j==[]:
            break
        jkl=bytes(j[0][2:len(j[0])-1],'utf-8')
        fernet = Fernet(jkl)
        decMessage = fernet.decrypt(bytes(j[1][2:len(j[1])-1],'utf-8')).decode()
        decMessage2 = fernet.decrypt(bytes(j[2][2:len(j[2])-1],'utf-8')).decode()
        bdg=list(map(float,decMessage.split()))
        bdg=np.array(bdg)
        unknown_image = face_recognition.load_image_file("test1.jpg")
        try:
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        except:
            messagebox.showerror("information", "Face is not detected")
            return 

        results = face_recognition.compare_faces([bdg], unknown_encoding)
        if results[0]:
            glb_key=jkl
            glb_filename=j[2]


            ff=open("nothing/"+str(j[2])+".txt","r").read().split("\n")
            glb_name=fernet.decrypt(bytes(ff[0][2:len(j[1])-1],'utf-8')).decode()
            glb_height=fernet.decrypt(bytes(ff[1][2:len(j[1])-1],'utf-8')).decode()
            glb_weight=fernet.decrypt(bytes(ff[2][2:len(j[1])-1],'utf-8')).decode()
            glb_age=fernet.decrypt(bytes(ff[3][2:len(j[1])-1],'utf-8')).decode()
            glb_gender=fernet.decrypt(bytes(ff[4][2:len(j[1])-1],'utf-8')).decode()
            glb_cb=fernet.decrypt(bytes(ff[5][2:len(j[1])-1],'utf-8')).decode()
            glb_ns=fernet.decrypt(bytes(ff[6][2:len(j[1])-1],'utf-8')).decode()
            glb_ne=fernet.decrypt(bytes(ff[7][2:len(j[1])-1],'utf-8')).decode()
            glb_yoga=fernet.decrypt(bytes(ff[8][2:len(j[1])-1],'utf-8')).decode()
            glb_min=fernet.decrypt(bytes(ff[9][2:len(j[1])-1],'utf-8')).decode()
            glb_camera=fernet.decrypt(bytes(ff[10][2:len(j[1])-1],'utf-8')).decode()
            
            welcome_home()


            flag=1
    if flag==0:
        messagebox.showinfo("information", "Your profile doesn't exist")




## welcomePage functions

def welcome_home():
    global glb_name,glb_filename,welcomePage,startingPage,welcomeMsg
    welcomeMsg.config(text="Hi, "+glb_name.upper() )
    startingPage.grid_forget()
    welcomePage.grid(row=0,column=0)



#starting page

startingPage=Frame(root,bg="black")

f1=mainImageFunction(1.5,"startingPage.png")
sideimg=Label(startingPage,image=f1)
sideimg.grid(row=0,column=0)

startingPage_right=Frame(startingPage,bg="black")

login=Button(startingPage_right,text="Login",font=("Times", "26", "bold italic") ,width=15,bg="#FFCC00",command=check_facematch)
login.grid(row=0,column=0,padx=10,pady=10)

signup=Button(startingPage_right,text="Sign Up",font=("Times", "26", "bold italic") ,width=15,bg="#FFCC00" , command=signupPannuga)
signup.grid(row=1,column=0,padx=10,pady=10)

bottomText=Label(startingPage_right,text="New user? Signup . Have account - Login",font=("Times",15),fg="#FFCC00" ,bg="black")
bottomText.grid(row=3,column=0,pady=20)

startingPage_right.grid(row=0,column=1,padx=30)

startingPage.grid(row=0,column=0)



# signupPage #FF914D

signupPage=Frame(root,bg="black")

f2=mainImageFunction(1.5,"signup1.png")
sidimg=Label(signupPage,image=f2)
sidimg.grid(row=0,column=0)

signupPage_right=Frame(signupPage ,bg="black")
nameLabel=Label(signupPage_right,text="Enter your Name:" ,font=("Times", "18", "bold italic") ,fg="#FF914D",bg="black")
nameLabel.grid(row=0,column=0,pady=10)
nameSignUp=Entry(signupPage_right,width=17   ,font=("Times", "18", "bold italic"),bg="#FF914D")
nameSignUp.grid(row=0,column=1,pady=10,padx=10)

heightLabel=Label(signupPage_right,text="Enter your Height(cm):" ,font=("Times", "18", "bold italic") ,fg="#FF914D",bg="black")
heightLabel.grid(row=1,column=0,pady=10)
heightSignUp=Entry(signupPage_right,width=17   ,font=("Times", "18", "bold italic"),bg="#FF914D")
heightSignUp.grid(row=1,column=1,pady=10,padx=10)

weightLabel=Label(signupPage_right,text="Enter your Weight(kg):" ,font=("Times", "18", "bold italic") ,fg="#FF914D",bg="black")
weightLabel.grid(row=2,column=0,pady=10)
weightSignUp=Entry(signupPage_right,width=17   ,font=("Times", "18", "bold italic"),bg="#FF914D")
weightSignUp.grid(row=2,column=1,pady=10,padx=10)

ageLabel=Label(signupPage_right,text="Enter your Age:" ,font=("Times", "18", "bold italic") ,fg="#FF914D",bg="black")
ageLabel.grid(row=3,column=0,pady=10)
ageSignUp=Entry(signupPage_right,width=17   ,font=("Times", "18", "bold italic"),bg="#FF914D")
ageSignUp.grid(row=3,column=1,pady=10,padx=10)


gender=StringVar()
genders=["male","female"]
gender.set(genders[0])
genderLabel=Label(signupPage_right,text="Select your Gender:" ,font=("Times", "18", "bold italic") ,fg="#FF914D",bg="black")
genderLabel.grid(row=4,column=0,pady=10)
genderSignUp=OptionMenu(signupPage_right,gender,*genders)
genderSignUp.config(width=15   ,font=("Times", "15", "bold italic"),bg="#FF914D")
genderSignUp.grid(row=4,column=1,pady=10,padx=10)




signupSave=Button(signupPage_right,text="Sign Up",font=("Times", "18", "bold italic") ,width=25,bg="#FF914D",command=signupPannitanga)
signupSave.grid(row=5,column=0,pady=10,columnspan=2)

goBack=Button(signupPage_right,text="Go Back",font=("Times", "18", "bold italic"),command=lambda: navigate(signupPage,startingPage) ,width=25,bg="#FF914D")
goBack.grid(row=6,column=0,pady=10,columnspan=2)

signupPage_right.grid(row=0,column=1,padx=40)


# welcomepage

welcomePage=Frame(root,bg="black")

f3=mainImageFunction(1.5,"homePage2.png")
sdimg=Label(welcomePage,image=f3)
sdimg.grid(row=0,column=0)

welcomePage_right=Frame(welcomePage,bg="black")
welcomeMsg=Label(welcomePage_right,text="",font=("Times", "20", "bold"),bg="black",fg="#38B6FF")
welcomeMsg.grid(row=0,column=0,pady=20)

gym=Button(welcomePage_right,text="GYM",font=("Times", "18", "bold italic") ,width=15,bg="#38B6FF",command=lambda:navigate(welcomePage,gymPage))
gym.grid(row=1,column=0,pady=10)

yoga=Button(welcomePage_right,text="YOGA",font=("Times", "18", "bold italic") ,width=15,bg="#38B6FF",command=lambda:navigate(welcomePage,yogaPage))
yoga.grid(row=2,column=0,pady=10)

dietplan=Button(welcomePage_right,text="DIET PLAN",font=("Times", "18", "bold italic") ,width=15,bg="#38B6FF",command=diet_page)
dietplan.grid(row=3,column=0,pady=10)

profile=Button(welcomePage_right,text="PROFILE",font=("Times", "18", "bold italic") ,width=15,bg="#38B6FF",command=profile_visit)
profile.grid(row=4,column=0,pady=10)


settings=Button(welcomePage_right,text="SETTINGS",font=("Times", "18", "bold italic") ,width=15,bg="#38B6FF",command=go_to_settings)
settings.grid(row=5,column=0,pady=10)

logout=Button(welcomePage_right,text="LOGOUT",font=("Times", "18", "bold italic") ,width=15,bg="#38B6FF",command=lambda: navigate(welcomePage,startingPage))
logout.grid(row=6,column=0,pady=10)

welcomePage_right.grid(row=0,column=1,padx=50)



#gym #FF1616

gymPage=Frame(root,bg="black")

f4=mainImageFunction(1.5,"gym.png")
ggimg=Label(gymPage,image=f4)
ggimg.grid(row=0,column=0)

gymPage_right=Frame(gymPage,bg="black")

abs=Button(gymPage_right,text="ABS",font=("Times", "18", "bold italic") ,width=15,bg="#FF1616",command=lambda:navigate(gymPage,absPage))
abs.grid(row=1,column=0,pady=10)

arm=Button(gymPage_right,text="ARM",font=("Times", "18", "bold italic") ,width=15,bg="#FF1616",command=lambda:navigate(gymPage,armsPage))
arm.grid(row=2,column=0,pady=10)

leg=Button(gymPage_right,text="LEGS",font=("Times", "18", "bold italic") ,width=15,bg="#FF1616",command=lambda:navigate(gymPage,legsPage))
leg.grid(row=3,column=0,pady=10)

chest=Button(gymPage_right,text="CHEST",font=("Times", "18", "bold italic") ,width=15,bg="#FF1616",command=lambda:navigate(gymPage,chestPage))
chest.grid(row=4,column=0,pady=10)

shoulder=Button(gymPage_right,text="SHOULDER",font=("Times", "18", "bold italic") ,width=15,bg="#FF1616",command=lambda:navigate(gymPage,shouldersPage))
shoulder.grid(row=5,column=0,pady=10)

backHome=Button(gymPage_right,text="GO BACK",font=("Times", "18", "bold italic") ,width=15,bg="#FF1616",command=lambda:navigate(gymPage,welcomePage))
backHome.grid(row=6,column=0,pady=10)

gymPage_right.grid(row=0,column=1,padx=50)


## abs #FF1616

absPage=Frame(root,bg="black")

absPic=mainImageFunction(1.5,"abs1.png")
ggimg=Label(absPage,image=absPic)
ggimg.grid(row=0,column=0)

absPage_right=Frame(absPage,bg="black")

jumpingjacks=Button(absPage_right,text="JUMPING JACKS",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(absPage,excersice1))
jumpingjacks.grid(row=1,column=0,pady=10)


abdominalcrunches=Button(absPage_right,text="ABDOMINAL CRUNCHES",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(absPage,excersice2))
abdominalcrunches.grid(row=2,column=0,pady=10)

mountainclimbers=Button(absPage_right,text="MOUNTAIN CLIMBERS",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(absPage,excersice3))
mountainclimbers.grid(row=3,column=0,pady=10)

legraises=Button(absPage_right,text="LEG RAISES",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(absPage,excersice4))
legraises.grid(row=4,column=0,pady=10)

plank=Button(absPage_right,text="PLANK",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(absPage,excersice5))
plank.grid(row=5,column=0,pady=10)

cobrastrech=Button(absPage_right,text="COBRA STRECH",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(absPage,excersice6))
cobrastrech.grid(row=6,column=0,pady=10)

backHome=Button(absPage_right,text="GO BACK",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(absPage,gymPage))
backHome.grid(row=7,column=0,pady=10)


absPage_right.grid(row=0,column=1,padx=50)


#chest #FF1616


chestPage=Frame(root,bg="black")

chestPic=mainImageFunction(1.5,"chest.png")
chestimg=Label(chestPage,image=chestPic)
chestimg.grid(row=0,column=0)

chestPage_right=Frame(chestPage,bg="black")

jumpingjacks=Button(chestPage_right,text="JUMPING JACKS",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(chestPage,excersice1))
jumpingjacks.grid(row=1,column=0,pady=10)


inclinepushups=Button(chestPage_right,text="INCLINE PUSHUPS",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(chestPage,excersice17))
inclinepushups.grid(row=2,column=0,pady=10)

kneepushups=Button(chestPage_right,text="KNEE PUSHUPS",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(chestPage,excersice16))
kneepushups.grid(row=3,column=0,pady=10)

pushups=Button(chestPage_right,text="PUSHUPS",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(chestPage,excersice9))
pushups.grid(row=4,column=0,pady=10)

cobrastrech=Button(chestPage_right,text="COBRA STRECH",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(chestPage,excersice6))
cobrastrech.grid(row=5,column=0,pady=10)

backHome=Button(chestPage_right,text="GO BACK",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(chestPage,gymPage))
backHome.grid(row=7,column=0,pady=10)

chestPage_right.grid(row=0,column=1,padx=50)









#arms

armsPage=Frame(root,bg="black")

armsPic=mainImageFunction(1.5,"arm1.png")
armimg=Label(armsPage,image=armsPic)
armimg.grid(row=0,column=0)

armsPage_right=Frame(armsPage,bg="black")

armraise=Button(armsPage_right,text="ARM RAISE",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(armsPage,excersice7))
armraise.grid(row=1,column=0,pady=10)


tricepdips=Button(armsPage_right,text="TRICEP DIPS",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(armsPage,excersice8))
tricepdips.grid(row=2,column=0,pady=10)

pushups=Button(armsPage_right,text="PUSHUPS",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(armsPage,excersice9))
pushups.grid(row=3,column=0,pady=10)

jumpingjacks=Button(armsPage_right,text="JUMPING JACKS",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(armsPage,excersice1))
jumpingjacks.grid(row=4,column=0,pady=10)


backHome=Button(armsPage_right,text="GO BACK",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(armsPage,gymPage))
backHome.grid(row=7,column=0,pady=10)

armsPage_right.grid(row=0,column=1,padx=50)



#leg

legsPage=Frame(root,bg="black")

legsPic=mainImageFunction(1.5,"leg1.png")
legimg=Label(legsPage,image=legsPic)
legimg.grid(row=0,column=0)

legsPage_right=Frame(legsPage,bg="black")

squats=Button(legsPage_right,text=" SQUATS",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(legsPage,excersice10))
squats.grid(row=1,column=0,pady=10)


sidelyingleglift=Button(legsPage_right,text="LEG LIFT LEFT",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(legsPage,excersice11))
sidelyingleglift.grid(row=2,column=0,pady=10)

sidelyinglegright=Button(legsPage_right,text="LEG LIFT RIGHT",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(legsPage,excersice12))
sidelyinglegright.grid(row=3,column=0,pady=10)

backwardlunge=Button(legsPage_right,text="BACKWARD LUNGE",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(legsPage,excersice13))
backwardlunge.grid(row=4,column=0,pady=10)

donkeykickright=Button(legsPage_right,text="DONKEY KICK RIGHT",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(legsPage,excersice15))
donkeykickright.grid(row=5,column=0,pady=10)

donkeykickleft=Button(legsPage_right,text="DONKEY KICK LEFT",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(legsPage,excersice14))
donkeykickleft.grid(row=6,column=0,pady=10)

backHome=Button(legsPage_right,text="GO BACK",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(legsPage,gymPage))
backHome.grid(row=7,column=0,pady=10)

legsPage_right.grid(row=0,column=1,padx=50)


#Shoulder

shouldersPage=Frame(root,bg="black")

shouldersPic=mainImageFunction(1.5,"shoulder.png")
shoulderimg=Label(shouldersPage,image=shouldersPic)
shoulderimg.grid(row=0,column=0)

shouldersPage_right=Frame(shouldersPage,bg="black")

jumpingjack=Button(shouldersPage_right,text="JUMPING JACK",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(shouldersPage,excersice1))
jumpingjack.grid(row=1,column=0,pady=10)


armraise=Button(shouldersPage_right,text="ARM RAISES",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(shouldersPage,excersice7))
armraise.grid(row=2,column=0,pady=10)

pushups=Button(shouldersPage_right,text="PUSHUPS",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(shouldersPage,excersice9))
pushups.grid(row=3,column=0,pady=10)

tricepdips=Button(shouldersPage_right,text="TRICEP DIPS",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(shouldersPage,excersice8))
tricepdips.grid(row=4,column=0,pady=10)

inclinepushups=Button(shouldersPage_right,text="INCLINE PUSHUPS",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(shouldersPage,excersice17))
inclinepushups.grid(row=5,column=0,pady=10)


backHome=Button(shouldersPage_right,text="GO BACK",font=("Times", "18", "bold italic") ,width=22,bg="#FF1616",command=lambda:navigate(shouldersPage,gymPage))
backHome.grid(row=7,column=0,pady=10)

shouldersPage_right.grid(row=0,column=1,padx=50)

#yoga #7ED957

yogaPage=Frame(root,bg="black")

f5=mainImageFunction(1.5,"yoga.png")
gggimg=Label(yogaPage,image=f5)
gggimg.grid(row=0,column=0)

yogaPage_right=Frame(yogaPage,bg="black")


basic=Button(yogaPage_right,text="BASIC",font=("Times", "18", "bold italic") ,width=15,bg="#7ED957",command=lambda:navigate(yogaPage,basicsPage))
basic.grid(row=1,column=0,pady=10)

intermediate=Button(yogaPage_right,text="INTERMEDIATE",font=("Times", "18", "bold italic") ,width=15,bg="#7ED957",command=lambda:navigate(yogaPage,intermediatesPage))
intermediate.grid(row=2,column=0,pady=10)

advanced=Button(yogaPage_right,text="ADVANCED",font=("Times", "18", "bold italic") ,width=15,bg="#7ED957",command=lambda:navigate(yogaPage,advancedsPage))
advanced.grid(row=3,column=0,pady=10)

backHome=Button(yogaPage_right,text="GO BACK",font=("Times", "18", "bold italic") ,width=15,bg="#7ED957",command=lambda:navigate(yogaPage,welcomePage))
backHome.grid(row=4,column=0,pady=10)


yogaPage_right.grid(row=0,column=1,padx=50)


#basic

basicsPage=Frame(root,bg="black")

basicsPic=mainImageFunction(1.5,"basic.png")
basicimg=Label(basicsPage,image=basicsPic)
basicimg.grid(row=0,column=0)

basicsPage_right=Frame(basicsPage,bg="black")

chairpose=Button(basicsPage_right,text="CHAIR POSE",font=("Times", "18", "bold italic") ,width=22,bg="#7ED957",command=lambda:navigate(basicsPage,yoga1))
chairpose.grid(row=1,column=0,pady=10)


downwarddog=Button(basicsPage_right,text="DOWNWARD DOG",font=("Times", "18", "bold italic") ,width=22,bg="#7ED957",command=lambda:navigate(basicsPage,yoga2))
downwarddog.grid(row=2,column=0,pady=10)

warriorII=Button(basicsPage_right,text="WARRIOR II",font=("Times", "18", "bold italic") ,width=22,bg="#7ED957",command=lambda:navigate(basicsPage,yoga3))
warriorII.grid(row=3,column=0,pady=10)

treepose=Button(basicsPage_right,text="TREE POSE",font=("Times", "18", "bold italic") ,width=22,bg="#7ED957",command=lambda:navigate(basicsPage,yoga4))
treepose.grid(row=4,column=0,pady=10)

triangularpose=Button(basicsPage_right,text="TRIANGULAR POSE",font=("Times", "18", "bold italic") ,width=22,bg="#7ED957",command=lambda:navigate(basicsPage,yoga5))
triangularpose.grid(row=5,column=0,pady=10)

puppyonchair=Button(basicsPage_right,text="PUPPY ON CHAIR",font=("Times", "18", "bold italic") ,width=22,bg="#7ED957",command=lambda:navigate(basicsPage,yoga6))
puppyonchair.grid(row=6,column=0,pady=10)


backHome=Button(basicsPage_right,text="GO BACK",font=("Times", "18", "bold italic") ,width=22,bg="#7ED957",command=lambda:navigate(basicsPage,yogaPage))
backHome.grid(row=7,column=0,pady=10)

basicsPage_right.grid(row=0,column=1,padx=50)

#intermediate

intermediatesPage=Frame(root,bg="black")

intermediatesPic=mainImageFunction(1.5,"intermediate.png")
intermediateimg=Label(intermediatesPage,image=intermediatesPic)
intermediateimg.grid(row=0,column=0)

intermediatesPage_right=Frame(intermediatesPage,bg="black")

plank=Button(intermediatesPage_right,text="PLANK",font=("Times", "18", "bold italic") ,width=22,bg="#7ED957",command=lambda:navigate(intermediatesPage,excersice5))
plank.grid(row=1,column=0,pady=10)


cobrapose=Button(intermediatesPage_right,text="COBRA POSE",font=("Times", "18", "bold italic") ,width=22,bg="#7ED957",command=lambda:navigate(intermediatesPage,excersice6))
cobrapose.grid(row=2,column=0,pady=10)

warriorI=Button(intermediatesPage_right,text="WARRIOR I",font=("Times", "18", "bold italic") ,width=22,bg="#7ED957",command=lambda:navigate(intermediatesPage,yoga7))
warriorI.grid(row=3,column=0,pady=10)


camelpose=Button(intermediatesPage_right,text="CAMEL POSE",font=("Times", "18", "bold italic") ,width=22,bg="#7ED957",command=lambda:navigate(intermediatesPage,yoga8))
camelpose.grid(row=5,column=0,pady=10)


backHome=Button(intermediatesPage_right,text="GO BACK",font=("Times", "18", "bold italic") ,width=22,bg="#7ED957",command=lambda:navigate(intermediatesPage,yogaPage))
backHome.grid(row=7,column=0,pady=10)

intermediatesPage_right.grid(row=0,column=1,padx=50)

# Advanced


advancedsPage=Frame(root,bg="black")

advancedsPic=mainImageFunction(1.5,"advanced.png")
advancedimg=Label(advancedsPage,image=advancedsPic)
advancedimg.grid(row=0,column=0)

advancedsPage_right=Frame(advancedsPage,bg="black")

sideplank=Button(advancedsPage_right,text="SIDE PLANK",font=("Times", "18", "bold italic") ,width=22,bg="#7ED957",command=lambda:navigate(advancedsPage,yoga9))
sideplank.grid(row=1,column=0,pady=10)


plank=Button(advancedsPage_right,text="PLANK",font=("Times", "18", "bold italic") ,width=22,bg="#7ED957",command=lambda:navigate(advancedsPage,excersice5))
plank.grid(row=2,column=0,pady=10)

warriorII=Button(advancedsPage_right,text="WARRIOR II",font=("Times", "18", "bold italic") ,width=22,bg="#7ED957",command=lambda:navigate(advancedsPage,yoga3))
warriorII.grid(row=3,column=0,pady=10)



backHome=Button(advancedsPage_right,text="GO BACK",font=("Times", "18", "bold italic") ,width=22,bg="#7ED957",command=lambda:navigate(advancedsPage,yogaPage))
backHome.grid(row=7,column=0,pady=10)

advancedsPage_right.grid(row=0,column=1,padx=50)


# profile #00ffea

profilePage=Frame(root,bg="black")

f6=mainImageFunction(1.5,"profile.png")
profileImage1=Label(profilePage,image=f6)
profileImage1.grid(row=0,column=0)

profilePage_right=Frame(profilePage,bg="black")

nam=Label(profilePage_right,text="Name : ",font=("Times", "12", "bold"),fg="#00ffea",bg="black")
nam.grid(row=0,column=0,pady=5)

hei=Label(profilePage_right,text="Name : ",font=("Times", "12", "bold"),fg="#00ffea",bg="black")
hei.grid(row=1,column=0,pady=5)

wei=Label(profilePage_right,text="Name : ",font=("Times", "12", "bold"),fg="#00ffea",bg="black")
wei.grid(row=2,column=0,pady=5)

ag=Label(profilePage_right,text="Name : ",font=("Times", "12", "bold"),fg="#00ffea",bg="black")
ag.grid(row=3,column=0,pady=5)

gen=Label(profilePage_right,text="Name : ",font=("Times", "12", "bold"),fg="#00ffea",bg="black")
gen.grid(row=4,column=0,pady=5)

cb=Label(profilePage_right,text="Calories Burned : ",font=("Times", "12", "bold"),fg="#00ffea" ,bg="black")
cb.grid(row=5,column=0,pady=5)

ms=Label(profilePage_right,text="Minutes Spent : ",font=("Times", "12", "bold "),fg="#00ffea",bg="black")
ms.grid(row=6,column=0,pady=5,)


sd=Label(profilePage_right,text="Number Of  Sets Done : ",font=("Times", "12", "bold "),fg="#00ffea",bg="black")
sd.grid(row=7,column=0,pady=5,)


ed=Label(profilePage_right,text="Number Of  Excercise Done : ",font=("Times", "12", "bold "),fg="#00ffea",bg="black")
ed.grid(row=8,column=0,pady=5,)


yd=Label(profilePage_right,text="Number Of  Yogasanam's Done : ",font=("Times", "12", "bold"),fg="#00ffea",bg="black")
yd.grid(row=9,column=0,pady=5)

update=Button(profilePage_right,text="UPDATE",font=("Times", "15", "bold italic") ,width=15,bg="#00ffea",command=lambda:navigate(profilePage,updatePage))
update.grid(row=10,column=0,pady=10)

backHome=Button(profilePage_right,text="GO BACK",font=("Times", "15", "bold italic") ,width=15,bg="#00ffea",command=lambda:navigate(profilePage,welcomePage))
backHome.grid(row=11,column=0,pady=10)

profilePage_right.grid(row=0,column=1,padx=50)








#diet plans #FF66C4

dietPage=Frame(root,bg="black")

dimage=mainImageFunction(1.5,"diet.png")

dietImage=Label(dietPage,image=dimage,bg="black")
dietImage.grid(row=0,column=0)


dietPage_right=Frame(dietPage,bg="black")

whatType=Label(dietPage_right,bg="black", fg="#FF66C4",font=("Times", "22", "bold italic") )
whatType.grid(row=0,column=0,pady=20,columnspan=2)

weightLoss=Button(dietPage_right,text="WEIGHT LOSS",font=("Times", "12", "bold italic") ,width=25,bg="#FF66C4",command=weight_loss_page)
weightLoss.grid(row=1,column=0,pady=10,)

weightLossMsg=Label(dietPage_right,text="",bg="black", fg="#FF66C4",font=("Times", "10", "bold italic") )
weightLossMsg.grid(row=1,column=1,pady=2,padx=5)

weightGain=Button(dietPage_right,text="WEIGHT GAIN",font=("Times", "12", "bold italic") ,width=25,bg="#FF66C4",command=weight_gain_page)
weightGain.grid(row=2,column=0,pady=10,)

weightGainMsg=Label(dietPage_right,text="",bg="black", fg="#FF66C4",font=("Times", "10", "bold italic") )
weightGainMsg.grid(row=2,column=1,padx=5)

backHome=Button(dietPage_right,text="GO BACK",font=("Times", "12", "bold italic") ,width=25,bg="#FF66C4",command=lambda:navigate(dietPage,welcomePage))
backHome.grid(row=3,column=0,pady=10)

dietPage_right.grid(row=0,column=1,padx=20)

#weight gain page

weightGainPage=Frame(root,bg="black")

weightGainPageImage=mainImageFunction(1.5,"diet.png")

dietImage=Label(weightGainPage,image=dimage,bg="black")
dietImage.grid(row=0,column=0)

weightGainPage_right=Frame(weightGainPage,bg="black")

weightGainPage_right_report=Label(weightGainPage_right,text="Your Diet Plan Report",font=("Times", "20", "bold italic"),bg="black", fg="#FF66C4")



weightGainPage_right_report.grid(row=0,column=0,pady=10)

weightGainPage_right1=Frame(weightGainPage_right)
S = Scrollbar(weightGainPage_right1)
weightGainPage_right_report1 = Text(weightGainPage_right1, height=6, width=50,bg="#FF66C4")

S.pack(side = RIGHT, fill = Y)

weightGainPage_right_report1 .pack()
S.config(command=weightGainPage_right_report1.yview)
weightGainPage_right_report1 .config(yscrollcommand=S.set)
weightGainPage_right_report1 .config(yscrollcommand=S.set)
weightGainPage_right_report1 .config(state= DISABLED)

weightGainPage_right1.grid(row=1,column=0,pady=10)

weightGainPage_right_whatToEat=Label(weightGainPage_right,text="What to Eat:-",font=("Times", "20", "bold italic"),bg="black", fg="#FF66C4")
weightGainPage_right_whatToEat.grid(row=2,column=0,pady=10)

style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=("Times", "10", "bold italic"),fg="black", bg="#FF66C4") 

weightGainPage_right_wte1=Frame(weightGainPage_right,bg="black")
weightGainPage_right_wte =ttk.Treeview(weightGainPage_right_wte1,style="mystyle.Treeview", height=4)

V = Scrollbar(weightGainPage_right_wte1)
V.pack(side = RIGHT, fill = Y)

weightGainPage_right_wte['columns']=('Food', 'Quantity', 'Time')
weightGainPage_right_wte.column('#0', width=0, stretch=NO)
weightGainPage_right_wte.column('Food', anchor=CENTER, width=250)
weightGainPage_right_wte.column('Quantity', anchor=CENTER, width=80)
weightGainPage_right_wte.column('Time', anchor=CENTER, width=80)
weightGainPage_right_wte.heading('#0', text='', anchor=CENTER)
weightGainPage_right_wte.heading('Food', text='FOOD', anchor=CENTER)
weightGainPage_right_wte.heading('Quantity', text='QUANTITY', anchor=CENTER)
weightGainPage_right_wte.heading('Time', text='TIME', anchor=CENTER)

weightGainPage_right_wte.pack()
V.config(command=weightGainPage_right_wte.yview)
weightGainPage_right_wte.config(yscrollcommand=V.set)
weightGainPage_right_wte1.grid(row=4,column=0)


sdp=Button(weightGainPage_right,text="SHOW DIFFERENT PLAN",font=("Times", "12", "bold italic") ,width=30,bg="#FF66C4",command=weight_gain_page)
sdp.grid(row=5,column=0,pady=10)

backHome=Button(weightGainPage_right,text="GO BACK",font=("Times", "12", "bold italic") ,width=15,bg="#FF66C4",command=lambda:navigate(weightGainPage,dietPage))
backHome.grid(row=6,column=0,pady=10)

weightGainPage_right.grid(row=0,column=1,padx=50)



#weight loss page

weightLossPage=Frame(root,bg="black")

weightLossPageImage=mainImageFunction(1.5,"diet.png")

dietImage=Label(weightLossPage,image=dimage,bg="black")
dietImage.grid(row=0,column=0)

weightLossPage_right=Frame(weightLossPage,bg="black")

weightLossPage_right_report=Label(weightLossPage_right,text="Your Diet Plan Report",font=("Times", "20", "bold italic"),bg="black", fg="#FF66C4")



weightLossPage_right_report.grid(row=0,column=0,pady=10)

weightLossPage_right1=Frame(weightLossPage_right)
S = Scrollbar(weightLossPage_right1)
weightLossPage_right_report1 = Text(weightLossPage_right1, height=6, width=50,bg="#FF66C4")

S.pack(side = RIGHT, fill = Y)

weightLossPage_right_report1 .pack()
S.config(command=weightLossPage_right_report1.yview)
weightLossPage_right_report1 .config(yscrollcommand=S.set)
weightLossPage_right_report1 .config(yscrollcommand=S.set)
weightLossPage_right_report1 .config(state= DISABLED)

weightLossPage_right1.grid(row=1,column=0,pady=10)

weightLossPage_right_whatToEat=Label(weightLossPage_right,text="What to Eat:-",font=("Times", "20", "bold italic"),bg="black", fg="#FF66C4")
weightLossPage_right_whatToEat.grid(row=2,column=0,pady=10)

style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=("Times", "10", "bold italic"),fg="black", bg="#FF66C4") 

weightLossPage_right_wte1=Frame(weightLossPage_right,bg="black")
weightLossPage_right_wte =ttk.Treeview(weightLossPage_right_wte1,style="mystyle.Treeview", height=4)

V = Scrollbar(weightLossPage_right_wte1)
V.pack(side = RIGHT, fill = Y)

weightLossPage_right_wte['columns']=('Food', 'Quantity', 'Time')
weightLossPage_right_wte.column('#0', width=0, stretch=NO)
weightLossPage_right_wte.column('Food', anchor=CENTER, width=250)
weightLossPage_right_wte.column('Quantity', anchor=CENTER, width=80)
weightLossPage_right_wte.column('Time', anchor=CENTER, width=80)
weightLossPage_right_wte.heading('#0', text='', anchor=CENTER)
weightLossPage_right_wte.heading('Food', text='FOOD', anchor=CENTER)
weightLossPage_right_wte.heading('Quantity', text='QUANTITY', anchor=CENTER)
weightLossPage_right_wte.heading('Time', text='TIME', anchor=CENTER)


V.config(command=weightLossPage_right_wte.yview)
weightLossPage_right_wte .config(yscrollcommand=V.set)

weightLossPage_right_wte.pack()

weightLossPage_right_wte1.grid(row=4,column=0)


sdp=Button(weightLossPage_right,text="SHOW DIFFERENT PLAN",font=("Times", "12", "bold italic") ,width=30,bg="#FF66C4",command=weight_loss_page)
sdp.grid(row=5,column=0,pady=10)

backHome=Button(weightLossPage_right,text="GO BACK",font=("Times", "12", "bold italic") ,width=15,bg="#FF66C4",command=lambda:navigate(weightLossPage,dietPage))
backHome.grid(row=6,column=0,pady=10)

weightLossPage_right.grid(row=0,column=1,padx=50)











#settings #8C52FF





settingsPage=Frame(root,bg="black")

simage=mainImageFunction(1.5,"setting.png")
settingsImage=Label(settingsPage,image=simage,bg="black")
settingsImage.grid(row=0,column=0)

settingsPage_right=Frame(settingsPage,bg="black")

whichCamera=StringVar()
cameras=["Primary","Secondary"]
whichCamera.set(cameras[0])
cameraLabel=Label(settingsPage_right,text="Select Tracking Camera:" ,font=("Times", "18", "bold italic") ,fg="#8C52FF",bg="black")
cameraLabel.grid(row=1,column=0,pady=10)
cameraSetting=OptionMenu(settingsPage_right,whichCamera,*cameras)
cameraSetting.config(width=15   ,font=("Times", "15", "bold italic"),bg="#8C52FF")
cameraSetting.grid(row=2,column=0,pady=10,padx=10)

saveSettings=Button(settingsPage_right,text="SAVE",font=("Times", "15", "bold italic") ,width=25,bg="#8C52FF",command=settings_save)
saveSettings.grid(row=3,column=0,pady=10,columnspan=2)

backHome=Button(settingsPage_right,text="GO BACK",font=("Times", "15", "bold italic") ,width=25,bg="#8C52FF",command=lambda:navigate(settingsPage,welcomePage))
backHome.grid(row=4,column=0,pady=10,columnspan=2)

settingsPage_right.grid(row=0,column=1,padx=20)



#update #FF5757 




def update_fn(what):
    global sets_or_time,menu,glb_weight,glb_ns,glb_ne,glb_cb,glb_min
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras,upadateEntry,updateLabel,updatePage_right1,updatePage_right2
    global glb_whatToUpdate

    glb_whatToUpdate=what

    updatePage_right1.grid_forget()
    updatePage_right2.grid(row=0,column=0)

    updateLabel.config(text="Enter the updated "+what+":")


def update_fn1():
    global sets_or_time,menu,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_age,glb_height
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras,upadateEntry,updateLabel,glb_whatToUpdate
    global updatePage_right2,updatePage_right1
    what=glb_whatToUpdate
    f=open("nothing/"+str(glb_filename)+".txt","r")
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)
    updated_encrypt=str(fernet.encrypt(updateEntry.get().encode()))
    for i in range(len(ff)):
        if what=="age" and i==3:
            fg.write(updated_encrypt+" \n")
            glb_age=str(updateEntry.get())
        elif what=="height" and i==1:
            fg.write(updated_encrypt+" \n")
            glb_height=str(updateEntry.get())
        elif what=="weight" and i==2:
            fg.write(updated_encrypt+" \n")
            glb_weight=str(updateEntry.get())
        else:
            fg.write(ff[i]+" \n")

    updateEntry.delete(0,"end")

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

    navigate(updatePage_right2,updatePage_right1)
    profile_visit1()




updatePage=Frame(root,bg="black")
uimage=mainImageFunction(1.5,"update.png")


updateImage=Label(updatePage,image=uimage,bg="black")
updateImage.grid(row=0,column=0)

updatePage_right=Frame(updatePage,bg="black")


updatePage_right1=Frame(updatePage_right,bg="black")
updateAge=Button(updatePage_right1,text="UPDATE AGE",font=("Times", "12", "bold italic") ,width=30,bg="#FF5757",command=lambda:update_fn("age"))
updateAge.grid(row=0,column=0,pady=10)

updateHeight=Button(updatePage_right1,text="UPDATE HEIGHT",font=("Times", "12", "bold italic") ,width=30,bg="#FF5757",command=lambda:update_fn("height"))
updateHeight.grid(row=1,column=0,pady=10)

updateWeight=Button(updatePage_right1,text="UPDATE WEIGHT",font=("Times", "12", "bold italic") ,width=30,bg="#FF5757",command=lambda:update_fn("weight"))
updateWeight.grid(row=2,column=0,pady=10)

backHome=Button(updatePage_right1,text="GO BACK",font=("Times", "12", "bold italic") ,width=25,bg="#FF5757",command=lambda:navigate(updatePage,profilePage))
backHome.grid(row=3,column=0,pady=10,columnspan=2)

updatePage_right1.grid(row=0,column=0)



updatePage_right2=Frame(updatePage_right,bg="black")
updateLabel=Label(updatePage_right2,text="" ,font=("Times", "18", "bold italic") ,fg="#FF5757",bg="black")
updateLabel.grid(row=0,column=0,pady=10)
updateEntry=Entry(updatePage_right2,width=20,font=("Times", "15", "bold italic"),bg="#FF5757")
updateEntry.grid(row=1,column=0,pady=10,padx=10)

updateEnter=Button(updatePage_right2,text="UPDATE",font=("Times", "12", "bold italic") ,width=25,bg="#FF5757",command=update_fn1)
updateEnter.grid(row=2,column=0,pady=10)

backHome=Button(updatePage_right2,text="GO BACK",font=("Times", "12", "bold italic") ,width=25,bg="#FF5757",command=lambda:navigate(updatePage_right2,updatePage_right1))
backHome.grid(row=3,column=0,pady=10,columnspan=2)


updatePage_right.grid(row=0,column=1,padx=30)



#excersice functions

#jumping jacks

def openlinks(url):
    webbrowser.open_new(url)


excersice1_url="https://www.youtube.com/watch?v=CWpmIW6l-YA"
def jumpjack_fn():
    global sets_or_time,menu,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender,glb_yoga
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=jumpingJacks(sets_or_time,menu.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(3.5/24)*(0.00027*wsets)*10
    print(calburned)
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_ns=str(int(glb_ns)+wsets)
    glb_ne=str(int(glb_ne)+1)
    glb_min=str(round(float(glb_min)+(secs/60),2))
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]


    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))


    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

excersice1=Frame(root,bg="black")
jj1=mainImageFunction(1.5,"excersice1.png")
excersice1Pic=Label(excersice1,image=jj1,bg="black")
excersice1Pic.grid(row=0,column=0)

excersice1_right=Frame(excersice1,bg="black")
excersice1_right_top=Frame(excersice1_right,bg="black")
WhatExcersice=Label(excersice1_right_top,text="JUMPING JACKS",bg="black",fg="#FF1616", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)
excersice1_right_top_1=Frame(excersice1_right_top,bg="black")
sets1=Button(excersice1_right_top_1,text="SETS",font=("Times", "13", "bold italic") ,width=12,bg="black",fg="#FF1616",command=lambda:exnavigate(sets1,time1,"#FF1616","sets"))
sets1.grid(row=0,column=0,padx=10)
time1=Button(excersice1_right_top_1,text="TIME",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:exnavigate(time1,sets1,"#FF1616","time"))
time1.grid(row=0,column=1,padx=10)
excersice1_right_top_1.grid(row=1,column=0,pady=20)

excersice1_right_top_2set=Frame(excersice1_right_top,bg="black")

menu= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu.set(nsets[0])

drop= OptionMenu(excersice1_right_top_2set, menu,*nsets)
drop.config(bg="#FF1616")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(excersice1_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=jumpjack_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(excersice1_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:spnavigate(excersice1))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(excersice1_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#FF1616",command=lambda:openlinks(excersice1_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

excersice1_right_top_2set.grid(row=2,column=0)

excersice1_right_top.grid(row=0,column=0,pady=20)



excersice1_right_bottom=Frame(excersice1_right)


excersice1_right_bottom.grid(row=1,column=0,pady=30)


excersice1_right.grid(row=0,column=1,padx=30)




#abdominal crunches
excersice2_url="https://www.youtube.com/watch?v=RUNrHkbP4Pc&ab_channel=LeapFitness"
def abdominalcrunches_fn():
    global sets_or_time,menu,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras,menu2
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=abdominalcrunchesf(sets_or_time,menu2.get(),glb_camera)

    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(3.5/24)*(0.00027*wsets)*10
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_ns=str(int(glb_ns)+wsets)
    glb_ne=str(int(glb_ne)+1)
    glb_min=str(round(float(glb_min)+(secs/60),2))
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]

    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

    

excersice2=Frame(root,bg="black")
jj2=mainImageFunction(1.5,"pics/excersice2.png")
excersice2Pic=Label(excersice2,image=jj2,bg="black")
excersice2Pic.grid(row=0,column=0)

excersice2_right=Frame(excersice2,bg="black")
excersice2_right_top=Frame(excersice2_right,bg="black")
WhatExcersice=Label(excersice2_right_top,text="ABDOMINAL CRUNCHES",bg="black",fg="#FF1616", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)
excersice2_right_top_1=Frame(excersice2_right_top,bg="black")
sets=Button(excersice2_right_top_1,text="SETS",font=("Times", "13", "bold italic") ,width=12,bg="black",fg="#FF1616",command=lambda:exnavigate(sets,time,"#FF1616","sets"))
sets.grid(row=0,column=0,padx=10)
time=Button(excersice2_right_top_1,text="TIME",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:exnavigate(time,sets,"#FF1616","time"))
time.grid(row=0,column=1,padx=10)
excersice2_right_top_1.grid(row=1,column=0,pady=20)

excersice2_right_top_2set=Frame(excersice2_right_top,bg="black")

menu2= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu2.set(nsets[0])

drop= OptionMenu(excersice2_right_top_2set, menu2,*nsets)
drop.config(bg="#FF1616")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(excersice2_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=abdominalcrunches_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(excersice2_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:spnavigate(excersice2))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(excersice2_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#FF1616",command=lambda:openlinks(excersice2_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

excersice2_right_top_2set.grid(row=2,column=0)

excersice2_right_top.grid(row=0,column=0,pady=20)



excersice2_right_bottom=Frame(excersice2_right)


excersice2_right_bottom.grid(row=1,column=0,pady=30)


excersice2_right.grid(row=0,column=1,padx=30)



#mountain climbers
excersice3_url="https://www.youtube.com/watch?v=cnyTQDSE884&ab_channel=Well%2BGood"

def mountainclimbers_fn():
    global sets_or_time,menu,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras,menu3
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=mountainclimbersf(sets_or_time,menu3.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(3.5/24)*(0.00027*wsets)*10
    print(calburned)
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_ns=str(int(glb_ns)+wsets)
    glb_ne=str(int(glb_ne)+1)
    glb_min=str(round(float(glb_min)+(secs/60),2))
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]

    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

excersice3=Frame(root,bg="black")
jj3=mainImageFunction(1.5,"pics/excersice3.png")
excersice3Pic=Label(excersice3,image=jj3,bg="black")
excersice3Pic.grid(row=0,column=0)

excersice3_right=Frame(excersice3,bg="black")
excersice3_right_top=Frame(excersice3_right,bg="black")
WhatExcersice=Label(excersice3_right_top,text="MOUNTAIN CLIMBERS",bg="black",fg="#FF1616", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)
excersice3_right_top_1=Frame(excersice3_right_top,bg="black")
sets=Button(excersice3_right_top_1,text="SETS",font=("Times", "13", "bold italic") ,width=12,bg="black",fg="#FF1616",command=lambda:exnavigate(sets,time,"#FF1616","sets"))
sets.grid(row=0,column=0,padx=10)
time=Button(excersice3_right_top_1,text="TIME",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:exnavigate(time,sets,"#FF1616","time"))
time.grid(row=0,column=1,padx=10)
excersice3_right_top_1.grid(row=1,column=0,pady=20)

excersice3_right_top_2set=Frame(excersice3_right_top,bg="black")

menu3= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu3.set(nsets[0])

drop= OptionMenu(excersice3_right_top_2set, menu3,*nsets)
drop.config(bg="#FF1616")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(excersice3_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=mountainclimbers_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(excersice3_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:spnavigate(excersice3))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(excersice3_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#FF1616",command=lambda:openlinks(excersice3_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

excersice3_right_top_2set.grid(row=2,column=0)

excersice3_right_top.grid(row=0,column=0,pady=20)



excersice3_right_bottom=Frame(excersice3_right)


excersice3_right_bottom.grid(row=1,column=0,pady=30)


excersice3_right.grid(row=0,column=1,padx=30)



#leg raises
excersice4_url="https://www.youtube.com/watch?v=l4kQd9eWclE&ab_channel=Howcast"

def legraises_fn():
    global sets_or_time,menu4,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=legraisesf(sets_or_time,menu4.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(3.5/24)*(0.00027*wsets)*10
    print(calburned)
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_ns=str(int(glb_ns)+wsets)
    glb_ne=str(int(glb_ne)+1)
    glb_min=str(round(float(glb_min)+(secs/60),2))
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]

    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

excersice4=Frame(root,bg="black")
jj4=mainImageFunction(1.5,"pics/excersice4.png")
excersice4Pic=Label(excersice4,image=jj4,bg="black")
excersice4Pic.grid(row=0,column=0)

excersice4_right=Frame(excersice4,bg="black")
excersice4_right_top=Frame(excersice4_right,bg="black")
WhatExcersice=Label(excersice4_right_top,text="LEG RAISES",bg="black",fg="#FF1616", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)
excersice4_right_top_1=Frame(excersice4_right_top,bg="black")
sets=Button(excersice4_right_top_1,text="SETS",font=("Times", "13", "bold italic") ,width=12,bg="black",fg="#FF1616",command=lambda:exnavigate(sets,time,"#FF1616","sets"))
sets.grid(row=0,column=0,padx=10)
time=Button(excersice4_right_top_1,text="TIME",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:exnavigate(time,sets,"#FF1616","time"))
time.grid(row=0,column=1,padx=10)
excersice4_right_top_1.grid(row=1,column=0,pady=20)

excersice4_right_top_2set=Frame(excersice4_right_top,bg="black")

menu4= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu4.set(nsets[0])

drop= OptionMenu(excersice4_right_top_2set, menu4,*nsets)
drop.config(bg="#FF1616")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(excersice4_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=legraises_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(excersice4_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:spnavigate(excersice4))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(excersice4_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#FF1616",command=lambda:openlinks(excersice4_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

excersice4_right_top_2set.grid(row=2,column=0)

excersice4_right_top.grid(row=0,column=0,pady=20)



excersice4_right_bottom=Frame(excersice4_right)


excersice4_right_bottom.grid(row=1,column=0,pady=30)


excersice4_right.grid(row=0,column=1,padx=30)



#plank
excersice5_url="https://www.youtube.com/watch?v=kL_NJAkCQBg&ab_channel=Calisthenicmovement"
def plank_fn():
    global sets_or_time,menu5,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")

    sets_or_time="time"
    wsets,secs=plankf(sets_or_time,menu5.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(3.5/24)*(0.00027*wsets)*10
    print(calburned)
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_ns=str(int(glb_ns)+wsets)
    glb_ne=str(int(glb_ne)+1)
    glb_min=str(round(float(glb_min)+(secs/60),2))
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]

    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

excersice5=Frame(root,bg="black")
jj5=mainImageFunction(1.5,"pics/excersice5.png")
excersice5Pic=Label(excersice5,image=jj5,bg="black")
excersice5Pic.grid(row=0,column=0)

excersice5_right=Frame(excersice5,bg="black")
excersice5_right_top=Frame(excersice5_right,bg="black")
WhatExcersice=Label(excersice5_right_top,text="PLANK",bg="black",fg="#FF1616", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


excersice5_right_top_2set=Frame(excersice5_right_top,bg="black")

menu5= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu5.set(nsets[0])

drop= OptionMenu(excersice5_right_top_2set, menu5,*nsets)
drop.config(bg="#FF1616")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(excersice5_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=plank_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(excersice5_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:spnavigate(excersice5))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(excersice5_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#FF1616",command=lambda:openlinks(excersice5_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

excersice5_right_top_2set.grid(row=2,column=0)

excersice5_right_top.grid(row=0,column=0,pady=20)



excersice5_right_bottom=Frame(excersice5_right)


excersice5_right_bottom.grid(row=1,column=0,pady=30)


excersice5_right.grid(row=0,column=1,padx=30)

# cobrastrech

excersice6_url="https://www.youtube.com/watch?v=JDcdhTuycOI&ab_channel=FitnessBlender"
def cobrastrech_fn():
    global sets_or_time,menu6,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    sets_or_time="time"
    wsets,secs=cobrastrechf(sets_or_time,menu6.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(3.5/24)*(0.00027*wsets)*10
    print(calburned)
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_ns=str(int(glb_ns)+wsets)
    glb_ne=str(int(glb_ne)+1)
    glb_min=str(round(float(glb_min)+(secs/60),2))
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]

    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

excersice6=Frame(root,bg="black")
jj6=mainImageFunction(1.5,"pics/excersice6.png")
excersice6Pic=Label(excersice6,image=jj6,bg="black")
excersice6Pic.grid(row=0,column=0)

excersice6_right=Frame(excersice6,bg="black")
excersice6_right_top=Frame(excersice6_right,bg="black")
WhatExcersice=Label(excersice6_right_top,text="COBRA STRECH",bg="black",fg="#FF1616", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


excersice6_right_top_2set=Frame(excersice6_right_top,bg="black")

menu6= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu6.set(nsets[0])

drop= OptionMenu(excersice6_right_top_2set, menu6,*nsets)
drop.config(bg="#FF1616")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(excersice6_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=cobrastrech_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(excersice6_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:spnavigate(excersice6))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(excersice6_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#FF1616",command=lambda:openlinks(excersice6_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

excersice6_right_top_2set.grid(row=2,column=0)

excersice6_right_top.grid(row=0,column=0,pady=20)



excersice6_right_bottom=Frame(excersice6_right)


excersice6_right_bottom.grid(row=1,column=0,pady=30)


excersice6_right.grid(row=0,column=1,padx=30)



#armraises
excersice7_url="https://www.youtube.com/watch?v=YslHgg2E-Ro&ab_channel=LeapFitness"
def armraises_fn():
    global sets_or_time,menu7,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=armraisesf(sets_or_time,menu7.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(3.5/24)*(0.00027*wsets)*10
    print(calburned)
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_ns=str(int(glb_ns)+wsets)
    glb_ne=str(int(glb_ne)+1)
    glb_min=str(round(float(glb_min)+(secs/60),2))
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]
    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

excersice7=Frame(root,bg="black")
jj7=mainImageFunction(1.5,"pics/excersice7.png")
excersice7Pic=Label(excersice7,image=jj7,bg="black")
excersice7Pic.grid(row=0,column=0)

excersice7_right=Frame(excersice7,bg="black")
excersice7_right_top=Frame(excersice7_right,bg="black")
WhatExcersice=Label(excersice7_right_top,text="ARM RAISES",bg="black",fg="#FF1616", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


excersice7_right_top_2set=Frame(excersice7_right_top,bg="black")

menu7= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu7.set(nsets[0])

drop= OptionMenu(excersice7_right_top_2set, menu7,*nsets)
drop.config(bg="#FF1616")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(excersice7_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=armraises_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(excersice7_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:spnavigate(excersice7))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(excersice7_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#FF1616",command=lambda:openlinks(excersice7_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

excersice7_right_top_2set.grid(row=2,column=0)

excersice7_right_top.grid(row=0,column=0,pady=20)



excersice7_right_bottom=Frame(excersice7_right)


excersice7_right_bottom.grid(row=1,column=0,pady=30)


excersice7_right.grid(row=0,column=1,padx=30)


#tricep dips
excersice8_url="https://www.youtube.com/watch?v=6kALZikXxLc&ab_channel=Howcast"
def tricepdips_fn():
    global sets_or_time,menu8,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=tricepdipsf(sets_or_time,menu8.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(3.5/24)*(0.00027*wsets)*10
    print(calburned)
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_ns=str(int(glb_ns)+wsets)
    glb_ne=str(int(glb_ne)+1)
    glb_min=str(round(float(glb_min)+(secs/60),2))
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]

    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

excersice8=Frame(root,bg="black")
jj8=mainImageFunction(1.5,"pics/excersice8.png")
excersice8Pic=Label(excersice8,image=jj8,bg="black")
excersice8Pic.grid(row=0,column=0)

excersice8_right=Frame(excersice8,bg="black")
excersice8_right_top=Frame(excersice8_right,bg="black")
WhatExcersice=Label(excersice8_right_top,text="TRICEP DIPS",bg="black",fg="#FF1616", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


excersice8_right_top_2set=Frame(excersice8_right_top,bg="black")

menu8= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu8.set(nsets[0])

drop= OptionMenu(excersice8_right_top_2set, menu8,*nsets)
drop.config(bg="#FF1616")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(excersice8_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=tricepdips_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(excersice8_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:spnavigate(excersice8))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(excersice8_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#FF1616",command=lambda:openlinks(excersice8_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

excersice8_right_top_2set.grid(row=2,column=0)

excersice8_right_top.grid(row=0,column=0,pady=20)



excersice8_right_bottom=Frame(excersice8_right)


excersice8_right_bottom.grid(row=1,column=0,pady=30)


excersice8_right.grid(row=0,column=1,padx=30)


#pushups
excersice9_url="https://www.youtube.com/watch?v=Q7cPaJZoOng&ab_channel=Howcast"

def pushups_fn():
    global sets_or_time,menu9,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=pushupsf(sets_or_time,menu9.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(3.5/24)*(0.00027*wsets)*10
    print(calburned)
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_ns=str(int(glb_ns)+wsets)
    glb_ne=str(int(glb_ne)+1)
    glb_min=str(round(float(glb_min)+(secs/60),2))
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]

    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

excersice9=Frame(root,bg="black")
jj9=mainImageFunction(1.5,"pics/excersice9.png")
excersice9Pic=Label(excersice9,image=jj9,bg="black")
excersice9Pic.grid(row=0,column=0)

excersice9_right=Frame(excersice9,bg="black")
excersice9_right_top=Frame(excersice9_right,bg="black")
WhatExcersice=Label(excersice9_right_top,text="PUSH UPS",bg="black",fg="#FF1616", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


excersice9_right_top_2set=Frame(excersice9_right_top,bg="black")

menu9= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu9.set(nsets[0])

drop= OptionMenu(excersice9_right_top_2set, menu9,*nsets)
drop.config(bg="#FF1616")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(excersice9_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=pushups_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(excersice9_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:spnavigate(excersice9))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(excersice9_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#FF1616",command=lambda:openlinks(excersice9_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

excersice9_right_top_2set.grid(row=2,column=0)

excersice9_right_top.grid(row=0,column=0,pady=20)



excersice9_right_bottom=Frame(excersice9_right)


excersice9_right_bottom.grid(row=1,column=0,pady=30)


excersice9_right.grid(row=0,column=1,padx=30)



#squats
excersice10_url="https://www.youtube.com/watch?v=UXJrBgI2RxA&ab_channel=Howcast"
def squats_fn():
    global sets_or_time,menu10,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=squatsf(sets_or_time,menu10.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(3.5/24)*(0.00027*wsets)*10
    print(calburned)
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_ns=str(int(glb_ns)+wsets)
    glb_ne=str(int(glb_ne)+1)
    glb_min=str(round(float(glb_min)+(secs/60),2))
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]

    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

excersice10=Frame(root,bg="black")

jj10=mainImageFunction(1.5,"pics/excersice10.png")
excersice10Pic=Label(excersice10,image=jj10,bg="black")
excersice10Pic.grid(row=0,column=0)

excersice10_right=Frame(excersice10,bg="black")
excersice10_right_top=Frame(excersice10_right,bg="black")
WhatExcersice=Label(excersice10_right_top,text="SQUATS",bg="black",fg="#FF1616", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


excersice10_right_top_2set=Frame(excersice10_right_top,bg="black")

menu10= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu10.set(nsets[0])

drop= OptionMenu(excersice10_right_top_2set, menu10,*nsets)
drop.config(bg="#FF1616")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(excersice10_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=squats_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(excersice10_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:spnavigate(excersice10))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(excersice10_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#FF1616",command=lambda:openlinks(excersice10_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

excersice10_right_top_2set.grid(row=2,column=0)

excersice10_right_top.grid(row=0,column=0,pady=20)



excersice10_right_bottom=Frame(excersice10_right)


excersice10_right_bottom.grid(row=1,column=0,pady=30)


excersice10_right.grid(row=0,column=1,padx=30)

#sideleglift left
excersice11_url="https://www.youtube.com/watch?v=VlwBJE1WtOQ&ab_channel=LeapFitness"
def sideleglift_left_fn():
    global sets_or_time,menu11,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=sideleglift_leftf(sets_or_time,menu11.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(3.5/24)*(0.00027*wsets)*10
    print(calburned)
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_ns=str(int(glb_ns)+wsets)
    glb_ne=str(int(glb_ne)+1)
    glb_min=str(round(float(glb_min)+(secs/60),2))
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]

    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

excersice11=Frame(root,bg="black")
jj11=mainImageFunction(1.5,"pics/excersice11.png")
excersice11Pic=Label(excersice11,image=jj11,bg="black")
excersice11Pic.grid(row=0,column=0)

excersice11_right=Frame(excersice11,bg="black")
excersice11_right_top=Frame(excersice11_right,bg="black")
WhatExcersice=Label(excersice11_right_top,text="SIDE LEG LIFT LEFT",bg="black",fg="#FF1616", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


excersice11_right_top_2set=Frame(excersice11_right_top,bg="black")

menu11= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu11.set(nsets[0])

drop= OptionMenu(excersice11_right_top_2set, menu11,*nsets)
drop.config(bg="#FF1616")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(excersice11_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=sideleglift_left_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(excersice11_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:spnavigate(excersice11))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(excersice11_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#FF1616",command=lambda:openlinks(excersice11_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

excersice11_right_top_2set.grid(row=2,column=0)

excersice11_right_top.grid(row=0,column=0,pady=20)



excersice11_right_bottom=Frame(excersice11_right)


excersice11_right_bottom.grid(row=1,column=0,pady=30)


excersice11_right.grid(row=0,column=1,padx=30)


#sideleglift right
excersice11_url="https://www.youtube.com/watch?v=VlwBJE1WtOQ&ab_channel=LeapFitness"

def sideleglift_right_fn():
    global sets_or_time,menu12,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=sideleglift_rightf(sets_or_time,menu12.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(3.5/24)*(0.00027*wsets)*10
    print(calburned)
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_ns=str(int(glb_ns)+wsets)
    glb_ne=str(int(glb_ne)+1)
    glb_min=str(round(float(glb_min)+(secs/60),2))
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]
    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

excersice12=Frame(root,bg="black")
jj12=mainImageFunction(1.5,"pics/excersice12.png")
excersice12Pic=Label(excersice12,image=jj12,bg="black")
excersice12Pic.grid(row=0,column=0)

excersice12_right=Frame(excersice12,bg="black")
excersice12_right_top=Frame(excersice12_right,bg="black")
WhatExcersice=Label(excersice12_right_top,text="SIDE LEG LIFT right",bg="black",fg="#FF1616", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


excersice12_right_top_2set=Frame(excersice12_right_top,bg="black")

menu12= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu12.set(nsets[0])

drop= OptionMenu(excersice12_right_top_2set, menu12,*nsets)
drop.config(bg="#FF1616")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(excersice12_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=sideleglift_right_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(excersice12_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:spnavigate(excersice12))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(excersice12_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#FF1616",command=lambda:openlinks(excersice11_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

excersice12_right_top_2set.grid(row=2,column=0)

excersice12_right_top.grid(row=0,column=0,pady=20)



excersice12_right_bottom=Frame(excersice12_right)


excersice12_right_bottom.grid(row=1,column=0,pady=30)


excersice12_right.grid(row=0,column=1,padx=30)


#backward lunge
excersice13_url="https://www.youtube.com/watch?v=_LGpDtENZ5U&ab_channel=LeapFitness"
def backwardlunge_fn():
    global sets_or_time,menu13,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=backwardlungef(sets_or_time,menu13.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(3.5/24)*(0.00027*wsets)*10
    print(calburned)
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_ns=str(int(glb_ns)+wsets)
    glb_ne=str(int(glb_ne)+1)
    glb_min=str(round(float(glb_min)+(secs/60),2))
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]

    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

excersice13=Frame(root,bg="black")
jj13=mainImageFunction(1.5,"pics/excersice13.png")
excersice13Pic=Label(excersice13,image=jj13,bg="black")
excersice13Pic.grid(row=0,column=0)

excersice13_right=Frame(excersice13,bg="black")
excersice13_right_top=Frame(excersice13_right,bg="black")
WhatExcersice=Label(excersice13_right_top,text="BACKWARD LUNGE",bg="black",fg="#FF1616", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


excersice13_right_top_2set=Frame(excersice13_right_top,bg="black")

menu13= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu13.set(nsets[0])

drop= OptionMenu(excersice13_right_top_2set, menu13,*nsets)
drop.config(bg="#FF1616")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(excersice13_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=backwardlunge_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(excersice13_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:spnavigate(excersice13))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(excersice13_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#FF1616",command=lambda:openlinks(excersice13_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

excersice13_right_top_2set.grid(row=2,column=0)

excersice13_right_top.grid(row=0,column=0,pady=20)



excersice13_right_bottom=Frame(excersice13_right)


excersice13_right_bottom.grid(row=1,column=0,pady=30)


excersice13_right.grid(row=0,column=1,padx=30)

#donkey kick left

excersice14_url="https://www.youtube.com/watch?v=4ranVQDqlaU&ab_channel=LeapFitness"
def donkeykickleft_fn():
    global sets_or_time,menu14,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=donkeykickleftf(sets_or_time,menu14.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(3.5/24)*(0.00027*wsets)*10
    print(calburned)
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_ns=str(int(glb_ns)+wsets)
    glb_ne=str(int(glb_ne)+1)
    glb_min=str(round(float(glb_min)+(secs/60),2))
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]

    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

excersice14=Frame(root,bg="black")
jj14=mainImageFunction(1.5,"pics/excersice14.png")
excersice14Pic=Label(excersice14,image=jj14,bg="black")
excersice14Pic.grid(row=0,column=0)

excersice14_right=Frame(excersice14,bg="black")
excersice14_right_top=Frame(excersice14_right,bg="black")
WhatExcersice=Label(excersice14_right_top,text="DONKEY KICK LEFT",bg="black",fg="#FF1616", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


excersice14_right_top_2set=Frame(excersice14_right_top,bg="black")

menu14= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu14.set(nsets[0])

drop= OptionMenu(excersice14_right_top_2set, menu14,*nsets)
drop.config(bg="#FF1616")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(excersice14_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=donkeykickleft_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(excersice14_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:spnavigate(excersice14))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(excersice14_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#FF1616",command=lambda:openlinks(excersice14_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

excersice14_right_top_2set.grid(row=2,column=0)

excersice14_right_top.grid(row=0,column=0,pady=20)



excersice14_right_bottom=Frame(excersice14_right)


excersice14_right_bottom.grid(row=1,column=0,pady=30)


excersice14_right.grid(row=0,column=1,padx=30)

#donkeykickright
excersice14_url="https://www.youtube.com/watch?v=4ranVQDqlaU&ab_channel=LeapFitness"

def donkeykickright_fn():
    global sets_or_time,menu15,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=donkeykickrightf(sets_or_time,menu15.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(3.5/24)*(0.00027*wsets)*10
    print(calburned)
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_ns=str(int(glb_ns)+wsets)
    glb_ne=str(int(glb_ne)+1)
    glb_min=str(round(float(glb_min)+(secs/60),2))
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]
    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

excersice15=Frame(root,bg="black")
jj15=mainImageFunction(1.5,"pics/excersice15.png")
excersice15Pic=Label(excersice15,image=jj15,bg="black")
excersice15Pic.grid(row=0,column=0)

excersice15_right=Frame(excersice15,bg="black")
excersice15_right_top=Frame(excersice15_right,bg="black")
WhatExcersice=Label(excersice15_right_top,text="DONKEY KICK right",bg="black",fg="#FF1616", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


excersice15_right_top_2set=Frame(excersice15_right_top,bg="black")

menu15= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu15.set(nsets[0])

drop= OptionMenu(excersice15_right_top_2set, menu,*nsets)
drop.config(bg="#FF1616")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(excersice15_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=donkeykickright_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(excersice15_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:spnavigate(excersice15))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(excersice15_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#FF1616",command=lambda:openlinks(excersice14_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

excersice15_right_top_2set.grid(row=2,column=0)

excersice15_right_top.grid(row=0,column=0,pady=20)



excersice15_right_bottom=Frame(excersice15_right)


excersice15_right_bottom.grid(row=1,column=0,pady=30)


excersice15_right.grid(row=0,column=1,padx=30)


#knee pushups
excersice16_url="https://www.youtube.com/watch?v=jWxvty2KROs&ab_channel=LeapFitness"
def kneepushups_fn():
    global sets_or_time,menu16,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=kneepushupsf(sets_or_time,menu16.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(3.5/24)*(0.00027*wsets)*10
    print(calburned)
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_ns=str(int(glb_ns)+wsets)
    glb_ne=str(int(glb_ne)+1)
    glb_min=str(round(float(glb_min)+(secs/60),2))
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]

    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

excersice16=Frame(root,bg="black")
jj16=mainImageFunction(1.5,"pics/excersice17.png")
excersice16Pic=Label(excersice16,image=jj16,bg="black")
excersice16Pic.grid(row=0,column=0)

excersice16_right=Frame(excersice16,bg="black")
excersice16_right_top=Frame(excersice16_right,bg="black")
WhatExcersice=Label(excersice16_right_top,text="KNEE PUSHUPS",bg="black",fg="#FF1616", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


excersice16_right_top_2set=Frame(excersice16_right_top,bg="black")

menu16= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu16.set(nsets[0])

drop= OptionMenu(excersice16_right_top_2set, menu16,*nsets)
drop.config(bg="#FF1616")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(excersice16_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=kneepushups_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(excersice16_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:spnavigate(excersice16))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(excersice16_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#FF1616",command=lambda:openlinks(excersice16_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

excersice16_right_top_2set.grid(row=2,column=0)

excersice16_right_top.grid(row=0,column=0,pady=20)



excersice16_right_bottom=Frame(excersice16_right)


excersice16_right_bottom.grid(row=1,column=0,pady=30)


excersice16_right.grid(row=0,column=1,padx=30)


#incline pushups
excersice17_url="https://www.youtube.com/watch?v=UT03_KPhoR8&ab_channel=LeapFitness"
def inclinepushups_fn():
    global sets_or_time,menu17,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=inclinepushupsf(sets_or_time,menu17.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(3.5/24)*(0.00027*wsets)*10
    print(calburned)
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_ns=str(int(glb_ns)+wsets)
    glb_ne=str(int(glb_ne)+1)
    glb_min=str(round(float(glb_min)+(secs/60),2))
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]
    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

excersice17=Frame(root,bg="black")
jj17=mainImageFunction(1.5,"pics/excersice16.png")
excersice17Pic=Label(excersice17,image=jj17,bg="black")
excersice17Pic.grid(row=0,column=0)

excersice17_right=Frame(excersice17,bg="black")
excersice17_right_top=Frame(excersice17_right,bg="black")
WhatExcersice=Label(excersice17_right_top,text="INCLINE PUSHUPS",bg="black",fg="#FF1616", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


excersice17_right_top_2set=Frame(excersice17_right_top,bg="black")

menu17= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu17.set(nsets[0])

drop= OptionMenu(excersice17_right_top_2set, menu17,*nsets)
drop.config(bg="#FF1616")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(excersice17_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=inclinepushups_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(excersice17_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#FF1616",command=lambda:spnavigate(excersice17))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(excersice17_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#FF1616",command=lambda:openlinks(excersice17_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

excersice17_right_top_2set.grid(row=2,column=0)

excersice17_right_top.grid(row=0,column=0,pady=20)



excersice17_right_bottom=Frame(excersice17_right)


excersice17_right_bottom.grid(row=1,column=0,pady=30)


excersice17_right.grid(row=0,column=1,padx=30)



#yogasana #7ED957

#chairpose
yoga1_url="https://www.youtube.com/watch?v=ZDPMdCSy4jQ&ab_channel=Howcast"
def chairpose_fn():
    global sets_or_time,menu18,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender,glb_yoga
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=chairposef(sets_or_time,menu18.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(2/24)*(0.00027*wsets)*10
    
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_min=str(round(float(glb_min)+(secs/60),2))
    glb_yoga=str(int(glb_yoga)+1)
    
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]
    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

yoga1=Frame(root,bg="black")
yy1=mainImageFunction(1.5,"pics/yoga1.png")
yoga1Pic=Label(yoga1,image=yy1,bg="black")
yoga1Pic.grid(row=0,column=0)

yoga1_right=Frame(yoga1,bg="black")
yoga1_right_top=Frame(yoga1_right,bg="black")
WhatExcersice=Label(yoga1_right_top,text="COBRA STRECH",bg="black",fg="#7ED957", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


yoga1_right_top_2set=Frame(yoga1_right_top,bg="black")

menu18= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu18.set(nsets[0])

drop= OptionMenu(yoga1_right_top_2set, menu18,*nsets)
drop.config(bg="#7ED957")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(yoga1_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#7ED957",command=chairpose_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(yoga1_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#7ED957",command=lambda:spnavigate(yoga1))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(yoga1_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#7ED957",command=lambda:openlinks(yoga1_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

yoga1_right_top_2set.grid(row=2,column=0)

yoga1_right_top.grid(row=0,column=0,pady=20)



yoga1_right_bottom=Frame(yoga1_right)


yoga1_right_bottom.grid(row=1,column=0,pady=30)


yoga1_right.grid(row=0,column=1,padx=30)



#downward dog
yoga2_url="https://www.youtube.com/watch?v=ayRU3ecmPbI&ab_channel=Howcast"
def downwarddog_fn():
    global sets_or_time,menu19,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender,glb_yoga
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=downwarddogf(sets_or_time,menu19.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(2/24)*(0.00027*wsets)*10
    
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_min=str(round(float(glb_min)+(secs/60),2))
    glb_yoga=str(int(glb_yoga)+1)
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]
    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

yoga2=Frame(root,bg="black")
yy2=mainImageFunction(1.5,"pics/yoga2.png")
yoga2Pic=Label(yoga2,image=yy2,bg="black")
yoga2Pic.grid(row=0,column=0)

yoga2_right=Frame(yoga2,bg="black")
yoga2_right_top=Frame(yoga2_right,bg="black")
WhatExcersice=Label(yoga2_right_top,text="DOWNWARD DOG",bg="black",fg="#7ED957", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


yoga2_right_top_2set=Frame(yoga2_right_top,bg="black")

menu19= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu19.set(nsets[0])

drop= OptionMenu(yoga2_right_top_2set, menu19,*nsets)
drop.config(bg="#7ED957")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(yoga2_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#7ED957",command=downwarddog_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(yoga2_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#7ED957",command=lambda:spnavigate(yoga2))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(yoga2_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#7ED957",command=lambda:openlinks(yoga2_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

yoga2_right_top_2set.grid(row=2,column=0)

yoga2_right_top.grid(row=0,column=0,pady=20)



yoga2_right_bottom=Frame(yoga2_right)


yoga2_right_bottom.grid(row=1,column=0,pady=30)


yoga2_right.grid(row=0,column=1,padx=30)


# WarriorII
yoga3_url="https://www.youtube.com/watch?v=QbIrd6onJwQ&ab_channel=Howcast"
def warriorII_fn():
    global sets_or_time,menu20,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender,glb_yoga
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=warriorIIf(sets_or_time,menu20.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(2/24)*(0.00027*wsets)*10
    
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_min=str(round(float(glb_min)+(secs/60),2))
    glb_yoga=str(int(glb_yoga)+1)
    glb_min=str(round(float(glb_min)+(secs/60),2))
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]
    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

yoga3=Frame(root,bg="black")
yy3=mainImageFunction(1.5,"pics/yoga3.png")
yoga3Pic=Label(yoga3,image=yy3,bg="black")
yoga3Pic.grid(row=0,column=0)

yoga3_right=Frame(yoga3,bg="black")
yoga3_right_top=Frame(yoga3_right,bg="black")
WhatExcersice=Label(yoga3_right_top,text="WARRIOR II",bg="black",fg="#7ED957", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


yoga3_right_top_2set=Frame(yoga3_right_top,bg="black")

menu20= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu20.set(nsets[0])

drop= OptionMenu(yoga3_right_top_2set, menu20,*nsets)
drop.config(bg="#7ED957")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(yoga3_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#7ED957",command=warriorII_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(yoga3_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#7ED957",command=lambda:spnavigate(yoga3))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(yoga3_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#7ED957",command=lambda:openlinks(yoga3_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

yoga3_right_top_2set.grid(row=2,column=0)

yoga3_right_top.grid(row=0,column=0,pady=20)



yoga3_right_bottom=Frame(yoga3_right)


yoga3_right_bottom.grid(row=1,column=0,pady=30)


yoga3_right.grid(row=0,column=1,padx=30)


#tree pose
yoga4_url="https://www.youtube.com/watch?v=wdln9qWYloU&ab_channel=Howcast"

def treepose_fn():
    global sets_or_time,menu21,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender,glb_yoga
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=treeposef(sets_or_time,menu21.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(2/24)*(0.00027*wsets)*10
    
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_min=str(round(float(glb_min)+(secs/60),2))
    glb_yoga=str(int(glb_yoga)+1)
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]
    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

yoga4=Frame(root,bg="black")
yy4=mainImageFunction(1.5,"pics/yoga4.png")
yoga4Pic=Label(yoga4,image=yy4,bg="black")
yoga4Pic.grid(row=0,column=0)

yoga4_right=Frame(yoga4,bg="black")
yoga4_right_top=Frame(yoga4_right,bg="black")
WhatExcersice=Label(yoga4_right_top,text="TREE POSE",bg="black",fg="#7ED957", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


yoga4_right_top_2set=Frame(yoga4_right_top,bg="black")

menu21= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu21.set(nsets[0])

drop= OptionMenu(yoga4_right_top_2set, menu21,*nsets)
drop.config(bg="#7ED957")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(yoga4_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#7ED957",command=treepose_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(yoga4_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#7ED957",command=lambda:spnavigate(yoga4))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(yoga4_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#7ED957",command=lambda:openlinks(yoga4_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

yoga4_right_top_2set.grid(row=2,column=0)

yoga4_right_top.grid(row=0,column=0,pady=20)



yoga4_right_bottom=Frame(yoga4_right)


yoga4_right_bottom.grid(row=1,column=0,pady=30)


yoga4_right.grid(row=0,column=1,padx=30)


#triangular pose
yoga5_url="https://www.youtube.com/watch?v=dllfZZp0k_8&ab_channel=Howcast"
def triangularpose_fn():
    global sets_or_time,menu22,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender,glb_yoga
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=triangularf(sets_or_time,menu22.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(2/24)*(0.00027*wsets)*10
    
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_min=str(round(float(glb_min)+(secs/60),2))
    glb_yoga=str(int(glb_yoga)+1)
    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]
    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

yoga5=Frame(root,bg="black")
yy5=mainImageFunction(1.5,"pics/yoga5.png")
yoga5Pic=Label(yoga5,image=yy5,bg="black")
yoga5Pic.grid(row=0,column=0)

yoga5_right=Frame(yoga5,bg="black")
yoga5_right_top=Frame(yoga5_right,bg="black")
WhatExcersice=Label(yoga5_right_top,text="TRIANGULAR POSE",bg="black",fg="#7ED957", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


yoga5_right_top_2set=Frame(yoga5_right_top,bg="black")

menu22= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu22.set(nsets[0])

drop= OptionMenu(yoga5_right_top_2set, menu22,*nsets)
drop.config(bg="#7ED957")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(yoga5_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#7ED957",command=triangularpose_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(yoga5_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#7ED957",command=lambda:spnavigate(yoga5))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(yoga5_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#7ED957",command=lambda:openlinks(yoga5_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

yoga5_right_top_2set.grid(row=2,column=0)

yoga5_right_top.grid(row=0,column=0,pady=20)



yoga5_right_bottom=Frame(yoga5_right)


yoga5_right_bottom.grid(row=1,column=0,pady=30)


yoga5_right.grid(row=0,column=1,padx=30)


#puppyonchair

yoga6_url="https://www.youtube.com/watch?v=NKLuF1248YE&ab_channel=MyYogaBirth"
def puppyonchair_fn():
    global sets_or_time,menu23,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender,glb_yoga
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=puppyonchairf(sets_or_time,menu23.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(2/24)*(0.00027*wsets)*10
    
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_min=str(round(float(glb_min)+(secs/60),2))
    glb_yoga=str(int(glb_yoga)+1)


    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]
    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

yoga6=Frame(root,bg="black")
yy6=mainImageFunction(1.5,"pics/yoga6.png")
yoga6Pic=Label(yoga6,image=yy6,bg="black")
yoga6Pic.grid(row=0,column=0)

yoga6_right=Frame(yoga6,bg="black")
yoga6_right_top=Frame(yoga6_right,bg="black")
WhatExcersice=Label(yoga6_right_top,text="PUPPY ON CHAIR",bg="black",fg="#7ED957", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


yoga6_right_top_2set=Frame(yoga6_right_top,bg="black")

menu23= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu23.set(nsets[0])

drop= OptionMenu(yoga6_right_top_2set, menu23,*nsets)
drop.config(bg="#7ED957")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(yoga6_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#7ED957",command=puppyonchair_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(yoga6_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#7ED957",command=lambda:spnavigate(yoga6))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(yoga6_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#7ED957",command=lambda:openlinks(yoga6_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

yoga6_right_top_2set.grid(row=2,column=0)

yoga6_right_top.grid(row=0,column=0,pady=20)



yoga6_right_bottom=Frame(yoga6_right)


yoga6_right_bottom.grid(row=1,column=0,pady=30)


yoga6_right.grid(row=0,column=1,padx=30)




#warrior I
yoga7_url="https://www.youtube.com/watch?v=k4qaVoAbeHM&ab_channel=Howcast"
def warriorI_fn():
    global sets_or_time,menu24,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender,glb_yoga
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=warriorIf(sets_or_time,menu24.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(2/24)*(0.00027*wsets)*10
    
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_min=str(round(float(glb_min)+(secs/60),2))
    glb_yoga=str(int(glb_yoga)+1)


    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]
    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

yoga7=Frame(root,bg="black")
yy7=mainImageFunction(1.5,"pics/yoga9.png")
yoga7Pic=Label(yoga7,image=yy7,bg="black")
yoga7Pic.grid(row=0,column=0)

yoga7_right=Frame(yoga7,bg="black")
yoga7_right_top=Frame(yoga7_right,bg="black")
WhatExcersice=Label(yoga7_right_top,text="WARRIOR I",bg="black",fg="#7ED957", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


yoga7_right_top_2set=Frame(yoga7_right_top,bg="black")

menu24= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu24.set(nsets[0])

drop= OptionMenu(yoga7_right_top_2set, menu24,*nsets)
drop.config(bg="#7ED957")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(yoga7_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#7ED957",command=warriorI_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(yoga7_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#7ED957",command=lambda:spnavigate(yoga7))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(yoga7_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#7ED957",command=lambda:openlinks(yoga7_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

yoga7_right_top_2set.grid(row=2,column=0)

yoga7_right_top.grid(row=0,column=0,pady=20)



yoga7_right_bottom=Frame(yoga7_right)


yoga7_right_bottom.grid(row=1,column=0,pady=30)


yoga7_right.grid(row=0,column=1,padx=30)



#camelpose

yoga8_url="https://www.youtube.com/watch?v=84hg8nkQXTc&ab_channel=Howcast"
def camelpose_fn():
    global sets_or_time,menu25,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender,glb_yoga
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=camelposef(sets_or_time,menu25.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(2/24)*(0.00027*wsets)*10
    
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_min=str(round(float(glb_min)+(secs/60),2))
    glb_yoga=str(int(glb_yoga)+1)


    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]
    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

yoga8=Frame(root,bg="black")
yy8=mainImageFunction(1.5,"pics/yoga10.png")
yoga8Pic=Label(yoga8,image=yy8,bg="black")
yoga8Pic.grid(row=0,column=0)

yoga8_right=Frame(yoga8,bg="black")
yoga8_right_top=Frame(yoga8_right,bg="black")
WhatExcersice=Label(yoga8_right_top,text="CAMEL POSE",bg="black",fg="#7ED957", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


yoga8_right_top_2set=Frame(yoga8_right_top,bg="black")

menu25= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu25.set(nsets[0])

drop= OptionMenu(yoga8_right_top_2set, menu25,*nsets)
drop.config(bg="#7ED957")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(yoga8_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#7ED957",command=camelpose_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(yoga8_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#7ED957",command=lambda:spnavigate(yoga8))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(yoga8_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#7ED957",command=lambda:openlinks(yoga8_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

yoga8_right_top_2set.grid(row=2,column=0)

yoga8_right_top.grid(row=0,column=0,pady=20)



yoga8_right_bottom=Frame(yoga8_right)


yoga8_right_bottom.grid(row=1,column=0,pady=30)


yoga8_right.grid(row=0,column=1,padx=30)




#sideplank

yoga9_url="https://www.youtube.com/watch?v=krrxMqVQPCU&ab_channel=Howcast"

def sideplank_fn():
    global sets_or_time,menu26,glb_weight,glb_ns,glb_ne,glb_cb,glb_min,glb_gender,glb_yoga
    global glb_key,glb_fileName,glb_camera,whichCamera,cameras
    f=open("nothing/"+str(glb_filename)+".txt","r")
    wsets,secs=sideplankf(sets_or_time,menu26.get(),glb_camera)


    if glb_gender=="male":
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)+5
    else:
        bmr=10*int(glb_height)+6.25*int(glb_weight)-5*int(glb_age)-161

    calburned=bmr*(2/24)*(0.00027*wsets)*10
    
    ff=f.read().split("\n")
    fg=open("nothing/xxx.txt","a")
    fernet = Fernet(glb_key)

    glb_cb=str(float(glb_cb)+round(calburned,2))
    glb_min=str(round(float(glb_min)+(secs/60),2))
    glb_yoga=str(int(glb_yoga)+1)


    infos=[glb_name,glb_height,glb_weight,glb_age,glb_gender,glb_cb,glb_ns
    ,glb_ne, glb_yoga,glb_min,glb_camera]
    messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))

    for i in infos:
        fg.write(str(fernet.encrypt(str(i).encode()))+" \n")

    profile_visit1()

    f.close()
    fg.close()
    os.remove("nothing/"+str(glb_filename)+".txt")
    os.rename("nothing/xxx.txt","nothing/"+str(glb_filename)+".txt")

yoga9=Frame(root,bg="black")
yy9=mainImageFunction(1.5,"pics/yoga9.png")
yoga9Pic=Label(yoga9,image=yy9,bg="black")
yoga9Pic.grid(row=0,column=0)

yoga9_right=Frame(yoga9,bg="black")
yoga9_right_top=Frame(yoga9_right,bg="black")
WhatExcersice=Label(yoga9_right_top,text="SIDE PLANK",bg="black",fg="#7ED957", font=("Times", "20", "bold italic") )
WhatExcersice.grid(row=0,column=0,pady=20)


yoga9_right_top_2set=Frame(yoga9_right_top,bg="black")

menu26= IntVar()
nsets = [10, 15, 20, 25, 30,45,60,75,90,105,120,135]
menu26.set(nsets[0])

drop= OptionMenu(yoga9_right_top_2set, menu26,*nsets)
drop.config(bg="#7ED957")
drop.config(font=("Times", "13", "bold italic") )
drop.config(width=10)
drop.grid(row=0,column=0,padx=10)

track=Button(yoga9_right_top_2set,text="TRACK",font=("Times", "13", "bold italic") ,width=12,bg="#7ED957",command=sideplank_fn)
track.grid(row=0,column=1,padx=10)

backHome=Button(yoga9_right_top_2set,text="GO BACK",font=("Times", "13", "bold italic") ,width=12,bg="#7ED957",command=lambda:spnavigate(yoga9))
backHome.grid(row=0,column=2,padx=10)


watchHowToDoIt=Button(yoga9_right_top_2set,text="WATCH  HOW  TO  DO  IT",font=("Times", "13", "bold italic") ,width=20,bg="#7ED957",command=lambda:openlinks(yoga9_url))
watchHowToDoIt.grid(row=1,column=0,padx=10,pady=20,columnspan=3)

yoga9_right_top_2set.grid(row=2,column=0)

yoga9_right_top.grid(row=0,column=0,pady=20)



yoga9_right_bottom=Frame(yoga9_right)


yoga9_right_bottom.grid(row=1,column=0,pady=30)


yoga9_right.grid(row=0,column=1,padx=30)



root.mainloop()
