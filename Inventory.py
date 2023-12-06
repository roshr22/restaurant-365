#Inventory: Getting Ingredient and Quantity input from user
from openpyxl import *
from tkinter import *
from tkinter import messagebox
def addprod():
    global prod1,quant1,maxv1
    prod_name=prod1
    quant_val=quant1
    max_val=maxv1
    for i in range(2, workbook_sheet.max_row + 1):
        product = workbook_sheet[f'{column_names["Product"]}{i}'].value
        if product==prod_name:
            messagebox.showerror("Error",f"{prod_name}exists!")
            break
    else:
        workbook_sheet[f'{column_names["Product"]}{workbook_sheet.max_row + 1}'] = prod_name
        workbook_sheet[f'{column_names["Quantity"]}{workbook_sheet.max_row}'] = quant_val
        workbook_sheet[f'{column_names["Max Capacity"]}{workbook_sheet.max_row}'] = max_val
        workbook.save("test.xlsx")
        

def remprod():
    global prod1
    temp=0
    prod_name=prod1
    for i in range(2, workbook_sheet.max_row + 1):
        product = workbook_sheet[f'{column_names["Product"]}{i}'].value
        if product==prod_name:
            workbook_sheet[f'{column_names["Product"]}{i}']=''
            workbook_sheet[f'{column_names["Quantity"]}{i}']=''
            workbook_sheet[f'{column_names["Max Capacity"]}{i}']=''
            temp=i
            workbook_sheet.delete_rows(temp, 1)
            workbook.save("test.xlsx")
            break

            
            
    else:
       messagebox.showerror("Error",f"{prod_name} doesn't exist")
  
    
'''def saveprod():
    prod_name=prod.get()
    quant_val=int(quant.get())
    for i in range(2, workbook_sheet.max_row + 1):
        product = workbook_sheet[f'{column_names["Product"]}{i}'].value
        quantity = workbook_sheet[f'{column_names["Quantity"]}{i}'].value
        if product == prod_name and quantity:
            workbook_sheet[f'{column_names["Quantity"]}{i}']=workbook_sheet[f'{column_names["Quantity"]}{i}'].value+quant_val
            workbook.save("test.xlsx")
            break
        elif product == prod_name and not quantity:
            workbook_sheet[f'{column_names["Quantity"]}{i}']=quant_val
            workbook.save("test.xlsx")
            break
    else:
        messagebox.showerror("Error",f"{prod_name} dosen't exist!")
        
def removequantity():
    prod_name=prod.get()
    quant_val=int(quant.get())
    for i in range(2, workbook_sheet.max_row + 1):
        product = workbook_sheet[f'{column_names["Product"]}{i}'].value
        quantity = workbook_sheet[f'{column_names["Quantity"]}{i}'].value
        if product == prod_name and quantity:
            workbook_sheet[f'{column_names["Quantity"]}{i}']=workbook_sheet[f'{column_names["Quantity"]}{i}'].value-quant_val
            if workbook_sheet[f'{column_names["Quantity"]}{i}'].value<0:
                messagebox.showerror("Error","Invalid quantity input!")
            else:
                workbook.save("test.xlsx")
            break
        elif product == prod_name and not quantity:
            workbook_sheet[f'{column_names["Quantity"]}{i}']=quant_val
            workbook.save("test.xlsx")
            break
    else:
        messagebox.showerror("Error",f"{prod_name} dosen't exist in inventory!")
        

def below_threshold():
    for i in range(2,workbook_sheet.max_row+1):
        product= workbook_sheet[f'{column_names["Product"]}{i}'].value
        quantity = workbook_sheet[f'{column_names["Quantity"]}{i}'].value
        m_quantity=workbook_sheet[f'{column_names["Max Capacity"]}{i}'].value
        if quantity<=0.1*m_quantity:
            messagebox.showerror("Error",f"Alert!{product} is below threshold! Purchase soon!")'''

column_names = {"Product":"A", "Quantity":"B", "Max Capacity":"C"}

try:
    workbook = load_workbook("test.xlsx")
    workbook_sheet = workbook.active
except FileNotFoundError:
    workbook = Workbook()
    workbook_sheet = workbook.active
    workbook_sheet.title = "Inventory"
    workbook_sheet.append(list(column_names.keys()))
    workbook.save("test.xlsx")

def close_window():
    root.destroy()
def new_window1():
    global prod1, quant1, maxv1
    def prod2():
        global prod1, quant1, maxv1
        prod1+=prod.get()
        quant1+=int(quant.get())
        maxv1+=int(maxv.get())
    
    root=Tk()
    root.title("Add new product")
    root.geometry("1200x800")
    f=Frame(root,height=600,width=1000)
    f.pack()
    prod=Entry(f, width=50)
    prod.place(x=300, y=300)
    prodlabel=Label(f, text="Product")
    prodlabel.place(x=100, y=300)
    quant = Entry(f, width=50)
    quant.place(x=300, y=350)
    quantlabel=Label(f, text="Quantity")
    quantlabel.place(x=100, y=350)
    maxv=Entry(f, width=50)
    maxv.place(x=300,y=400)
    maxvlabel=Label(f, text="Quantity")
    maxvlabel.place(x=100, y=400)
    add=Button(f,text="Add new product", command=lambda:(prod2(),addprod()))
    add.place(x=300,y=450)
    root.mainloop()

def new_window2():
    global prod1
    def prod3():
        global prod1
        prod1+=prod.get()

    r=Tk()
    r.title("Remove existing product")
    r.geometry("1200x800")
    f=Frame(r,height=600,width=1000)
    f.pack()
    prod=Entry(f, width=50)
    prod.place(x=300, y=300)
    prodlabel=Label(f, text="Product")
    remove=Button(f,text='Remove existing product', command=lambda:(prod3(),remprod()))
    remove.place(x=300,y=400)
    r.mainloop()
    

prod1=""
quant1=0
maxv1=0
root = Tk()
root.title("Inventory")
root.geometry("1200x800")
fr=Frame(root,height=600,width=1000)
fr.pack()
add_new_prod=Button(fr,text="Add new product", command=lambda:(close_window(),new_window1()))
add_new_prod.place(x=300,y=300)
remove_prod=Button(fr,text="Remove existing product", command=lambda:(close_window(),new_window2()))
remove_prod.place(x=300,y=400)
root.mainloop()

'''root = Tk()
root.title("Inventory")
root.geometry("1200x800")
frame = Frame(root, height = 600, width = 1000)
frame.pack()
prod= Entry(frame, width=50)
prod.place(x=300, y=300)
quant = Entry(frame, width=50)
quant.place(x=300, y=350)


add = Button(frame, text = "Add", command = lambda:(saveprod(),below_threshold()))
rem=Button(frame, text="Remove", command=lambda:(removequantity(),below_threshold()))
add.place(x=300, y=500)
rem.place(x=550,y=500)

root.mainloop()'''


