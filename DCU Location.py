import requests
import time
import sqlite3

def search_dcu_loc(con_number):
    connection = sqlite3.connect('meters.db')
    cursor = connection.cursor()
    data=cursor.execute(f"""select * from locations where ESP ='{con_number}'""")
    data=data.fetchone()
    connection.close()
    return data

data = search_dcu_loc(5)
print (data)

