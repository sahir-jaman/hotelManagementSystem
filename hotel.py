from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_win
from room import Room_win

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        
        # ================== 1st image =====================
        img1 = Image.open(r"E:\python with vs code\python projects\Hotel management system\pictures\hotel2.png")
        img1 = img1.resize((1556,140))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimage = Label(self.root, image=self.photoimg1, bd = 4, relief= RIDGE)
        lblimage.place(x=0,y=0,width=1550,height=140)

        # ================== Logo image =====================
        img2 = Image.open(r"E:\python with vs code\python projects\Hotel management system\pictures\hotelLogo.jpg")
        img2 = img2.resize((230,140))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimage = Label(self.root, image=self.photoimg2, bd = 4, relief= RIDGE)
        lblimage.place(x=0,y=0,width=230,height=140)

        #=================== Title ========================
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 34, "bold"), bg = "black", fg="gold",bd = 4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #=================== main frame ========================
        mainFrame = Label(self.root, bd=4, relief=RIDGE)
        mainFrame.place(x=0,y=190,width=1550,height=620)

        # ==================== Menue ========================
        lbl_menue = Label(mainFrame, text="Menue", font=("times new roman", 15, "bold"), bg = "black", fg="Red", relief=RIDGE)
        lbl_menue.place(x=0,y=0,width=225)

        #=================== button frame ========================
        btn_frame = Frame(mainFrame, bd=4, relief=RIDGE)
        btn_frame.place(x=0,y=35,width=225,height=220)

        #=================== buttons ========================
        btn_1 = Button(btn_frame,text="Customer", command=self.cust_details,width=15,font=("times new roman", 14, "bold"), bg = "black", fg="gold", relief=RIDGE)
        btn_1.grid(row=0,column=0)

        btn_2 = Button(btn_frame,text="Room", command=self.room_details, width=15,font=("times new roman", 14, "bold"), bg = "black", fg="gold", relief=RIDGE)
        btn_2.grid(row=1,column=0)

        btn_3 = Button(btn_frame,text="Details",width=15,font=("times new roman", 14, "bold"), bg = "black", fg="gold", relief=RIDGE)
        btn_3.grid(row=2,column=0)

        btn_4 = Button(btn_frame,text="Report",width=15,font=("times new roman", 14, "bold"), bg = "black", fg="gold", relief=RIDGE)
        btn_4.grid(row=3,column=0)

        btn_5 = Button(btn_frame,text="Logout",width=15,font=("times new roman", 14, "bold"), bg = "black", fg="gold", relief=RIDGE)
        btn_5.grid(row=4,column=0)

        # ============================ right slide image =============================

        img3 = Image.open(r"E:\python with vs code\python projects\Hotel management system\pictures\hotelDoor.jpg")
        img3 = img3.resize((1350,590))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimage = Label(mainFrame, image=self.photoimg3, bd = 4, relief= RIDGE)
        lblimage.place(x=226,y=0,width=1350,height=590)

        # ========================== 2 mini left images ===============================

        img4 = Image.open(r"E:\python with vs code\python projects\Hotel management system\pictures\room1.jpg")
        img4 = img4.resize((230,190))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimage = Label(mainFrame, image=self.photoimg4, bd = 4, relief= RIDGE)
        lblimage.place(x=0,y=250,width=230, height=190)


        img5 = Image.open(r"E:\python with vs code\python projects\Hotel management system\pictures\hotelDoor.jpg")
        img5 = img5.resize((230,190))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimage = Label(mainFrame, image=self.photoimg5, bd = 4, relief= RIDGE)
        lblimage.place(x=0,y=420,width=230, height=190)
        
    def cust_details(self):
        Cust_win(Toplevel(self.root))
    def room_details(self):
        Room_win(Toplevel(self.root))

        

if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()