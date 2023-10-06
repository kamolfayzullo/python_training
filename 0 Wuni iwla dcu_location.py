import psycopg2 #pythondan postgresqlga boglashga ishlatiladgan library
import json
import time
import requests
import urllib
import datetime as dt




#bot manzil
bot_token = '6129894724:AAEZc_cSdJCOJWTnypyPtLgfOPuUXA08IZM'
base_url = f'https://api.telegram.org/bot{bot_token}/'


#Yordamchi

offset = None


#Knopkalar
keyboard=[['Rasxod'],['Kirim']]
keyboard1=[['Oylik'],['Boshqa']]
keyboard2=[['so`m'],['dollar']]

#build keyboard chala darbotka kerak
def build_keyboard(keyboard):
    reply_markup = {"keyboard":keyboard,
                    "one_time_keyboard":True,
                    "resize_keyboard":True,
                    "input_field_placeholder":"Quyidagilardan birini tanlang! So`z yozmang"}
    return json.dumps(reply_markup) #wuni sal chunmadm

#Knopkalar2
inbord2=[[{'text':'Konsentrator' ,   'callback_data':'DCU'},{'text':'Xisoblagich' ,   'callback_data':'METER'}]]
inbord1=[[{'text':'Qoraqalpoq HETK',             'callback_data':'35000'},
        {'text':'Andijon HETK',                  'callback_data':'03000'}],
         [{'text':'Buxoro HETK',                 'callback_data':'06000'},
         {'text':'Jizzax HETK',                  'callback_data':'08000'}],
         [{'text':'Qashqadaryo HETK',            'callback_data':'10000'},
         {'text':'Navoiy HETK',                  'callback_data':'12000'}],
         [{'text':'Namangan HETK',               'callback_data':'14000'},
         {'text':'Samarqand HETK',               'callback_data':'18000'}],
         [{'text':'Surxondaryo HETK',            'callback_data':'22000'},
         {'text':'Sirdaryo HETK',                'callback_data':'24000'}],
         [{'text':'Toshkent HETK',               'callback_data':'27000'},
         {'text':"Farg‘ona HETK",                'callback_data':'30000'}],
         [{'text':'Xorazm HETK',                 'callback_data':'33000'},
         {'text':'Toshkent shahar ETK',          'callback_data':'26000'}]]

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




#database bn aloqa region aniqlaw un__________________________
dbname = "reestr"
user = "fayzullo"
password = "fayzullo"
host = "192.168.14.74"
port = "5432"

def region(regioncode):
    cursor=None
    conn=None
    data=None
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cursor = conn.cursor()
        sql_commanda="select distinct  esp , espcode  from output1_csv where ptes_code  Ilike  %s;"
        cursor.execute(sql_commanda,(regioncode,))
        data = list(cursor.fetchall())
    except psycopg2.Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return data


#database bn aloqa tuman aniqlaw un__________________________
dbname = "reestr"
user = "fayzullo"
password = "fayzullo"
host = "192.168.14.74"
port = "5432"

def esp(espcode):
    cursor=None
    conn=None
    data=None
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cursor = conn.cursor()
        sql_commanda="select esp , esp_code  from cas_area where esp_code  ilike %s;"
        cursor.execute(sql_commanda,(espcode,))
        data = list(cursor.fetchall())
    except psycopg2.Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return data

#database bn aloqa dcu topiw un__________________________
dbname = "reestr"
user = "fayzullo"
password = "fayzullo"
host = "192.168.14.74"
port = "5432"

def dcu_info(dcu_number):
    cursor=None
    conn=None
    data=None
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cursor = conn.cursor()
        sql_commanda="select * from output1_csv where dev_no =%s"
        cursor.execute(sql_commanda,(dcu_number,))
        data = list(cursor.fetchone())
    except psycopg2.Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return data



#Kelgan smsni obrobotka
while True:
    response = requests.get(base_url + f"getUpdates?offset={offset}")
    if response.ok:
        data = response.json()
        if data["ok"]:
            if data["result"]:
                for update in data["result"]:
                    #print (update)
                    if 'message' in update:
                        chatId = update['message']["chat"]["id"]
                        if "text" in update['message']:
                            print(update)
                            sendMessage(chatId,"Bot ga hush kelibsiz!! \n Ushbu bot yordamida siz konsentratorlarni lokatsiyasi haqida ma`lumot olishingiz mumkin \n Buning uchun siz o`zingiga kerak bo`lgan qurilmani tanlang tanlang")
                            sendMessage(chatId,"Qaysi qurilma haqida ma`lumot qidiramiz?",inline_keyboard(inbord2))
                            # print (update['message']["text"])
                        if 'text' in update['message']:
                            #print ("tugri1")
                            malumot1 = update["message"]["text"] 
                            #sendMessage(chatId,"sz oddiy suz yubordiz")
                    elif 'callback_query' in update:
                        #print('knopka') 
                        chatId =update['callback_query']['message']["chat"]["id"]
                        callbackdata = update['callback_query']['data']
                        if "DCU" in update['callback_query']['data']:
                            sendMessage(chatId,"O`zingizga kerakli bo`lgan hududni tanlang DCU",inline_keyboard(inbord1))      
                        elif "METER" in update['callback_query']['data']:
                            sendMessage(chatId,"Xozircha Xisoblagichlar haqida ma`lumot yubora olmaymiz")          
                    elif 'callback_query' in update:
                        #print('knopka') 
                        chatId =update['callback_query']['message']["chat"]["id"]
                        callbackdata = update['callback_query']['data']
                        a = region(str(callbackdata))
                        sending_text='Katta Xolamn rayonlari \n'
                        for q in a:
                            sending_text=sending_text+q[0]+' - '+q[1]+'\n'
                        sendMessage(chatId,sending_text)
                        sendMessage(chatId,"Qaysi hudud",inline_keyboard(inbord1))
                    offset = update["update_id"] + 1
        else:
            print("Error in API response:", data["description"])
    else:
        print("Failed to make the API request.")
    time.sleep(0.1) 
# #keladigan oddiy sms    
        #       if "text" in update['message']:
        # {'update_id': 412296779, 
        #  'message': {'message_id': 1789, 'from': {'id': 171319245, 'is_bot': False, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'language_code': 'ru'},
        #               'chat': {'id': 171319245, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'type': 'private'},
        #                 'date': 1695030771, 
        #                 'text': '/start', 
        #                 'entities': [{'offset': 0, 'length': 6, 'type': 'bot_command'}]}}
    

# #Inline knopkadan kegan sms
    #             if "text" in update['callback_query']['message']:
    # {'update_id': 412296771, 
    #  'callback_query': {'id': '735810555401851063',
    #                      'from': {'id': 171319245, 'is_bot': False, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'language_code': 'ru'}, 
    #                      'message': {'message_id': 1780, 'from': {'id': 6129894724, 'is_bot': True, 'first_name': 'Requests Test Bot', 'username': 'reqtest_bot'}, 
    #                                  'chat': {'id': 171319245, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'type': 'private'}, 
    #                                  'date': 1695022887, 
    #                                  'text': 'Ushbu BOT sizga Konsentratorlar haqida ma`lumot beradi! \n Bunin uchun siz o`z hududingizni tanlang', 
    #                                  'reply_markup': {'inline_keyboard': [[{'text': '1', 'callback_data': 'bir'}, 
    #                                                                        {'text': '2', 'callback_data': 'ikki'},
    #                                                                          {'text': '3', 'callback_data': 'uch'}],
    #                                                                            [{'text': '4', 'callback_data': 'tort'},
    #                                                                              {'text': '5', 'callback_data': 'besh'},
    #                                                                                {'text': '6', 'callback_data': 'olti'}]]}}, 
    #                                                                                'chat_instance': '5323233157514262773',
    #                                                                                  'data': 'olti'}}


    


# ['Zafar ShETK',                      #1 ESP
#  '27220' ,                           #2 ESP Code
#    'NS DVZ-2 35/10 kV',              #Substation
#    'ТОШЛОК',                         #Feeder
#    '666',                            #TR
#    'DCU',                            #dev_type
#    '119201029745',                   #dev_no
#    'Offline',                        #Status
#      '19/05/2022 19:04:59',          #on_off_time
#        'UZMOBILE',                   #com_operatot
#          '40.335285',                #latititude
#          '69.24172667',              #Longtitude
#            '92.63.204.30',           #dev_ip
#              '2697',                 #dev_port
#                'hes-fep-1-group1-0.hes-hs.prod.svc.cluster.local',  #server_ip 
#                '899989900260899054',   #sim_no SSID
#                  '',                   #manager_name
#                  '',                   #manager_phone
#                    '',                 #phone_no
#                      '']               #account_id

##{'update_id': 412296856
# , 'message': {'message_id': 1948,
# 'from': {'id': 171319245, 'is_bot': False, 
# 'first_name': 'Fayzullo', 
# 'last_name': 'Kamol', 'username': 'kamolfayzullo',
# 'language_code': 'ru'}, 'chat': {'id': 171319245, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'type': 'private'}, 
# 'date': 1696524005, 'text': '123'}}