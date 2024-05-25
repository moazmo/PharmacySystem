from tkinter import * # type: ignore
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")
        
        # =============== AddMed variable =============== #
        self.addMed_var = StringVar()
        self.refMed_var = StringVar()
        
        # =============== Main Variable =============== #
        
        self.ref_var = StringVar()
        self.cmpname_var = StringVar()
        self.type_var = StringVar()
        self.medname_var = StringVar()
        self.lotno_var = StringVar()
        self.issuedate_var = StringVar()
        self.expdate_var = StringVar()
        self.uses_var = StringVar()
        self.sideeffects_var = StringVar()
        self.warning_var = StringVar()
        self.dosage_var = StringVar()
        self.price_var = StringVar()
        self.productqt_var = StringVar()
        
        
        title = Label(self.root, text="Pharmacy Management System", bd=15, relief=RIDGE, bg="white", fg="darkgreen", font=("times new roman", 50, "bold"), pady=4, padx=2)
        title.pack(side=TOP, fill=X)
        
        img2 = Image.open(r"images\logo.webp")
        img2 = img2.resize((80, 82), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img2)
        b1 = Button(title, image=self.photoimg1, borderwidth=0)
        b1.place(x=210, y=0)
        
        # =============== Data Frame =============== #
        DataFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        DataFrame.place(x=0, y=120, width=1530, height=400)
        
        DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Information", fg="darkgreen", font=("arial", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)
        
        # =============== Buttons Frame =============== #
        ButtonFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        ButtonFrame.place(x=0, y=520, width=1530, height=65)
        
        # =============== Main Button =============== #
        btnAddData = Button(ButtonFrame, text="Medicine Add", font=("arial", 12, "bold"),bg="darkgreen", fg="white", command=self.add_data)
        btnAddData.grid(row=0, column=0)
        
        btnUpdateData = Button(ButtonFrame, text="Update", font=("arial", 13, "bold"), width=14, bg="darkgreen", fg="white", command=self.Update)
        btnUpdateData.grid(row=0, column=1)
        
        btnDeleteData = Button(ButtonFrame, text="Delete", font=("arial", 13, "bold"), width=14, bg="red", fg="white", command=self.delete)
        btnDeleteData.grid(row=0, column=2)
        
        btnResetData = Button(ButtonFrame, text="Reset", font=("arial", 13, "bold"), width=14, bg="darkgreen", fg="white", command=self.reset)
        btnResetData.grid(row=0, column=3)
        
        btnExit = Button(ButtonFrame, text="Exit", font=("arial", 13, "bold"), width=14, bg="darkgreen", fg="white", command=self.exit)
        btnExit.grid(row=0, column=4)
        
        # =============== Search By =============== #
        lblSearch = Label(ButtonFrame, font=("arial", 17, "bold"), text="Search By", padx=2, bg="red", fg="white")
        lblSearch.grid(row=0, column=5, sticky=W)
        
        self.search_var = StringVar()

        search_combo = ttk.Combobox(ButtonFrame, textvariable=self.search_var, font=("arial", 17, "bold"), width=12, state="readonly")
        search_combo["values"] = ("Ref_No", "medname", "LotNo")
        search_combo.grid(row=0, column=6)
        search_combo.current(0)
        
        self.search_txt_var = StringVar()
        txtsearch = Entry(ButtonFrame, textvariable=self.search_txt_var, font=("arial", 17, "bold"), width=12, bd=3, relief=RIDGE)
        txtsearch.grid(row=0, column=7)
        
        searchBtn = Button(ButtonFrame, text="Search", font=("arial", 13, "bold"), width=14, bg="darkgreen", fg="white", command=self.search_data)
        searchBtn.grid(row=0, column=8)
        
        ShowAllBtn = Button(ButtonFrame, text="Show All", font=("arial", 13, "bold"), width=14, bg="darkgreen", fg="white", command=self.fetch_data)
        ShowAllBtn.grid(row=0, column=9)
        
        # =============== Label & Entry =============== #
        lblRef = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Reference No", padx=2)
        lblRef.grid(row=0, column=0, sticky=W)
        
        conn = mysql.connector.connect(host="localhost", user="root", password="Mkomko123@", database="pharmacy")
        c = conn.cursor()
        c.execute("select Ref from pharma")
        row = c.fetchall()
        
        ref_combo = ttk.Combobox(DataFrameLeft, textvariable=self.ref_var, font=("arial", 12, "bold"), width=27, state="readonly")
        ref_combo["values"] = row
        ref_combo.grid(row=0, column=1)
        ref_combo.current(0)
        
        lblCmpName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Company Name", padx=2, pady=6)
        lblCmpName.grid(row=1, column=0, sticky=W)
        txtCmpName = Entry(DataFrameLeft, textvariable=self.cmpname_var, font=("arial", 13, "bold"), width=29, bd=2, relief=RIDGE, bg="white")
        txtCmpName.grid(row=1, column=1)
        
        lblTypeofMed = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Type of Medicine", padx=2, pady=6)
        lblTypeofMed.grid(row=2, column=0, sticky=W)
        
        comTypeofMed = ttk.Combobox(DataFrameLeft, textvariable=self.type_var, font=("arial", 12, "bold"), width=27, state="readonly")
        comTypeofMed["values"] = ("Tablet", "Liquid", "Capsules", "Topical Medicine", "Injection", "Drops", "Inhales")
        comTypeofMed.current(0)
        comTypeofMed.grid(row=2, column=1)
        
        # =============== Add Medicine =============== #
        lblMedicineName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Medicine Name", padx=2, pady=6)
        lblMedicineName.grid(row=3, column=0, sticky=W)
        
        conn = mysql.connector.connect(host="localhost", user="root", password="Mkomko123@", database="pharmacy")
        c = conn.cursor()
        c.execute("select MedName from pharma")
        med = c.fetchall()
        
        comMedicineName = ttk.Combobox(DataFrameLeft, textvariable=self.medname_var, font=("arial", 12, "bold"), width=27, state="readonly")
        comMedicineName["values"] = med
        comMedicineName.current(0)
        comMedicineName.grid(row=3, column=1)
        
        lblLotNo = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot No:", padx=2, pady=6)
        lblLotNo.grid(row=4, column=0, sticky=W)
        txtLotNo = Entry(DataFrameLeft, textvariable=self.lotno_var, font=("arial", 13, "bold"), width=29, bd=2, relief=RIDGE, bg="white")
        txtLotNo.grid(row=4, column=1)
        
        lblIssueDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(DataFrameLeft, textvariable=self.issuedate_var, font=("arial", 13, "bold"), width=29, bd=2, relief=RIDGE, bg="white")
        txtIssueDate.grid(row=5, column=1)
        
        lblExDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExDate.grid(row=6, column=0, sticky=W)
        txtExDate = Entry(DataFrameLeft, textvariable=self.expdate_var, font=("arial", 13, "bold"), width=29, bd=2, relief=RIDGE, bg="white")
        txtExDate.grid(row=6, column=1)
        
        lblUses = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Uses:", padx=2, pady=6)
        lblUses.grid(row=7, column=0, sticky=W)
        txtUses = Entry(DataFrameLeft, textvariable=self.uses_var, font=("arial", 13, "bold"), width=29, bd=2, relief=RIDGE, bg="white")
        txtUses.grid(row=7, column=1)
        
        lblSideEffect = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataFrameLeft,textvariable=self.sideeffects_var, font=("arial", 13, "bold"), width=29, bd=2, relief=RIDGE, bg="white")
        txtSideEffect.grid(row=8, column=1)
        
        lblPrecWarning = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Prec&Warning:", padx=15)
        lblPrecWarning.grid(row=0, column=2, sticky=W)
        txtPrecWarning = Entry(DataFrameLeft, textvariable=self.warning_var, font=("arial", 13, "bold"), width=29, bd=2, relief=RIDGE, bg="white")
        txtPrecWarning.grid(row=0, column=3)
        
        lblDosage = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dosage:", padx=15, pady=6)
        lblDosage.grid(row=1, column=2, sticky=W)
        txtDosage = Entry(DataFrameLeft, textvariable=self.dosage_var, font=("arial", 13, "bold"), width=29, bd=2, relief=RIDGE, bg="white")
        txtDosage.grid(row=1, column=3)
        
        lblPrice = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Tablets Price:", padx=15, pady=6)
        lblPrice.grid(row=2, column=2, sticky=W)
        txtPrice = Entry(DataFrameLeft, textvariable=self.price_var, font=("arial", 13, "bold"), width=29, bd=2, relief=RIDGE, bg="white")
        txtPrice.grid(row=2, column=3)
        
        lblProductQt = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Product Qt:", padx=15, pady=6)
        lblProductQt.grid(row=3, column=2, sticky=W)
        txtProductQt = Entry(DataFrameLeft, textvariable=self.productqt_var, font=("arial", 13, "bold"), width=29, bd=2, relief=RIDGE, bg="white")
        txtProductQt.grid(row=3, column=3)
        
        # =============== Images =============== #
        lblHome = Label(DataFrameLeft, font=("arial", 15, "bold"), text="Stay Home Stay Safe:", padx=2, pady=6, bg="white", fg="red", width=37)
        lblHome.place(x=410, y=140)
        
        img2 = Image.open(r"images\tab2.webp")
        img2 = img2.resize((150, 135), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b1 = Button(self.root, image=self.photoimg2, borderwidth=0)
        b1.place(x=770, y=330)
        
        img3 = Image.open(r"images\tab3.jpg")
        img3 = img3.resize((150, 135), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b1 = Button(self.root, image=self.photoimg3, borderwidth=0)
        b1.place(x=620, y=330)
        
        img4 = Image.open(r"images\eng.webp")
        img4 = img4.resize((150, 135), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(self.root, image=self.photoimg4, borderwidth=0)
        b1.place(x=475, y=330)
        
        # =============== DataFrameRight =============== #
        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Add Department", fg="darkgreen", font=("arial", 12, "bold"))
        DataFrameRight.place(x=910, y=5, width=540, height=350)
        
        img5 = Image.open(r"images\tab4.jpg")
        img5 = img5.resize((200, 75), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(self.root, image=self.photoimg5, borderwidth=0)
        b1.place(x=960, y=160)
        
        img6 = Image.open(r"images\tab4.jpg")
        img6 = img6.resize((200, 75), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(self.root, image=self.photoimg6, borderwidth=0)
        b1.place(x=1160, y=160)
        
        img7 = Image.open(r"images\tab2.webp")
        img7 = img7.resize((200, 145), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(self.root, image=self.photoimg7, borderwidth=0)
        b1.place(x=1270, y=160)
        
        lblRefNo = Label(DataFrameRight, font=("arial", 12, "bold"), text="Reference No:")
        lblRefNo.place(x=0, y=80)
        txtRefNo = Entry(DataFrameRight, textvariable=self.refMed_var, font=("arial", 15, "bold"), width=14, bd=2, relief=RIDGE, bg="white")
        txtRefNo.place(x=135, y=80)
        
        lblMedName = Label(DataFrameRight, font=("arial", 12, "bold"), text="Medicine Name:")
        lblMedName.place(x=0, y=110)
        txtMedName = Entry(DataFrameRight, textvariable=self.addMed_var, font=("arial", 15, "bold"), width=14, bd=2, relief=RIDGE, bg="white")
        txtMedName.place(x=135, y=110)
        
        # =============== Side Frame =============== #
        side_frame = Frame(DataFrameRight, bd=4, relief=RIDGE, bg="white")
        side_frame.place(x=0, y=150, width=290, height=160)
        
        sc_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT, fill=Y)
        
        self.medicine_table = ttk.Treeview(side_frame, columns=("ref", "medname"), xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)
        
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)
        
        self.medicine_table.heading("ref", text="Ref")
        self.medicine_table.heading("medname", text="Medicine Name")
        
        self.medicine_table["show"] = "headings"
        self.medicine_table.pack(fill=BOTH, expand=1)
        
        self.medicine_table.column("ref", width=100)
        self.medicine_table.column("medname", width=100)
        
        self.medicine_table.bind("<ButtonRelease-1>", self.Medget_cursor) # type: ignore
        
        # =============== Medicine Add Buttons =============== #
        down_frame = Frame(DataFrameRight, bd=4, relief=RIDGE, bg="darkgreen")
        down_frame.place(x=330, y=150, width=135, height=160)
        
        btnAddMed= Button(down_frame, text="Add", font=("arial", 12, "bold"), width=12, bg="lime", fg="white", pady=4, command=self.add_medicine)
        btnAddMed.grid(row=0, column=0)
        
        btnUpdateMed = Button(down_frame, text="Update", font=("arial", 12, "bold"),bg="purple", fg="white", pady=4, width=12, command=self.updateMed)
        btnUpdateMed.grid(row=1, column=0)
        
        btnDeleteMed = Button(down_frame, text="Delete", font=("arial", 12, "bold"),bg="red", fg="white", pady=4, width=12, command=self.deleteMed)
        btnDeleteMed.grid(row=2, column=0)
        
        btnClearMed = Button(down_frame, text="Clear", font=("arial", 12, "bold"),bg="orange", fg="white", pady=4, width=12, command=self.clearMed)
        btnClearMed.grid(row=3, column=0)
        
        # =============== Frame Details =============== #
        frameDetails = Frame(self.root, bd=15, relief=RIDGE)
        frameDetails.place(x=0, y=580, width=1530, height=210)
        
        # =============== Main Table & scrollbar =============== #
        Table_frame= Frame(frameDetails, bd=15, relief=RIDGE, padx=20)
        Table_frame.place(x=0, y=1, width=1500, height=180)
        
        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.main_table = ttk.Treeview(Table_frame, columns=("reg", "companyname", "type", "tabletname", "lotno", "issuedate", "expdate", "uses", "sideeffects", "warning", "dosage", "price", "productqt"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.config(command=self.main_table.xview)
        scroll_y.config(command=self.main_table.yview)
        
        self.main_table["show"] = "headings"
        
        self.main_table.heading("reg", text="Referece No")
        self.main_table.heading("companyname", text="Company Name")
        self.main_table.heading("type", text="Type")
        self.main_table.heading("tabletname", text="Tablet Name")
        self.main_table.heading("lotno", text="Lot No")
        self.main_table.heading("issuedate", text="Issue Date")
        self.main_table.heading("expdate", text="Exp Date")
        self.main_table.heading("uses", text="Uses")
        self.main_table.heading("sideeffects", text="Side Effects")
        self.main_table.heading("warning", text="Warning")
        self.main_table.heading("dosage", text="Dosage")
        self.main_table.heading("price", text="Price")
        self.main_table.heading("productqt", text="Product Qt")
        
        self.main_table.pack(fill=BOTH, expand=1)
        
        self.main_table.column("reg", width=100)
        self.main_table.column("companyname", width=100)
        self.main_table.column("type", width=100)
        self.main_table.column("tabletname", width=100)
        self.main_table.column("lotno", width=100)
        self.main_table.column("issuedate", width=100)
        self.main_table.column("expdate", width=100)
        self.main_table.column("uses", width=100)
        self.main_table.column("sideeffects", width=100)
        self.main_table.column("warning", width=100)
        self.main_table.column("dosage", width=100)
        self.main_table.column("price", width=100)
        self.main_table.column("productqt", width=100)
        self.fetch_dataMed()
        self.fetch_data()
        self.main_table.bind("<ButtonRelease-1>", self.get_cursor) # type: ignore
        
    # =============== Add Medicine Functionality Declaration (DB) =============== #
    def add_medicine(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Mkomko123@", database="pharmacy")
        c = conn.cursor()
        c.execute("insert into pharma(Ref,MedName) values(%s,%s)",
                (
            self.refMed_var.get(),
            self.addMed_var.get()
        )
        )
        conn.commit()
        self.fetch_dataMed()
        self.Medget_cursor()
        conn.close()
        messagebox.showinfo("Success", "Medicine Added")
    
    def fetch_dataMed(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Mkomko123@", database="pharmacy")
        c = conn.cursor()
        c.execute("select * from pharma")
        rows = c.fetchall()
        if len(rows) != 0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for row in rows:
                self.medicine_table.insert("", END, values=row) # type: ignore
            conn.commit()
        conn.close()
    
    # =============== Med Get cursor =============== #
    def Medget_cursor(self, event=""):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row = content["values"]
        self.refMed_var.set(row[0])
        self.addMed_var.set(row[1])
        
    def updateMed(self):
        if self.refMed_var.get() == "" or self.addMed_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Mkomko123@", database="pharmacy")
            c = conn.cursor()
            c.execute("update pharma set MedName=%s where Ref=%s", (self.addMed_var.get(), self.refMed_var.get()))
            conn.commit()
            self.fetch_dataMed()
            conn.close()
            
            messagebox.showinfo("Success", "Medicine Updated")
    
    def deleteMed(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Mkomko123@", database="pharmacy")
        c = conn.cursor()
        c.execute("delete from pharma where Ref=%s", (self.refMed_var.get(),))
        conn.commit()
        self.fetch_dataMed()
        conn.close()
    
    def clearMed(self):
        self.refMed_var.set("")
        self.addMed_var.set("")

    # =============== Main Table =============== #
    def add_data(self):
        if self.ref_var.get() == "" or self.lotno_var.get() == "" or self.issuedate_var.get() == "" or self.expdate_var.get() == "" or self.uses_var.get() == "" or self.sideeffects_var.get() == "" or self.warning_var.get() == "" or self.dosage_var.get() == "" or self.price_var.get() == "" or self.productqt_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Mkomko123@", database="pharmacy")
            c = conn.cursor()
            c.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                self.ref_var.get(),
                self.cmpname_var.get(),
                self.type_var.get(),
                self.medname_var.get(),
                self.lotno_var.get(),
                self.issuedate_var.get(),
                self.expdate_var.get(),
                self.uses_var.get(),
                self.sideeffects_var.get(),
                self.warning_var.get(),
                self.dosage_var.get(),
                self.price_var.get(),
                self.productqt_var.get()
            )
            )
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Data Added")
        
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Mkomko123@", database="pharmacy")
        c = conn.cursor()
        c.execute("select * from pharmacy")
        rows = c.fetchall()
        if len(rows) != 0:
            self.main_table.delete(*self.main_table.get_children())
            for row in rows:
                self.main_table.insert("", END, values=row) # type: ignore
            conn.commit()
        conn.close()
    
    def get_cursor(self, event=""):
        cursor_row = self.main_table.focus()
        content = self.main_table.item(cursor_row)
        row = content["values"]
        self.ref_var.set(row[0])
        self.cmpname_var.set(row[1])
        self.type_var.set(row[2])
        self.medname_var.set(row[3])
        self.lotno_var.set(row[4])
        self.issuedate_var.set(row[5])
        self.expdate_var.set(row[6])
        self.uses_var.set(row[7])
        self.sideeffects_var.set(row[8])
        self.warning_var.set(row[9])
        self.dosage_var.set(row[10])
        self.price_var.set(row[11])
        self.productqt_var.set(row[12])
    
    def Update(self):
        if self.ref_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Mkomko123@", database="pharmacy")
            c = conn.cursor()
            c.execute("update pharmacy set CmpName=%s, TypeMed=%s, medname=%s, LotNo=%s, Issuedate=%s, Expdate=%s, uses=%s, Sideeffect=%s, warning=%s, dosage=%s, price=%s, product=%s where Ref_No=%s", (
                self.cmpname_var.get(),
                self.type_var.get(),
                self.medname_var.get(),
                self.lotno_var.get(),
                self.issuedate_var.get(),
                self.expdate_var.get(),
                self.uses_var.get(),
                self.sideeffects_var.get(),
                self.warning_var.get(),
                self.dosage_var.get(),
                self.price_var.get(),
                self.productqt_var.get(),
                self.ref_var.get()
            )
            )
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Data Updated")
    
    def delete(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Mkomko123@", database="pharmacy")
        c = conn.cursor()
        c.execute("delete from pharmacy where Ref_No=%s", (self.ref_var.get(),))
        conn.commit()
        self.fetch_data()
        conn.close()
    
    def reset(self):
        # self.ref_var.set("")
        self.cmpname_var.set("")
        # self.type_var.set("")
        # self.medname_var.set("")
        self.lotno_var.set("")
        self.issuedate_var.set("")
        self.expdate_var.set("")
        self.uses_var.set("")
        self.sideeffects_var.set("")
        self.warning_var.set("")
        self.dosage_var.set("")
        self.price_var.set("")
        self.productqt_var.set("")
    
    def exit(self):
        self.root.destroy()
    
    def search_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Mkomko123@", database="pharmacy")
        c = conn.cursor()
        c.execute("select * from pharmacy where "+str(self.search_var.get())+" LIKE '%"+str(self.search_txt_var.get())+"%'")
        rows = c.fetchall()
        if len(rows) != 0:
            self.main_table.delete(*self.main_table.get_children())
            for row in rows:
                self.main_table.insert("", END, values=row) # type: ignore
            conn.commit()
        conn.close()
        
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()