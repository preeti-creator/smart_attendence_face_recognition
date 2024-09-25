from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1350x700")
                self.root.title("face Recogniton System")
        
        #variables
                self.var_atten_id=StringVar()
                self.var_atten_USN=StringVar()
                self.var_atten_name=StringVar()
                self.var_atten_dep=StringVar()
                self.var_atten_time=StringVar()
                self.var_atten_date=StringVar()
                self.var_atten_attendance=StringVar()

        #1st
                img_top=Image.open(r"photos\WhatsApp Image 2024-07-21 at 19.14.20_1197a8ce.jpg")
                img_top=img_top.resize((650,150))
                self.photoimg_top=ImageTk.PhotoImage(img_top)
        
                f_lbl=Label(self.root,image=self.photoimg_top)
                f_lbl.place(x=0,y=0,width=650,height=150)
        
        #2nd
                img_top1=Image.open(r"photos\WhatsApp Image 2024-07-21 at 19.14.21_cf20473b.jpg")
                img_top1=img_top1.resize((700,150))
                self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
                f_lbl=Label(self.root,image=self.photoimg_top1)
                f_lbl.place(x=650,y=0,width=700,height=150)
        
        #bg image
                img1=Image.open(r"photos\CMRIT_campus.jpg")
                img1=img1.resize((1350,550))
                self.photoimg1=ImageTk.PhotoImage(img1)
        
                bg_img=Label(self.root,image=self.photoimg1)
                bg_img.place(x=0,y=150,width=1350,height=550)
        
                title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM ",font=("times new roman",25,"bold"),fg="darkgreen",bg="white")
                title_lbl.place(x=0,y=0,width=1350,height=25)
        
                main_frame =Frame(bg_img,bd=2,bg="white")
                main_frame.place(x=10,y=30,width=1250,height=500)
        
        #left label frame
                Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT ATTENDANCE DETIELS",font=("times new roman",12,"bold"))
                Left_frame.place(x=5,y=5,width=630,height=500)
        
                img_left=Image.open(r"photos\OIP.jpeg")
                img_left=img_left.resize((620,60))
                self.photoimg_left=ImageTk.PhotoImage(img_left)
        
                bg_img=Label(Left_frame,image=self.photoimg_left)
                bg_img.place(x=2,y=0,width=620,height=60)
        
                Left_inside_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE)
                Left_inside_frame.place(x=5,y=65,width=620,height=350)
        
        #labeland entry
        #Attendance ID
                attendanceId_label=Label(Left_inside_frame,text="AttendanceId :",font=("times new roman",12,"bold"),bg="white")
                attendanceId_label.grid(row=1,column=0,padx=10,sticky=W)
                
                atten_id=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
                atten_id.grid(row=1,column=1,padx=1,pady=5,sticky=W)
                
                #USN
                USN_label=Label(Left_inside_frame,text="USN :",font=("times new roman",12,"bold"),bg="white")
                USN_label.grid(row=1,column=2,padx=20,sticky=W)
                
                atten_USN=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_USN,font=("times new roman",12,"bold"))
                atten_USN.grid(row=1,column=3,padx=1,pady=5,sticky=W)
                
                #name
                name_label=Label(Left_inside_frame,text="Name :",font=("times new roman",12,"bold"),bg="white")
                name_label.grid(row=2,column=0,padx=10,sticky=W)
                
                atten_name=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
                atten_name.grid(row=2,column=1,padx=1,pady=5,sticky=W)
                
                #department
                dep_label=Label(Left_inside_frame,text="Department :",font=("times new roman",12,"bold"),bg="white")
                dep_label.grid(row=2,column=2,padx=10,sticky=W)
                
                atten_dep=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
                atten_dep.grid(row=2,column=3,padx=1,pady=5,sticky=W)
                
                #time
                time_label=Label(Left_inside_frame,text="Time :",font=("times new roman",12,"bold"),bg="white")
                time_label.grid(row=3,column=0,padx=10,sticky=W)
                
                atten_time=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
                atten_time.grid(row=3,column=1,padx=1,pady=5,sticky=W)
                
                #date
                date_label=Label(Left_inside_frame,text="Date :",font=("times new roman",12,"bold"),bg="white")
                date_label.grid(row=3,column=2,padx=10,sticky=W)
                
                atten_date=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
                atten_date.grid(row=3,column=3,padx=1,pady=5,sticky=W)
                
                #Attendance status
                attendancel_label=Label(Left_inside_frame,text="Attendance :",font=("times new roman",12,"bold"),bg="white")
                attendancel_label.grid(row=4,column=0,padx=1)
                
                self.atten_status=ttk.Combobox(Left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly",width=18)
                self.atten_status["values"]=("Status","Present","Absent")
                self.atten_status.grid(row=4,column=1,pady=7)
                self.atten_status.current(0)
                
                #bbutton frame
                btn_frame=Frame(Left_inside_frame,bd=2,relief=RIDGE,bg="white")
                btn_frame.place(x=0,y=250,width=620,height=35)
                
                import_btn=Button(btn_frame,text="Import ",command=self.importCsv,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
                import_btn.grid(row=0,column=0)
                
                export_btn=Button(btn_frame,text="Export",width=16,command=self.exportCsv,font=("times new roman",12,"bold"),bg="blue",fg="white")
                export_btn.grid(row=0,column=1)
                
                update_btn=Button(btn_frame,text="Update",width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
                update_btn.grid(row=0,column=2)
                
                reset_btn=Button(btn_frame,text="Reset",width=16,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
                reset_btn.grid(row=0,column=3)
                
                #right label frame
                Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="ATTENDANCE DETIELS",font=("times new roman",12,"bold"))
                Right_frame.place(x=640,y=5,width=600,height=490)
                
                table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
                table_frame.place(x=5,y=5,width=590,height=420)
                
                #########score bar table########
                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
                
                self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","USN","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                
                scroll_x.config(command=self.AttendanceReportTable.xview)
                scroll_y.config(command=self.AttendanceReportTable.yview)
                
                self.AttendanceReportTable.heading("id",text="Attendance ID")
                self.AttendanceReportTable.heading("USN",text="USN")
                self.AttendanceReportTable.heading("name",text="Name")
                self.AttendanceReportTable.heading("department",text="Department")
                self.AttendanceReportTable.heading("time",text="Time")
                self.AttendanceReportTable.heading("date",text="Date")
                self.AttendanceReportTable.heading("attendance",text="Attendance")
                
                self.AttendanceReportTable["show"]="headings"
                
                self.AttendanceReportTable.column("id",width=100)
                self.AttendanceReportTable.column("USN",width=100)
                self.AttendanceReportTable.column("name",width=100)
                self.AttendanceReportTable.column("department",width=100)
                self.AttendanceReportTable.column("time",width=100)
                self.AttendanceReportTable.column("date",width=100)
                self.AttendanceReportTable.column("attendance",width=100)
                
                self.AttendanceReportTable.pack(fill=BOTH,expand=1)
                
                self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
                
        
        #fetch data
        
        
        def fetchData(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)
                
        #import CSV
        def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File",".*")),parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)
                
        #export CSv
        def exportCsv(self):
            try:
                if len(mydata)<1:
                    messagebox.showerror("No Data","No Data found to export",parent=self.root) 
                    return False                
                fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".csv"),("ALL File",".*")),parent=self.root)
                with open(fln,mode="w",newline="") as myfile:
                    exp_write=csv.writer(myfile,delimiter=",")
                    for i in mydata:
                        exp_write.writerow(i)
                    messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
        
        
        def get_cursor(self,event=""):
            cursor_row=self.AttendanceReportTable.focus()
            content=self.AttendanceReportTable.item(cursor_row)
            rows=content['values'] 
            self.var_atten_id.set(rows[0])
            self.var_atten_USN.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6])
        
        
        def reset_data(self):
            self.var_atten_id.set("")
            self.var_atten_USN.set("")
            self.var_atten_name.set("")
            self.var_atten_dep.set("")
            self.var_atten_time.set("")
            self.var_atten_date.set("")
            self.var_atten_attendance.set("")
        
        
        
if  __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()