from tkinter import *
import customtkinter


class Table:
    def __init__(self, name, capacity, occupied = False):
        self.name = "Table " + name
        self.capacity = capacity
        self.occupied = occupied




def number_of_tables(root1):
    def table_count():
        if tablecount.get() == 'Enter Restaurant Name':
            tablecount.delete(0, END)

    root1.destroy()
    customtkinter.set_appearance_mode("dark")
    root = Tk()
    root.geometry('1366x768')
    root.state('zoomed')

    tablecountlabel = Label(root, bg="white", fg="black", text="Number of tables", font=('Garamond', 60, "bold"), bd=0)
    tablecountlabel.place(x=285, y=60)

    tablecount = Entry(root, bg="white", fg="grey", font=('Garamond', 20), width=28, bd=0)
    tablecount.place(x=190, y=210)
    tablecount.insert(0, "Enter Table Count")
    tablecount.bind('<FocusIn>', table_count)
    line1 = Frame(root, height=2, width=375, bg="black")
    line1.place(x=185, y=255)

    continuebutton = Button(root, bg="#015450", fg="white", activebackground="#015450", activeforeground="white",
                         text="Continue", font=('Garamond', 20), bd=0, cursor='hand2', command=tables)
    continuebutton.place(x=350, y=410)

def tables():


