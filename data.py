from openpyxl import *
from tkinter import messagebox


def data(registration_number, email_id, password_, restaurant_name, phone_number, address_, state_, pincode_):
    column_names = {"Registration Number": "A", "Email": "B", "Password": "C", "Name": "D", "Phone Number": "E",
                    "Address": "F", "State": "G", "Pincode": "H"}

    try:
        workbook = load_workbook("User_Data.xlsx")
        worksheet = workbook["User Data"]

    except FileNotFoundError:
        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = "User Data"
        worksheet.append(list(column_names.keys()))
        workbook.save("User_Data.xlsx")
        
    for i in range(2, worksheet.max_row + 1):
        email_excel = worksheet[f'{column_names["Email"]}{i}'].value
        registration_excel = worksheet[f'{column_names["Registration Number"]}{i}'].value
        if registration_excel == registration_number:
            messagebox.showerror("Error", f"Account exists! Please login")
            break
        elif email_excel == email_id:
            messagebox.showerror("Error", f"Account exists! Please login or try again with a different email id")
            break
    else:
        worksheet[f'{column_names["Registration Number"]}{worksheet.max_row+1}'] = registration_number
        worksheet[f'{column_names["Email"]}{worksheet.max_row}'] = email_id
        worksheet[f'{column_names["Password"]}{worksheet.max_row}'] = password_
        worksheet[f'{column_names["Name"]}{worksheet.max_row}'] = restaurant_name
        worksheet[f'{column_names["Phone Number"]}{worksheet.max_row}'] = phone_number
        worksheet[f'{column_names["Address"]}{worksheet.max_row}'] = address_
        worksheet[f'{column_names["State"]}{worksheet.max_row}'] = state_
        worksheet[f'{column_names["Pincode"]}{worksheet.max_row}'] = pincode_
        workbook.save("User_Data.xlsx")

    workbook.close()
