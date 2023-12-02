import smtplib
from email.message import EmailMessage
import random
from tkinter import *
from tkinter import messagebox
import customtkinter
from PIL import ImageTk
import sys

otp = 0


def verification_window(name, email_id, root1, registration_number, password_, restaurant_name, phone_number, address_,
                        state_, pincode_):
    global otp
    count = 0

    def generate_otp():
        nonlocal count
        OTP = otpentry.get()
        if OTP.isdigit() is False or len(OTP) != 6:
            messagebox.showerror('Error', 'Enter Valid OTP')

        elif count > 1:
            messagebox.showerror('Error', 'Invalid OTP entered 3 times! Please try again later...')
            root.destroy()
            sys.exit(0)
            
        elif int(OTP) == otp and count < 2:
            data(registration_number, email_id, password_, restaurant_name, phone_number, address_, state_, pincode_)
        
        elif int(OTP) != otp and count < 2:
            messagebox.showerror('Error', 'Invalid OTP! Resending OTP...')
            verification(name, email_id)
            count += 1

    def data(registration_number, email_id, password_, restaurant_name, phone_number, address_, state_, pincode_):
        import data
        data.data(registration_number, email_id, password_, restaurant_name, phone_number, address_, state_, pincode_)
    
    verification(name, email_id)
    root1.destroy()
    customtkinter.set_appearance_mode("dark")
    root = Tk()
    root.geometry('1366x768')
    root.state('zoomed')

    # Placing a background colour
    bgframe = Label(root, bg="white", width=1366, height=768)
    bgframe.place(x=0, y=0)
    bgimage = ImageTk.PhotoImage(file='emailverification.png')
    bglabel = Label(root, image=bgimage, bd=0)
    bglabel.pack()

    otplabel = Label(root, text=f"OTP has been sent to your \nregistered email id: \n{email_id}", bg="white",
                     fg="black", font=('Garamond', 18), bd=0)
    otplabel.place(x=505, y=305)
    otpentry = Entry(root, bg="white", fg="black", font=('Garamond', 20), width=6, bd=0)
    otpentry.place(x=590, y=415)
    line = Frame(root, height=2, width=90, bg="grey")
    line.place(x=587, y=450)

    confirmbutton = Button(root, bg="#015450", fg="white", activebackground="#015450", activeforeground="white",
                           text="Confirm", font=('Garamond', 18), command=generate_otp, bd=0, cursor='hand2')
    confirmbutton.place(x=585, y=480)
    root.mainloop()


def verification(name, email_id):
    global otp

    def gen_otp():
        OTP = random.randint(100000, 999999)
        return OTP
    email_sender = "metamorphosisrestaurant365@gmail.com"
    email_password = "crbh givt ayhd cxct"
    email_receiver = email_id
    otp = gen_otp()
    subject = "OTP Verification for Restaurant 365 Account Registration"
    body = f"""Dear {name},

Welcome to Restaurant 365! We're excited to have you on board, and thank you for choosing our platform.

To verify your identity, please enter the below OTP on your application window.

Your One-Time Password (OTP) is: {otp}.

We're thrilled to have you join Restaurant 365, and we look forward to providing you with a seamless and secure experience.

Best regards,

Team Restaurant 365"""

    email = EmailMessage()
    email['from'] = email_sender
    email['to'] = email_receiver  # receiver's email id
    email['subject'] = subject     # subject of the email

    email.set_content(body)  # Content to be sent
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()  # Identify yourself to an ESMTP server using EHLO
        smtp.starttls()  # Put the SMTP connection in TLS (Transport Layer Security) mode
        smtp.login(email_sender, email_password)  # Sender's email ID and password
        smtp.send_message(email)
