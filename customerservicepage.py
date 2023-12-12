from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter
from PIL import ImageTk
import os
from openpyxl import *

final_directory = ""
"""customtkinter.set_appearance_mode("dark")
root = Tk()
root.geometry('1366x768')
root.state('zoomed')

bgimage = ImageTk.PhotoImage(file='customerservicepage.png')
bglabel = Label(root, image=bgimage)
bglabel.place(x=0, y=0)

ordersimage = ImageTk.PhotoImage(file='ordersbutton.png')
ordersbutton = Button(root, image = ordersimage , fg='white', bg='white', activeforeground='white',
                    activebackground='white', cursor='hand2', bd=0) #, command=orderspage)
ordersbutton.place(x=180, y=270)

reservationsimage = ImageTk.PhotoImage(file='reservationsbutton.png')
reservationsbutton = Button(root, image = reservationsimage , fg='white', bg='white', activeforeground='white',
                    activebackground='white', cursor='hand2', bd=0)#, command=reservationspage)
reservationsbutton.place(x=180, y=420)

root.mainloop()"""

def orderspage(registration_number):
    global final_directory
    global order
    def order(i):
        root.destroy()
        column = {"Item": "A", "Price":"B"}
        workbook1 = load_workbook(final_directory + r"\Menu.xlsx")
        worksheet1 = workbook1["Menu"]
        
        customtkinter.set_appearance_mode("dark")
        root1 = Tk()
        root1.geometry('1366x768')
        root1.state('zoomed')

        bgimage1 = ImageTk.PhotoImage(file='orderpage.png')
        bglabel = Label(root1, image=bgimage1)
        bglabel.place(x=0, y=0)

        tablelabel = Label(root1, text=f"TABLE {i}", bg="white", fg="black", font=("Garamond", 25), bd=0)
        tablelabel.place(x=150, y=500)

        # Create the canvas widget
        canvas = Canvas(root1, width=700, height=415, bg="white", bd=0, highlightbackground="white", highlightcolor="white")

        # Create the scrollbar widget
        scroll = Scrollbar(root1, orient=VERTICAL, command=canvas.yview, bd=0, highlightbackground="white", highlightcolor="white", troughcolor="black")
        canvas.config(yscrollcommand=scroll.set)

        # Create the frame widget
        frame = Frame(canvas, width=690, height=405, bg="white")

        capacity = []
        # Create labels and entry boxes and add them to the frame
        for i in range(2, int(worksheet1.max_row) + 1):  ###
            textvalue = worksheet1[f'{column["Item"]}{i}'].value
            pricevalue = worksheet1[f'{column["Price"]}{i}'].value
            exec(f'food{i}label = Label(frame, text=textvalue, bg="white", fg="black", font=("Garamond", 25), bd=0)')
            exec(f'price{i}label = Label(frame, text=pricevalue, bg="white", fg="black", font=("Garamond", 25), bd=0)')
            exec(f'food{i}label.grid(row=i, column=0, padx=70, pady=10)')
            exec(f'price{i}label.grid(row=i, column=1, padx=15, pady=10)')

        # Add the frame to the canvas
        canvas.create_window(10, 10, window=frame, anchor="nw")

        # Update the scrollregion of the canvas
        root.update()
        canvas.configure(scrollregion = canvas.bbox('all'))

        # Place the canvas and the scrollbar in the window
        canvas.place(x=240, y=185)
        scroll.place(x=955, y=185, height=415)
        
        root1.mainloop()
        
    current_directory = os.getcwd()
    directory = registration_number
    final_directory += os.path.join(current_directory, directory)
    workbook = load_workbook(final_directory + r"\Customer Service.xlsx")
    worksheet = workbook["Tables"]

    #root1.destroy()
    customtkinter.set_appearance_mode("dark")
    root = Tk()
    root.geometry('1366x768')
    root.state('zoomed')

    bgimage = ImageTk.PhotoImage(file='orderspage.png')
    bglabel = Label(root, image=bgimage)
    bglabel.place(x=0, y=0)
    
    # Create the canvas widget
    canvas = Canvas(root, width=700, height=415, bg="white", bd=0, highlightbackground="white", highlightcolor="white")

    # Create the scrollbar widget
    scroll = Scrollbar(root, orient=VERTICAL, command=canvas.yview, bd=0, highlightbackground="white", highlightcolor="white", troughcolor="black")
    canvas.config(yscrollcommand=scroll.set)

    # Create the frame widget
    frame = Frame(canvas, width=690, height=405, bg="white")

    capacity = []
    # Create labels and entry boxes and add them to the frame
    for i in range(1, int(worksheet.max_row)):
        print(locals())
        print(globals())
        exec(f'global table{i}orderbutton')
        exec(f'table{i}label = Label(frame, text=f"TABLE {i}", bg="white", fg="black", font=("Garamond", 25), bd=0)')
        exec(f'table{i}orderbutton = Button(frame, bg="#015450", fg="white", activebackground="#015450", activeforeground="white",text="ORDER", font=("Garamond", 20), bd=0, cursor="hand2", width=12, command = lambda: (order({i})))')
        exec(f'table{i}billingbutton = Button(frame, bg="#015450", fg="white", activebackground="#015450", activeforeground="white",text="BILLING", font=("Garamond", 20), bd=0, cursor="hand2", width=12)')
        exec(f'table{i}label.grid(row=i, column=0, padx=70, pady=10)')
        exec(f'table{i}orderbutton.grid(row=i, column=1, padx=15, pady=10)')
        exec(f'table{i}billingbutton.grid(row=i, column=2, padx=15, pady=10)')
        
    # Add the frame to the canvas
    canvas.create_window(10, 10, window=frame, anchor="nw")

    # Update the scrollregion of the canvas
    root.update()
    canvas.configure(scrollregion = canvas.bbox('all'))

    # Place the canvas and the scrollbar in the window
    canvas.place(x=240, y=185)
    scroll.place(x=955, y=185, height=415)

    root.mainloop()

orderspage("11111111111111")
