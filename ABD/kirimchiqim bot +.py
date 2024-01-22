import sqlite3
import json
import time
import requests
import urllib
import datetime as dt


offset = None
kredit = None
debt = None
izoh = None

restart=[[{'text':'Tel raqamni yuborish📞','request_contact':True}]]

izohsiz=[[{'text':'Izohsiz'}]]

menyu=[['Kirim'],['Chiqim'],['Hisobot']]
menyu_reordered = [menyu[0], menyu[1], menyu[2]]
kirim=[[{'text':' Oylik ', 'callback_data':'Oylik'},
{'text':' Leviy ', 'callback_data':'Leviy'}],
[{'text':' Qarz_oldim ', 'callback_data':'Qarz_oldim'},
{'text':' Bonus ', 'callback_data':'Bonus'}]]

chiqim=[[{'text':' Mowina ', 'callback_data':'Mowina'},
{'text':' Uyga ', 'callback_data':'Uyga'}],
[{'text':' Waxsiy ', 'callback_data':'Waxsiy'},
{'text':' Qarz_berdim ', 'callback_data':'Qarz_berdim'}],
[{'text':' Mayda_chuda ', 'callback_data':'Mayda_chuda'},
{'text':' Ehson ', 'callback_data':'Ehson'}]]

#bot manzil
bot_token = '6129894724:AAEZc_cSdJCOJWTnypyPtLgfOPuUXA08IZM'
base_url = f'https://api.telegram.org/bot{bot_token}/'

#build keyboard chala darbotka kerak
def build_keyboard(keyboard):
    reply_markup = {"keyboard":keyboard,
                    "one_time_keyboard":True,
                    "resize_keyboard":True,
                    "input_field_placeholder":"Quyidagilardan birini tanlang!"}
    return json.dumps(reply_markup) #wuni sal chunmadm

#ikkinchi turdagi keyboard
def inline_keyboard(inbord):
    reply_markup={'inline_keyboard':inbord}
    return json.dumps(reply_markup)

#xabar yuboradi
def sendMessage(chatId,text,reply_markup=None):
    messageUrl=base_url+f"sendMessage?chat_id={chatId}&text={text}"
    if reply_markup:
        messageUrl = messageUrl +  "&reply_markup={}".format(reply_markup)
    requests.get(messageUrl)

#raqamsaqlawdan oldin tekwiriw _______________________________________________________________
# def proverkaid():
#     conn = sqlite3.connect('data.db')
#     cursor = conn.cursor()
#     cursor.execute('''select userid from foydalanuvchilarruyhati''')    
#     # Получаем все результаты запроса
#     rows = cursor.fetchall()
#     conn.close()
#     return rows

def is_numeric(input_str):
    return input_str.isdigit()

def harajatturi(aaa):
    sss = str(aaa)
    return (sss)


def kirimchiqim(aaa):
    if aaa in ('Oylik', 'Leviy', 'Qarz_oldim', 'Bonus'):
        return "kirim"
    else:
        return "chiqim"

def harajatsaqlaw(chatid,kirimchiqim,harajatturi,summasi,izohi):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS harajatlarbazasi 
(   id INTEGER PRIMARY KEY AUTOINCREMENT,
 	userid INTEGER,
 	kirimchiqim text,
    harajatturi text,
    summasi INTEGER,
    izoh text,
    regvaqti date)''')
    cursor.execute(f'''insert into harajatlarbazasi (userid   ,kirimchiqim ,      harajatturi ,       summasi  ,      izoh ,        regvaqti) 
			                                 values ({chatid} ,'{kirimchiqim}', "{harajatturi}"    ,'{summasi}' ,   '{izohi}'  ,date('now')  )''')
    #result=cursor.execute('''select * from testtable''')
    #data=result.fetchall()
    #print(data)

    conn.commit()
    conn.close()


    
    


def proverkaid(user_id):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute(f'''select userid from foydalanuvchilarruyhati where userid={user_id}''')    
    rows = cursor.fetchall()
    conn.close()
    if len(rows)>0:
        return 1
    elif len(rows)==0:
        return 0
    else:
        return -1




#def tekshirish()
#raqamni saqlab olish
def raqamsaqlaw(chatid,name,telnomer):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS foydalanuvchilarruyhati ( 
    userid INTEGER PRIMARY KEY,
    fio text,
    contact text,
    regvaqti date)''')
    cursor.execute(f'''insert into foydalanuvchilarruyhati (userid , fio, contact ,regvaqti) 
			   values ('{chatid}' ,'{name}' , '{telnomer}' ,date('now')  )''')
    #result=cursor.execute('''select * from testtable''')
    #data=result.fetchall()
    #print(data)

    conn.commit()
    conn.close()


#Kelgan smsni obrobotka
while True:
    response = requests.get(base_url + f"getUpdates?offset={offset}")
    if response.ok:
        data = response.json()
        if data["ok"]:
            if data["result"]:
                for update in data["result"]:
                    print (update)
                    if 'message' in update:
                        chatId = update['message']["chat"]["id"]
                        if "text" in update['message']:
                            print(update)
                            if "/start" in update ['message']["text"]:
                                sendMessage(chatId,"Bot ga hush kelibsiz!! \n Ushbu bot yordamida siz harajatlaringizni hisoblab yurishingiz mumkin \n Buning uchun siz o`zingizni kontaktizni yuboring", build_keyboard(restart))
                            elif izoh == 1:
                                comment = update['message']["text"]
                                izoh = None
                                harajatsaqlaw(chatId,kirimyokichiqim,harajatturi,summa,comment)
                                debt = None
                                sendMessage(chatId,"Ma`lumotlar saqlandi", build_keyboard(menyu))
                            elif "Kirim" == update['message']["text"]:
                                sendMessage (chatId,"Kirim turini tanlang",inline_keyboard(kirim))                            
                            elif "Chiqim" == update['message']["text"]:
                                sendMessage (chatId,"Chiqim turini tanlang",inline_keyboard(chiqim))
                            elif is_numeric(update['message']["text"]):
                                if debt ==1:
                                    summa = int(update ['message']["text"])
                                    sendMessage(chatId,"Izoh qoldiring",build_keyboard(izohsiz))
                                    izoh = 1
                                    debt = None
                                else:
                                    sendMessage(chatId,"Raqam kiritmang")
                            elif "dsgvbdsjhbvdsv " != update:
                                sendMessage (chatId,"Xatolik1")
                        elif 'contact' in update['message']:
                            sendMessage(chatId, 'Siz kontakt yubordiz')
                            name = str(update['message']['chat']['first_name'])
                            telnomer = str((update['message']['contact']['phone_number'])[-9:])
                            contactid = update['message']['contact']['user_id']
                            contactid1 = str(contactid)
                            if chatId != contactid:
                                sendMessage(chatId,"O`zingizni kontaktizni yuboring")
                            elif proverkaid(contactid) == 1:
                                sendMessage (chatId,"Ro`yxatdan o`tgansiz",build_keyboard(menyu_reordered))
                            elif proverkaid(contactid) == 0:
                                raqamsaqlaw(chatId,name,telnomer)                                
                                sendMessage(chatId,"Raqamingiz saqlandi",build_keyboard(menyu_reordered))                                             
                        elif 'voice' in update['message']:
                            sendMessage(chatId, 'Siz Ovozli habar')                          
                        elif update != 'dsvdsvsdbdsb':
                            sendMessage(chatId,"xatolik") 
                            print (update)
                    elif 'callback_query' in update:
                            print('knopka')
                            print(update)
                            chatId =update['callback_query']['message']["chat"]["id"]
                            callbackdata = update['callback_query']['data']
                            kirimyokichiqim = str(kirimchiqim(callbackdata))
                            harajatturi = callbackdata
                            debt =1
                            print (str(kirimyokichiqim) +  "siz wuni tanladiz")
                            sendMessage(chatId,"Summani kiriting",)
                    offset = update["update_id"] + 1
        else:
            print("Error in API response:", data["description"])
    else:
        print("Failed to make the API request.")
    time.sleep(0.1) 


#Contact------------------------------------------------------------------------------
{'update_id': 412296991, 
 'message': {'message_id': 2149, 
             'from': {'id': 171319245, 'is_bot': False, 'first_name': 'Fayzullo', 
                      'last_name': 'Kamol', 
                      'username': 'kamolfayzullo', 
                      'language_code': 'ru'}, 
             'chat': {'id': 171319245, 
                      'first_name': 'Fayzullo', 
                      'last_name': 'Kamol', 
                      'username': 'kamolfayzullo', 
                      'type': 'private'}, 
             'date': 1704865961, 
             'contact': {'phone_number': '+998901361011', 
                         'first_name': 'Abdulazizaka Cas', 
                         'user_id': 39663146}}}

# #oddiy sms------------------------------------------------------------------------------
# {'update_id': 412296990,
#  'message': {'message_id': 2147, 
#              'from': {'id': 171319245, 
#                       'is_bot': False, 
#                       'first_name': 'Fayzullo', 
#                       'last_name': 'Kamol',
#                       'username': 'kamolfayzullo', 
#                       'language_code': 'ru'}, 
#              'chat': {'id': 171319245,
#                       'first_name': 
#                           'Fayzullo',
#                           'last_name':
#                               'Kamol',
#                               'username':
#                                   'kamolfayzullo', 
#                                   'type': 'private'}, 
#              'date': 1704865939, 
#              'text': 'gdfdgfd'}}

#Ovozli habar-----------------------------------------------------------------------------------------
{'update_id': 412297019,
 'message':
     {'message_id': 2189, 
             'from': {'id': 171319245, 
                      'is_bot': False, 
                      'first_name': 'Fayzullo',
                      'last_name': 'Kamol', 
                      'username': 'kamolfayzullo', 
                      'language_code': 'ru'}, 
             'chat': {'id': 171319245,
                      'first_name': 'Fayzullo', 
                      'last_name': 'Kamol',
                      'username':  'kamolfayzullo', 
                      'type': 'private'},
             'date': 1704869594, 
             'voice': {'duration': 1,
                       'mime_type': 'audio/ogg', 
                       'file_id': 'AwACAgIAAxkBAAIIjWWePtrcIMU0SbSlqk3m-g80uSfuAALbRQACpMLwSAx0UqPFOoLWNAQ', 
                       'file_unique_id': 'AgAD20UAAqTC8Eg', 
                       'file_size': 3722}}}
#callback------------------------------------------------------------------------------------------------
{'update_id': 412297024, 
 'callback_query': {'id': '735810557059754475', 
                    'from': {'id': 171319245,
                             'is_bot': False, 
                             'first_name': 'Fayzullo', 
                             'last_name': 'Kamol', 
                             'username': 'kamolfayzullo', 
                             'language_code': 'ru'},
                    'message': {'message_id': 2114,
                                'from': {'id': 6129894724, 
                                         'is_bot': True,
                                         'first_name': 'Requests Test Bot', 
                                         'username': 'reqtest_bot'},
                                'chat': {'id': 171319245, 
                                         'first_name': 'Fayzullo', 
                                         'last_name': 'Kamol',
                                         'username': 'kamolfayzullo', 
                                         'type': 'private'}, 
                                'date': 1704710824, 
                                'text': 'O`zingizga kerakli bo`lgan tumanni tanlang!',
                                'reply_markup': 
                                    {'inline_keyboard':
                                        [[{'text': 'Qoraqalpog`iston', 
                                           'callback_data': '35000'}, 
                                          {'text': 'Andijon', 
                                           'callback_data': '03000'}], 
                                         [{'text': 'Buxoro', 
                                           'callback_data': '06000'},
                                          {'text': 'Jizzax', 
                                           'callback_data': '08000'}], 
                                         [{'text': 'Qashqadaryo', 
                                           'callback_data': '10000'}, 
                                          {'text': 'Navoiy', 
                                           'callback_data': '12000'}],
                                         [{'text': 'Namangan',
                                           'callback_data': '14000'}, 
                                          {'text': 'Samarqand',
                                           'callback_data': '18000'}],
                                         [{'text': 'Surxondaryo', 
                                           'callback_data': '22000'}, 
                                          {'text': 'Sirdaryo', 
                                           'callback_data': '24000'}],
                                         [{'text': 'Toshkent', 
                                           'callback_data': '27000'}, 
                                          {'text': 'Farg‘ona', 
                                           'callback_data': '30000'}], 
                                         [{'text': 'Xorazm',
                                           'callback_data': '33000'}, 
                                          {'text': 'Toshkent shahar', 
                                           'callback_data': '26000'}]]}}, 
                    'chat_instance': '5323233157514262773', 
                    'data': '33000'}}


# #baza bn iwlidigan joyi--------------------------------------------------------------------------------

conn = sqlite3.connect('data.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS testtable (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fio text,
    kirim_chiqim text,
    xarajat_turi text,
    koment text,
    summasi integer,
    xarajat_vaqti date
)''')

cursor.execute(f'''insert into testtable ( fio , kirim_chiqim , xarajat_turi ,  koment ,  summasi ,  xarajat_vaqti) 
			   values  ('elyor' , 'kirim' , 'cobalt', 'benzin', 2000 ,date('now')  )''')

result=cursor.execute('''select * from testtable''')
data=result.fetchall()
print(data)

conn.commit()
conn.close()
#---------------------------------------------------------------------------------------------------
{'update_id': 412297080, 'message': {'message_id': 2321, 
                                     'from': {'id': 171319245, 
                                              'is_bot': False, 
                                              'first_name': 'Fayzullo',
                                              'last_name': 'Kamol', 
                                              'username': 'kamolfayzullo',
                                              'language_code': 'ru'}, 
                                     'chat': {'id': 171319245, 
                                              'first_name': 'Fayzullo', 
                                              'last_name': 'Kamol', 
                                              'username': 'kamolfayzullo',
                                              'type': 'private'}, 'date': 1704974194, 
                                     'reply_to_message': {'message_id': 2320, 
                                                          'from': {'id': 6129894724, 
                                                                   'is_bot': True, 
                                                                   'first_name': 'Requests Test Bot', 
                                                                   'username': 'reqtest_bot'}, 
                                                          'chat': {'id': 171319245, 'first_name':
                                                              'Fayzullo', 'last_name': 'Kamol', 
                                                              'username': 'kamolfayzullo', 'type': 'private'},
                                                          'date': 1704974192, 'text': 
                                                              'Bot ga hush kelibsiz!! \n Ushbu bot yordamida siz harajatlaringizni hisoblab yurishingiz mumkin \n Buning uchun siz o`zingizni kontaktizni yuboring'}, 
                                     'contact': {'phone_number': '+998979988899',
                                                 'first_name': 'Fayzullo', 
                                                 'last_name': 'Kamol',
                                                 'user_id': 171319245}}}