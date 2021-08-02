from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

root = Tk()
root.title('UNIMAP PARCEL SYSTEM')

#list your path location below for using parcel system icon (Please '#' other user path location when using your own path)
#icon_location = 'C:/Users/User/Desktop/UNIMAP Class/Sem 2/VGT123/Gui Hub/Example/parcel-software-mini-project/imej/icon-unimap.ico' #PC Wan
#icon_location = 'D:/SEM 2/VGT123/computer programming/parcel-software-mini-project/imej/Icon-unimap.ico' #PC winfei
icon_location = 'D:/ASSIGNMENTS/1. UNIMAP (RY87)/SEM 2/VGT123/Mini Project/Parcel software/parcel-software-mini-project/imej/icon-unimap.ico' #PC Danial
#icon_location = 'C:/Users/Akmal Nazim/Desktop/Mini Project VGT123/GitHub/parcel-software-mini-project/imej/Icon-unimap.ico' #PC Akmal
root.iconbitmap(icon_location)
root.resizable(False, False)

#submit data function
def submit():
    con = sqlite3.connect(f'parcel_system_{month.get()}.db')
    c = con.cursor()
    c.execute("INSERT INTO parcel_system VALUES (:name, :phone, :trackno, :rack, :date, :status)",
            {
                'name' : name_id.get().upper(),
                'phone' : parcel_no.get(),
                'trackno' : parcel_serial.get().upper(),  
                'rack' : rack_no.get(),
                'date': date.get(),
                'status': status.get()
            })
    name_id.delete(0, END)
    parcel_no.delete(0, END)
    parcel_serial.delete(0, END)
    rack_no.delete(0, END)
    date.delete(0, END)
    messagebox.showinfo('SUCCESS!', "Data submitted")

    con.commit()
    con.close()

#show DISPLAY
def display():
    display = Tk()
    display.title('Records')
    display.iconbitmap(icon_location)
    

    con = sqlite3.connect(f'parcel_system_{month.get()}.db')
    c = con.cursor()
    c.execute("SELECT*, oid FROM parcel_system")
    records = c.fetchall()
    print(records)
    print(len(records))
    
    current_count = 1
    Label(display, text = 'Name').grid(row = 0, column = 0, padx = (0, 10))
    Label(display, text = 'Phone No.').grid(row = 0, column = 1, padx = (0, 10))
    Label(display, text = 'Tracking No.').grid(row = 0, column = 2, padx = (0, 10))
    Label(display, text = 'Rack No.').grid(row = 0, column = 3, padx = (0, 10))
    Label(display, text = 'Date').grid(row = 0, column = 4, padx = (0, 10))
    Label(display, text = 'Status').grid(row = 0, column = 5, padx = (0, 10))

    for record in records:
        for x in range(6):
            Label(display, text = record[x]).grid(row = current_count, column = x)
        current_count += 1
    con.commit()
    con.close()

#search Data
def search_data():
    search = Tk()
    search.title('Search')
    search.iconbitmap(icon_location)
    

    con = sqlite3.connect(f'parcel_system_{month.get()}.db')
    c = con.cursor()
    record_status = select_box.get().upper()
    c.execute("SELECT* FROM parcel_system WHERE trackno=" + f"'{record_status}'")
    records = c.fetchall()
    
    #Global Variable
    global name_id_editor
    global parcel_no_editor
    global parcel_serial_editor
    global rack_no_editor
    global date_editor
    global status_editor

    error = 0

    for record in records:
        if record[2] == record_status:
            error = 1
            Label(search, text = 'Name').grid(row = 0, column = 0, padx = (0, 10))
            Label(search, text = 'Phone No.').grid(row = 0, column = 1, padx = (0, 10))
            Label(search, text = 'Tracking No.').grid(row = 0, column = 2, padx = (0, 10))
            Label(search, text = 'Rack No.').grid(row = 0, column = 3, padx = (0, 10))
            Label(search, text = 'Date').grid(row = 0, column = 4, padx = (0, 10))
            Label(search, text = 'Status').grid(row = 0, column = 5, padx = (0, 10))

            for record in records:
                for x in range(6):
                    Label(search, text = record[x]).grid(row = 1, column = x)
    
    if error == 0:
        search.destroy()
        data_notfound()

#update data function
def update_data():   
    
    con = sqlite3.connect(f'parcel_system_{month.get()}.db')
    c = con.cursor()
    record_status = select_box.get().upper()
    c.execute("SELECT* FROM parcel_system WHERE trackno=" + f"'{record_status}'")
    records = c.fetchall()
    
    #Global Variable
    global name_id_editor
    global parcel_no_editor
    global parcel_serial_editor
    global rack_no_editor
    global date_editor
    global status_editor

    error = 0

    for record in records:
        if record[2] == record_status:
            error = 1
            editor = Tk()
            editor.title('Editor')
            editor.iconbitmap(icon_location)
            label_1 =Label(editor, text = "Name:")
            label_1.grid(row = 0, column = 0, sticky = W, pady = 10, padx = 5)
            label_2 =Label(editor, text = "Phone Number:")
            label_2.grid(row = 1, column = 0, sticky = W, pady = 10, padx = 5)
            label_3 =Label(editor, text = "Tracking Number:")
            label_3.grid(row = 2, column = 0, sticky = W, pady = 10, padx = 5)
            label_5 =Label(editor, text = "Rack Number:")
            label_5.grid(row = 3, column = 0, sticky = W, pady = 10, padx = 5)
            label_6 =Label(editor, text = "Date:")
            label_6.grid(row = 4, column = 0, sticky = W, pady = 10, padx = 5)
            label_7 =Label(editor, text = "Status:")
            label_7.grid(row = 5, column = 0, sticky = W, pady = 10, padx = 5)

    if error == 0:
        data_notfound()

# data not found pop up
def data_notfound():
    messagebox.showinfo('Info', "Data Not Found")

#Checking selected month
def check_database(current_month, val):
    if current_month == 'Select Month':
        messagebox.showinfo('Info', "You don't Selected Month!!")        
        print("You don't Selected Month")
    else:
        if val == 1:
            submit()
        elif val == 2:
            display()
        elif val == 3:
            search_data()
        elif val == 4:
            update_data()

#frame 1 layout
#label
label_1 =Label(root, text = "Name:")
label_1.grid(row = 0, column = 0, sticky = W, pady = 10, padx = 5)
label_2 =Label(root, text = "Phone Number:")
label_2.grid(row = 1, column = 0, sticky = W, pady = 10, padx = 5)
label_3 =Label(root, text = "Tracking Number:")
label_3.grid(row = 2, column = 0, sticky = W, pady = 10, padx = 5)
label_5 =Label(root, text = "Rack Number:")
label_5.grid(row = 3, column = 0, sticky = W, pady = 10, padx = 5)
label_6 =Label(root, text = "Date:")
label_6.grid(row = 4, column = 0, sticky = W, pady = 10, padx = 5)
label_4 =Label(root, text = "Select Tracking No:")
label_4.grid(row = 1, column = 2, sticky = W, pady = 10, padx = 5)
label_7 =Label(root, text = "Status:")
label_7.grid(row = 5, column = 0, sticky = W, pady = 10, padx = 5)

#entry
name_id =Entry(root)
name_id.grid(row = 0, column = 1, sticky = W, pady = 10)
parcel_no =Entry(root)
parcel_no.grid(row = 1, column = 1, sticky = W, pady = 10)
parcel_serial =Entry(root)
parcel_serial.grid(row = 2, column = 1, sticky = W, pady = 10)
rack_no = Entry(root)
rack_no.grid(row = 3, column = 1, sticky = W, pady = 10)
date = Entry(root)
date.grid(row = 4, column = 1, sticky = W, pady = 10)
select_box = Entry(root)
select_box.grid(row=1, column=3, sticky = E, pady = 10)

#Select combo box status
status = ttk.Combobox(root, value=["Select Status", "Pickup", "Onhold"])
status.current(0)
status.grid(row = 5, column= 1)

#submit button
submitbutton=Button(root, text = "CONFIRM", command=lambda:check_database(month.get(), 1))
submitbutton.grid(row = 5, column = 3, pady = 5, padx = 5)

#cancel button
cancelbutton=Button(root, text = "CANCEL", command = root.quit)
cancelbutton.grid(row = 5, column = 4, pady = 5, padx = 5)

#display button
history_button = Button(root, text ="View all",  command=lambda:check_database(month.get(), 2))
history_button.grid(row=0, column=4, pady=10, padx=10, ipadx=30)

#Search button
search_button = Button(root,  text ="Search", command=lambda:check_database(month.get(), 3))
search_button.grid(row=1, column=4, pady=10, padx=10, ipadx=30)

#update button
update_button = Button(root, text ="Update", command=lambda:check_database(month.get(), 4))
update_button.grid(row=2, column=4, pady=10, padx=10, ipadx=30)

#Delete button
delete_button = Button(root, text ="Delete")
delete_button.grid(row=3, column=4, pady=10, padx=10, ipadx=30)

#Select combo box month
month = ttk.Combobox(root, value=["Select Month", 'Jan', 'Feb', 'Mac', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Spt', 'Oct', 'Nov', 'Dec'])
month.current(0)
month.grid(row = 4, column= 4)

root.mainloop()