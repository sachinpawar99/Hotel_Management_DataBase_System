from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import Databasehotel
import datetime
import  time
from datetime import datetime, timedelta
#FrontEnd

class Hotel:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Database Management System")
        self.root.geometry("1350x800+0+0")

        MainFrame=Frame(self.root)
        MainFrame.grid()
        TopFrame=Frame(MainFrame,bd=10,width=1350,height=550,padx=2,relief=RIDGE)
        TopFrame.pack(side=TOP)

        LeftFrame = Frame(TopFrame, bd=5, width=400, height=550, relief=RIDGE)
        LeftFrame.pack(side=LEFT)

        RightFrame = Frame(TopFrame, bd=5, width=820, height=550, relief=RIDGE)
        RightFrame.pack(side=RIGHT)

        RightFrame1 = Frame(RightFrame, bd=5, width=800, height=50,padx=10, relief=RIDGE)
        RightFrame1.grid(row=0,column=0)
        RightFrame2 = Frame(RightFrame, bd=5, width=800, height=100,padx=3, relief=RIDGE)
        RightFrame2.grid(row=1,column=0)
        RightFrame3 = Frame(RightFrame, bd=5, width=800, height=400,padx=4, relief=RIDGE)
        RightFrame3.grid(row=3,column=0)

        ButtonFrame=Frame(MainFrame,bd=10,width=1350,height=150,padx=2,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        global hd

        CusID=StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        Address = StringVar()
        PostCode= StringVar()
        Mobile = StringVar()
        Email = StringVar()
        Nationality = StringVar()
        DOB = StringVar()
        ProveID = StringVar()
        Gender = StringVar()
        DateIn = StringVar()
        DateOut = StringVar()
        Meal = StringVar()
        RoomType = StringVar()
        RoomNo = StringVar()
        RoomExtNo = StringVar()
        TotalCost = StringVar()
        SubTotal = StringVar()
        PaidTax=StringVar()
        TotalDays=StringVar()

        DateIn.set(time.strftime("%d/%m/%Y"))
        DateOut.set(time.strftime("%d/%m/%Y"))

        x=random.randint(1190,8746)
        randref=str(x)
        CusID.set("Hotel"+randref)

        def iExit():
            iExit=tkinter.messagebox.askyesno("Hotel Database Management System","Confirm if you want Exit")
            if iExit>0:
                root.destroy()

        def Reset():
            Meal.set("")
            RoomExtNo.set("")
            RoomNo.set("")
            RoomType.set("")
            TotalCost.set("")
            ProveID.set("")
            TotalDays.set("")

            self.txtDOB.delete(0,END)
            self.txtFirstName.delete(0,END)
            self.txtLastName.delete(0, END)
            self.txtCuId.delete(0, END)
            self.txtAddress.delete(0, END)
            self.txtPostCode.delete(0, END)
            self.txtEmail.delete(0, END)
            self.txtMobile.delete(0, END)
            self.txtSubTotal.delete(0, END)
            self.txtTotal.delete(0, END)
            self.txtDateIn.delete(0, END)
            self.txtDateOut.delete(0, END)
            self.txtPaidTax.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtNationality.delete(0, END)

            DateIn.set(time.strftime("%d/%m/%Y"))
            DateOut.set(time.strftime("%d/%m/%Y"))

            x = random.randint(1190, 8746)
            randref = str(x)
            CusID.set("Hotel" + randref)

        def addData():
            if(len(CusID.get())!=0):
                Databasehotel.addHotelRec(CusID.get(),Firstname.get(),
                Lastname.get(),Address.get(),Gender.get(),Mobile.get(),Nationality.get(),ProveID.get(),
                                DateIn.get(),DateOut.get(),Email.get())
                lstHotel.delete(0,END)
                lstHotel.insert(END,(CusID.get(),Firstname.get(),Lastname.get(),Address.get(),Gender.get(),Mobile.get(),Nationality.get(),ProveID.get(),
                                DateIn.get(),DateOut.get(),Email.get()))

        def DisplayData():
            lstHotel.delete(0,END)
            for row in Databasehotel.viewData():
                lstHotel.insert(END,row,str(""))

        def HotelRec(event=None):
            global hd

            searchHdDb=lstHotel.curselection()[0]
            hd=lstHotel.get(searchHdDb)

            self.txtCuId.delete(0,END)
            self.txtCuId.insert(END,hd[1])
            self.txtFirstName.delete(0,END)
            self.txtFirstName.insert(END,hd[2])
            self.txtLastName.delete(0,END)
            self.txtLastName.insert(END,hd[3])
            self.txtAddress.delete(0,END)
            self.txtAddress.insert(END,hd[4])
            self.txtGender.delete(0,END)
            self.txtGender.insert(END,hd[5])
            self.txtMobile.delete(0,END)
            self.txtMobile.insert(END,hd[6])
            self.txtNationality.delete(0,END)
            self.txtNationality.insert(END,hd[7])
            self.cboProveID.delete(0,END)
            self.cboProveID.insert(END,hd[8])
            self.txtDateIn.delete(0,END)
            self.txtDateIn.insert(END,hd[9])
            self.txtDateOut.delete(0,END)
            self.txtDateOut.insert(END,hd[10])
            self.txtEmail.delete(0,END)
            self.txtEmail.insert(END,hd[11])

        def DeleteData():
            if(len(CusID.get())!=0):
                Databasehotel.deleteRec(hd[0])
                Reset()
                DisplayData()

        def searchDatabase():
            lstHotel.delete(0,END)
            for row in Databasehotel.searchData(CusID.get(),Firstname.get(),
                Lastname.get(),Address.get(),Gender.get(),Mobile.get(),Nationality.get(),ProveID.get(),
                                DateIn.get(),DateOut.get(),Email.get()):
                lstHotel.insert(END,row,str(""))

        def Update():
            if(len(CusID.get())!=0):
                Databasehotel.deleteRec(hd[0])
            if(len(CusID.get())!=0):
                Databasehotel.addHotelRec(CusID.get(), Firstname.get(),
                                       Lastname.get(), Address.get(), Gender.get(), Mobile.get(), Nationality.get(),
                                       ProveID.get(),
                                       DateIn.get(), DateOut.get(), Email.get())
                lstHotel.delete(0, END)
                lstHotel.insert(END,(CusID.get(), Firstname.get(),
                                Lastname.get(), Address.get(), Gender.get(), Mobile.get(), Nationality.get(),
                                ProveID.get(),
                                DateIn.get(), DateOut.get(), Email.get()))

        def TotalCostandAddData():
            addData()

            InDate=DateIn.get()
            OutDate=DateOut.get()
            InDate=datetime.strptime(InDate,"%d/%m/%Y")
            OutDate=datetime.strptime(OutDate,"%d/%m/%Y")
            TotalDays.set(abs((OutDate-InDate).days))

            if(Meal.get()=="Breakfast" and RoomType.get()=="Single"):
                print("Sachin")
                q1=float(17)
                q2=float(34)
                q3=float(TotalDays.get())
                q4=float(q1+q2)
                q5=float(q3*q4)
                Tax="$"+str("%.2f"%((q5)*0.09))
                ST = "$" + str("%.2f" % ((q5)))
                TT="$"+str("%.2f"%(q5+((q5)*0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)

            elif (Meal.get() == "Breakfast" and RoomType.get() == "Double"):
                q1 = float(35)
                q2 = float(44)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "$" + str("%.2f" % ((q5) * 0.09))
                ST = "$" + str("%.2f" % ((q5)))
                TT = "$" + str("%.2f" % (q5 + ((q5) * 0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
                print(Tax," ",ST," ",TT)

            elif (Meal.get() == "Breakfast" and RoomType.get() == "Family"):
                q1 = float(45)
                q2 = float(63)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "$" + str("%.2f" % ((q5) * 0.09))
                ST = "$" + str("%.2f" % ((q5)))
                TT = "$" + str("%.2f" % (q5 + ((q5) * 0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)

            elif (Meal.get() == "Lunch" and RoomType.get() == "Single"):
                q1 = float(29)
                q2 = float(37)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "$" + str("%.2f" % ((q5) * 0.09))
                ST = "$" + str("%.2f" % ((q5)))
                TT = "$" + str("%.2f" % (q5 + ((q5) * 0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)

            elif (Meal.get() == "Lunch" and RoomType.get() == "Double"):
                q1 = float(37)
                q2 = float(43)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "$" + str("%.2f" % ((q5) * 0.09))
                ST = "$" + str("%.2f" % ((q5)))
                TT = "$" + str("%.2f" % (q5 + ((q5) * 0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)

            elif(Meal.get()=="Lunch" and RoomType.get()=="Family"):
                q1=float(20)
                q2=float(37)
                q3=float(TotalDays.get())
                q4=float(q1+q2)
                q5=float(q3*q4)
                Tax="$"+str("%.2f"%((q5)*0.09))
                ST = "$" + str("%.2f" % ((q5)))
                TT="$"+str("%.2f"%(q5+((q5)*0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)

            elif (Meal.get() == "Dinner" and RoomType.get() == "Single"):
                q1 = float(29)
                q2 = float(37)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "$" + str("%.2f" % ((q5) * 0.09))
                ST = "$" + str("%.2f" % ((q5)))
                TT = "$" + str("%.2f" % (q5 + ((q5) * 0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)

            elif (Meal.get() == "Dinner" and RoomType.get() == "Double"):
                q1 = float(30)
                q2 = float(43)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "$" + str("%.2f" % ((q5) * 0.09))
                ST = "$" + str("%.2f" % ((q5)))
                TT = "$" + str("%.2f" % (q5 + ((q5) * 0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)

            elif (Meal.get() == "Dinner" and RoomType.get() == "Family"):
                q1 = float(43)
                q2 = float(67)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "$" + str("%.2f" % ((q5) * 0.09))
                ST = "$" + str("%.2f" % ((q5)))
                TT = "$" + str("%.2f" % (q5 + ((q5) * 0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)

        #=================================================================Widget==================================================
        self.lblCuId=Label(LeftFrame,font=("arial",12,"bold"),text="Customer Ref:",padx=1)
        self.lblCuId.grid(row=0,column=0,sticky=W)
        self.txtCuId = Entry(LeftFrame, font=("arial", 12, "bold"),width=18,textvariable=CusID)
        self.txtCuId.grid(row=0, column=1,pady=3,padx=20)

        self.lblFirstName = Label(LeftFrame, font=("arial", 12, "bold"), text="FirstName:", padx=1)
        self.lblFirstName.grid(row=1, column=0, sticky=W)
        self.txtFirstName = Entry(LeftFrame, font=("arial", 12, "bold"), width=18,textvariable=Firstname)
        self.txtFirstName.grid(row=1, column=1, pady=3, padx=20)

        self.lblLastName = Label(LeftFrame, font=("arial", 12, "bold"), text="LastName:", padx=1)
        self.lblLastName.grid(row=2, column=0, sticky=W)
        self.txtLastName = Entry(LeftFrame, font=("arial", 12, "bold"), width=18,textvariable=Lastname)
        self.txtLastName.grid(row=2, column=1, pady=3, padx=20)

        self.lblAddress = Label(LeftFrame, font=("arial", 12, "bold"), text="Address:", padx=1,pady=2)
        self.lblAddress.grid(row=3, column=0, sticky=W)
        self.txtAddress = Entry(LeftFrame, font=("arial", 12, "bold"), textvariable=Address,width=18)
        self.txtAddress.grid(row=3, column=1, pady=3, padx=20)

        self.lblDOB = Label(LeftFrame, font=("arial", 12, "bold"), text="Date of Birth:", padx=2,pady=2)
        self.lblDOB.grid(row=4, column=0, sticky=W)
        self.txtDOB = Entry(LeftFrame, font=("arial", 12, "bold"), width=18,textvariable=DOB)
        self.txtDOB.grid(row=4, column=1, pady=3, padx=20)

        self.lblPostCode = Label(LeftFrame, font=("arial", 12, "bold"), text="PostCode:", padx=2,pady=2)
        self.lblPostCode.grid(row=5, column=0, sticky=W)
        self.txtPostCode = Entry(LeftFrame, font=("arial", 12, "bold"),textvariable=PostCode, width=18)
        self.txtPostCode.grid(row=5, column=1, pady=3, padx=20)

        self.lblMobile = Label(LeftFrame, font=("arial", 12, "bold"), text="Mobile:",pady=2, padx=2)
        self.lblMobile.grid(row=6, column=0, sticky=W)
        self.txtMobile = Entry(LeftFrame, textvariable=Mobile,font=("arial", 12, "bold"), width=18)
        self.txtMobile.grid(row=6, column=1, pady=3, padx=20)

        self.lblEmail = Label(LeftFrame, font=("arial", 12, "bold"), text="Email:",pady=2, padx=2)
        self.lblEmail.grid(row=7, column=0, sticky=W)
        self.txtEmail = Entry(LeftFrame,textvariable=Email, font=("arial", 12, "bold"), width=18)
        self.txtEmail.grid(row=7, column=1, pady=3, padx=20)

        self.lblNationality = Label(LeftFrame, font=("arial", 12, "bold"), text="Nationality:", pady=2, padx=2)
        self.lblNationality.grid(row=8, column=0, sticky=W)
        self.txtNationality = Entry(LeftFrame, textvariable=Nationality,font=("arial", 12, "bold"), width=18)
        self.txtNationality.grid(row=8, column=1, pady=3, padx=20)

        self.lblGender = Label(LeftFrame, font=("arial", 12, "bold"), text="Gender:", pady=2, padx=2)
        self.lblGender.grid(row=9, column=0, sticky=W)
        self.txtGender = Entry(LeftFrame,textvariable=Gender, font=("arial", 12, "bold"), width=18)
        self.txtGender.grid(row=9, column=1, pady=3, padx=20)

        self.lblDateIn = Label(LeftFrame, font=("arial", 12, "bold"), text="Check In Date:", pady=2, padx=1)
        self.lblDateIn.grid(row=10, column=0, sticky=W)
        self.txtDateIn = Entry(LeftFrame,textvariable=DateIn, font=("arial", 12, "bold"), width=18)
        self.txtDateIn.grid(row=10, column=1, pady=3, padx=20)

        self.lblDateOut = Label(LeftFrame, font=("arial", 12, "bold"), text="Check Out Date:", pady=2, padx=1)
        self.lblDateOut.grid(row=11, column=0, sticky=W)
        self.txtDateOut = Entry(LeftFrame,textvariable=DateOut, font=("arial", 12, "bold"), width=18)
        self.txtDateOut.grid(row=11, column=1, pady=3, padx=20)

        self.lblProveID= Label(LeftFrame, font=("arial", 12, "bold"), text="Type of ID:", pady=2, padx=1)
        self.lblProveID.grid(row=12, column=0, sticky=W)
        self.cboProveID=ttk.Combobox(LeftFrame,textvariable=ProveID,state="readonly",font=("arial", 12, "bold"),width=16)
        self.cboProveID['value']=(' ','Pilot Lincence',"Driving Lincence","Student ID","Passport")
        self.cboProveID.current(0)
        self.cboProveID.grid(row=12,column=1,pady=3,padx=2)

        self.lblMeal = Label(LeftFrame, font=("arial", 12, "bold"), text="Meal:", pady=2, padx=1)
        self.lblMeal.grid(row=13, column=0, sticky=W)
        self.cboMeal = ttk.Combobox(LeftFrame,textvariable=Meal, state="readonly", font=("arial", 12, "bold"), width=16)
        self.cboMeal['value'] = (' ', 'Breakfast', "Lunch", "Dinner")
        self.cboMeal.current(0)
        self.cboMeal.grid(row=13, column=1, pady=3, padx=2)

        self.lblRoomType = Label(LeftFrame, font=("arial", 12, "bold"), text="Room Type:", pady=2, padx=2)
        self.lblRoomType.grid(row=14, column=0, sticky=W)
        self.cboRoomType = ttk.Combobox(LeftFrame, textvariable=RoomType,state="readonly", font=("arial", 12, "bold"), width=16)
        self.cboRoomType['value'] = (' ', 'Single', "Double", "Family")
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14, column=1, pady=3, padx=2)

        self.lblRoomNo = Label(LeftFrame, font=("arial", 12, "bold"), text="Room No:", pady=2, padx=2)
        self.lblRoomNo.grid(row=15, column=0, sticky=W)
        self.cboRoomNo = ttk.Combobox(LeftFrame,textvariable=RoomNo, state="readonly", font=("arial", 12, "bold"), width=16)
        self.cboRoomNo['value'] = (' ', '001', "002", "003","004","005","006")
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row=15, column=1, pady=3, padx=2)

        self.lblRoomExtNo = Label(LeftFrame, font=("arial", 12, "bold"), text="Room Ext No:", pady=2, padx=2)
        self.lblRoomExtNo.grid(row=16, column=0, sticky=W)
        self.cboRoomExtNo = ttk.Combobox(LeftFrame, textvariable=RoomExtNo,state="readonly", font=("arial", 12, "bold"), width=16)
        self.cboRoomExtNo['value'] = (' ', '101', "102", "103","104","105","106")
        self.cboRoomExtNo.current(0)
        self.cboRoomExtNo.grid(row=16, column=1, pady=3, padx=2)
#===================================Label=============================================================================================================
        self.lblLabel = Label(RightFrame1, font=("arial", 10, "bold"), text="Customer Ref\tFirstname\tLastName\Address\tGender\tMobile\tNationality"
                                    "\tProveOfID\tDateIn\tDateOut\t\tEmail:",
                              pady=10, padx=6)
        self.lblLabel.grid(row=0, column=0, columnspan=17)

        scrollbar=Scrollbar(RightFrame2)
        scrollbar.grid(row=0,column=0,sticky="ns")
        lstHotel=Listbox(RightFrame2,width=103,height=14,font=("arial", 12, "bold"),yscrollcommand=scrollbar.set)
        lstHotel.bind('<<ListboxSelect>>',HotelRec)
        lstHotel.grid(row=0,column=0,padx=7,sticky="nsew")
        scrollbar.config(command=lstHotel.xview)
#==========================Widget=====================================================================================
        self.lblDay=Label(RightFrame3,font=("arial",12,"bold"),text="No of days:",padx=2,pady=2)
        self.lblDay.grid(row=0,column=0,sticky=W)
        self.txtDay = Entry(RightFrame3, font=("arial", 12, "bold"), textvariable=TotalDays,width=76)
        self.txtDay.grid(row=0, column=1, pady=3, padx=20)

        self.lblPaidTax = Label(RightFrame3, font=("arial", 12, "bold"), text="Paid Tax:", padx=2, pady=2)
        self.lblPaidTax.grid(row=1, column=0, sticky=W)
        self.txtPaidTax = Entry(RightFrame3, font=("arial", 12, "bold"), width=76,textvariable=PaidTax)
        self.txtPaidTax.grid(row=1, column=1, pady=3, padx=20)

        self.lblSubTotal = Label(RightFrame3, font=("arial", 12, "bold"), text="Subtotal:", padx=2, pady=2)
        self.lblSubTotal.grid(row=2, column=0, sticky=W)
        self.txtSubTotal = Entry(RightFrame3, font=("arial", 12, "bold"), width=76,textvariable=SubTotal)
        self.txtSubTotal.grid(row=2, column=1, pady=3, padx=20)

        self.lblTotal = Label(RightFrame3, font=("arial", 12, "bold"), text="Total Cost:", padx=2, pady=2)
        self.lblTotal.grid(row=3, column=0, sticky=W)
        self.txtTotal = Entry(RightFrame3, font=("arial", 12, "bold"), width=76,textvariable=TotalCost)
        self.txtTotal.grid(row=3, column=1, pady=3, padx=20)

# ==========================Button=====================================================================================
        self.btntotalandAddData=Button(ButtonFrame, font=("arial", 16, "bold"), bd=4,
                                    width=13,height=2,text="AddNew/Total",command=TotalCostandAddData)
        self.btntotalandAddData.grid(row=0, column=0, padx=4,pady=1)

        self.btnDisplay = Button(ButtonFrame, font=("arial", 16, "bold"), bd=4,
                                      width=13, height=2, text="Display",command=DisplayData)
        self.btnDisplay.grid(row=0, column=1, padx=4, pady=1)

        self.btnUpdate = Button(ButtonFrame, font=("arial", 16, "bold"), bd=4,
                                      width=13, height=2, text="Update",command=Update)
        self.btnUpdate.grid(row=0, column=2, padx=4, pady=1)

        self.btnDelete = Button(ButtonFrame, font=("arial", 16, "bold"), bd=4,
                                      width=13, height=2, text="Delete:",command=DeleteData)
        self.btnDelete.grid(row=0, column=3, padx=4, pady=1)

        self.btnSearch = Button(ButtonFrame, font=("arial", 16, "bold"), bd=4,
                                      width=13, height=2, text="Search",command=searchDatabase)
        self.btnSearch.grid(row=0, column=4, padx=4, pady=1)

        self.btnreset = Button(ButtonFrame, font=("arial", 16, "bold"), bd=4,
                                      width=13, height=2, text="Reset:",command=Reset)
        self.btnreset.grid(row=0, column=5, padx=4, pady=1)

        self.btnExit = Button(ButtonFrame, font=("arial", 16, "bold"), bd=4,
                                      width=13, height=2, text="Exit:",command=iExit)
        self.btnExit.grid(row=0, column=6, padx=4, pady=1)


if __name__ == '__main__':
    root =Tk()
    application=Hotel(root)
    root.mainloop()



