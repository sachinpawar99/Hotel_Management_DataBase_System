#BackEnd
import sqlite3

def hotelData():
    con=sqlite3.connect("booking.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF  NOT EXISTS hotel (id INTEGER PRIMARY KEY,CusID TEXT,Firstname text,lastname text, Address text,Gender text,Mobile text, Nationality text,\
    ProveID text,DateIn text,DateOut text,Email text)")
    con.commit()
    con.close()

def addHotelRec(CusID,Firstname,lastname, Address ,Gender ,Mobile , Nationality ,
         ProveID ,DateIn ,DateOut ,Email):
    con=sqlite3.connect("booking.db")
    cur=con.cursor()
    cur.execute("Insert into hotel values (NULL,?,? ,?,? ,?,? ,?,?, ?,? ,?)", \
                ( CusID, Firstname, lastname, Address, Gender, Mobile, Nationality,
                ProveID, DateIn, DateOut, Email))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("booking.db")
    cur = con.cursor()
    cur.execute("Select * from hotel")
    row=cur.fetchall()
    con.close()
    return  row

def deleteRec(id):
    con = sqlite3.connect("booking.db")
    cur = con.cursor()
    cur.execute("Delete from  hotel where id=?",(id,))
    con.commit()
    con.close()

def searchData(CusID="",Firstname="",lastname="", Address="" ,Gender="" ,Mobile="" , Nationality ="",
         ProveID="" ,DateIn="" ,DateOut="" ,Email=""):
    con = sqlite3.connect("booking.db")
    cur = con.cursor()
    cur.execute("Select * from hotel where CusID=? or Firstname=? or lastname=? or  Address=? or Gender=? or Mobile=? or  Nationality=? or \
    ProveID=? or DateIn=? or  DateOut=? or  Email=?",\
                (CusID, Firstname, lastname, Address, Gender, Mobile, Nationality,
                ProveID, DateIn, DateOut, Email))
    row=cur.fetchall()
    con.close()
    return  row

def dataUpdate(id,CusID="",Firstname="",lastname="", Address="" ,Gender="" ,Mobile="" , Nationality ="",
         ProveID="" ,DateIn="" ,DateOut="" ,Email=""):
    con = sqlite3.connect("booking.db")
    cur = con.cursor()
    cur.execute("Update hotel set CusID=?,Firstname=?,lastname=?, Address=? ,Gender=? ,Mobile=? , Nationality=?,\
              ProveID=? ,DateIn=? ,DateOut=? ,Email=? where id=?",\
                (CusID, Firstname, lastname, Address, Gender, Mobile, Nationality,
                ProveID, DateIn, DateOut, Email,id))
    con.commit()
    con.close()

hotelData()




