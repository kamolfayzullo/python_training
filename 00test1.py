import sqlite3
conn = sqlite3.connect("dcu_location.db")
cursor = conn.cursor()
cursor.execute()('''CREATE TABLE harajatlar(harajat_nomi text NOT null , summa REAL NOT null , sana date DEFAULT CURRENT_TIMESTAMP, kirim_ciqim text DEFAULT kirim) ''')


conn.commit()
cursor.close()
conn.close()
