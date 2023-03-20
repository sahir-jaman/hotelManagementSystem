from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Page")
        self.root.geometry("1310x560+232+230")

        # ===================== varibles which are connecting MySQL =====================
        self.varRef = StringVar()
        x = random.randint(1000, 9999)
        self.varRef.set(str(x))

        self.varName = StringVar()
        self.varMother = StringVar()
        self.varGender = StringVar()
        self.varPost = StringVar()
        self.varMobile = StringVar()
        self.varEmail = StringVar()
        self.varNationality = StringVar()
        self.varIdProof = StringVar()
        self.varIdNumber = StringVar()
        self.varAddress = StringVar()

        # ==================== title ==============
        custTitle = Label(self.root, text="Add Customer Details", font=(
            "Times new roman", 18, "bold"), fg="Gold", background="black", relief="solid")
        custTitle.place(x=0, y=0, width=1310, height=40)

        # ================== Logo image =====================
        img2 = Image.open(r"E:\python with vs code\python projects\Hotel management system\pictures\hotelLogo.jpg")
        img2 = img2.resize((100, 40))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimage = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimage.place(x=0, y=0, width=60, height=40)

        # =================== customer Details Left Box =====================

        leftBox = LabelFrame(self.root, width=485, height=470, relief='solid',
                             text='Customer Details', fg='blue', font=("Times new roman", 14, "bold"), padx=2)
        leftBox.place(x=1, y=42, width=485, height=470)

        # =================== input lines & entries =================
        # customer Reference
        custRef = Label(leftBox, text='Customer Reference',
                        font=("Times new roman", 13, "bold"), padx=6)
        custRef.grid(row=0, column=0, sticky='w')
        custRef = ttk.Entry(leftBox, width=26, font=("Times new roman", 12, 'bold'),
                            textvariable=self.varRef, foreground='blue', state='readonly')
        custRef.grid(row=0, column=1)

        # Cutomer name
        nameType = Label(leftBox, text='Customer Name', font=(
            "Times new roman", 13, "bold"), padx=6)
        nameType.grid(row=1, column=0, sticky='w')
        nameEntry = ttk.Entry(leftBox, width=26, font=(
            "Times new roman", 12,), textvariable=self.varName, foreground='blue')
        nameEntry.grid(row=1, column=1)

        # Mother name
        motherName = Label(leftBox, text='Mother Name', font=(
            "Times new roman", 13, "bold"), padx=6)
        motherName.grid(row=2, column=0, sticky='w')
        motherName = ttk.Entry(leftBox, width=26, font=(
            "Times new roman", 12), textvariable=self.varMother, foreground='blue')
        motherName.grid(row=2, column=1)

        # Gender
        genderType = Label(leftBox, text='Gender', font=(
            "Times new roman", 13, "bold"), padx=6)
        genderType.grid(row=3, column=0, sticky='w')

        genderComboBox = ttk.Combobox(leftBox, width=22, values=[
                                      'Male', 'Female', 'others'], textvariable=self.varGender, font=("Times new roman", 13), state='readonly')
        genderComboBox.grid(row=3, column=1)

        # PostCode
        postCode = Label(leftBox, text='Post Code  ', font=(
            "Times new roman", 13, "bold"), padx=6)
        postCode.grid(row=4, column=0, sticky='w')
        postCode = ttk.Entry(leftBox, width=26, font=(
            "Times new roman", 12), textvariable=self.varPost, foreground='blue')
        postCode.grid(row=4, column=1)

        # Mobile
        mobileNum = Label(leftBox, text='Moble Number  ', font=(
            "Times new roman", 13, "bold"), padx=6)
        mobileNum.grid(row=5, column=0, sticky='w')
        mobileNum = ttk.Entry(leftBox, width=26, font=(
            "Times new roman", 12), textvariable=self.varMobile, foreground='blue')
        mobileNum.grid(row=5, column=1)

        # Email
        emailType = Label(leftBox, text='Email  ', font=(
            "Times new roman", 13, "bold"), padx=6)
        emailType.grid(row=6, column=0, sticky='w')
        emailType = ttk.Entry(leftBox, width=26, font=(
            "Times new roman", 12), textvariable=self.varEmail, foreground='blue')
        emailType.grid(row=6, column=1)

        # Nationality
        nameType = Label(leftBox, text='nationality', font=(
            "Times new roman", 13, "bold"), padx=6)
        nameType.grid(row=7, column=0, sticky='w')

        nationalityComboBox = ttk.Combobox(leftBox, width=22, values=['Bangladeshi', 'Indian', 'pakistani', 'others'], textvariable=self.varNationality, font=("Times new roman", 13), state='readonly')
        nationalityComboBox.grid(row=7, column=1)

        # id Proof Type
        idType = Label(leftBox, text='id Proof', font=("Times new roman", 13, "bold"), padx=6)
        idType.grid(row=8, column=0, sticky='w')

        idComboBox = ttk.Combobox(leftBox, width=22, values=['AdharCard', 'DrivingLicence', 'Passport'], textvariable=self.varIdProof, font=("Times new roman", 13), state='readonly')
        idComboBox.grid(row=8, column=1)

        # id number
        idType = Label(leftBox, text='id Number  ', font=(
            "Times new roman", 13, "bold"), padx=6)
        idType.grid(row=9, column=0, sticky='w')
        idEntry = ttk.Entry(leftBox, width=26, font=(
            "Times new roman", 12), textvariable=self.varIdNumber, foreground='blue')
        idEntry.grid(row=9, column=1)

        # address
        addressType = Label(leftBox, text='Address ', font=(
            "Times new roman", 13, "bold"), padx=6)
        addressType.grid(row=10, column=0, sticky='w')
        addressEntry = ttk.Entry(leftBox, width=26, font=(
            "Times new roman", 12,), textvariable=self.varAddress, foreground='blue')
        addressEntry.grid(row=10, column=1)

        # ================ Footer ====================
        buttonFrame = Frame(leftBox, width=485, height=40,
                            relief='solid', background='white')
        buttonFrame.place(x=0, y=380, width=478, height=40)

        # Button1
        buttonAdd = Button(buttonFrame, text='Add', command=self.add_data, font=(
            'arial', 10, 'bold'), width=11, relief='ridge', bg='black', fg='gold')
        buttonAdd.grid(row=0, column=0)

        # Button2
        buttonAdd = Button(buttonFrame, text='Update', command=self.updateOperation, font=('arial', 10, 'bold'), width=11, relief='ridge', bg='black', fg='gold',)
        buttonAdd.grid(row=0, column=1)

        # Button3
        buttonAdd = Button(buttonFrame, text='Delete',command=self.deleteOperation, font=(
            'arial', 10, 'bold'), width=11, relief='ridge', bg='black', fg='gold')
        buttonAdd.grid(row=0, column=2)

        # Button4
        buttonAdd = Button(buttonFrame, text='Reset',command=self.resetOperation, font=(
            'arial', 10, 'bold'), width=11, relief='ridge', bg='black', fg='gold')
        buttonAdd.grid(row=0, column=3)

        # ========================== Search System / Right-slide Label Frame ===========================1310x560 width=485,height=470
        rightSlideFrame = LabelFrame(self.root, text='View Details and Search System', font=('arial', 12, 'bold'), fg='blue', width=820, height=470, relief='solid')
        rightSlideFrame.place(x=490, y=42, width=820, height=470)

        searchByLabel = Label(rightSlideFrame, text='Search By:', background='black', fg='gold', font=('arial', 11, 'bold'), width=10, height=1, relief='solid', padx=6)
        searchByLabel.grid(row=0, column=0, padx=5)

        self.searchVar = StringVar()
        searchByEntry = ttk.Combobox(rightSlideFrame,textvariable=self.searchVar, values=['Mobile', 'Ref'], width=20, state='readonly',)
        searchByEntry.grid(row=0, column=1, padx=5)

        self.textSearch = StringVar()
        randomTextinput = ttk.Entry(rightSlideFrame,textvariable=self.textSearch, width=18, font=('arial', 12, 'bold'))
        randomTextinput.grid(row=0, column=2, padx=5)

        # 2Buttons
        searchButton = Button(rightSlideFrame, text='Search',command=self.searchingOperation, background='black',fg='gold', font=('arial', 10, 'bold'), width=10)
        searchButton.grid(row=0, column=3, padx=2)
        searchButton2 = Button(rightSlideFrame, text='Show All',command=self.fetchDataFromSql,background='black', fg='gold', font=('arial', 10, 'bold'), width=10)
        searchButton2.grid(row=0, column=4, padx=2)

        # ========================= inside Label Frame =====================
        details_table = LabelFrame(rightSlideFrame, width=810, height=365, relief='solid')
        details_table.place(x=2, y=50, width=810, height=365)

        # scrollbar
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, columns=('ref', 'name', 'mother', 'gender', 'post', 'mobile',
                                               'email', 'nationality', 'idProof', 'idNumber', "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side='bottom', fill='x')
        scroll_y.pack(side='right', fill='y')
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        # headings
        self.Cust_Details_Table.heading('ref', text="Refer No")
        self.Cust_Details_Table.heading('name', text="Name")
        self.Cust_Details_Table.heading('mother', text="Mother Name")
        self.Cust_Details_Table.heading('gender', text="Gender")
        self.Cust_Details_Table.heading('post', text="PostCode")
        self.Cust_Details_Table.heading('mobile', text="Mobile")
        self.Cust_Details_Table.heading('email', text="Email")
        self.Cust_Details_Table.heading('nationality', text="Nationality")
        self.Cust_Details_Table.heading('idProof', text="Id Proof")
        self.Cust_Details_Table.heading('idNumber', text="Id Number")
        self.Cust_Details_Table.heading('address', text="Address")

        self.Cust_Details_Table['show'] = 'headings'

        self.Cust_Details_Table.column('ref', width=100)
        self.Cust_Details_Table.column('name', width=100)
        self.Cust_Details_Table.column('mother', width=100)
        self.Cust_Details_Table.column('gender', width=100)
        self.Cust_Details_Table.column('post', width=100)
        self.Cust_Details_Table.column('mobile', width=100)
        self.Cust_Details_Table.column('email', width=100)
        self.Cust_Details_Table.column('nationality', width=100)
        self.Cust_Details_Table.column('idProof', width=100)
        self.Cust_Details_Table.column('idNumber', width=100)
        self.Cust_Details_Table.column('address', width=100)

        self.Cust_Details_Table.pack(fill='both', expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetchDataFromSql()

    def add_data(self):
        if self.varMobile.get() == "":
            messagebox.showerror(
                'Error', 'All Data Required', parent=self.root)
        else:
            try:
                mySqlConnection = mysql.connector.connect(
                    host='localhost', user='root', password='sahirs47', database='hotelManagement')
                myCursor = mySqlConnection.cursor()
                myCursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.varRef.get(), self.varName.get(), self.varMother.get(
                    ), self.varGender.get(), self.varPost.get(), self.varMobile.get(),
                    self.varEmail.get(), self.varNationality.get(), self.varIdProof.get(
                    ), self.varIdNumber.get(), self.varAddress.get()
                ))
                mySqlConnection.commit()
                self.fetchDataFromSql()
                mySqlConnection.close()
                messagebox.showinfo("success", "Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetchDataFromSql(self):
        mySqlConnection = mysql.connector.connect(
            host='localhost', user='root', password='sahirs47', database='hotelManagement')
        mycursor = mySqlConnection.cursor()
        mycursor.execute("select * from customer")
        row = mycursor.fetchall()
        if len(row) != 0:
            self.Cust_Details_Table.delete(
                *self.Cust_Details_Table.get_children())
            for i in row:
                self.Cust_Details_Table.insert('', END, values=i)
                mySqlConnection.commit()
            mySqlConnection.close()

    def get_cursor(self, event=""):
        cursorRow = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursorRow)
        row = []
        row = content['values']
        self.varRef.set(row[0]),
        self.varName.set(row[1]),
        self.varMother.set(row[2]),
        self.varGender.set(row[3]),
        self.varPost.set(row[4]),
        self.varMobile.set(row[5]),
        self.varEmail.set(row[6]),
        self.varNationality.set(row[7]),
        self.varIdProof.set(row[8]),
        self.varIdNumber.set(row[9]),
        self.varAddress.set(row[10])

    def updateOperation(self):
        if self.varMobile.get() == "":
            messagebox.showerror("Error", "Please enter your mobile Number", parent=self.root)
        else:
            mySqlConnection = mysql.connector.connect(host='localhost', user='root', password='sahirs47', database='hotelManagement')
            myCursor = mySqlConnection.cursor()
            myCursor.execute("update customer SET Name=%s, Mother=%s, Gender=%s, PostCode=%s, Mobile=%s, Email=%s, Nationality=%s, IdProof=%s, IdNumber=%s, Address=%s where Ref=%s",
                             (
                                 self.varName.get(), self.varMother.get(), self.varGender.get(
                                 ), self.varPost.get(), self.varMobile.get(),
                                 self.varEmail.get(), self.varNationality.get(), self.varIdProof.get(
                                 ), self.varIdNumber.get(), self.varAddress.get(), self.varRef.get()

                             ))
            mySqlConnection.commit()
            mySqlConnection.close()
            messagebox.showinfo("Success","Customer Details has been updated", parent=self.root)
            
    ############### My Code ###############
    # def deleteOperation(self):
    #     mySqlConnection = mysql.connector.connect(host='localhost', user='root', password='sahirs47', database='hotelManagement')
    #     myCursor = mySqlConnection.cursor()
    #     myCursor.execute("delete from customer where Ref=%s",(self.varRef.get(),))
    #     mySqlConnection.commit()
    #     self.fetchDataFromSql()
    #     mySqlConnection.close()
    #     messagebox.showinfo("Success","The Record has been Deleted",parent=self.root)
    
    def deleteOperation(self):
        deleteOperation = messagebox.askyesno("Hotel Management system","Do your want to delete this customer record",parent=self.root)
        if deleteOperation>0:
            mySqlConnection = mysql.connector.connect(host='localhost', user='root', password='sahirs47', database='hotelManagement')
            myCursor = mySqlConnection.cursor()
            query = 'delete from customer where Ref=%s'
            value=(self.varRef.get(),)
            myCursor.execute(query,value)
        else:
            if not deleteOperation:
                return
        mySqlConnection.commit()
        self.fetchDataFromSql()
        mySqlConnection.close()
        messagebox.showinfo("Success","The Record has been Deleted",parent=self.root)
        
    def resetOperation(self):
        self.varName.set(""),
        self.varMother.set(""),
        #self.varGender.set(""),
        self.varPost.set(""),
        self.varMobile.set(""),
        self.varEmail.set(""),
        #self.varNationality.set(""),
        #self.varIdProof.set(""),
        self.varIdNumber.set(""),
        self.varAddress.set("")
        
        x=random.randint(1000, 9999)
        self.varRef.set(str(x))
    
    def searchingOperation(self):
        mySqlConnection = mysql.connector.connect(host='localhost', user='root', password='sahirs47', database='hotelManagement')
        myCursor = mySqlConnection.cursor()
        
        myCursor.execute("select * from customer where "+str(self.searchVar.get())+" LIKE '%"+str(self.textSearch.get())+"%'")
        row = myCursor.fetchall()
        if len(row)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in row:
                self.Cust_Details_Table.insert("", END, values=i)
            mySqlConnection.commit()
        mySqlConnection.close()
            
            
            
            
        


if __name__ == "__main__":
    root = Tk()
    obj = Cust_win(root)
    root.mainloop()
