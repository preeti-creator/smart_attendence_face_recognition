from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700")
        self.root.title("face Recogniton System")
        
        
        title_lbl=Label(self.root,text="Train Data Set",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1350,height=25)
        
        img_top=Image.open(r"photos\train1.webp")
        img_top=img_top.resize((1350,300))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=25,width=1350,height=300)
        
        #button
        b1_1=Button(self.root, text="TRAIN DATA",command=self.train_classifier, cursor="hand2",font=("times new roman",60,"bold"),bg="blue",fg="white")
        b1_1.place(x=0,y=320,width=1350,height=70)
        
        img_bottom=Image.open(r"photos\train2.jpg")
        img_bottom=img_bottom.resize((1350,280))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=390,width=1350,height=280)

        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]
    
        faces=[]
        ids=[]
    
        for image in path:
            img=Image.open(image).convert('L')  #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
        
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
    #===================train the classifer and save============================        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")                    
        
        

if  __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()