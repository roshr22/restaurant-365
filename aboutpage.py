from tkinter import *
import customtkinter
from PIL import ImageTk

# customtkinter and tkinter are used for GUI


def aboutpage():
    def signup(root1):
        import signuppage
        signuppage.signup_page(root1)

    def login(root1):
        import loginpage
        loginpage.login_page(root1)

    # Creating a window
    customtkinter.set_appearance_mode("dark")
    root = Tk()
    root.geometry('1366x768')
    root.state('zoomed')

    # Placing a background image
    bgimage = ImageTk.PhotoImage(file='about.png')
    bglabel = Label(root, image=bgimage)
    bglabel.place(x=0, y=0)

    # Buttons
    signupbutton = Button(root, text="Sign Up", font=('Garamond', 25), fg="#015450", bg='#D6E3E2',
                          activeforeground='#015450', activebackground='#D6E3E2', cursor='hand2', bd=0,
                          command=lambda: (signup(root)))
    signupbutton.place(x=240, y=510)

    loginbutton = Button(root, text="Login", font=('Garamond', 25), fg="#015450", bg='#D6E3E2',
                         activeforeground='#015450', activebackground='#D6E3E2', cursor='hand2', bd=0,
                         command=lambda: (login(root)))
    loginbutton.place(x=440, y=510)

    root.mainloop()
