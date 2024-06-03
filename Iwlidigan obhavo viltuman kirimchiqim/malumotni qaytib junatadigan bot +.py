import sqlite3
import json
import time
import requests
import urllib
from datetime import datetime
import os 

offset = None

bot_token = '6671112279:AAEg5YkmX4FvHRDQ2tmo-pIm-1TFkIpAL1k'
base_url = f'https://api.telegram.org/bot{bot_token}/'

import requests


input_path ="C:/Users/Admin/Desktop/python_training/work_files/bot.log"

#file yuboradi
def sendDocument(chat_id,caption,input_path):
    with open(input_path,'rb') as f:
        url = base_url + f"sendDocument?chat_id={chat_id}&caption={caption}"
        requests.post(url,files={'document':f})
    
#sendDocument(chatId,"Ma`lumot",input_path)






# # Ваши данные
# bot_token = "YOUR_BOT_TOKEN"
# chat_id = "YOUR_CHAT_ID"
# log_file_path = "/путь/к/вашему/лог-файлу/log.txt"

# Отправка лог-файла
# send_log(bot_token, chat_id, log_file_path)

#xabar yuboradi

def sendMessage(chatId,text,reply_markup=None):
    messageUrl=base_url+f"sendMessage?chat_id={chatId}&text={text}"
    if reply_markup:
        messageUrl = messageUrl +  "&reply_markup={}".format(reply_markup)
    requests.get(messageUrl)

## log save
def log_save(chat_id,m_type,username,date_time):
    date_time=datetime.utcfromtimestamp(vaqt).strftime('%H:%M %d.%m.%Y')
    my_file=open('bot.log','w')
    my_file.write(f'ChatID . {chat_id} \n Message . {m_type} \n username. {username} \n kelgan vaqti  {date_time}')
    my_file.close()
    




offset = None
chatId = None
sms = None  
vaqt = None
username = None





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
                        vaqt = update['message']["date"]
                        username = update['message']["chat"]["username"]
                        print(update['message'])
                        if "text" in update['message']:
                            print("text")
                            sms = "text"
                        elif "voice" in update['message']:
                            print("voice")
                            sms = "voice"
                        elif "contact" in update['message']:
                            print("contact")
                            sms = "contact"
                        else:
                            print("Bowqa")
                            sms = "Bowqa"
                        log_save(chatId,sms,username,vaqt)
                        sendDocument(chatId,"Ma`lumot",input_path)
                    else:
                        print ("Xatolik1")
                    offset = update["update_id"] + 1
        else:
            print("Error in API response:", data["description"])
    else:
        print("Failed to make the API request.")
    time.sleep(0.1) 
    
#so`z    
{'update_id': 534266325, 
 'message': {'message_id': 21, 
             'from': {'id': 171319245, 'is_bot': False, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'language_code': 'ru'}, 
             'chat': {'id': 171319245, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'type': 'private'}, 
             'date': 1705920258, 
             'text': '/start', 
             'entities': [{'offset': 0, 'length': 6, 'type': 'bot_command'}]}}

#voice
{'update_id': 534266326, 
 'message':
    {'message_id': 22, 'from': {'id': 171319245, 'is_bot': False, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'language_code': 'ru'},
     'chat': {'id': 171319245, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'type': 'private'},
     'date': 1705920273, 
     'voice': {'duration': 1, 'mime_type': 'audio/ogg', 'file_id': 'AwACAgIAAxkBAAMWZa5HEW8dK2FWkqDNoMK57-luKggAAjVCAAJQAAFxSWFXAxDK_mc4NAQ', 'file_unique_id': 'AgADNUIAAlAAAXFJ', 'file_size': 3902}}}

#contact
{'update_id': 534266327, 
 'message': 
     {'message_id': 23, 
     'from': {'id': 171319245, 'is_bot': False, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'language_code': 'ru'}, 
     'chat': {'id': 171319245, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'type': 'private'}, 
     'date': 1705920282, 
     'forward_date': 1705908987,
     'contact': {'phone_number': '998998805453', 'first_name': 'Aaaaaa', 'user_id': 134048533}}}

#1)file yaratish
#new_file=open('test1.txt','x')

#2)read
#my_file=open('test1.txt','r')
#print(my_file.read())

#3)write ustiga yozvoradi
# my_file=open('test1.txt','w')
# my_file.write('Xusan')

#4)append va 'a'
# my_file=open('test1.txt','a')
# my_file.write('\nNuriddin')

my_file=open('test1.txt','r')
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
for i in my_file:
    print(i)

# print(my_file.read())

# print(my_file.read(2))

# print(my_file.readlines())
# for row in my_file.readlines():
#     print(row)
# print('\n\n\n\n')
# print(dir(my_file))

# os.remove('test.txt')
# os.remove('test1.txt')


