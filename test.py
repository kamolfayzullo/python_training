

import sqlite3

connection = sqlite3.connect('meters.db')
cursor = connection.cursor()



data=cursor.execute('''SELECT  PTES,DEV_STATUS,PHASE FROM METERS''')

data=data.fetchmany(10) #fetchall(),fetchone()

#print(DATA)
connection.close()

#print (data)
data = set(data)
comis = 0
instal = 0
ing = 0
for i in data:
    if "Commissioned" in i:
        
    
# uniq = set(data)
# for i in uniq:
#     jami = 0
#     comissined = 0
#     comissining = 0
#     for m in data:
#         if i == m:
#             soni = soni + 1
#     print (i,jami)







# data = DATA
# uniq = set(data)
# #print (uniq)
# for i in uniq:
#     soni=0
#     for m in data:
#         if i==m:
#             soni=soni+1
#     print(i,soni)