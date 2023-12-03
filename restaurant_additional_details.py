from tkinter import *
import customtkinter
import os
from openpyxl import *


class Table:
    def __init__(self, name, capacity, occupied = False):
        self.name = "Table " + name
        self.capacity = capacity
        self.occupied = occupied


column_names = {"Table Number": "A", "Capacity": "B", "Occupied": "C"}
final_directory = ""

def excel(registration_number):
    global final_directory
    current_directory = os.getcwd()
    directory = registration_number
    final_directory = os.path.join(current_directory, directory)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Tables"
    worksheet.append(list(column_names.keys()))
    final_directory += r"\Customer Service.xlsx"
    workbook.save(final_directory)



def number_of_tables(registration_number):  # Add root1,
    def table_count(event):
        if tablecount.get() == 'Enter Table Count':
            tablecount.delete(0, END)

    # root1.destroy()
    excel(registration_number)
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
                            text="Continue", font=('Garamond', 20), bd=0, cursor='hand2',
                            command=lambda: (tables(tablecount.get(), root)))
    continuebutton.place(x=350, y=410)
    root.mainloop()


def tables(tablecount, root1):

    def tabledata(capacity):
        workbook = load_workbook(final_directory)
        worksheet = workbook["Tables"]
        for x in range(1, int(tablecount)+1):
            exec(f'table_{x} = Table(str({x}),capacity[{x-1}].get())')
            exec(f'table = table_{x}')
            exec(f"worksheet[f'{column_names['''Table Number''']}{worksheet.max_row + 1}'] = table_{x}.name")
            exec(f"worksheet[f'{column_names['''Capacity''']}{worksheet.max_row}'] = table_{x}.capacity")
            exec(f"worksheet[f'{column_names['''Occupied''']}{worksheet.max_row}'] = table_{x}.occupied")
            workbook.create_sheet(title=f'Table {x}')
            workbook.save(final_directory)


    root1.destroy()
    customtkinter.set_appearance_mode("dark")
    root = Tk()
    root.geometry('1366x768')
    root.state('zoomed')

    # Create the canvas widget
    canvas = Canvas(root, width=400, height=300)

    # Create the scrollbar widget
    scroll = Scrollbar(root, orient=VERTICAL, command=canvas.yview)

    # Configure the canvas widget to use the scrollbar
    canvas['yscrollcommand'] = scroll.set

    # Create the frame widget
    frame = Frame(canvas)

    capacity = []
    # Create 10 labels and entry boxes and add them to the frame
    for i in range(1, int(tablecount)+1):
        exec(f'table{i}label = Label(frame, text=f"Table {i}")')
        exec(f'table{i}capacity = Entry(frame)')
        exec(f'capacity.append(table{i}capacity)')
        exec(f'table{i}label.grid(row=i, column=0, padx=10, pady=10)')
        exec(f'table{i}capacity.grid(row=i, column=2, padx=10, pady=10)')

    # Add the frame to the canvas
    canvas.create_window(0, 0, anchor=NW, window=frame)

    # Update the scrollregion of the canvas
    root.update()
    canvas['scrollregion'] = canvas.bbox('all')

    # Place the canvas and the scrollbar in the window
    canvas.grid(row=0, column=0, sticky=N + S + E + W)
    scroll.grid(row=0, column=1, sticky=N + S)

    continuebutton = Button(root, bg="#015450", fg="white", activebackground="#015450", activeforeground="white",
                            text="Continue", font=('Garamond', 20), bd=0, cursor='hand2',
                            command=lambda: (tabledata(capacity)))
    continuebutton.place(x=350, y=410)

    # Start the main loop
    root.mainloop()


number_of_tables("11111111111111")
