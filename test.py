import sqlite3

connection = sqlite3.connect('meters.db')
cursor = connection.cursor()

DATA=cursor.execute('''SELECT ESP FROM METERS''')
DATA=DATA.fetchall() #fetchall(),fetchone()
#print(DATA)
connection.close()


data = DATA
uniq = set(data)
#print (uniq)
for i in uniq:
    soni=0
    for m in data:
        if i==m:
            soni=soni+1
    print(i,soni)