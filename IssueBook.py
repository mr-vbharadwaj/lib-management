from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

mypass = "2001"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="Varun", password=mypass, database=mydatabase)
cur = con.cursor()

issueTable = "books_issued"
bookTable = "books"

allBid = []

def issue():
    global issuedBtn, labelFrame, lb1, inf1, inf2, quitBtn, Varun, Canvas1, status

    try:
        bid = int(inf1.get())  
        issuedto = inf2.get()

        issuedBtn.destroy()
        labelFrame.destroy()
        lb1.destroy()
        inf1.destroy()
        inf2.destroy()

        extractBid = "select bid from " + bookTable
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from " + bookTable + " where bid = '" + str(bid) + "'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'avail':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error", "Book ID not present")
    except ValueError:
        messagebox.showinfo("Error", "Invalid Book ID. Please enter a valid integer.")

    issueSql = "insert into " + issueTable + " values ('" + str(bid) + "','" + issuedto + "')"
    show = "select * from " + issueTable

    updateStatus = "update " + bookTable + " set status = 'issued' where bid = '" + str(bid) + "'"
    if bid in allBid and status == True:
        cur.execute(issueSql)
        con.commit()
        cur.execute(updateStatus)
        con.commit()
        messagebox.showinfo('Success', "Book Issued Successfully")
        Varun.destroy()
    else:
        allBid.clear()
        messagebox.showinfo('Message', "Book Already Issued")
        Varun.destroy()
        return

    allBid.clear()


def issueBook():
    global issuedBtn, labelFrame, lb1, inf1, inf2, quitBtn, Varun, Canvas1, status

    Varun = Tk()
    Varun.title("Library")
    Varun.minsize(width=400, height=400)
    Varun.geometry("600x500")

    Canvas1 = Canvas(Varun)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(Varun, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(Varun, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    lb2 = Label(labelFrame, text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    issuedBtn = Button(Varun, text="Issue", bg='#d1ccc0', fg='black', command=issue)
    issuedBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(Varun, text="Quit", bg='#aaa69d', fg='black', command=Varun.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    Varun.mainloop()
