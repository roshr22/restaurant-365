from tkinter import *
import customtkinter
from PIL import ImageTk


# customtkinter and tkinter are used for GUI

def nextpg():  # Importing aboutpage
    root.destroy()
    import aboutpage
    aboutpage.aboutpage()
# GUI
# Creating a window


customtkinter.set_appearance_mode("dark")
root = Tk()
root.geometry('1366x768')
root.state('zoomed')

# Placing a background image
bgImage = ImageTk.PhotoImage(file='intro.png')
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

# Buttons
nextbutton = Button(root, text='Next', font=('Garamond', 25), fg='black', bg='#f2f2e2', activeforeground='black',
                    activebackground='#f2f2e8', cursor='hand2', bd=0, command=nextpg)
nextbutton.place(x=1075, y=560)


root.mainloop()
