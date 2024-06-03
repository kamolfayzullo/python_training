import requests
import sqlite3
import psycopg2


input_path="C:/Users/Admin/Desktop/python_training/work_files/bot.log"

db_params = {
    'host': '192.168.14.74',
    'database': 'reestr',
    'user': 'test',
    'password': 'test',
    'port': '5432',
}





   
def harajatsaqlaw():
    conn = sqlite3.connect('all_reestr')
    cursor = conn.cursor()
    cursor.execute('''SELECT DISTINCT model FROM reestr_respublika rr''')
    rows = cursor.fetchall()
    return rows
    conn.commit()
    conn.close()
   






# def get_meter_info(db_params,meter_no):
#     try:
#         with psycopg2.connect(**db_params).cursor() as cursor:
#             cursor.execute("select * from reestr_respublika where meter_no =%s",(meter_no,))
#             result=cursor.fetchall()
#             return result
#     except  Exception as e:
#         print('Bror korhol boldi :',e)
#         return -1

def get_meter_info(db_params,meter_no):
    try:
        connection=psycopg2.connect(**db_params)
        cursor=connection.cursor()
        cursor.execute("select * from reestr_respublika where meter_no =%s",(meter_no,))
        result=cursor.fetchall()
        return result
    except  Exception as e:
        print('Bror korhol boldi :',e)
        return -1
    finally:
        if connection is not None:
            connection.close()
        if cursor is not None:
            cursor.close()




def harajatsaqlaw():
    conn = sqlite3.connect('all_reestr')
    cursor = conn.cursor()
    cursor.execute('''SELECT DISTINCT model FROM reestr_respublika rr''')
    rows = [row[0] for row in cursor.fetchall()]
    conn.close()
    return rows


# print(get_meter_info(db_params,'121206820426'))
db_params = {
    'host': '192.168.14.74',
    'database': 'reestr',
    'user': 'test',
    'password': 'test',
    'port': '5432',
}


meter= [123200456123,EX-123456, EX-2453145]

def is_askue(meter):
    if len(meter) in (9) and meter[:4] == 'EX-1':
        return 1
    elif len(meter) in (10) and meter[:4] == 'EX-2':
        return 1
    elif len(meter) == 12:
        if meter[:2] == '20' and meter[2:4] in ('15', '16', '17', '18', '19', '20', '21', '22'):
            return 1
        elif meter[:2] == '11' and meter[2:3] in ('1', '3', '4', '5'):
            return 1
        elif meter[:2] == '02' and meter[2:3] in ('1', '3', '4'):
            return 1
        elif meter[:2] == '12' and meter[2:3] in ('1', '3', '4'):
            return 1
        else:
            return 0
    else:
        return 0



def show_info(name,age):
    print(f'Mening ismim {name} va yoshim {str(age)}')
men_haqimda={'name':'fayzullo','age':22}

show_info(name='fayzullo',age=22)
show_info(**men_haqimda)








