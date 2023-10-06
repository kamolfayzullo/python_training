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






import sqlite3
database_name='dcu_location.db'

conn=sqlite3.connect(database_name)
cursor=conn.cursor()
cursor.execute("""
insert into somsa values('tomchi','jizax','yumaloq',4.55)
               """)
conn.commit()
cursor.close()
conn.close()


















