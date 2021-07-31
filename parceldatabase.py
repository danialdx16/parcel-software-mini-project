import sqlite3

month = [
        'Jan',
        'Feb',
        'Mac',
        'Apr',
        'May',
        'Jun',
        'Jul',
        'Aug',
        'Spt',
        'Oct',
        'Nov',
        'Dec'
        ]

for x in range(len(month)):
    con = sqlite3.connect(f'parcel_system_{month[x]}.db')
    c = con.cursor()
    
    c.execute("""CREATE TABLE parcel_system(
        name text, 
        phone string,
        trackno string,
        rack integer,
        date integer,
        status
        )""")

    con.commit()
    con.close() 