import sqlite3

conn = sqlite3.connect("meters.db")
cursor = conn.cursor()
select_query = "SELECT * FROM meters"
cursor.execute(select_query)
rows = cursor.fetchmany(1000)
conn.close()
meters=rows
#print(meters)

# ('19209920',                             0
#   'ABDULLAYEVA ULBOLSIN KENDJAYEV',      1
#     'BABANOVA  д.3',                    2
#     'EX-2894241',                       3
#       '1',                              4
#         '35411',                        5 
#           '192',                         6
#             'CAS')
f=open('meter_info','w')

tarraqab = 0
for i in meters:
 #print (str(tarraqab) + (str)(i))
 zavno = i[3]
 uzunlikzavno = str(len(zavno))
 if uzunlikzavno in ["12"]:
   bowraqam = str(zavno[0:3])
   if bowraqam in ("123"):
    turi = ("EX 100A")
   elif bowraqam in ("124"):
    turi = ("EX 5A")
   elif bowraqam in ("125"):
    turi = ("EX 100V")   
   elif bowraqam in ("121"):
    turi = ("EX 1faz")
   elif bowraqam in ("111"):
    turi = ("TE 1faz")
   elif bowraqam in ("113"):
    turi = ("TE 100A")
   elif bowraqam in ("114"):
    turi = ("TE 5A")
   elif bowraqam in ("115"):
    turi = ("TE 100V")
   else:
    pass
 else:
   pass
 if uzunlikzavno in ["10"]:
   bowraqam = str(zavno[0:3])
   if bowraqam in ("EX-"):
    turi = ("EX 1-faz")
 else:
   pass
 if uzunlikzavno in ["9"]:
   bowraqam = str(zavno[0:3])
   if bowraqam in ("EX-"):
    turi = ("EX 3-faz")
   else:
    pass
 else:
  pass
 if turi == (""):
  askue = ("Yo`q")
 else:
  askue = ("Ha")
 tarraqab = tarraqab + 1
 print ((str(tarraqab) + ". " + i[3] + "  Account ID: " + i[0]) 
+ " Hisoblagich turi: " + str(turi) + ":      " + "Askue: " + str(askue) )
 f.write((str(tarraqab) + ". " + i[3] + "  Account ID: " + i[0]) 
+ " Hisoblagich turi: " + str(turi) + ":      " + "Askue: " + str(askue))
print(dir(f))

 





 






# list []
# dictionary {}
# tuple ()

# my_tuple = ("salom", "test", "test", "test1")  # o'zgarmaydi,ordered
# print(dir(my_tuple))

# print(my_tuple.count("test"))  # necha marta qatnashgani
# print(len(my_tuple))
# print(my_tuple.index("test", 2))  # 2chi indexdan boshlab nechanchi indexda turgani
# print(my_tuple[0])  # elementni chaqrb olish













# _____________________________________________________________#
# DATA TYPE
# sinle value(single value)
# numeric
# datetime
# string
# complex (dimensional)
# list -ozgaruvchgan,ordered [,]
# dictionary - ozgariuvchan,ordered {:,}
# tuples - ozgarmas,unchangable,ordered (,)
# sets -ozgarmas,no dublicate {,}

# sets
# mevalar = {"olma", "sabzi", "tuxum", "sabzi"}
# print(mevalar)

# a = ("anjir", "shoftoli", "tuxum", "sabzi", "sabzi", "tuxum", "sabzi")
# new_set = set(a)

# print(dir(new_set))
# new_set.pop() #taxminiy kaltalatish
# print(len(new_set))

# for i in new_set:
#     print(i)
   

