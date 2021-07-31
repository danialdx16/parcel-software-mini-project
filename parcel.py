from tkinter import *
from tkinter import ttk

root = Tk()
root.title('UNIMAP PARCEL SYSTEM')
#Change this path location for parcel system
icon_location = 'C:/Users/User/Desktop/UNIMAP Class/Sem 2/VGT123/Gui Hub/Example/parcel-software-mini-project/imej/icon-unimap.ico'
root.iconbitmap(icon_location)
root.resizable(False, False)


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

#Select box status
status = ttk.Combobox(root, value=["Select Status", "Pickup", "Onhold"])
status.current(0)
status.grid(row = 5, column= 1)

#submit button
submitbutton=Button(root, text = "CONFIRM")
submitbutton.grid(row = 5, column = 3, pady = 5, padx = 5)

#cancel button
cancelbutton=Button(root, text = "CANCEL", command=root.quit)
cancelbutton.grid(row = 5, column = 4, pady = 5, padx = 5)

#display button
history_button = Button(root, text="View all")
history_button.grid(row=0, column=4, pady=10, padx=10, ipadx=30)

#Search button
search_button = Button(root,  text="Search")
search_button.grid(row=1, column=4, pady=10, padx=10, ipadx=30)

#update button
update_button = Button(root, text="Update")
update_button.grid(row=2, column=4, pady=10, padx=10, ipadx=30)

#Delete button
delete_button = Button(root, text="Delete")
delete_button.grid(row=3, column=4, pady=10, padx=10, ipadx=30)

#Select box month
month = ttk.Combobox(root, value=["Select Month", 'Jan', 'Feb', 'Mac', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Spt', 'Oct', 'Nov', 'Dec'])
month.current(0)
month.grid(row = 4, column= 4)

root.mainloop()