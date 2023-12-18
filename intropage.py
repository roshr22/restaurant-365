from tkinter import *
import customtkinter
from PIL import ImageTk
import os

# Getting location of application data and stored in direct
direct = ""
def location(registration_number):
    global final_directory
    current_directory = os.getcwd()
    direct += current_directory

# Importing aboutpage
def nextpg(direct):
    root.destroy()
    import aboutpage
    aboutpage.aboutpage(direct)

# Creating a window
customtkinter.set_appearance_mode("dark")
root = Tk()
root.geometry('1366x768')
root.state('zoomed')

# Placing a background image
imgloc = os.path.join(direct, r'images\intro.png')
bgimage = ImageTk.PhotoImage(file=imgloc)
bglabel = Label(root, image=bgimage)
bglabel.place(x=0, y=0)

# Buttons
nextbutton = Button(root, text='Next', font=('Garamond', 25), fg='black', bg='#f2f2e2',
                    activeforeground='black', activebackground='#f2f2e8', cursor='hand2', bd=0,
                    command=lambda:(nextpg(direct)))
nextbutton.place(x=1075, y=560)


root.mainloop()
