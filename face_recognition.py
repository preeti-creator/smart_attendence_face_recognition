from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700")
        self.root.title("face Recogniton System")
        
        
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",25,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1350,height=25)
        
        
        #1st
        img_top=Image.open(r"photos\face2.jpeg")
        img_top=img_top.resize((500,600))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=35,width=500,height=600)
        
        
        #2nd
        img_top1=Image.open(r"photos\face1.webp")
        img_top1=img_top1.resize((850,600))
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
        f_lbl=Label(self.root,image=self.photoimg_top1)
        f_lbl.place(x=500,y=35,width=850,height=600)
                    
        #button
        b1_1=Button(f_lbl, text="Face Recognition",command=self.face_recog, cursor="hand2",font=("times new roman",20,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=315,y=530,width=220,height=35)
    #####attendence
    def mark_attendance(self,i,r,n,d):
        with open("vinay.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
            
            
            
    #face recognition
    
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="MSD07@csk",database="face_recognizer")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select USN from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                
                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"USN:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                
                coord=[x,y,w,h]
        
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face recognition",img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Attendance Marked.")
        
        
        
   
if  __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()