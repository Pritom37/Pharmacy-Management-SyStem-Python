from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector

from tkinter import messagebox


class PhramacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1400x800+0+0")
#---------Add Medicine Variable------
        self.addmed_var=StringVar()
        self.refmed_var=StringVar()


        lbltitle=Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,bg='darkgreen',
        fg="white",font=("times new roman",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open("D:\Pharmacy Logo\istockphoto-1070588384-612x612.jpg")
        img1=img1.resize((70,70),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=20,y=20)

#-----------Data Frame--------------
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1400,height=400)


        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",
              fg="darkgreen",font=("times new roman",13,"bold"))

        DataFrameLeft.place(x=0,y=5,width=800,height=350)


        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add",
              fg="darkgreen",font=("times new roman",13,"bold"))

        DataFrameRight.place(x=810,y=5,width=520,height=350)
#-------------Button Frame-----------
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1500,height=65)

#------------Main Button-------------
        btnAddData=Button(ButtonFrame,text="Medicine Add",font=("times new roman",13,"bold"),width=13,fg="white",bg="darkgreen")
        btnAddData.grid(row=0,column=0)
#--------------Update-----------
        btnUpdateMed=Button(ButtonFrame,text="UPDATE",font=("times new roman",13,"bold"),width=13,fg="white",bg="darkgreen")
        btnUpdateMed.grid(row=0,column=1)
#------------DELETE-------------
        btnDeleteMed=Button(ButtonFrame,text="DELETE",font=("times new roman",13,"bold"),width=13,fg="white",bg="red")
        btnDeleteMed.grid(row=0,column=2)
#------------RESET-------------
        btnRestMed=Button(ButtonFrame,text="RESET",font=("times new roman",13,"bold"),width=13,fg="white",bg="darkgreen")
        btnRestMed.grid(row=0,column=3)
#------------EXIT-------------
        btnExitMed=Button(ButtonFrame,text="EXIT",font=("times new roman",13,"bold"),width=13,fg="white",bg="darkgreen")
        btnExitMed.grid(row=0,column=4)

#----------Search By-----------------
        lblSearch=Button(ButtonFrame,text="Search By",font=("times new roman",13,"bold"),width=13,fg="white",bg="red")
        lblSearch.grid(row=0,column=5,sticky=W)

        search_combo=ttk.Combobox(ButtonFrame,width=12,font=("times new roman",13,"bold"),state="readonly")
        search_combo["values"]=("Ref","Medname","Lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)
 #--------text search----------------       
        txtSearch=Entry(ButtonFrame,bd=3,relief=RIDGE,width=12,font=("times new roman",13,"bold"))
        txtSearch.grid(row=0,column=7)

        searchButton=Button(ButtonFrame,text="SEARCH",font=("times new roman",13,"bold"),width=13,fg="white",bg="darkgreen")
        searchButton.grid(row=0,column=8)

        showAll=Button(ButtonFrame,text="SHOW ALL",font=("times new roman",12,"bold"),width=13,fg="white",bg="darkgreen")
        showAll.grid(row=0,column=9)

#--------Levels and Entry------
        lblrefno=Label(DataFrameLeft,text="Reference No",font=("times new roman",13,"bold"),padx=2,)
        lblrefno.grid(row=0,column=0,sticky=W)

        ref_combo=ttk.Combobox(DataFrameLeft ,width=24,font=("times new roman",13,"bold"),state="readonly")
        ref_combo["values"]=("Ref","Medname","Lot")
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)

#-------Add Medicine----------------
        lblCompanyName=Label(DataFrameLeft,text="Company Name:",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblCompanyName.grid(row=1,column=0,sticky=W)
        txtCompanyName=Entry(DataFrameLeft,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtCompanyName.grid(row=1,column=1)

        lblTypeOfMedcine=Label(DataFrameLeft,text="Type Of Medicine:",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblTypeOfMedcine.grid(row=2,column=0,sticky=W)

        comTypeOfMedicine=ttk.Combobox(DataFrameLeft ,state="readonly",font=("times new roman",13,"bold"),width=24)
        comTypeOfMedicine["values"]=("Tablet","Liquid","Capsules","Drops","Inhales","Injection")
        comTypeOfMedicine.grid(row=2,column=1)
        comTypeOfMedicine.current(0)

        lblMedicineName=Label(DataFrameLeft,text="Medicine Name",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)

        comMedicineName=ttk.Combobox(DataFrameLeft ,state="readonly",font=("times new roman",13,"bold"),width=24)
        comMedicineName["values"]=("Napa","Ace","Seclo","Maxpro")
        comMedicineName.grid(row=3,column=1)
        comMedicineName.current(0)
        
        lblLotN0=Label(DataFrameLeft,text="Lot No:",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblLotN0.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtLotNo.grid(row=4,column=1)

        
        lblIssueDate=Label(DataFrameLeft,text="Issue Date:",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtIssueDate.grid(row=5,column=1)

        lblExDate=Label(DataFrameLeft,text=" Date:",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate=Entry(DataFrameLeft,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtExDate.grid(row=6,column=1)

        lblUses=Label(DataFrameLeft,text="Uses:",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtUses.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,text="Side Effect:",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtSideEffect.grid(row=8,column=1)

        lblDosage=Label(DataFrameLeft,text="Dosage:",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblDosage.grid(row=0,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtDosage.grid(row=0,column=3)

        lblPrice=Label(DataFrameLeft,text="Price:",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblPrice.grid(row=1,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtPrice.grid(row=1,column=3)
#----------Images-----------
        img2=Image.open("D:\Pharmacy Logo\jjjhhhpp.jpg")
        img2=img2.resize((315,230),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=500,y=250)


#-------------Data Frame Right---------

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add",
              fg="darkgreen",font=("times new roman",13,"bold"))

        DataFrameRight.place(x=810,y=5,width=520,height=350)

        lblrefno=Label(DataFrameRight,text="Referance No:",font=("times new roman",13,"bold"))
        lblrefno.place(x=0,y=20)
        txtrefno=Entry(DataFrameRight,textvariable=self.refmed_var,font=("times new roman",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtrefno.place(x=135,y=20)

        lblrefno=Label(DataFrameRight,text="Medicine Name:",font=("times new roman",13,"bold"))
        lblrefno.place(x=0,y=50)
        txtrefno=Entry(DataFrameRight,textvariable=self.addmed_var,font=("times new roman",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtrefno.place(x=135,y=50)

#-------------Side Frame------------
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=100,width=300,height=200)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)
  
        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)

#---------Medicine Add Button--------
        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=320,y=100,width=140,height=166)

        btnAddmed=Button(down_frame,text="Add",font=("times new roman",13,"bold"),width=12,bg="green",fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)
       

        btnUpdate=Button(down_frame,text="UPDATE",font=("times new roman",13,"bold"),width=12,bg="purple",fg="white",pady=4)
        btnUpdate.grid(row=1,column=0)

        btnDelete=Button(down_frame,text="DELETE",font=("times new roman",13,"bold"),width=12,bg="red",fg="white",pady=4)
        btnDelete.grid(row=2,column=0)

        btnClear=Button(down_frame,text="CLEAR",font=("times new roman",13,"bold"),width=12,bg="orange",fg="white",pady=4)
        btnClear.grid(row=3,column=0)

#----------Frame Details-------------
        Framedeatails=Frame(self.root,bd=15,relief=RIDGE,bg="darkgreen")
        Framedeatails.place(x=0,y=585,width=1553,height=200)

#---------Main Table And Scrollbar AT BOTTOM--------
        table_frame=Frame(Framedeatails,bd=15,relief=RIDGE)
        table_frame.place(x=0,y=1,width=1450,height=180)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        self.pharmacy_Table=ttk.Treeview(table_frame,column=("reg","companyname","type","tablatname","lotno","issuedate","expdate","uses","sideeffect","dosage","price"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.pharmacy_Table.xview)
        scroll_y.config(command=self.pharmacy_Table.yview)
        
        self.pharmacy_Table["show"]="headings"

        self.pharmacy_Table.heading("reg",text="Referance No:")
        self.pharmacy_Table.heading("companyname",text="Company Name:")
        self.pharmacy_Table.heading("type",text="Type Of Medicine:")
        self.pharmacy_Table.heading("tablatname",text="Tablat Name:" )
        self.pharmacy_Table.heading("lotno",text="Lot No:")
        self.pharmacy_Table.heading("issuedate",text="Issue Date:")
        self.pharmacy_Table.heading("expdate",text="Exp Date:")
        self.pharmacy_Table.heading("uses",text="Uses:")
        self.pharmacy_Table.heading("sideeffect",text="Side Effect:")
        self.pharmacy_Table.heading("dosage",text="Dosage:")
        self.pharmacy_Table.heading("price",text="Price:")
        self.pharmacy_Table.pack(fill=BOTH,expand=1)

        self.pharmacy_Table.column("reg",width=100)
        self.pharmacy_Table.column("companyname",width=100)
        self.pharmacy_Table.column("type",width=100)
        self.pharmacy_Table.column("tablatname",width=100)
        self.pharmacy_Table.column("lotno",width=100)
        self.pharmacy_Table.column("issuedate",width=100)
        self.pharmacy_Table.column("expdate",width=100)
        self.pharmacy_Table.column("uses",width=100)
        self.pharmacy_Table.column("sideeffect",width=100)
        self.pharmacy_Table.column("dosage",width=100)
        self.pharmacy_Table.column("price",width=100)



#------------Add med Data Base------
def Addmed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="pritomghosh@01971",database="pharmacy_schema")
        my_coursor=conn.cursor()
        my_coursor.execute("insert into pharma(Ref,MedName)values(%s,%s)",(self.refmed_var.get(),self.addmed_var.get() ))
        

        conn.commit()
        conn.close
        messagebox.showinfo("Success","Medicine Added")

      



if __name__ =="__main__":
    root=Tk()
    obj=PhramacyManagementSystem(root)
    root.mainloop()



