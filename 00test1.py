# import psycopg2
# import traceback

# # Database connection parameters
# dbname = "reestr"
# user = "fayzullo"
# password = "fayzullo"
# host = "192.168.14.74"
# port = "5432"
# # ______________ Postgress ga yangi file create qiliw
# def region():
#     try:
#         # Connect to the PostgreSQL database
#         conn = psycopg2.connect(
#             dbname=dbname,
#             user=user,
#             password=password,
#             host=host,
#             port=port
#         )

#         # Create a cursor
#         cursor = conn.cursor()

#         # SQL command to create the 'tyolkalar' table
#         sql_command = """
#             create table tuxumlar(
#                 ismi varchar not null,
#                 yoshi integer not null,
#                 qiziqan_fani varchar null,
#                 jinsi varchar(5) not null
#                 );
#         """

#         # Execute the SQL command
#         cursor.execute(sql_command)

#         # Commit the changes to the database
#         conn.commit()

#         print("Table 'tyolkalar' created successfully.")

#     except psycopg2.Error as e:
#         print(f"Error: {e}")
#         print("Error traceback:", traceback.format_exc())

#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()

# # Call the function to create the 'tyolkalar' table
# region()

# import sqlite3
# database_name='dcu_location.db'

# conn=sqlite3.connect(database_name)
# cursor=conn.cursor()
# cursor.execute("""
#                create table somsa(
#                    turi text not null,
#                    qayeriki text,
#                    shakli tex,
#                    narxi real
#                )
#                """)
# cursor.close()
# conn.close()






# import sqlite3
# database_name='dcu_location.db'

# conn=sqlite3.connect(database_name)
# cursor=conn.cursor()
# cursor.execute("""
# insert into somsa values('tomchi','jizax','yumaloq',4.55)
#                """)
# conn.commit()
# cursor.close()
# conn.close()





# javob = 0

# a = (input ('Raqam kiriting '))
# for i in a:
#     i = int(i)
#     javob = javob + i
        
# print (str(javob))


# davlat = []

# for x in unique:
#     ayol = 0
#     erke = 0
#     hunasa = 0
#     for i in a:
#         if x==i["country"]:
#             if i["gender"]== "Female":
#                 ayol = ayol + 1
#             elif i["gender"]== "Male":
#                 erke = erke + 1
#             else:
#                 hunasa = hunasa + 1


# meter = "EX-123123"

# def is_numeric(input_str):
#     return input_str.isdigit()




# def is_askue(meter):
#     if len(meter) in (9) and meter[:4] == 'EX-1':
#         if is_numeric(meter[-6:]):
#             return 1
#     else:
#         return 0
    
# is_askue(meter)
        
# print (is_askue)


# if is_numeric(meter):
#     b = "raqam"
# else:
#     b = "raqam emas"
# print (b)
#3333333333333333333


meter = "11200112346"

def is_numeric(input_str):
    return input_str.isdigit()

def is_askue(meter):
    if len(meter) == 9 and meter.startswith('EX-1'):
        if is_numeric(meter[-6:]):
            return 1
    elif len(meter) == 10 and meter.startswith('EX-2'):
        if is_numeric(meter[-7:]):
            return 1
    elif len(meter) == 12 and is_numeric(meter[-12:]):
        return 1
    else:
        return 0
    
    
result = is_askue(meter)
print(result)


# qo`wildi  !!!`
