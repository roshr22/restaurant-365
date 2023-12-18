from tkinter import *
from tkinter import messagebox
import customtkinter
from PIL import ImageTk
from openpyxl import *
import bcrypt
import os

def login_page(direct, root1):
    root1.destroy()
    count = 0
    
    def signup(root1, direct):
        import signuppage
        signuppage.signup_page(direct, root1)

    def email(event):
        if emailid.get() == 'Enter Email Id':
            emailid.delete(0, END)

    def passwd(event):
        if password.get() == 'Enter Password':
            password.delete(0, END)
            password.configure(show='*')

    def hide():
        closeyeimg = os.path.join(direct, r'images\closeye.png')
        openeye.configure(file=closeyeimg)
        password.configure(show='')
        eyebutton.configure(command=show)
        
    def show():
        openeyeimg = os.path.join(direct, r'images\openeye.png')
        openeye.configure(file=openeyeimg)
        password.configure(show='*')
        eyebutton.configure(command=hide)

    def verification(direct):
        email_id = emailid.get()
        password_ = password.get().encode('UTF-8')
        column_names = {"Registration Number": "A", "Email": "B", "Password": "C", "Name": "D", "Phone Number": "E",
                        "Address": "F", "State": "G", "Pincode": "H"}

        try:
            workbookpath = os.path.join(direct, r'User_Data.xlsx')
            workbook = load_workbook(workbookpath)
            worksheet = workbook["User Data"]

        except FileNotFoundError:
            messagebox.showerror('Error', "Account doesn't exist! Sign up now!")
            return

        for i in range(2, worksheet.max_row + 1):
            email_excel = worksheet[f'{column_names["Email"]}{i}'].value
            password_excel = worksheet[f'{column_names["Password"]}{i}'].value.encode('UTF-8')
            registration_excel = worksheet[f'{column_names["Registration Number"]}{i}'].value
            if email_excel == email_id and bcrypt.checkpw(password_, password_excel):
                datadirect = os.path.join(direct, registration_excel)
                root.destroy()
                import landingpage
                landingpage.landingpage(direct, datadirect)
                break
            elif email_excel == email_id and not bcrypt.checkpw(password_, password_excel):
                messagebox.showerror("Error", "Incorrect Password! Try again")
                break
        else:
            messagebox.showerror("Error", f"{email_id} not registered... Sign up now!")

        workbook.close()
            
    customtkinter.set_appearance_mode("dark")
    root = Tk()
    root.geometry('1366x768')
    root.state('zoomed')

    # Placing a background colour
    bgimg = os.path.join(direct, r'images\login.png')
    loginimage = ImageTk.PhotoImage(file=bgimg)
    loginimagelabel = Label(root, image=loginimage)
    loginimagelabel.place(x=0, y=0)

    loginlabel = Label(root, bg="white", fg="black", text="Login", font=('Garamond', 60, "bold"), bd=0)
    loginlabel.place(x=285, y=60)

    # Email Id
    emailid = Entry(root, bg="white", fg="black", font=('Garamond', 20), width=28, bd=0)
    emailid.place(x=190, y=210)
    emailid.insert(0, "Enter Email Id")
    emailid.bind('<FocusIn>', email)
    line1 = Frame(root, height=2, width=375, bg="black")
    line1.place(x=185, y=255)

    # Password
    password = Entry(root, bg="white", fg="black", font=('Garamond', 20), width=28, bd=0)
    password.place(x=190, y=310)
    password.insert(0, "Enter Password")
    password.bind('<FocusIn>', passwd)
    line5 = Frame(root, height=2, width=375, bg="black")
    line5.place(x=185, y=355)
    openeyeimg = os.path.join(direct, r'images\openeye.png')
    openeye = PhotoImage(file=openeyeimg)
    eyebutton = Button(root, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
    eyebutton.place(x=550, y=320)

    loginbutton = Button(root, bg="#015450", fg="white", activebackground="#015450", activeforeground="white",
                         text="Login", font=('Garamond', 20), bd=0, cursor='hand2', command=lambda:(verification(direct)))
    loginbutton.place(x=350, y=410)

    signupbutton = Button(root, bg="white", fg="black", activebackground="white", activeforeground="#015450",
                          text="New to Restaurant 365? Click here to signup", font=('Garamond', 20, "underline"), bd=0,
                          command=lambda: (signup(root, direct)), cursor='hand2')
    signupbutton.place(x=140, y=470)
    root.mainloop()
