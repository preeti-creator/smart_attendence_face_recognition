from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help 
from time import strftime 
from datetime import datetime

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700")
        self.root.title("Face Recognition System")
        
        img1=Image.open(r"photos\CMRIT_campus.jpg")
        img1=img1.resize((1350,700))
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1350,height=700)
        
        #logo
        img=Image.open(r"photos\cmritlogo.jpeg")
        img=img.resize((130,90))
        self.photoimg=ImageTk.PhotoImage(img)
        
        b1=Label(bg_img,image=self.photoimg)
        b1.place(x=0,y=0,width=130,height=90)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",25,"bold"),fg="black",bg="white")
        title_lbl.place(x=130,y=30,width=1200,height=35)
        
         #============time====================
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time) 
        lbl=Label(title_lbl,font=('times new roman',14,'bold'),bg="white",fg="black")
        lbl.place(x=0,y=0,width=110,height=40)
        time()
        
        #student
        img2=Image.open(r"photos\student.jpeg")
        img2=img2.resize((200,200))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        b2=Button(bg_img,image=self.photoimg2,command=self.student_details,cursor="hand2")
        b2.place(x=150,y=100,width=200,height=200)
        
        b2_1=Button(bg_img, text="STUDENT DETAILS",command=self.student_details, cursor="hand2")
        b2_1.place(x=150,y=270,width=200,height=30)
        
        #attendence
        img3=Image.open(r"photos\atten.webp")
        img3=img3.resize((200,200))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        b3=Button(bg_img,image=self.photoimg3,command=self.atten_data,cursor="hand2")
        b3.place(x=650,y=100,width=200,height=200)
        
        b3_1=Button(bg_img, text="ATTENDENCE", command=self.atten_data,cursor="hand2")
        b3_1.place(x=650,y=270,width=200,height=30)
        
        #FACE DETECTOR
        img4=Image.open(r"photos\attendence.jpeg")
        img4=img4.resize((200,200))
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b4=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.face_data)
        b4.place(x=400,y=100,width=200,height=200)#650 
        
        b4_1=Button(bg_img, text="FACE DETECTOR", cursor="hand2",command=self.face_data)
        b4_1.place(x=400,y=270,width=200,height=30)
        
        #developer
        img9=Image.open(r"photos\developer.jpeg")
        img9=img9.resize((200,200))
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b9=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.devl_data)
        b9.place(x=900,y=100,width=200,height=200)
        
        b9_1=Button(bg_img, text="DEVELOPER", cursor="hand2",command=self.devl_data)
        b9_1.place(x=900,y=270,width=200,height=30)
        
        #TRAIN DATA
        img5=Image.open(r"photos\train.jpeg")
        img5=img5.resize((200,200))
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b5=Button(bg_img,image=self.photoimg5,command=self.train_data,cursor="hand2")
        b5.place(x=150,y=350,width=200,height=200)
        
        b5_1=Button(bg_img, text="TRAIN DATA", command=self.train_data,cursor="hand2")
        b5_1.place(x=150,y=520,width=200,height=30)
        
        #photos
        img6=Image.open(r"photos\photo.png")
        img6=img6.resize((200,200))
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b5=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.open_img)
        b5.place(x=400,y=350,width=200,height=200)
        
        b5_1=Button(bg_img, text="PHOTOS",command=self.open_img, cursor="hand2")
        b5_1.place(x=400,y=520,width=200,height=30)
        
        #help
        img8=Image.open(r"photos\help.jpg")
        img8=img8.resize((200,200))
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b8=Button(bg_img,image=self.photoimg8,command=self.help_desk,cursor="hand2")
        b8.place(x=650,y=350,width=200,height=200)
        
        b8_1=Button(bg_img, text="HELP",command=self.help_desk, cursor="hand2")
        b8_1.place(x=650,y=520,width=200,height=30)
        
        #exit
        img7=Image.open(r"photos\exit.jpg")
        img7=img7.resize((200,200))
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b5=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.iExit)
        b5.place(x=900,y=350,width=200,height=200)
        
        b5_1=Button(bg_img, text="EXIT", cursor="hand2",command=self.iExit)
        b5_1.place(x=900,y=520,width=200,height=30) 
        
    def open_img(self):
        os.startfile("data")
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face recognition","Are you sure exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
        
    #================FUNCTION BUTTON=====================
    
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def atten_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def devl_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
        
        
        

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()