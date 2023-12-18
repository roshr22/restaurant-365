from tkinter import *
import customtkinter
from PIL import ImageTk
import os

#Aboutpage
def aboutpage(direct):

    #Importing signup page
    def signup(root1, direct):
        import signuppage
        signuppage.signup_page(direct, root1)

    #importing login page
    def login(root1, direct):
        import loginpage
        loginpage.login_page(direct, root1)

    # Creating a window
    customtkinter.set_appearance_mode("dark")
    root = Tk()
    root.geometry('1366x768')
    root.state('zoomed')

    # Placing a background image
    imgloc = os.path.join(direct, r'images\about.png')
    bgimage = ImageTk.PhotoImage(file=imgloc)
    bglabel = Label(root, image=bgimage)
    bglabel.place(x=0, y=0)

    # Buttons
    signupbutton = Button(root, text="Sign Up", font=('Garamond', 25), fg="white", bg='#015450',
                          activeforeground='white', activebackground='#015450', cursor='hand2', bd=0,
                          command=lambda: (signup(root, direct)))
    signupbutton.place(x=240, y=510)

    loginbutton = Button(root, text="Login", font=('Garamond', 25), fg="white", bg='#015450',
                         activeforeground='white', activebackground='#015450', cursor='hand2', bd=0,
                         command=lambda: (login(root, direct)))
    loginbutton.place(x=440, y=510)

    root.mainloop()
