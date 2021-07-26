from tkinter import *
import sqlite3

root = Tk()
root.title('parceldatabase')
root.iconbitmap('')
root.iconbitmap('D:\SEM 2\VGT123\computer programming\labmodule')
root.geometry("400x400")



con = sqlite3.connect('parcel_system.db')
c = con.cursor()
 
c.execute("""CREATE TABLE parcel_system(
    name text, 
    phone integer,
    trackno integer,
    rack integer,
    date integer,
    status
    )""")

con.commit()
con.close() 
root.mainloop()