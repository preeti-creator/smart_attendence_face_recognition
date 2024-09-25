from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700") 
        self.root.title("face Recognition System")
        
        img_top=Image.open(r"photos\helpdesk.jpeg")
        img_top=img_top.resize((1350,700))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1350,height=700)
        
        dev_label=Label(f_lbl,text="Email:vinay16r@gmail.com",font=("times new roman",20,"bold"),bg="white",fg="black")
        dev_label.place(x=520,y=350) 


if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()