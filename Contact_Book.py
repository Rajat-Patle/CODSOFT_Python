import tkinter as tk
import mysql.connector
import tkinter.messagebox
from tkinter import simpledialog

conn = mysql.connector.connect(host="localhost", user="root", password="")
cur = conn.cursor(buffered=True)

try:
    cur.execute("USE contact_db")
except mysql.connector.Error:
    cur.execute("CREATE DATABASE contact_db")
    cur.execute("USE contact_db")

def add_Contact():
          try:
                    
                    global cur, conn  
                    sql = f"INSERT INTO contact_db (Name, Phone_no, E_mail, Address) VALUES ('{e2.get()}','{e3.get()}','{e4.get()}','{e5.get()}')"
                    cur.execute(sql)
                    conn.commit()
                    msg = "Contact has been Added Successfully !!"
                    tkinter.messagebox.showinfo("Contact List",msg)
          except Exception as E:
                    print(E)

def view_Contact():
    try:
        sql = "SELECT * FROM contact_db"
        cur.execute(sql)
        rows = cur.fetchall()
        data = ""
        for idx, a in enumerate(rows, start=1):
            data += f"ID: {idx}\nName: {a[1]}\nPhone No.: {a[2]}\nE-mail: {a[3]}\nAddress: {a[4]}\n\n"
        tkinter.messagebox.showinfo("Contact List", data)
    except Exception as E:
        print(E)

def delete_Contact():
    try:
        selected_contact_Name = simpledialog.askstring("Delete Contact", "Enter the Name of the contact to delete:")

        if selected_contact_Name is not None:
            sql = f"DELETE FROM contact_db WHERE Name = '{selected_contact_Name}'"
            cur.execute(sql)
            conn.commit()

            tkinter.messagebox.showinfo("Contact Deleted", f"Contact with Name {selected_contact_Name} has been deleted.")
            view_Contact()
    except Exception as E:
        print(E)

def update_Contact():
    try:
        selected_contact_Name = simpledialog.askstring("Update Contact", "Enter the Name of the contact to update:")

        if selected_contact_Name is not None:
            sql_fetch = f"SELECT * FROM contact_db WHERE Name = '{selected_contact_Name}'"
            cur.execute(sql_fetch)
            existing_contact = cur.fetchone()

            if existing_contact:
                new_name = simpledialog.askstring("Update Contact", f"Enter new Name for {selected_contact_Name}:")
                new_phone = simpledialog.askstring("Update Contact", f"Enter new Phone number for {selected_contact_Name}:")
                new_email = simpledialog.askstring("Update Contact", f"Enter new E-mail for {selected_contact_Name}:")
                new_address = simpledialog.askstring("Update Contact", f"Enter new Address for {selected_contact_Name}:")

                sql_update = f"UPDATE contact_db SET Name = '{new_name}', Phone_no = '{new_phone}', E_mail = '{new_email}', Address = '{new_address}' WHERE Name = '{selected_contact_Name}'"
                cur.execute(sql_update)
                conn.commit()

                tkinter.messagebox.showinfo("Contact Updated", f"Contact with Name {selected_contact_Name} has been updated.")
                view_Contact()
            else:
                tkinter.messagebox.showinfo("Contact Not Found", f"No contact found with Name {selected_contact_Name}.")
    except Exception as E:
        print(E)

def search_Contact():
    try:
        search_criteria = simpledialog.askstring("Search Contact", "Enter the search criteria (Name, Phone number, etc.):")

        if search_criteria is not None:
            sql_search = f"SELECT * FROM contact_db WHERE Name LIKE '%{search_criteria}%' OR Phone_no LIKE '%{search_criteria}%' OR E_mail LIKE '%{search_criteria}%' OR Address LIKE '%{search_criteria}%'"
            cur.execute(sql_search)
            matching_contacts = cur.fetchall()

            if matching_contacts:
                data = ""
                for idx, contact in enumerate(matching_contacts, start=1):
                    data += f"ID: {idx}\nName: {contact[1]}\nPhone No.: {contact[2]}\nE-mail: {contact[3]}\nAddress: {contact[4]}\n\n"
                tkinter.messagebox.showinfo("Matching Contacts", data)
            else:
                tkinter.messagebox.showinfo("No Matching Contacts", f"No contacts found matching the criteria: {search_criteria}")
    except Exception as E:
        print(E)                   
                    
top = tk.Tk()
top.title("Contact Book")
top.geometry("700x500")

# Label
l1 = tk.Label(top, text="Enter Your Details:-")
l2 = tk.Label(top, text="Enter Name:")
l3 = tk.Label(top, text="Enter Phone number:")
l4 = tk.Label(top, text="Enter E-mail:")
l5 = tk.Label(top, text="Enter Address:")

l1.grid(row=1, column=1)
l2.grid(row=2, column=1)
l3.grid(row=3, column=1)
l4.grid(row=4, column=1)
l5.grid(row=5, column=1)

# Text Boxes
e2 = tk.Entry(top)
e3 = tk.Entry(top)
e4 = tk.Entry(top)
e5 = tk.Entry(top)

e2.grid(row=2, column=2)
e3.grid(row=3, column=2)
e4.grid(row=4, column=2)
e5.grid(row=5, column=2)

B1 = tk.Button(top, text="Add Contact", command=add_Contact)
B1.grid(row=7, column=1)

b2 = tk.Button(top,text="View Contact", command=view_Contact)
b2.grid(row=7,column=3)

b3 = tk.Button(top,text="Delete Contact",command=delete_Contact)
b3.grid(row=8,column=1)

b4 = tk.Button(top,text="Update Contact",command=update_Contact)
b4.grid(row=8,column=3)

b5 = tk.Button(top,text="Search Contact",command=search_Contact)
b5.grid(row=9,column=2)
tk.mainloop()
