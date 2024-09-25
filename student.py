from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime

class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700")
        self.root.title("Face Recognisation System")
        
        
        #===========variables=============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_USN=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        
        
        #background image
        img1=Image.open(r"C:\Users\91720\OneDrive\Desktop\smart_attendence\photos\CMRIT_campus.jpg")
        img1=img1.resize((1350,700))
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1350,height=700)
        
        #logo
        img=Image.open(r"C:\Users\91720\OneDrive\Desktop\smart_attendence\photos\cmritlogo.jpeg")
        img=img.resize((130,90))
        self.photoimg=ImageTk.PhotoImage(img)
        
        b1=Label(bg_img,image=self.photoimg)
        b1.place(x=0,y=0,width=130,height=90)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),fg="black",bg="white")
        title_lbl.place(x=140,y=30,width=1000,height=30)
         
          #============time====================
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time) 
        
        lbl=Label(title_lbl,font=('times new roman',14,'bold'),bg="white",fg="black")
        lbl.place(x=0,y=0,width=110,height=35)
        time()
         
        #main frame
        main_frame =Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=90,width=1300,height=600)
        
       
        
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETIELS",font=("times new roman",12,"bold"))
        Left_frame.place(x=5,y=5,width=650,height=580)
        
        #image
        img_left=Image.open(r"C:\Users\91720\OneDrive\Desktop\smart_attendence\photos\student_management.jpg")
        img_left=img_left.resize((640,80))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        bg_img=Label(Left_frame,image=self.photoimg_left)
        bg_img.place(x=2,y=0,width=640,height=80)
        
        #current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=85,width=640,height=100)
        
        #department
        dep_label=Label(current_course_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","CSE","ISE","IT","CIVIL","MECH","ECE","EEE","CSDS","AIML","AIDS","CSML")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=7,sticky=W)
        
        #course
        course_label=Label(current_course_frame,text="Course:",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=7,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select course","MBA","MCA","ARCHITECHTURE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=7,sticky=W)
        
        #year
        year_label=Label(current_course_frame,text="Year:",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=7,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","First","Second","Third","Forth")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=7,sticky=W)
        
        #semester
        semester_label=Label(current_course_frame,text="Semester:",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=7,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semister","SEM-1","SEM-2","SEM-3","SEM-4","SEM-5","SEM-6","SEM-7","SEM-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=7,sticky=W)
        
        #class student infomation 
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class student information",font=("times new roman",12,"bold"),bg="white")
        class_student_frame.place(x=5,y=195,width=640,height=300)
        
        #studentID
        studentid_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,sticky=W)
        
        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=13,font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=1,pady=5,sticky=W)
        
        #student name
        studentname_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=1,pady=5,sticky=W)
        
        #class didvision
        studentiddiv_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        studentiddiv_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        studentdiv_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=12,font=("times new roman",12,"bold"))
        studentdiv_entry.grid(row=1,column=1,padx=1,pady=5,sticky=W)
        
        studentdiv_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=12)
        studentdiv_combo["values"]=("Select division","A","B","C","D","E","F","G","H","I","J","K")
        studentdiv_combo.current(0)
        studentdiv_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)
        
        
        #roll number
        USN_label=Label(class_student_frame,text="USN:",font=("times new roman",12,"bold"),bg="white")
        USN_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        USN_entry=ttk.Entry(class_student_frame,textvariable=self.var_USN,width=20,font=("times new roman",12,"bold"))
        USN_entry.grid(row=1,column=3,padx=1,pady=5,sticky=W)
        
        #gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=12,font=("times new roman",12,"bold"))
        gender_entry.grid(row=2,column=1,padx=1,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=12)
        gender_combo["values"]=("Select Gender","MALE","FEMALE")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)
        
        
        #dob
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=1,pady=5,sticky=W)
        
        #email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=15,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=1,pady=5,sticky=W)
        
        #phoneno
        phoneno_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phoneno_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phoneno_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phoneno_entry.grid(row=3,column=3,padx=1,pady=5,sticky=W)
        
        #adress
        adress_label=Label(class_student_frame,text="Adress:",font=("times new roman",12,"bold"),bg="white")
        adress_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        adress_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=15,font=("times new roman",12,"bold"))
        adress_entry.grid(row=4,column=1,padx=1,pady=5,sticky=W)
        
        
        #radio buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
        radionbtn1.grid(row=5,column=0)
        
        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radionbtn2.grid(row=5,column=1)
        
        
        #bbutton frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=635,height=35)
        
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        
        update_btn=Button(btn_frame,text="Update",width=16,command=self.update_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",width=16,command=self.delete_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=240,width=635,height=35)
        
        takephoto_btn=Button(btn_frame1,command=self.generate_dataset,text="Take A Photo Sample",width=34,font=("times new roman",12,"bold"),bg="blue",fg="white")
        takephoto_btn.grid(row=0,column=0)
        
        updatephoto_btn=Button(btn_frame1,text="update Photo Sample",width=34,font=("times new roman",12,"bold"),bg="blue",fg="white")
        updatephoto_btn.grid(row=0,column=1)
        
        ######################################################
        
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETIELS",font=("times new roman",12,"bold"))
        Right_frame.place(x=660,y=5,width=600,height=580)
        
        #image
        img_right=Image.open(r"C:\Users\91720\OneDrive\Desktop\smart_attendence\photos\student_dtails.jpg")
        img_right=img_right.resize((590,80))
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        bg_img=Label(Right_frame,image=self.photoimg_right)
        bg_img.place(x=5,y=0,width=590,height=80)
        
        #search
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=85,width=580,height=70)
        
        search_label=Label(search_frame,text="Search by:",font=("times new roman",13,"bold"),bg="black",fg="white")
        search_label.grid(row=0,column=0,padx=1,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=14)
        search_combo["values"]=("Select","USN","PHONE_NO")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=1,pady=10,sticky=W)
        
        search_entry=ttk.Entry(search_frame,width=14,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=1,pady=5,sticky=W)
        
        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=2)
        
        #show
        showall_btn=Button(search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=2)
        
        #=================table frame===============
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=160,width=580,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","USN","gender","dob","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Sem")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="StudentName")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("USN",text="USN")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("USN",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #==================FUNCTION DECCLARATION==============
    
    def add_data(self):
        if self.var_dep.get()=="select department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","ALL FIELDS ARE REQUIRED",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="MSD07@csk",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_sem.get(),
                                                                                                            self.var_id.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_USN.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_radio1.get()
                                                                                                
                                                                                                          ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    
    ############################fetch data ####################
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="MSD07@csk",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    ###################get cursor###################
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0])
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_USN.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_radio1.set(data[13])
        
        
    #############update#############
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","ALL FIELDS ARE REQUIRED",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="MSD07@csk",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Sem=%s,Student_Id=%s,Name=%s,Division=%s,USN=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_USN.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_id.get()
                                                                                                                                                                                    ))    
                else:
                    if not Update:
                        return
                conn.commit()
                self.fetch_data()
                messagebox.showinfo("Success","updated successful",parent=self.root)
                
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        
################# delete fuction ##########################
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="MSD07@csk",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted Student",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            
            
    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semister")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select division")
        self.var_USN.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")
        
    #################genrate data set +++++++++++++++
    def generate_dataset(self):
        if self.var_dep.get()=="select department" or self.var_name.get()=="" or self.var_id.get()=="":
           messagebox.showerror("Error","ALL FIELDS ARE REQUIRED",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="MSD07@csk",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Sem=%s,Name=%s,Division=%s,USN=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                self.var_USN.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.var_id.get()==id+1
                                                                                                                                                                             ))
                
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                ####load pre data face open cv#######
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factro=1.3
                    #minimum neighbor=5
                    
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0) 
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compled!!!")
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            
            
if __name__ == "__main__":
    root = Tk()
    obj=Student(root)
    root.mainloop()