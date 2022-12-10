#from logging import root
from email.mime import message
import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
import sqlite3
from tkcalendar import DateEntry
# انشاء قاعدة بيانات والاتصال بها
db = sqlite3.connect("preson.db")
cr = db.cursor() 
class date:
    def __init__(self, year, month, day):
        if int(year) > 1960 and int(year) < datetime.datetime.now().year:
            self.__year = year
        else:
            #print("the year must be in range from 1950 to now")
            raise Exception("the year must be in range from 1950 to now")
        if int(month) > 0 and int(month) < 13:
            self.__month = month
        else:
            raise Exception("the month must be in range from 1 to 12")
            print("the month must be in range from 1 to 12")
        if int(day) > 0 and int(day) < 32:
            self.__day = day
        else:
            raise Exception("the day must be in range from 1 to 31")
            #print("the day must be in range from 1 to 31")

    def getYear(self):
        return self.__year

    def getMonth(self):
        return self.__month

    def getDay(self):
        return self.__day

    def alDate(self):
        return self.getYear()+str("-")+self.getMonth()+str("-")+self.getDay()


class Person:
    def __init__(self, Id, firstName, father, lastName, gender, birthYear, address):
        if Id > 0:
            self.__Id = Id
        else:
            raise Exception("Error value must be Size greater than zero")
        if len(firstName) > 1:
            self.__firstName = firstName
        else:
            raise Exception("The First Name must be greater than a character")
        if len(father) > 1:
            self.__father = father
        else:
            raise Exception("The Name Father must be greater than a character")
        if len(lastName) > 1:
            self.__lastName = lastName
        else:
            raise Exception("The Last Name must be greater than a character")
        if gender in ("male", "female", "Mail", "Female"):
            self.__gender = gender
        else:
            raise Exception("The gender must be male or female")
        # if birthYear > 1950 and birthYear < 2020:
        #     self.__birthYear = birthYear
        # else:
        #     raise Exception("Birth date must be between 1950 and 2020")
        if len(address) > 1:
            self.__address = address
        else:
            raise Exception("The Address must be greater than a character")

    def setFirstName(self, newFirstName):
        if len(newFirstName) > 1:
            self.__firstName = newFirstName
        else:
            raise Exception("The First Name must be greater than a character")

    def getId(self):
        return self.__Id

    def setId(self, newId):
        if newId > 0:
            self.__Id = newId
        else:
            raise Exception("Error value must be Size greater than zero")

    def getFirstName(self):
        return self.__firstName

    def setFather(self, newFather):
        if len(newFather) > 1:
            self.__fathera = newFather
        else:
            raise Exception("The Father Name must be greater than a character")

    def getFather(self):
        return self.__father

    def setlastName(self, newlastName):
        if len(newlastName) > 1:
            self.__lastName = newlastName
        else:
            raise Exception("The Last Name must be greater than a character")

    def getLastName(self):
        return self.__lastName

    def setGender(self, newGender):
        if newGender in ("male", "female", "Mail", "Female"):
            self.__gender = newGender
        else:
            raise Exception("The gender must be male or female")

    def getGender(self):
        return self.__gender

    def getBirthYear(self):
        return self.__birthYear

    def setAddress(self, newAddress):
        if len(newAddress) > 1:
            self.__address = newAddress
        else:
            raise Exception("The Address be greater than a character")

    def getAddress(self):
        return self.__address


class Dungeon:
    def __init__(self, Id, Name, size):
        if Id > 0:
            self.__Id = Id
        else:
            raise Exception("Error value must be Size greater than zero")
        if len(Name) > 1:
            self.__Name = Name
        else:
            raise Exception("The Name must be greater than a character")
        if size > 0:
            self.__size = size
        else:
            raise Exception("Error value must be Size greater than zero")

    def getId(self):
        return self.__Id

    def setId(self, newId):
        if newId > 0:
            self.__Id = newId
        else:
            raise Exception("Error value must be Size greater than zero")

    def setName(self, newName):
        if len(newName) > 1:
            self.__Name = newName
        else:
            raise Exception("The Name must be greater than a character")

    def getName(self):
        return self.__Name

    def setSize(self, newSize):
        if newSize > 0:
            self.__size = newSize
        else:
            raise Exception("Error value must be Size greater than zero")

    def getSize(self):
        return self.__size


class Offense:
    def __init__(self, Id, Name):
        if Id > 0:
            self.__Id = Id
        else:
            raise Exception("Error value must be Size greater than zero")
        if len(Name) > 1:
            self.__Name = Name
        else:
            raise Exception("The Name must be greater than a character")

    def getId(self):
        return self.__Id

    def setId(self, newId):
        if newId > 0:
            self.__Id = newId
        else:
            raise Exception("Error value must be Size greater than zero")

    def setName(self, newName):
        if len(newName) > 1:
            self.__Name = newName
        else:
            raise Exception("The Name must be greater than a character")

    def getName(self):
        return self.__Name
    

class Convicts:
    def __init__(self, Id, fromDate, toDate, personId, offenseId):
        if Id > 0:
            self.__Id = Id
        else:
            raise Exception("Error value must be Size greater than zero")
        if personId > 0:
            self.__personId = personId
        else:
            raise Exception("Error value must be Person Id greater than zero")
        if offenseId > 0:
            self.__offenseId = offenseId
        else:
            raise Exception("Error value must be Offense Id greater than zero")
        self.__fromDate = fromDate
        self.__toDate = toDate

    def getFromDate(self):
        return self.__fromDate

    def setFromDate(self, newFromDate):
        self.__fromDate = newFromDate

    def getToDate(self):
        return self.__toDate

    def setToDate(self, newTomDate):
        self.__toDate = newTomDate

    def getId(self):
        return self.__Id

    def setId(self, newId):
        if newId > 0:
            self.__Id = newId
        else:
            raise Exception("Error value must be Size greater than zero")

    def setPersonId(self, newPersonId):
        if newPersonId > 0:
            self.__personId = newPersonId
        else:
            raise Exception("Error value must be Person Id greater than zero")

    def getPersonId(self):
        return self.__personId

    def setOffenseId(self, newOffenseId):
        if newOffenseId > 0:
            self.__offenseId = newOffenseId
        else:
            raise Exception("Error value must be Offense Id greater than zero")

    def getOffenseId(self):
        return self.__offenseId


class DungeonMoves:
    def __init__(self, Id, dungeonId, personId, fromDate):
        if Id > 0:
            self.__Id = Id
        else:
            raise Exception("Error value must be Size greater than zero")
        if dungeonId > 0:
            self.__dungeonId = dungeonId
        else:
            raise Exception("Error value must be Dungeon Id greater than zero")
        if personId > 0:
            self.__personId = personId
        else:
            raise Exception("Error value must be Person Id greater than zero")
        self.__fromDate = fromDate

    def getId(self):
        return self.__Id

    def setId(self, newId):
        if newId > 0:
            self.__Id = newId
        else:
            raise Exception("Error value must be Size greater than zero")

    def setPersonId(self, newPersonId):
        if newPersonId > 0:
            self.__personId = newPersonId
        else:
            raise Exception("Error value must be Person Id greater than zero")

    def getPersonId(self):
        return self.__personId

    def setDungeonId(self, newDungeonId):
        if newDungeonId > 0:
            self.__dungeonId = newDungeonId
        else:
            raise Exception("Error value must be Offense Id greater than zero")

    def getDungeonId(self):
        return self.__dungeonId

    def getFromDate(self):
        return self.__fromDate

    def setFromDate(self, newFromDate):
        self.__fromDate = newFromDate


class Visitings:
    def __init__(self, Id, dataVisited, personId, visitorName, mountinMinutes):
        if Id > 0:
            self.__Id = Id
        else:
            raise Exception("Error value must be Size greater than zero")
        if personId > 0:
            self.__personId = personId
        else:
            raise Exception("Error value must be Person Id greater than zero")
        if len(visitorName) > 1:
            self.__visitorName = visitorName
        else:
            raise Exception(
                "The Visitor Name must be greater than a character")
        if mountinMinutes > 0:
            self.__mountinMinutes = mountinMinutes
        else:
            raise Exception(
                "Error value must be Mountin Minutes  greater than zero")
        self.__dataVisited = dataVisited

    def getId(self):
        return self.__Id

    def setId(self, newId):
        if newId > 0:
            self.__Id = newId
        else:
            raise Exception("Error value must be Size greater than zero")

    def setPersonId(self, newPersonId):
        if newPersonId > 0:
            self.__personId = newPersonId
        else:
            raise Exception("Error value must be Person Id greater than zero")

    def getPersonId(self):
        return self.__personId

    def setMountinMinutes(self, newMountinMinutes):
        if newMountinMinutes > 0:
            self.__mountinMinutes = newMountinMinutes
        else:
            raise Exception(
                "Error value must be Mountin Minutes  greater than zero")

    def getMountinMinutes(self):
        return self.__mountinMinutes

    def setVisitorName(self, newVisitorName):
        if len(newVisitorName) > 1:
            self.__visitorName = newVisitorName
        else:
            raise Exception("The Name must be greater than a character")

    def getVisitorName(self):
        return self.__visitorName

    def setDataVisited(self, newDataVisited):
        self.__dataVisited = newDataVisited

    def getDataVisitede(self):
        return self.__dataVisited
# Person انشاء جدول
cr.execute("""
 CREATE TABLE if not exists Person (
	Id INTEGER NOT NULL UNIQUE,
	firstName  TEXT NOT NULL,
	father	TEXT NOT NULL,
	lastName	TEXT NOT NULL,
	Gender	TEXT NOT NULL,
	birthYear	TEXT NOT NULL,
	address TEXT NOT NULL,
	PRIMARY KEY(Id AUTOINCREMENT)
        )
      """)
# Offense انشاء جدول
cr.execute("""
 CREATE TABLE if not exists Offense (
	Id	INTEGER NOT NULL UNIQUE,
	Name	TEXT NOT NULL,
	PRIMARY KEY(Id AUTOINCREMENT)
        )
      """)
# Dungeon انشاء جدول
cr.execute("""
    CREATE TABLE if not exists Dungeon (
        Id	INTEGER NOT NULL UNIQUE,
        Name	TEXT NOT NULL,
        size	INTEGER NOT NULL,
        PRIMARY KEY(Id AUTOINCREMENT)
        )
            """)
# Convicts انشاء جدول
cr.execute("""
    CREATE TABLE if not exists Convicts (
        Id	INTEGER NOT NULL UNIQUE,
        fromDate	TEXT NOT NULL,
        toDate	TEXT NOT NULL,
        personId	INTEGER NOT NULL,
        offenseId	INTEGER NOT NULL,
        PRIMARY KEY(Id AUTOINCREMENT),
        FOREIGN KEY(personId) REFERENCES Person(Id),
        FOREIGN KEY(offenseId) REFERENCES Offense(Id)
        )
            """)
# Visitings انشاء جدول
cr.execute("""
    CREATE TABLE if not exists Visitings (
        Id	INTEGER NOT NULL UNIQUE,
        dataVisited	TEXT NOT NULL,
        personId	INTEGER NOT NULL,
        visitorName	TEXT NOT NULL,
        mountinMinutes	INTEGER NOT NULL,
        PRIMARY KEY(Id AUTOINCREMENT),
        FOREIGN KEY(personId) REFERENCES Person(Id)
        )
           """)
# DungeonMoves انشاء جدول
cr.execute("""
    CREATE TABLE if not exists DungeonMoves (
        Id	INTEGER NOT NULL UNIQUE,
        dungeonId	INTEGER NOT NULL,
        personId	INTEGER NOT NULL,
        fromDate	TEXT NOT NULL,
        PRIMARY KEY(Id AUTOINCREMENT),
        FOREIGN KEY(personId) REFERENCES Person(Id),
        FOREIGN KEY(dungeonId) REFERENCES Dungeon(Id)
        )
            """)


class main():
    def __init__(self, root):
        # root window
        self.root = root
        x = 1000
        y = 600
        sx = root.winfo_screenwidth()
        sy = root.winfo_screenheight()
        xx = int((sx-x)/2)
        yy = int((sy-y)/2)
        self.root.geometry('%dx%d+%d+%d' % (x, y, xx, yy))
        self.root.title('Prison Administration')
        self.root.resizable(False, False)
        self.root.iconbitmap('jail.ico')

        # create a notebook
        self.notebook = ttk.Notebook(self.root, height=700)
        self.notebook.pack(pady=1, fill='both')

        # create frames
        self.person = ttk.Frame(self.notebook, width=400, height=280)
        self.Dungeon = ttk.Frame(self.notebook, width=400, height=280)
        self.Convicts = ttk.Frame(self.notebook, width=400, height=280)
        self.Offense = ttk.Frame(self.notebook, width=400, height=280)
        self.visit = ttk.Frame(self.notebook, width=400, height=280)
        self.Dungeonmoves = ttk.Frame(self.notebook, width=400, height=280)
# -------------------------------------------------
        self.person.pack(fill='both', expand=True)
        self.Dungeon.pack(fill='both', expand=True)
        self.Convicts.pack(fill='both', expand=True)
        self.Offense.pack(fill='both', expand=True)
        self.visit.pack(fill='both', expand=True)
        self.Dungeonmoves.pack(fill='both', expand=True)

        # add frames to notebook

        self.notebook.add(
            self.person, text='                   Person                      ')
        self.notebook.add(
            self.Dungeon, text='                     Dungeon                  ')
        self.notebook.add(
            self.Convicts, text='                  Convicts                   ')
        self.notebook.add(
            self.Offense, text='                Offense                       ')
        self.notebook.add(
            self.visit, text='                  Visitings                      ')
        self.notebook.add(self.Dungeonmoves,
                          text='             DungeonMoves             ')
# -------------------------------------------------------------------------


# fram data person
        self.framData = Frame(self.person, width=200, height=700, bg='#566E61')
        self.framData.pack(side=LEFT)

        self.lbl_id = Label(self.framData, text='Id', bg='#566E61',
                            fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_id.place(x=90, y=10)
        self.input_id = Entry(self.framData, border=0,
                              font=('tajawal', 12, 'normal'))
        self.input_id.place(x=10, y=35)
        # ---
        self.lbl_fn = Label(self.framData, text='First Name',
                            bg='#566E61', fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_fn.place(x=60, y=60)
        self.input_fn = Entry(self.framData, border=0,
                              font=('tajawal', 12, 'normal'))
        self.input_fn.place(x=10, y=85)
        # ---
        self.lbl_ln = Label(self.framData, text='Last Name',
                            bg='#566E61', fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_ln.place(x=60, y=110)
        self.input_ln = Entry(self.framData, border=0,
                              font=('tajawal', 12, 'normal'))
        self.input_ln.place(x=10, y=135)
        # -----
        self.lbl_fan = Label(self.framData, text='Father Name',
                             bg='#566E61', fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_fan.place(x=55, y=160)
        self.input_fan = Entry(self.framData, border=0,
                               font=('tajawal', 12, 'normal'))
        self.input_fan.place(x=10, y=185)
        # -----
        self.lbl_by = Label(self.framData, text='Birth year',
                            bg='#566E61', fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_by.place(x=65, y=210)
        self.input_by = Entry(self.framData, border=0,
                              font=('tajawal', 12, 'normal'))
        self.input_by.place(x=10, y=235)
        # --------
        self.lbl_ad = Label(self.framData, text='Address',
                            bg='#566E61', fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_ad.place(x=65, y=260)
        self.input_ad = Entry(self.framData, border=0,
                              font=('tajawal', 12, 'normal'))
        self.input_ad.place(x=10, y=285)
        # -----
        self.lbl_gen = Label(self.framData, text='Gender',
                             bg='#566E61', fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_gen.place(x=65, y=310)
        self.gender = ttk.Combobox(self.framData, width=27)
        self.gender['values'] = ('male', 'female')
        self.gender.current(0)
        self.gender.place(x=10, y=335)
# ------- end Labels and Entries
        # -- bar frame
        self.bar = Frame(self.framData, width=700, height=4, bg='white')
        self.bar.place(x=0, y=385)
        # --- buttons :
        self.btn_add = Button(self.framData, command=self.insert, text='Add', width=10, height=2,
                              bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_add.place(x=10, y=410)
        # ---
        self.btn_update = Button(self.framData, text='Update', command=self.Update, width=10,
                                 height=2, bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_update.place(x=110, y=410)
        # ----
        self.btn_clear = Button(self.framData, command=self.clear, text='Clear', width=10, height=2,
                                bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_clear.place(x=10, y=460)
        # ---
        self.btn_about = Button(self.framData, command=self.about, text='About', width=10, height=2,
                                bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_about.place(x=110, y=460)
        # ---
        self.lbl = Label(
            self.framData, text='By Abdullah Al-Houssein Developer', bg='#566E61', fg='#000000')
        self.lbl.place(x=3, y=530)
# ----------end work in frame data-----
# -----------frame top left sellect all,sellect selectbyid,select Tow tims
        self.framSearch = Frame(self.person, width=800,
                                height=100, bg='#A7D4BC')
        self.framSearch.pack(side=TOP)
        # --delete function
        self.btn_Delete = Button(self.framSearch, command=self.deleteById, text='Delete By Id', width=15,
                                 height=1, bg='#566E61', fg='#ffffff', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_Delete.place(x=20, y=38)
        # input id
        self.input_deleteid = Entry(
            self.framSearch, border=0, width=10, font=('tajawal', 12, 'normal'))
        self.input_deleteid.place(x=150, y=39)
        # bar vertical
        self.bar1 = Frame(self.framSearch, width=3, height=100, bg='white')
        self.bar1.place(x=255, y=0)
        # select between
        self.btn_Select = Button(self.framSearch, text='Select', width=15, height=1, bg='#566E61',
                                 command=self.SelectBetween, fg='#ffffff', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_Select.place(x=270, y=38)
        self.cal = DateEntry(self.framSearch, selectmode='day')
        self.cal.place(x=400, y=12)
        self.cal1 = DateEntry(self.framSearch, selectmode='day')
        self.cal1.place(x=400, y=60)
        # bar 2
        self.bar2 = Frame(self.framSearch, width=3, height=100, bg='white')
        self.bar2.place(x=510, y=0)
        # select All
        self.btn_SelectAll = Button(self.framSearch, text='Select All', command=self.selectall, width=15,
                                    height=1, bg='#566E61', fg='#ffffff', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_SelectAll.place(x=550, y=18)
        self.btn_SelectNamePersonOfOffense = Button(self.framSearch, text='Select By Offens', width=15, height=1, bg='#566E61',
                                                    command=self.SelectOffense, fg='#ffffff', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_SelectNamePersonOfOffense.place(x=550, y=50)

        self.input_offenseIdPerson = Entry(
            self.framSearch, border=0, width=10, font=('tajawal', 12, 'normal'))
        self.input_offenseIdPerson.place(x=675, y=50)

        self.table = ttk.Treeview(self.person, height=24, columns=(
            'Id', 'First Name', 'Father Name', 'Last Name', 'Gender', 'Birth Year', 'Address'), show='headings')
        self.table.pack()
        self.table.heading('Id', text='Id')
        self.table.heading('First Name', text='First Name')
        self.table.heading('Father Name', text='Father Name')
        self.table.heading('Last Name', text='Last Name')
        self.table.heading('Gender', text='Gender')
        self.table.heading('Birth Year', text='Birth Year')
        self.table.heading('Address', text='Address')
        self.table.column('Id', anchor=CENTER, width=70)
        self.table.column('First Name', anchor=CENTER, width=125)
        self.table.column('Last Name', anchor=CENTER, width=120)
        self.table.column('Father Name', anchor=CENTER, width=120)
        self.table.column('Birth Year', anchor=CENTER, width=120)
        self.table.column('Address', anchor=CENTER, width=120)
        self.table.column('Gender', anchor=CENTER, width=120)
        vsb = ttk.Scrollbar(self.person, orient="vertical",
                            command=self.table.yview)
        vsb.place(x=980, y=125, height=450)
        self.table.configure(yscrollcommand=vsb.set)

        # start farme data Dengeon
        self.framData1 = Frame(self.Dungeon, width=200,
                               height=700, bg='#566E61')
        self.framData1.pack(side=LEFT)
        self.lbl_id = Label(self.Dungeon, text='Id', bg='#566E61',
                            fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_id.place(x=90, y=90)
        self.input_idDungeon = Entry(
            self.Dungeon, border=0, font=('tajawal', 12, 'normal'))
        self.input_idDungeon.place(x=10, y=120)
        # ---
        self.lbl_name = Label(self.Dungeon, text='Name', bg='#566E61',
                              fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_name.place(x=75, y=150)
        self.input_name = Entry(self.Dungeon, border=0,
                                font=('tajawal', 12, 'normal'))
        self.input_name.place(x=10, y=180)
        # ---
        self.lbl_size = Label(self.Dungeon, text='Size', bg='#566E61',
                              fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_size.place(x=75, y=210)
        self.input_size = Entry(self.Dungeon, border=0,
                                font=('tajawal', 12, 'normal'))
        self.input_size.place(x=10, y=240)
        # -----

# ------- end Labels and Entries
        # -- bar frame
        self.bar = Frame(self.Dungeon, width=700, height=4, bg='white')
        self.bar.place(x=0, y=385)
        # --- buttons :
        self.btn_add = Button(self.Dungeon, command=self.insertDungeon, text='Add', width=10,
                              height=2, bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_add.place(x=10, y=410)
        # ---
        self.btn_update = Button(self.Dungeon, text='Update', command=self.Update, width=10,
                                 height=2, bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_update.place(x=110, y=410)
        # ----
        self.btn_clearDingeun = Button(self.Dungeon, command=self.clearDungeon, text='Clear', width=10,
                                       height=2, bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_clearDingeun.place(x=10, y=460)
        # ---
        self.btn_about = Button(self.Dungeon, command=self.about, text='About', width=10, height=2,
                                bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_about.place(x=110, y=460)
        # ---
        self.lbl = Label(
            self.Dungeon, text='By Abdullah Al-Houssein Developer', bg='#566E61', fg='#000000')
        self.lbl.place(x=3, y=530)
# ----------end work in frame data-----
        self.framSearch = Frame(self.Dungeon, width=800,
                                height=100, bg='#A7D4BC')
        self.framSearch.pack(side=TOP)
        # --delete function
        self.btn_Delete = Button(self.framSearch, command=self.deleteByIdDungeon, text='Delete By Id',
                                 width=15, height=1, bg='#566E61', fg='#ffffff', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_Delete.place(x=20, y=38)
        # input id
        self.input_deleteid1 = Entry(
            self.framSearch, border=0, width=10, font=('tajawal', 12, 'normal'))
        self.input_deleteid1.place(x=150, y=39)
        # bar vertical
        self.bar1 = Frame(self.framSearch, width=3, height=100, bg='white')
        self.bar1.place(x=255, y=0)
        # select between
        self.btn_SelectDungeun = Button(self.framSearch, text='Select Dungoen', width=15, height=1, bg='#566E61',
                                        command=self.SelectDungeun, fg='#ffffff', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_SelectDungeun.place(x=270, y=38)
        self.input_personId = Entry(
            self.framSearch, border=0, width=10, font=('tajawal', 12, 'normal'))
        self.input_personId.place(x=400, y=39)

        # bar 2
        self.bar2 = Frame(self.framSearch, width=3, height=100, bg='white')
        self.bar2.place(x=510, y=0)
        # select All
        self.btn_SelectAll = Button(self.framSearch, text='Select All', command=self.selectallDungeon,
                                    width=15, height=1, bg='#566E61', fg='#ffffff', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_SelectAll.place(x=600, y=38)

        self.table1 = ttk.Treeview(self.Dungeon, height=24, columns=(
            'Id', 'Name', 'Size'), show='headings')
        self.table1.pack()
        self.table1.heading('Id', text='Id')
        self.table1.heading('Name', text='Name')
        self.table1.heading('Size', text='Size')

        self.table1.column('Id', anchor=CENTER, width=200)
        self.table1.column('Name', anchor=CENTER, width=330)
        self.table1.column('Size', anchor=CENTER, width=330)
        vsb = ttk.Scrollbar(self.Dungeon, orient="vertical",
                            command=self.table1.yview)
        vsb.place(x=980, y=125, height=450)
        self.table1.configure(yscrollcommand=vsb.set)
        # end frame Dungeon
        # ------start fram convicts
        self.frameConvicts = Frame(self.Convicts, width=200,
                                   height=700, bg='#566E61')
        self.frameConvicts.pack(side=LEFT)
        self.lbl_id = Label(self.Convicts, text='Id', bg='#566E61',
                            fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_id.place(x=90, y=50)
        self.input_idConvicts = Entry(
            self.Convicts, border=0, font=('tajawal', 12, 'normal'))
        self.input_idConvicts.place(x=10, y=80)
        # ---
        self.lbl_fromDate = Label(self.Convicts, text='From Date', bg='#566E61',
                                  fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_fromDate.place(x=55, y=110)
        self.input_fromData = Entry(self.Convicts, border=0,
                                    font=('tajawal', 12, 'normal'))
        self.input_fromData.place(x=10, y=140)
        # ---
        self.lbl_toDate = Label(self.Convicts, text='To Date', bg='#566E61',
                                fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_toDate.place(x=65, y=170)
        self.input_toDate = Entry(self.Convicts, border=0,
                                  font=('tajawal', 12, 'normal'))
        self.input_toDate.place(x=10, y=200)
        self.lbl_personIdd = Label(self.Convicts, text='Person Id', bg='#566E61',
                                   fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_personIdd.place(x=55, y=230)
        self.input_personIdd = Entry(self.Convicts, border=0,
                                     font=('tajawal', 12, 'normal'))
        self.input_personIdd.place(x=10, y=260)
        # --
        self.lbl_offenseIdd = Label(self.Convicts, text='Offense Id', bg='#566E61',
                                    fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_offenseIdd.place(x=55, y=290)
        self.input_offenseIdd = Entry(self.Convicts, border=0,
                                      font=('tajawal', 12, 'normal'))
        self.input_offenseIdd.place(x=10, y=320)
        # -----

# ------- end Labels and Entries
        # -- bar frame
        self.bar = Frame(self.Convicts, width=700, height=4, bg='white')
        self.bar.place(x=0, y=385)
        # --- buttons :
        self.btn_addConvicts = Button(self.Convicts, command=self.insertConvicts, text='Add', width=10,
                                      height=2, bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_addConvicts.place(x=10, y=410)
        # ---
        self.btn_updateConvicts = Button(self.Convicts, text='Update', command=self.Update, width=10,
                                         height=2, bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_updateConvicts.place(x=110, y=410)
        # ----
        self.btn_clearConvicts = Button(self.Convicts, command=self.clearConvicts, text='Clear', width=10,
                                        height=2, bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_clearConvicts.place(x=10, y=460)
        # ---
        self.btn_about = Button(self.Convicts, command=self.about, text='About', width=10, height=2,
                                bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_about.place(x=110, y=460)
        # ---
        self.lbl = Label(
            self.Convicts, text='By Abdullah Al-Houssein Developer', bg='#566E61', fg='#000000')
        self.lbl.place(x=3, y=530)
# ----------end work in frame data-----
        self.framSearchConvicts = Frame(self.Convicts, width=800,
                                        height=100, bg='#A7D4BC')
        self.framSearchConvicts.pack(side=TOP)
        # --delete function
        self.btn_DeleteConvicts = Button(self.framSearchConvicts, command=self.deleteByIdConvicts, text='Delete By Id',
                                         width=15, height=1, bg='#566E61', fg='#ffffff', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_DeleteConvicts.place(x=60, y=38)
        # input id
        self.input_deleteid2 = Entry(
            self.framSearchConvicts, border=0, width=10, font=('tajawal', 12, 'normal'))
        self.input_deleteid2.place(x=200, y=39)

        # bar 2
        self.bar2 = Frame(self.framSearchConvicts,
                          width=3, height=100, bg='white')
        self.bar2.place(x=390, y=0)
        # select All
        self.btn_SelectAllConvicts = Button(self.framSearchConvicts, text='Select All', command=self.selectallConvicts,
                                            width=15, height=1, bg='#566E61', fg='#ffffff', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_SelectAllConvicts.place(x=540, y=38)

        self.table2 = ttk.Treeview(self.Convicts, height=24, columns=(
            'Id', 'From Date', 'To Date', 'Person Id', 'Offense Id'), show='headings')
        self.table2.pack()
        self.table2.heading('Id', text='Id')
        self.table2.heading('From Date', text='From Date')
        self.table2.heading('To Date', text='To Date')
        self.table2.heading('Person Id', text='Person Id')
        self.table2.heading('Offense Id', text='Offense Id')
        self.table2.column('Id', anchor=CENTER, width=100)
        self.table2.column('From Date', anchor=CENTER, width=200)
        self.table2.column('To Date', anchor=CENTER, width=200)
        self.table2.column('Person Id', anchor=CENTER, width=150)
        self.table2.column('Offense Id', anchor=CENTER, width=150)
        vsb = ttk.Scrollbar(self.Convicts, orient="vertical",
                            command=self.table2.yview)
        vsb.place(x=980, y=125, height=450)
        self.table2.configure(yscrollcommand=vsb.set)
        # end frame Convicts
        # ------start fram Offense
        self.frameOffense = Frame(self.Offense, width=200,
                                  height=700, bg='#566E61')
        self.frameOffense.pack(side=LEFT)
        self.lbl_idOffense = Label(self.Offense, text='Id', bg='#566E61',
                                   fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_idOffense.place(x=90, y=130)
        self.input_idOffense = Entry(
            self.Offense, border=0, font=('tajawal', 12, 'normal'))
        self.input_idOffense.place(x=10, y=160)
        # ---
        self.lbl_Name = Label(self.Offense, text='Name', bg='#566E61',
                              fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_Name.place(x=75, y=190)
        self.input_Name = Entry(self.Offense, border=0,
                                font=('tajawal', 12, 'normal'))
        self.input_Name.place(x=10, y=220)
        # ---

# ------- end Labels and Entries
        # -- bar frame
        self.bar = Frame(self.Offense, width=700, height=4, bg='white')
        self.bar.place(x=0, y=385)
        # --- buttons :
        self.btn_addOffense = Button(self.Offense, command=self.insertOffense, text='Add', width=10,
                                     height=2, bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_addOffense.place(x=10, y=410)
        # ---
        self.btn_updateOffense = Button(self.Offense, text='Update', command=self.Update, width=10,
                                        height=2, bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_updateOffense.place(x=110, y=410)
        # ----
        self.btn_clearOffene = Button(self.Offense, command=self.clearOffense, text='Clear', width=10,
                                      height=2, bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_clearOffene.place(x=10, y=460)
        # ---
        self.btn_about = Button(self.Offense, command=self.about, text='About', width=10, height=2,
                                bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_about.place(x=110, y=460)
        # ---
        self.lbl = Label(
            self.Offense, text='By Abdullah Al-Houssein Developer', bg='#566E61', fg='#000000')
        self.lbl.place(x=3, y=530)
# ----------end work in frame data-----
        self.framSearchOffense = Frame(self.Offense, width=800,
                                       height=100, bg='#A7D4BC')
        self.framSearchOffense.pack(side=TOP)
        # --delete function
        self.btn_DeleteOffense = Button(self.framSearchOffense, command=self.deleteByIdOffense, text='Delete By Id',
                                        width=15, height=1, bg='#566E61', fg='#ffffff', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_DeleteOffense.place(x=80, y=38)
        # input id
        self.input_deleteidOffense = Entry(
            self.framSearchOffense, border=0, width=10, font=('tajawal', 12, 'normal'))
        self.input_deleteidOffense.place(x=225, y=39)
        # bar vertical
        self.bar1 = Frame(self.framSearchOffense,
                          width=3, height=100, bg='white')
        self.bar1.place(x=400, y=0)

        # bar 2
        self.bar2 = Frame(self.framSearchOffense,
                          width=3, height=100, bg='white')
        #self.bar2.place(x=520, y=0)
        # select All
        self.btn_SelectAllOffense = Button(self.framSearchOffense, text='Select All', command=self.selectallOffense,
                                           width=15, height=1, bg='#566E61', fg='#ffffff', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_SelectAllOffense.place(x=550, y=38)

        self.table3 = ttk.Treeview(
            self.Offense, height=24, columns=('Id', 'Name'), show='headings')
        self.table3.pack()
        self.table3.heading('Id', text='Id')
        self.table3.heading('Name', text='Name')

        self.table3.column('Id', anchor=CENTER, width=400)
        self.table3.column('Name', anchor=CENTER, width=400)

        vsb = ttk.Scrollbar(self.Offense, orient="vertical",
                            command=self.table3.yview)
        vsb.place(x=980, y=125, height=450)
        self.table3.configure(yscrollcommand=vsb.set)
        # fram data Visisting
        self.framDataVisit = Frame(
            self.visit, width=200, height=700, bg='#566E61')
        self.framDataVisit.pack(side=LEFT)

        self.lbl_idVisit = Label(self.visit, text='Id', bg='#566E61',
                                 fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_idVisit.place(x=90, y=55)
        self.input_idVisit = Entry(self.visit, border=0,
                                   font=('tajawal', 12, 'normal'))
        self.input_idVisit.place(x=10, y=80)
        # ---
        self.lbl_DateVisit = Label(self.visit, text='Date Visited',
                                   bg='#566E61', fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_DateVisit.place(x=60, y=105)
        self.input_DateVisit = Entry(self.visit, border=0,
                                     font=('tajawal', 12, 'normal'))
        self.input_DateVisit.place(x=10, y=130)
        # ---
        self.lbl_perId = Label(self.visit, text='Person Id',
                               bg='#566E61', fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_perId.place(x=60, y=155)
        self.input_PerId = Entry(self.visit, border=0,
                                 font=('tajawal', 12, 'normal'))
        self.input_PerId.place(x=10, y=180)
        # -----
        self.lbl_VisitName = Label(self.visit, text='Visitor Name',
                                   bg='#566E61', fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_VisitName.place(x=55, y=205)
        self.input_VisitName = Entry(self.visit, border=0,
                                     font=('tajawal', 12, 'normal'))
        self.input_VisitName.place(x=10, y=230)
        # -----
        self.lbl_Minutes = Label(self.visit, text='Moutin Minutes',
                                 bg='#566E61', fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_Minutes.place(x=45, y=255)
        self.input_Minutes = Entry(self.visit, border=0,
                                   font=('tajawal', 12, 'normal'))
        self.input_Minutes.place(x=10, y=280)

# ------- end Labels and Entries
        # -- bar frame
        self.bar = Frame(self.visit, width=700, height=4, bg='white')
        self.bar.place(x=0, y=385)
        # --- buttons :
        self.btn_addVisit = Button(self.visit, command=self.insertVisit, text='Add', width=10, height=2,
                                   bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_addVisit.place(x=10, y=410)
        # ---
        self.btn_updateVisit = Button(self.visit, text='Update', command=self.Update, width=10,
                                      height=2, bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_updateVisit.place(x=110, y=410)
        # ----
        self.btn_clearVisit = Button(self.visit, command=self.clearVisit, text='Clear', width=10, height=2,
                                     bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_clearVisit.place(x=10, y=460)
        # ---
        self.btn_about = Button(self.visit, command=self.about, text='About', width=10, height=2,
                                bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_about.place(x=110, y=460)
        # ---
        self.lbl = Label(
            self.visit, text='By Abdullah Al-Houssein Developer', bg='#566E61', fg='#000000')
        self.lbl.place(x=3, y=530)
# ----------end work in frame data-----
# -----------frame top left sellect all,sellect selectbyid,select Tow tims
        self.framVisit = Frame(self.visit, width=800,
                               height=100, bg='#A7D4BC')
        self.framVisit.pack(side=TOP)
        # --delete function
        self.btn_DeleteVisit = Button(self.framVisit, command=self.deleteByIdVisit, text='Delete By Id', width=15,
                                      height=1, bg='#566E61', fg='#ffffff', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_DeleteVisit.place(x=20, y=38)
        # input id
        self.input_deleteidVisit = Entry(
            self.framVisit, border=0, width=10, font=('tajawal', 12, 'normal'))
        self.input_deleteidVisit.place(x=150, y=39)
        # bar vertical
        self.bar1 = Frame(self.framVisit, width=3, height=100, bg='white')
        self.bar1.place(x=255, y=0)
        # select between
        self.btn_Select = Button(self.framVisit, text='Select', width=15, height=1, bg='#566E61',
                                 command=self.SelectBetweenVisit, fg='#ffffff', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_Select.place(x=270, y=38)
        self.calvisit = DateEntry(self.framVisit, selectmode='day')
        self.calvisit.place(x=400, y=12)
        self.calVisit1 = DateEntry(self.framVisit, selectmode='day')
        self.calVisit1.place(x=400, y=60)
        # bar 2
        self.bar2 = Frame(self.framVisit, width=3, height=100, bg='white')
        self.bar2.place(x=510, y=0)
        # select All
        self.btn_SelectAllVisit = Button(self.framVisit, text='Select All', command=self.selectallVisit, width=15,
                                         height=1, bg='#566E61', fg='#ffffff', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_SelectAllVisit.place(x=600, y=38)

        self.table4 = ttk.Treeview(self.visit, height=24, columns=(
            'Id', 'Date Visited', 'Person Id', 'Visitor Name', 'Mountin Minutes'), show='headings')
        self.table4.pack()
        self.table4.heading('Id', text='Id')
        self.table4.heading('Date Visited', text='Date Visited')
        self.table4.heading('Person Id', text='Person Id')
        self.table4.heading('Visitor Name', text='Visitor Name')
        self.table4.heading('Mountin Minutes', text='Mountin Minutes')

        self.table4.column('Id', anchor=CENTER, width=100)
        self.table4.column('Date Visited', anchor=CENTER, width=200)
        self.table4.column('Person Id', anchor=CENTER, width=100)
        self.table4.column('Visitor Name', anchor=CENTER, width=200)
        self.table4.column('Mountin Minutes', anchor=CENTER, width=200)

        vsb = ttk.Scrollbar(self.visit, orient="vertical",
                            command=self.table.yview)
        vsb.place(x=980, y=125, height=450)
        self.table4.configure(yscrollcommand=vsb.set)
        # end frame Visiting

        # start farme data DengeonMoves
        self.framDungeonmoves = Frame(self.Dungeonmoves, width=200,
                                      height=700, bg='#566E61')
        self.framDungeonmoves.pack(side=LEFT)
        self.lbl_idDM = Label(self.Dungeonmoves, text='Id', bg='#566E61',
                              fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_idDM.place(x=90, y=60)
        self.input_idDungeonM = Entry(
            self.Dungeonmoves, border=0, font=('tajawal', 12, 'normal'))
        self.input_idDungeonM.place(x=10, y=85)
        # ---
        self.lbl_dungeonIdM = Label(self.Dungeonmoves, text='Dungeon Id', bg='#566E61',
                                    fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_dungeonIdM.place(x=50, y=110)
        self.input__dungeonIdM = Entry(self.Dungeonmoves, border=0,
                                       font=('tajawal', 12, 'normal'))
        self.input__dungeonIdM.place(x=10, y=135)
        # ---
        self.lbl_persIdM = Label(self.Dungeonmoves, text='Person Id', bg='#566E61',
                                 fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_persIdM.place(x=58, y=160)
        self.input_persIdM = Entry(self.Dungeonmoves, border=0,
                                   font=('tajawal', 12, 'normal'))
        self.input_persIdM.place(x=10, y=185)
        self.lbl_fromDateM = Label(self.Dungeonmoves, text='Date Visited',
                                   bg='#566E61', fg='#ffffff', font=('tajawal', 12, 'bold'))
        self.lbl_fromDateM.place(x=55, y=210)
        self.input_fromDateM = Entry(self.Dungeonmoves, border=0,
                                     font=('tajawal', 12, 'normal'))
        self.input_fromDateM.place(x=10, y=235)
        # -----

# ------- end Labels and Entries
        # -- bar frame
        self.bar = Frame(self.Dungeonmoves, width=700, height=4, bg='white')
        self.bar.place(x=0, y=385)
        # --- buttons :
        self.btn_addDungMov = Button(self.Dungeonmoves, command=self.insertDungeonMoves, text='Add', width=10,
                                     height=2, bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_addDungMov.place(x=10, y=410)
        # ---
        self.btn_updateDonMov = Button(self.Dungeonmoves, text='Update', command=self.Update, width=10,
                                       height=2, bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_updateDonMov.place(x=110, y=410)
        # ----
        self.btn_clearDunMov = Button(self.Dungeonmoves, command=self.clearDunMov, text='Clear', width=10,
                                      height=2, bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_clearDunMov.place(x=10, y=460)
        # ---
        self.btn_about = Button(self.Dungeonmoves, command=self.about, text='About', width=10, height=2,
                                bg='#A7D4BC', fg='#000000', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_about.place(x=110, y=460)
        # ---
        self.lbl = Label(
            self.Dungeonmoves, text='By Abdullah Al-Houssein Developer', bg='#566E61', fg='#000000')
        self.lbl.place(x=3, y=530)
# ----------end work in frame data-----
        self.framSearchDunMov = Frame(self.Dungeonmoves, width=800,
                                      height=100, bg='#A7D4BC')
        self.framSearchDunMov.pack(side=TOP)
        # --delete function
        self.btn_DeleteDunMov = Button(self.framSearchDunMov, command=self.deleteByIdDunMov, text='Delete By Id',
                                       width=15, height=1, bg='#566E61', fg='#ffffff', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_DeleteDunMov.place(x=85, y=38)
        # input id
        self.input_deleteidMoves = Entry(
            self.framSearchDunMov, border=0, width=10, font=('tajawal', 12, 'normal'))
        self.input_deleteidMoves.place(x=225, y=39)
        # bar vertical
        self.bar1 = Frame(self.framSearchDunMov, width=3,
                          height=100, bg='white')
        self.bar1.place(x=400, y=0)
        # select All
        self.btn_SelectAllDunMov = Button(self.framSearchDunMov, text='Select All', command=self.selectallDunMov,
                                          width=15, height=1, bg='#566E61', fg='#ffffff', cursor='hand2', bd=0, font=('tajawal', 9, 'bold'))
        self.btn_SelectAllDunMov.place(x=550, y=38)

        self.table5 = ttk.Treeview(self.Dungeonmoves, height=24, columns=(
            'Id', 'Dungeon Id', 'Person Id', 'From Date'), show='headings')
        self.table5.pack()
        self.table5.heading('Id', text='Id')
        self.table5.heading('Dungeon Id', text='Dungeon Id')
        self.table5.heading('Person Id', text='Person Id')
        self.table5.heading('From Date', text='From Date')

        self.table5.column('Id', anchor=CENTER, width=150)
        self.table5.column('Dungeon Id', anchor=CENTER, width=200)
        self.table5.column('Person Id', anchor=CENTER, width=200)
        self.table5.column('From Date', anchor=CENTER, width=250)
        vsb = ttk.Scrollbar(self.Dungeonmoves, orient="vertical",
                            command=self.table5.yview)
        vsb.place(x=980, y=125, height=450)
        self.table5.configure(yscrollcommand=vsb.set)
        
    # end frame DungeonMoves
    def selectall(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()

        cr.execute("""select * from Person""")
        trees = cr.fetchall()
        self.table.delete(*self.table.get_children())
        for i in trees:
            self.table.insert('', END, values=i)
            db.commit()
        db.close()

    def SelectOffense(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        if self.input_offenseIdPerson.get()=="":
            messagebox.showerror("Error","Entry is empty")
        else:
            cr.execute(
                """select * 
                        from Person 
                            where Person.Id in (SELECT Convicts.personId
                            from Convicts where
                            Convicts.offenseId=(SELECT Offense.Id
                            from Offense WHERE Offense.Name='{}'))
                        """.format(self.input_offenseIdPerson.get()))
            trees = cr.fetchall()
            self.table.delete(*self.table.get_children())
        for i in trees:
            self.table.insert('', END, values=i)
            db.commit()
        db.close()

    def SelectBetween(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        cr.execute("""select * FROM Person WHERE 
        Person.Id in (SELECT Convicts.personId 
        from Convicts  where fromDate >=('{}') AND
         toDate <=('{}') or fromDate <=('{}') AND toDate >=('{}'))"""
                   .format(self.cal.get_date(), self.cal1.get_date(),
                    self.cal1.get_date(), self.cal.get_date()))
        trees = cr.fetchall()
        self.table.delete(*self.table.get_children())
        for i in trees:
            self.table.insert('', END, values=i)
            db.commit()
        db.close()

    def deleteById(self):
        if self.input_deleteid.get()=="":
            messagebox.showerror("Error","Must be Id gretar than Zereo")
        else:
            db = sqlite3.connect("preson.db")
            cr = db.cursor()
            cr.execute("""DELETE from Person where Id='{}';""".format(
                self.input_deleteid.get()))
            db.commit()
            self.selectall()
            messagebox.showinfo('Prison Administration', 'Deleted successfully')
            db.close()

    def insert(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        if self.input_id.get()=="" and self.input_fn.get()=="" and self.input_fan.get()=="" and self.input_ln.get()=="" and self.input_by.get()=="" and self.input_ad.get()=="":
            messagebox.showerror("Error","Entry is Empty")
        else:
            cr.execute("""insert into Person values('{}','{}','{}','{}','{}','{}','{}');""".format(self.input_id.get(), self.input_fn.get(
            ), self.input_fan.get(), self.input_ln.get(), self.gender.get(), self.input_by.get(), self.input_ad.get()))
            db.commit()
            self.selectall()
            self.clear()
            messagebox.showinfo('Prison Administration',
                                'Data has been added successfully')
            db.close()

    def Update(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()

        cr.execute("""
            UPDATE Person SET firstName= '{}',father='{}',lastName= '{}',
            Gender='{}' ,birthYear= '{}',address= '{}' WHERE Id= '{}';
        """.format(self.input_fn.get(), self.input_fan.get(), self.input_ln.get(), self.gender.get(), self.input_by.get(), self.input_ad.get(), self.input_id.get(), ))

        db.commit()
        self.selectall()
        messagebox.showinfo('Prison Administration',
                            'Data has been updated successfully')
        db.close()
    # ------

    def clear(self):
        self.input_id.delete(0, 'end')
        self.input_fn.delete(0, 'end')
        self.input_ln.delete(0, 'end')
        self.input_fan.delete(0, 'end')
        self.input_ad.delete(0, 'end')
        self.input_by.delete(0, 'end')

    # ------


# Function Dungeon

    def selectallDungeon(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        cr.execute("""select * from Dungeon""")
        trees = cr.fetchall()
        self.table1.delete(*self.table1.get_children())
        for i in trees:
            self.table1.insert('', END, values=i)
            db.commit()
        db.close()
    # select list Dungeun for pirson

    def SelectDungeun(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        cr.execute(
            """select *
               from Dungeon where 
               Dungeon.Id in
               (select DungeonMoves.dungeonId 
               from DungeonMoves where 
               personId=(select Person.Id 
               from Person where Person.Id=('{}')  ))
               """.format(self.input_personId.get()))
        trees = cr.fetchall()
        self.table1.delete(*self.table1.get_children())
        for i in trees:
            self.table1.insert('', END, values=i)
            db.commit()
        messagebox.showinfo('Prison Administration',
                            'Query completed successfully')

    def deleteByIdDungeon(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        cr.execute("""DELETE from Dungeon where Id='{}';""".format(
            self.input_deleteid1.get()))
        db.commit()
        self.selectallDungeon()
        messagebox.showinfo('Prison Administration', 'Deleted successfully !')
        db.close()

    def insertDungeon(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        cr.execute("""insert into Dungeon values('{}','{}','{}');""".format(
            self.input_idDungeon.get(), self.input_name.get(), self.input_size.get()))
        db.commit()
        self.selectallDungeon()
        self.clearDungeon()
        messagebox.showinfo('Prison Administration',
                            'Data has been added successfully')
        db.close()

    def clearDungeon(self):
        self.input_idDungeon.delete(0, 'end')
        self.input_name.delete(0, 'end')
        self.input_size.delete(0, 'end')

    def about(self):
        messagebox.showinfo('Prison Administration',
                            'This Program coded By Abdullah Al-Houssein')
# Function Convicts

    def selectallConvicts(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        cr.execute("""select * from Convicts""")
        trees = cr.fetchall()
        self.table2.delete(*self.table2.get_children())
        for i in trees:
            self.table2.insert('', END, values=i)
            db.commit()
        db.close()

    def insertConvicts(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        cr.execute("""insert into Convicts values('{}','{}','{}','{}','{}');""".format(self.input_idConvicts.get(
        ), self.input_fromData.get(), self.input_toDate.get(), self.input_personIdd.get(), self.input_offenseIdd.get()))
        db.commit()
        self.clearConvicts()
        self.selectallConvicts()
        messagebox.showinfo('Prison Administration',
                            'Data has been added successfully')
        db.close()

    def clearConvicts(self):
        self.input_idConvicts.delete(0, 'end')
        self.input_fromData.delete(0, 'end')
        self.input_toDate.delete(0, 'end')
        self.input_personIdd.delete(0, 'end')
        self.input_offenseIdd.delete(0, 'end')

    def deleteByIdConvicts(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        cr.execute("""DELETE from Convicts where Id='{}';""".format(
            self.input_deleteid2.get()))
        db.commit()
        self.selectallConvicts()
        messagebox.showinfo('Prison Administration', 'Deleted successfully !')
        db.close()
# Function Offense

    def selectallOffense(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        cr.execute("""select * from Offense""")
        trees = cr.fetchall()
        self.table3.delete(*self.table3.get_children())
        for i in trees:
            self.table3.insert('', END, values=i)
            db.commit()
        db.close()

    def clearOffense(self):
        self.input_idOffense.delete(0, 'end')
        self.input_Name.delete(0, 'end')

    def insertOffense(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        cr.execute("""insert into Offense values('{}','{}');""".format(
            self.input_idOffense.get(), self.input_Name.get()))
        db.commit()
        self.clearOffense()
        self.selectallOffense()
        messagebox.showinfo('Prison Administration',
                            'Data has been added successfully')
        db.close()
    def deleteByIdOffense(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        cr.execute("""DELETE from Offense where Id='{}';""".format(
            self.input_deleteidOffense.get()))
        db.commit()
        self.selectallOffense()
        messagebox.showinfo('Prison Administration', 'Deleted successfully !')
        db.close()
    # function Visited

    def selectallVisit(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        cr.execute("""select * from Visitings""")
        trees = cr.fetchall()
        self.table4.delete(*self.table4.get_children())
        for i in trees:
            self.table4.insert('', END, values=i)
            db.commit()
        db.close()

    def insertVisit(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        cr.execute("""insert into Visitings values('{}','{}','{}','{}','{}');""".format(self.input_idVisit.get(), self.input_DateVisit.get(
        ), self.input_PerId.get(), self.input_VisitName.get(), self.input_Minutes.get()))
        db.commit()
        self.selectallVisit()
        self.clearVisit()
        messagebox.showinfo('Prison Administration',
                            'Data has been added successfully')
        db.close()

    def clearVisit(self):
        self.input_idVisit.delete(0, 'end')
        self.input_DateVisit.delete(0, 'end')
        self.input_PerId.delete(0, 'end')
        self.input_VisitName.delete(0, 'end')
        self.input_Minutes.delete(0, 'end')

    def deleteByIdVisit(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        cr.execute("""DELETE from Visitings where Id='{}';""".format(
            self.input_deleteidVisit.get()))
        db.commit()
        self.selectallVisit()
        messagebox.showinfo('Prison Administration', 'Deleted successfully !')
        db.close()

    def SelectBetweenVisit(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        cr.execute("""SELECT Visitings.Id,
        Visitings.dataVisited,
        Visitings.personId,
        Visitings.visitorName,
        Visitings.mountinMinutes,
        (select (Person.firstName||" "||Person.lastName) from Person where Person.Id=Visitings.personId)
         as presoned_name
        from Visitings 
        where (Visitings.dataVisited >= ('{}') and Visitings.dataVisited <= ('{}'))
        or ((Visitings.dataVisited <= ('{}') and Visitings.dataVisited >= ('{}'))) """
        .format(self.calvisit.get_date(), self.calVisit1.get_date(), self.calVisit1.get_date(), 
        self.calvisit.get_date()))
        trees = cr.fetchall()
        self.table4.delete(*self.table4.get_children())
        for i in trees:
            self.table4.insert('', END, values=i)
            db.commit()
        db.close()

    # function DoungeonMoves

    def insertDungeonMoves(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        cr.execute("""insert into DungeonMoves values('{}','{}','{}','{}');""".format(self.input_idDungeonM.get(), self.input__dungeonIdM.get(
        ), self.input_persIdM.get(), self.input_fromDateM.get()))
        db.commit()
        self.selectallDunMov()
        self.clearVisit()
        messagebox.showinfo('Prison Administration',
                            'Data has been added successfully')
        db.close()

    def selectallDunMov(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        cr.execute("""select * from DungeonMoves""")
        trees = cr.fetchall()
        self.table5.delete(*self.table5.get_children())
        for i in trees:
            self.table5.insert('', END, values=i)
            db.commit()
        db.close()

    def deleteByIdDunMov(self):
        db = sqlite3.connect("preson.db")
        cr = db.cursor()
        cr.execute("""DELETE from DungeonMoves where Id='{}';""".format(
            self.input_deleteidMoves.get()))
        db.commit()
        self.selectallDunMov()
        messagebox.showinfo('Prison Administration', 'Deleted successfully !')
        db.close()

    def clearDunMov(self):
        self.input_idDungeonM.delete(0, 'end')
        self.input__dungeonIdM.delete(0, 'end')
        self.input_persIdM.delete(0, 'end')
        self.input_fromDateM.delete(0, 'end')


root = tk.Tk()
app = main(root)
root.mainloop()
