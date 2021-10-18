import sqlite3
import temperature
#connect to a database
conn = sqlite3.connect('temperature.db')
#create a cursor
cursor =  conn.cursor()
#create a Table

#cursor.execute("""CREATE TABLE temperature(
#        year DATATYPE,
#        median DATATYPE,
#        upper DATATYPE,
#        lower DATATYPE
#    )""")

cursor.execute("INSERT INTO temperature VALUES()")
conn.commit()
conn.close()