import sqlite3 as sl

con = sl.connect('orders-executed.db')

with con:
    cur = con.cursor()

    cur.execute("SELECT * FROM ETHBUSD")
    con.commit()
    rows = cur.fetchall()

    for element in rows:
        print(element)
