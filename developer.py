from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700")
        self.root.title("Face Recognisation System")
        
        
        
        title_lbl=Label(self.root,text="DEVELOPERS",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1350,height=35)
        
        img_top=Image.open(r"photos\dev.jpg")
        img_top=img_top.resize((1350,650))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=35,width=1350,height=650)
        
        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=750,y=0,width=500,height=580)
        
        
        #developen info
        dev_label=Label(main_frame,text="Hello!!",font=("times new roman",20,"bold"),bg="white",fg="black")
        dev_label.place(x=200,y=10)
        
        dev_label=Label(main_frame,text="We are students of CMR Institute of Technology from",font=("times new roman",15,"bold"),bg="white",fg="black")
        dev_label.place(x=10,y=55)
        
        dev_label=Label(main_frame,text="Electronics and Communication Engineering Department.",font=("times new roman",15,"bold"),bg="white",fg="black")
        dev_label.place(x=10,y=85)
        
        
        dev_label=Label(main_frame,text="Team: ",font=("times new roman",20,"bold"),bg="white",fg="black")
        dev_label.place(x=10,y=160)
        
        dev_label=Label(main_frame,text="Preeti S Kataraki",font=("times new roman",15,"bold"),bg="white",fg="black")
        dev_label.place(x=40,y=210)
        
        dev_label=Label(main_frame,text="Vinay R ",font=("times new roman",15,"bold"),bg="white",fg="black")
        dev_label.place(x=40,y=240)
        
        dev_label=Label(main_frame,text="Vilas S Patil",font=("times new roman",15,"bold"),bg="white",fg="black")
        dev_label.place(x=40,y=270)
        
        
        img3=Image.open(r"photos\p1.jpg")
        img3=img3.resize((210,190))
        self.photoimg_top3=ImageTk.PhotoImage(img3)
        
        f_lbl=Label(main_frame,image=self.photoimg_top3)
        f_lbl.place(x=255,y=140,width=210,height=190)
        
        img1=Image.open(r"photos\vinay.jpg")
        img1=img1.resize((200,190))
        self.photoimg_top1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=30,y=360,width=200,height=190)
    
        img2=Image.open(r"photos\vilas1.jpg")
        img2=img2.resize((210,190))
        self.photoimg_top2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(main_frame,image=self.photoimg_top2)
        f_lbl.place(x=255,y=360,width=210,height=190)     
        
if __name__ == "__main__":
    root = Tk()
    obj=Developer(root)
    root.mainloop()