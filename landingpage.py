from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter
from PIL import ImageTk
import os

def landingpage(direct, datadirect):
    def logout():
        root.destroy()
        import intropage

    def inventorypage(root, direct, datadirect):
        root.destroy()
        import inventory
        inventory.main_window(direct, datadirect)

    def staffmanagementpage(root, direct, datadirect):
        root.destroy()
        import staffmanagementpage
        staffmanagementpage.staffdetailspage(direct, datadirect)
        
    def customerservicepage(root, direct, datadirect):
        root.destroy()
        import customerservicepage
        customerservicepage.orderspage(direct, datadirect)

    def menupage(root, direct, datadirect):
        root.destroy()
        import menu
        menu.main_window(direct, datadirect)
   
    customtkinter.set_appearance_mode("dark")
    root = Tk()
    root.geometry('1366x768')
    root.state('zoomed')
    
    lploc = os.path.join(direct, r'images\landingpage.png')
    bgimage = ImageTk.PhotoImage(file=lploc)
    bglabel = Label(root, image=bgimage)
    bglabel.place(x=0, y=0)

    ibloc = os.path.join(direct, r'images\inventorybutton.png')
    inventoryimage = ImageTk.PhotoImage(file=ibloc)
    inventorybutton = Button(root, image = inventoryimage , fg='white', bg='white', activeforeground='white',
                        activebackground='white', cursor='hand2', bd=0, command=lambda:(inventorypage(root, direct, datadirect)))
    inventorybutton.place(x=35, y=80)

    smbloc = os.path.join(direct, r'images\staffmanagementbutton.png')
    staffmanagementimage = ImageTk.PhotoImage(file=smbloc)
    staffmanagementbutton = Button(root, image = staffmanagementimage , fg='white', bg='white', activeforeground='white',
                        activebackground='white', cursor='hand2', bd=0, command=lambda:(staffmanagementpage(root, direct, datadirect)))
    staffmanagementbutton.place(x=660, y=80)

    csbloc = os.path.join(direct, r'images\customerservicebutton.png')
    customerserviceimage = ImageTk.PhotoImage(file=csbloc)
    customerservicebutton = Button(root, image = customerserviceimage , fg='white', bg='white', activeforeground='white',
                        activebackground='white', cursor='hand2', bd=0, command=lambda:(customerservicepage(root, direct, datadirect)))
    customerservicebutton.place(x=40, y=365)

    mbloc = os.path.join(direct, r'images\menubutton.png')
    menuimage = ImageTk.PhotoImage(file=mbloc)
    menubutton = Button(root, image = menuimage , fg='white', bg='white', activeforeground='white',
                        activebackground='white', cursor='hand2', bd=0, command=lambda:(menupage(root, direct, datadirect)))
    menubutton.place(x=660, y=365)

    logoutbutton = Button(root, bg="white", fg="black", activebackground="white", activeforeground="black",
                          text="LOGOUT", font=('Garamond', 20), bd=0, cursor='hand2', command=lambda:(logout()))
    logoutbutton.place(x=1125, y=15)

    root.mainloop()

