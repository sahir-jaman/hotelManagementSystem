from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Room_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Room Page")
        self.root.geometry("1310x560+232+230")
        
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
        custTitle = Label(self.root, text="Room Booking", font=("Times new roman", 18, "bold"), fg="Gold", background="black", relief="solid")
        custTitle.place(x=0, y=0, width=1310, height=40)

        # ================== Logo image =====================
        img2 = Image.open(r"E:\python with vs code\python projects\Hotel management system\pictures\hotelLogo.jpg")
        img2 = img2.resize((100, 40))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        lblimage = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimage.place(x=0, y=0, width=60, height=40)
        
        # =================== customer Details Left Box =====================

        leftBox = LabelFrame(self.root, width=485, height=470, relief='solid',text='RoomBooking Details', fg='blue', font=("Times new roman", 14, "bold"), padx=2)
        leftBox.place(x=1, y=42, width=485, height=470)
        
        # =================== input lines & entries =================

        # Cutomer contact
        customerContact = Label(leftBox, text='Customer Contact', font=("Times new roman", 13, "bold"), padx=6, pady=3)
        customerContact.grid(row=0, column=0, sticky='w')
        customerContactEntry = ttk.Entry(leftBox, width=18, font=("Times new roman", 12,),foreground='blue')
        customerContactEntry.grid(row=0, column=1, sticky='w')
        
        FetchDataButton = Button(leftBox, text='Fetch Data',font=("arial", 9, "bold"),bg='black', fg='gold', width=8)
        FetchDataButton.grid(row=0,column=1, sticky='e')

        # Check-in Date
        checkInDate = Label(leftBox, text='Check-in Date', font=("Times new roman", 13, "bold"), padx=6, pady=3)
        checkInDate.grid(row=1, column=0, sticky='w')
        checkInDateEntry = ttk.Entry(leftBox, width=26, font=("Times new roman", 12), foreground='blue')
        checkInDateEntry.grid(row=1, column=1)

        # Check-out Date
        checkOutDate = Label(leftBox, text='Check-out Date', font=("Times new roman", 13, "bold"), padx=6, pady=3)
        checkOutDate.grid(row=2, column=0, sticky='w')
        checkOutDateEntry = ttk.Entry(leftBox, width=26, font=("Times new roman", 12), foreground='blue')
        checkOutDateEntry.grid(row=2, column=1)

        # Room Type
        roomType = Label(leftBox, text='Room Type', font=("Times new roman", 13, "bold"), padx=6, pady=3)
        roomType.grid(row=3, column=0, sticky='w')
        roomTypeEntry = ttk.Combobox(leftBox, width=22, values=['Bangladeshi', 'Indian', 'pakistani', 'others'], font=("Times new roman", 13))
        roomTypeEntry.grid(row=3, column=1)

        # Available Room
        availableRoom = Label(leftBox, text='Available Room', font=("Times new roman", 13, "bold"), padx=6, pady=3)
        availableRoom.grid(row=4, column=0, sticky='w')
        availableRoomEntry = ttk.Entry(leftBox, width=26, font=("Times new roman", 12), foreground='blue')
        availableRoomEntry.grid(row=4, column=1)

        # Meal
        meal = Label(leftBox, text='Meal', font=("Times new roman", 13, "bold"), padx=6, pady=3)
        meal.grid(row=5, column=0, sticky='w')
        mealEntry = ttk.Entry(leftBox,width=26, font=("Times new roman", 12), foreground='blue')
        mealEntry.grid(row= 5, column = 1)
        
        # numberOfDays
        numberOfDays = Label(leftBox, text='Number Of Days', font=("Times new roman", 13, "bold"), padx=6, pady=3)
        numberOfDays.grid(row=6, column=0, sticky='w')
        numberOfDaysEntry = ttk.Entry(leftBox,width=26, font=("Times new roman", 12), foreground='blue')
        numberOfDaysEntry.grid(row= 6, column = 1)
        
        # Meal
        paidTax = Label(leftBox, text='Paid Tax', font=("Times new roman", 13, "bold"), padx=6, pady=3)
        paidTax.grid(row=7, column=0, sticky='w')
        paidTaxEntry = ttk.Entry(leftBox,width=26, font=("Times new roman", 12), foreground='blue')
        paidTaxEntry.grid(row= 7, column = 1)
        
        # subTotal
        subTotal = Label(leftBox, text='Sub Total', font=("Times new roman", 13, "bold"), padx=6, pady=3)
        subTotal.grid(row=8, column=0, sticky='w')
        subTotalEntry = ttk.Entry(leftBox,width=26, font=("Times new roman", 12), foreground='blue')
        subTotalEntry.grid(row= 8, column = 1)
        
        # Meal
        TotalCost = Label(leftBox, text='Total Cost', font=("Times new roman", 13, "bold"), padx=6, pady=3)
        TotalCost.grid(row=9, column=0, sticky='w')
        TotalCostEntry = ttk.Entry(leftBox,width=26, font=("Times new roman", 12), foreground='blue')
        TotalCostEntry.grid(row= 9, column = 1)
        
        # ================ Footer ====================
        
        buttonBill = Button(leftBox, text='Bill', font=('arial', 10, 'bold'), width=11, relief='ridge', bg='black', fg='gold')
        buttonBill.grid(row=10, column=0, sticky=W)
        
        buttonFrame = Frame(leftBox, width=485, height=40, relief='solid', background='white')
        buttonFrame.place(x=0, y=395, width=478, height=40)

        # Button1
        buttonAdd = Button(buttonFrame, text='Add', font=('arial', 10, 'bold'), width=11, relief='ridge', bg='black', fg='gold')
        buttonAdd.grid(row=0, column=0)

        # Button2
        buttonAdd = Button(buttonFrame, text='Update', font=('arial', 10, 'bold'), width=11, relief='ridge', bg='black', fg='gold',)
        buttonAdd.grid(row=0, column=1)

        # Button3
        buttonAdd = Button(buttonFrame, text='Delete', font=('arial', 10, 'bold'), width=11, relief='ridge', bg='black', fg='gold')
        buttonAdd.grid(row=0, column=2)

        # Button4
        buttonAdd = Button(buttonFrame, text='Reset', font=('arial', 10, 'bold'), width=11, relief='ridge', bg='black', fg='gold')
        buttonAdd.grid(row=0, column=3)
        
        # ========================== Search system ===========================1310x560 width=485,height=470
        rightSlideFrame = LabelFrame(self.root, text='View Details and Search System', font=('arial', 12, 'bold'), fg='blue', width=820, height=470, relief='solid')
        rightSlideFrame.place(x=490, y=260, width=820, height=253)

        searchByLabel = Label(rightSlideFrame, text='Search By:', background='black', fg='gold', font=('arial', 11, 'bold'), width=10, height=1, relief='solid', padx=6)
        searchByLabel.grid(row=0, column=0, padx=5)
        self.searchVar = StringVar()
        searchByEntry = ttk.Combobox(rightSlideFrame,textvariable=self.searchVar, values=['Contact', 'Room'], width=20, state='readonly')
        searchByEntry.grid(row=0, column=1, padx=5)

        self.textSearch = StringVar()
        randomTextinput = ttk.Entry(rightSlideFrame,textvariable=self.textSearch, width=18, font=('arial', 12, 'bold'))
        randomTextinput.grid(row=0, column=2, padx=5)
        
        
        # ========================= inside Label Frame =====================
        details_table = LabelFrame(rightSlideFrame, width=810, height=185, relief='solid')
        details_table.place(x=2, y=50, width=810, height=185)

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

        # 2Buttons
        searchButton = Button(rightSlideFrame, text='Search', background='black',fg='gold', font=('arial', 10, 'bold'), width=10)
        searchButton.grid(row=0, column=3, padx=2)
        searchButton2 = Button(rightSlideFrame, text='Show All',background='black', fg='gold', font=('arial', 10, 'bold'), width=10)
        searchButton2.grid(row=0, column=4, padx=2)
        
        # right side room image
        imgRoom = Image.open(r"E:\python with vs code\python projects\Hotel management system\pictures\room1.jpg")
        imgRoom = imgRoom.resize((450, 220))
        self.photoimgRoom = ImageTk.PhotoImage(imgRoom)
        
        lblimage = Label(self.root, image=self.photoimgRoom, bd=2, relief='solid')
        lblimage.place(x=860, y=40, width=450, height=220)
        
        # right side information box
        infoBox = LabelFrame(root, text='Customer info', font=("Times new roman",10, "bold"), relief='solid')
        infoBox.place(x=492, y=40, width=380, height=220)
        
        custName = Label(infoBox, text="Name: ").grid(row=0, column=0, padx=5, pady=5)
        custNameEntry = ttk.Entry(infoBox, width=26, font=("Times new roman", 12,), foreground='blue')
        custNameEntry.grid(row=0, column=1)
        
        custGender = Label(infoBox, text="Gender: ").grid(row=1, column=0, padx=5, pady=5)
        custGenderEntry = ttk.Entry(infoBox, width=26, font=("Times new roman", 12,), foreground='blue')
        custGenderEntry.grid(row=1, column=1)
        
        custEmail = Label(infoBox, text="Email: ").grid(row=2, column=0, padx=5, pady=5)
        custEmailEntry = ttk.Entry(infoBox, width=26, font=("Times new roman", 12,), foreground='blue')
        custEmailEntry.grid(row=2, column=1)
        
        custAddress = Label(infoBox, text="Address: ").grid(row=3, column=0, padx=5, pady=5)
        custAddressEntry = ttk.Entry(infoBox, width=26, font=("Times new roman", 12,), foreground='blue')
        custAddressEntry.grid(row=3, column=1)
        
        custNationality = Label(infoBox, text="Nationality: ").grid(row=4, column=0, padx=5, pady=5)
        custNationalityEntry = ttk.Entry(infoBox, width=26, font=("Times new roman", 12,), foreground='blue')
        custNationalityEntry.grid(row=4, column=1)
        
        
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
    obj = Room_win(root)
    root.mainloop()