# import sqlite3

# # a = str(+9981312979988899)
# # result = a[-9:]
# # print(result)
# def raqamsaqlaw(chatid,name,telnomer):
#     conn = sqlite3.connect('data.db')
#     cursor = conn.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS foydalanuvchilarruyhati 
# (   userid INTEGER PRIMARY KEY,
#     fio text,
#     contact text,
#     regvaqti date)''')
#     cursor.execute(f'''insert into foydalanuvchilarruyhati (userid , fio, contact ,regvaqti) 
# 			   values ('{chatid}' ,'{name}' , '{telnomer}' ,date('now')  )''')



# def proverkaid():
#     conn = sqlite3.connect('data.db')
#     cursor = conn.cursor()
#     cursor.execute('''select * from foydalanuvchilarruyhatitest''')    
#     # Получаем все результаты запроса
#     rows = cursor.fetchall()
#     conn.close()
#     return rows

# result = proverkaid()
# print (str(result))
# # for i in result:
# #     print (str(i))

# def is_numeric(input_str):
#     return input_str.isdigit()

# # Пример использования
# input_text = "khbkb"

# if is_numeric(input_text):
#     print(f"{input_text} является числом.")
# update1 = "vxzxzv"

# if update1 in 'Moshina' or  'Uy':
#     print ("xa")
# else:
#     print ("yuq")
    
# import pandas as pd

# # Создаем DataFrame
# data = {'Имя': ['Али', 'Бека', 'Гули', 'Давид'],
#         'Возраст': [25, 30, 22, 35],
#         'Город': ['Тбилиси', 'Батуми', 'Кутаиси', 'Телави']}

# df = pd.DataFrame(data)

# # Выводим DataFrame
# print(df)


def harajatturi(aaa):
    if aaa in ('Oylik', 'Leviy', 'Qarz_oldim', 'Bonus'):
        return "kirim"
    else:
        return "chiqim"
    
result = harajatturi(a)
    
print(result)




def harajatturi(aaa):
    if aaa in ('Oylik', 'Leviy', 'Qarz_oldim', 'Bonus'):
        return "kirim"
    else:
        return "chiqim"
    
a = "Oylik"

harajatturi(a)
    
print (str(harajatturi))

# update = {'message': {'message_id': 2149, 
#              'from': {'id': 171319245, 'is_bot': False, 'first_name': 'Fayzullo', 
#                       'last_name': 'Kamol', 
#                       'username': 'kamolfayzullo', 
#                       'language_code': 'ru'}, 
#              'chat': {'id': 171319245, 
#                       'first_name': 'Fayzullo', 
#                       'last_name': 'Kamol', 
#                       'username': 'kamolfayzullo', 
#                       'type': 'private'}, 
#              'date': 1704865961, 
#              'contact': {'phone_number': '+998901361011', 
#                          'first_name': 'Abdulazizaka Cas', 
#                          'user_id': 39663146}}}

# name = str(update['message']['chat']['first_name'])
# print(name)
# telnomer = str((update['message']['contact']['phone_number'])[-9:])
# print (telnomer)
# contactid = update['message']['contact']['user_id']
# print(contactid)

#raqamsaqlaw(contactid,name,telnomer)
# for row in result:
#     print(row)