from tkinter import *
from tkinter import messagebox
import pymysql

mypass = "2001"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="Varun", password=mypass, database=mydatabase)
cur = con.cursor()

issueTable = "books_issued"
bookTable = "books"


def deleteBook():
    bid = bookInfo1.get()

    try:
        bid = int(bid)  
    except ValueError:
        messagebox.showinfo("Error", "Invalid Book ID. Please enter a valid integer.")
        return

    deleteSql = "delete from " + bookTable + " where bid = '" + str(bid) + "'"
    deleteIssue = "delete from " + issueTable + " where bid = '" + str(bid) + "'"
    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        messagebox.showinfo('Success', "Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")

    bookInfo1.delete(0, END)
    Varun.destroy()


def delete():
    global bookInfo1, SubmitBtn, quitBtn, Canvas1, con, cur, bookTable, Varun

    Varun = Tk()
    Varun.title("Library")
    Varun.minsize(width=400, height=400)
    Varun.geometry("600x500")

    Canvas1 = Canvas(Varun)

    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(Varun, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(Varun, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    lb2 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    SubmitBtn = Button(Varun, text="SUBMIT", bg='#d1ccc0', fg='black', command=deleteBook)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(Varun, text="Quit", bg='#f7f1e3', fg='black', command=Varun.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    Varun.mainloop()
