from tkinter import messagebox, Tk, Toplevel, StringVar, Radiobutton, Entry, Label, Button, Scrollbar, ttk


def login():
    username = username_Var.get()
    password = password_Var.get()

    if username == "kshitij" and password == "kshitij123":
        login_window.destroy()

        root.deiconify()

    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def open_login_window():
    global login_window
    root.withdraw()
    login_window = Toplevel()
    login_window.title("Login")
    login_window.geometry("500x300")
    login_window.config(bg="lightblue")

    Label(login_window, text="Username:", bg="lightblue").pack(pady=10)
    Entry(login_window, textvariable=username_Var, bg="lightgray").pack(pady=10)
    Label(login_window, text="Password:", bg="lightblue").pack(pady=10)
    Entry(login_window, textvariable=password_Var, show="*", bg="lightgray").pack(pady=10)
    Button(login_window, text="Login", command=login, bg="green", fg="white").pack(pady=15)


import tkinter
import tkinter.ttk as ttk
from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("AlumniConnect")
root.geometry("780x400+0+0")
root.config(bg="Pink")

f_name = StringVar()
m_name = StringVar()
l_name = StringVar()
age = StringVar()
home_address = StringVar()
gender = StringVar()
phone_number = StringVar()


def Reset():
    f_name.set("")
    m_name.set("")
    l_name.set("")
    gender.set("")
    age.set("")
    home_address.set("")
    phone_number.set("")


def search():
    search_query = search_var.get().lower()

    tree.delete(*tree.get_children())

    connectn = sqlite3.connect("contactdata.db")
    cursor = connectn.cursor()

    cursor.execute(
        "SELECT * FROM `contactinformation` WHERE LOWER(`first_name`) LIKE ? OR LOWER(`last_name`) LIKE ? OR LOWER(`home_address`) LIKE ? OR LOWER(`phone_number`) LIKE ?",
        ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%'))

    fetchinfo = cursor.fetchall()

    for data in fetchinfo:
        tree.insert('', 'end', values=(data))

    cursor.close()
    connectn.close()


# For creating the database and the table
# For creating the database and the table
def Database():
    connectn = sqlite3.connect("contactdata.db")
    cursor = connectn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `contactinformation` (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, first_name TEXT, middle_name TEXT, last_name TEXT, gender TEXT, age TEXT, home_address TEXT, phone_number TEXT)")
    cursor.execute("SELECT * FROM `contactinformation` ORDER BY `last_name` ASC")
    fetchinfo = cursor.fetchall()
    for data in fetchinfo:
        tree.insert('', 'end', values=(data))
    cursor.close()
    connectn.close()


# Function for exiting the system
def Exit():
    O = tkinter.messagebox.askyesno("Alumni", "Do you want to exit the system")
    if O > 0:
        root.destroy()
        return


# Insert query for inserting the value in database Table
def Submit():
    if f_name.get() == "" or m_name.get() == "" or l_name.get() == "" or gender.get() == "" or age.get() == "" or home_address.get() == "" or phone_number.get() == "":
        msgg = messagebox.showwarning('', 'Please Complete All the Fields', icon="warning")
    else:
        tree.delete(*tree.get_children())
        connectn = sqlite3.connect("contactdata.db")
        cursor = connectn.cursor()

        cursor.execute(
            "INSERT INTO `contactinformation` (first_name, middle_name, last_name, gender, age, home_address, phone_number ) VALUES(?, ?, ?, ?, ?, ?, ?)",
            (str(f_name.get()), str(m_name.get()), str(l_name.get()), str(gender.get()), int(age.get()),
             str(home_address.get()),
             int(phone_number.get())))

        connectn.commit()
        cursor.execute("SELECT * FROM `contactinformation` ORDER BY `last_name` ASC")
        fetchinfo = cursor.fetchall()

    for data in fetchinfo:
        tree.insert('', 'end', values=(data))
    cursor.close()
    connectn.close()
    f_name.set("")
    m_name.set("")
    l_name.set("")
    gender.set("")
    age.set("")
    home_address.set("")
    phone_number.set("")


# Update Query for updating the table in the database
def Update():
    if gender.get() == "":
        msgg = tkinter.messagebox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        connectn = sqlite3.connect("contactdata.db")
        cursor = connectn.cursor()
        cursor.execute(
            "UPDATE `contactinformation` SET `first_name` = ?, `middle_name` = ? , `last_name` = ?, `gender` =?, `age` = ?, `home_address` = ?, `phone_number` = ? WHERE `id` = ?",
            (str(f_name.get()), str(m_name.get()), str(l_name.get()), str(gender.get()), int(age.get()),
             str(home_address.get()),
             str(phone_number.get()), int(id)))
        connectn.commit()
        cursor.execute("SELECT * FROM `contactinformation` ORDER BY `last_name` ASC")
        fetchinfo = cursor.fetchall()
        for data in fetchinfo:
            tree.insert('', 'end', values=(data))
        gender1 = gender.get()
        if not gender1:
            tkinter.messagebox.showerror("Please select the gender")
        cursor.close()
        connectn.close()
        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")


# Module for the update contact form window
def UpdateContact(event):
    global id, UpdateWindow
    curItem = tree.focus()
    contents = (tree.item(curItem))
    item = contents['values']
    id = item[0]
    f_name.set("")
    m_name.set("")
    l_name.set("")
    gender.set("")
    age.set("")
    home_address.set("")
    phone_number.set("")

    f_name.set(item[1])
    m_name.set(item[2])
    l_name.set(item[3])

    age.set(item[5])
    home_address.set(item[6])
    phone_number.set(item[7])

    UpdateWindow = Toplevel()
    UpdateWindow.title("Contact Information")
    UpdateWindow.geometry("500x520+0+0")
    UpdateWindow.resizable(0, 0)
    if 'Opennewwindow' in globals():
        'Opennewwindow'.destroy()

    # FRAMES
    # module is for the frame, labels, text entry, and button for update contact form window
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=gender, value="Male", font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=gender, value="Female", font=('arial', 14)).pack(side=LEFT)

    # LABELS
    label_title = Label(FormTitle, text="Update the Alumni Information", font=('Arial', 17), bg="light green",
                        width=400)
    label_title.pack(fill=X)
    label_FirstName = Label(ContactForm, text="First Name", font=('Calibri', 14), bd=5)
    label_FirstName.grid(row=0, sticky=W)

    label_MiddleName = Label(ContactForm, text="Last Name", font=('Calibri', 14), bd=5)
    label_MiddleName.grid(row=1, sticky=W)

    label_LastName = Label(ContactForm, text="Grad Year", font=('Calibri', 14), bd=5)
    label_LastName.grid(row=2, sticky=W)

    label_Gender = Label(ContactForm, text="Gender", font=('Calibri', 14), bd=5)
    label_Gender.grid(row=3, sticky=W)

    label_Age = Label(ContactForm, text="Age", font=('Calibri', 14), bd=5)
    label_Age.grid(row=4, sticky=W)

    label_HomeAddress = Label(ContactForm, text=" Comapany", font=('Calibri', 14), bd=5)
    label_HomeAddress.grid(row=5, sticky=W)

    label_PhoneNumber = Label(ContactForm, text="Phone Number", font=('Calibri', 14), bd=5)
    label_PhoneNumber.grid(row=6, sticky=W)

    # TEXT ENTRY
    FirstName = Entry(ContactForm, textvariable=f_name, font=('Calibri', 14, 'bold'), bd=2, width=20, justify='left')
    FirstName.grid(row=0, column=1)

    MiddleName = Entry(ContactForm, textvariable=m_name, font=('Calibri', 14, 'bold'), bd=2, width=20, justify='left')
    MiddleName.grid(row=1, column=1)

    LastName = Entry(ContactForm, textvariable=l_name, font=('Calibri', 14, 'bold'), bd=2, width=20, justify='left')
    LastName.grid(row=2, column=1)

    RadioGroup.grid(row=3, column=1)

    Age = Entry(ContactForm, textvariable=age, font=('Calibri', 14, 'bold'), bd=2, width=20, justify='left')
    Age.grid(row=4, column=1)

    HomeAddress = Entry(ContactForm, textvariable=home_address, font=('Calibri', 14, 'bold'), bd=2, width=20,
                        justify='left')
    HomeAddress.grid(row=5, column=1)

    PhoneNumber = Entry(ContactForm, textvariable=phone_number, font=('Calibri', 14, 'bold'), bd=2, width=20,
                        justify='left')
    PhoneNumber.grid(row=6, column=1)

    #  Buttons
    ButtonUpdatContact = Button(ContactForm, text='Update', bd=2, font=('Calibri', 14, 'bold'), fg="black",
                                bg="lightgreen", command=Update)
    ButtonUpdatContact.grid(row=8, columnspan=2, pady=10)


# Delete query for deleting the value
def Delete():
    if not tree.selection():
        msgg = tkinter.messagebox.showwarning('', 'Please Select the data!', icon="warning")
    else:
        msgg = tkinter.messagebox.askquestion('', 'Are You Sure You Want To Delete', icon="warning")
    if msgg == 'yes':
        curItem = tree.focus()
        contents = (tree.item(curItem))
        item = contents['values']
        tree.delete(curItem)
        connectn = sqlite3.connect("contactdata.db")
        cursor = connectn.cursor()
        cursor.execute("DELETE FROM `contactinformation` WHERE `id` = %d" % item[0])
        connectn.commit()
        cursor.close()
        connectn.close()


# For creating the frame, labels, text entry, and button for add new contact form window
def MyNewContact():
    global opennewwindow
    f_name.set("")
    m_name.set("")
    l_name.set("")
    gender.set("")
    age.set("")
    home_address.set("")
    phone_number.set("")

    Opennewwindow = Toplevel()
    Opennewwindow.title("Contact Details")
    Opennewwindow.resizable(0, 0)
    Opennewwindow.geometry("500x500+0+0")
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()

    #############Frames####################
    FormTitle = Frame(Opennewwindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(Opennewwindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=gender, value="Male", font=('Calibri', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=gender, value="Female", font=('Calibri', 14)).pack(
        side=LEFT)
    # ===================LABELS==============================
    label_title = Label(FormTitle, text="Adding New Contacts", bd=12, fg="black", bg="Lightgreen",
                        font=("Calibri", 15, "bold"), pady=2)
    label_title.pack(fill=X)
    label_FirstName = Label(ContactForm, text="First Name", font=('Calibri', 14), bd=5)
    label_FirstName.grid(row=0, sticky=W)

    label_MiddleName = Label(ContactForm, text="Last Name", font=('Calibri', 14), bd=5)
    label_MiddleName.grid(row=1, sticky=W)

    label_LastName = Label(ContactForm, text="Grad Year", font=('Calibri', 14), bd=5)
    label_LastName.grid(row=2, sticky=W)

    label_Gender = Label(ContactForm, text="Gender", font=('Calibri', 14), bd=5)
    label_Gender.grid(row=3, sticky=W)

    label_Age = Label(ContactForm, text="Age", font=('Calibri', 14), bd=5)
    label_Age.grid(row=4, sticky=W)

    label_HomeAddress = Label(ContactForm, text="Company", font=('Calibri', 14), bd=5)
    label_HomeAddress.grid(row=5, sticky=W)

    label_PhoneNumber = Label(ContactForm, text="Phone Number", font=('Calibri', 14), bd=5)
    label_PhoneNumber.grid(row=6, sticky=W)

    # ===================ENTRY===============================
    FirstName = Entry(ContactForm, textvariable=f_name, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
    FirstName.grid(row=0, column=1)

    MiddleName = Entry(ContactForm, textvariable=m_name, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
    MiddleName.grid(row=1, column=1)

    LastName = Entry(ContactForm, textvariable=l_name, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
    LastName.grid(row=2, column=1)

    RadioGroup.grid(row=3, column=1)

    Age = Entry(ContactForm, textvariable=age, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
    Age.grid(row=4, column=1)

    HomeAddress = Entry(ContactForm, textvariable=home_address, font=('Calibri', 14, 'bold'), bd=3, width=20,
                        justify='left')
    HomeAddress.grid(row=5, column=1)

    PhoneNumber = Entry(ContactForm, textvariable=phone_number, font=('Calibri', 14, 'bold'), bd=3, width=20,
                        justify='left')
    PhoneNumber.grid(row=6, column=1)

    # ==================BUTTONS==============================
    ButtonAddContact = Button(ContactForm, text='Please Save', bd=5, font=('Calibri', 12, 'bold'), fg="black",
                              bg="lightgreen", command=Submit)
    ButtonAddContact.grid(row=7, columnspan=2, pady=10)


# module for whole frame window, labels and button of contact management system
# ============================FRAMES======================================
Top = Frame(root, width=600, bd=1)
Top.pack(side=TOP)
M = Frame(root, width=650, bg="pink")
M.pack(side=BOTTOM)
F = Frame(width=7, height=8, bd=10, bg="pink")
F.pack(side=BOTTOM)
MR = Frame(M, width=100)  # Right Middle frame
MR.pack(side=RIGHT, pady=10)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)

# LABELS
label_title = Label(Top, text="AlumniConnect", bd=7, relief=GROOVE, fg="Black", bg="lightgreen",
                    font=("Calibri", 25, "bold"), pady=3)
label_title.pack(fill=X)

# BUTTONS
Add_Button = Button(F, text='Add New Alumni', font=('Calibri', 17, 'bold'), fg="black",
                    bg="lightgreen", command=MyNewContact).grid(row=0, column=0, ipadx=20, padx=30)

Delete_Button = Button(F, text='Delete The Alumni', font=('Calibri', 17, 'bold'), command=Delete,
                       fg="black", bg="lightgreen").grid(row=0, column=1, ipadx=20)

Exit_Button = Button(F, text='Exit System', font=('Calibri', 17, 'bold'), command=Exit,
                     fg="black", bg="lightgreen").grid(row=0, column=2, ipadx=20, padx=30)

# creating a tables in contact management system
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin,
                    columns=("Id", "First Name", "Last Name", "Grad Year", "Gender", "Age", "Company", "Phone Number"),
                    height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

tree.heading('Id', text="Id", anchor=W)
tree.heading('First Name', text="First Name", anchor=W)
tree.heading('Last Name', text="Last Name", anchor=W)
tree.heading('Grad Year', text="Grad Year", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('Age', text="Age", anchor=W)
tree.heading('Company', text="Company", anchor=W)
tree.heading('Phone Number', text="phone Number", anchor=W)

search_var = StringVar()
search_entry = Entry(F, textvariable=search_var, font=('Calibri', 17, 'bold'), bd=3, width=20, justify='left')
search_entry.grid(row=0, column=3, padx=20)
search_button = Button(F, text='Search', font=('Calibri', 17, 'bold'), command=search, fg="black", bg="lightgreen")
search_button.grid(row=0, column=4, ipadx=20, padx=30)

tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.column('#6', stretch=NO, minwidth=0, width=30)
tree.column('#7', stretch=NO, minwidth=0, width=120)

tree.pack()
tree.bind('<Double-Button-1>', UpdateContact)

# ============================INITIALIZATION==============================
if __name__ == '__main__':
    Database()
    username_Var = StringVar()
    password_Var = StringVar()
    open_login_window()
    root.mainloop()
