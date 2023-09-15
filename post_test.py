import psycopg2 #pythondan postgresqlga boglashga ishlatiladgan library
import json
import time
import requests
import urllib
import datetime as dt

#bot manzil
bot_token = '6473562141:AAEolg-naoNdusP6rppQ_eIhQgZc1V9M71s'
base_url = f'https://api.telegram.org/bot{bot_token}/'

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

#xabar yuboradi
def sendMessage(chatId,text,reply_markup=None):
    messageUrl=base_url+f"sendMessage?chat_id={chatId}&text={text}"
    if reply_markup:
        messageUrl = messageUrl +  "&reply_markup={}".format(reply_markup)
    requests.get(messageUrl)


#database bn aloqa__________________________
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
        sql_commanda="select * from dcu_location dl  where dev_no =%s"
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

while True:
    response = requests.get(base_url + f"getUpdates?offset={offset}")
    if response.ok:
        data = response.json()
        if data["ok"]:
            if data["result"]:
                for update in data["result"]:
                    #print (update)
                    chatId = update['message']["chat"]["id"]
                    if "text" in update['message']:
                        malumot = update["message"]["text"]              
                        if malumot == "/start":
                            sendMessage (chatId,"Salom bu BOT ni tugatwimiz kerak",build_keyboard(keyboard))   
                        elif malumot == "Kirim":
                            sendMessage (chatId,"Oylik tuwdimi?",build_keyboard(keyboard1)) 
                        elif malumot == "Oylik":
                            sendMessage (chatId,"Qancha tuwdi?" "Summani kiriting") 
                            kirim=1
                        elif kirim ==1:
                            summa = int(malumot)
                            print ("tugri2")
                            print (summa)
                            #bu yerga smsdan kelgan habarni yozamiz    
                            # print (kirim)
                            # yigindi = str(kirim)
                            # print (yigindi)
                        elif malumot != "sdvjnsdkvsdkskhbvdkshbvsdbigsdykassjvnhsdbvhsdvjsdb":
                            sendMessage(chatId,"So`z yozmang siz bilan gaplashib o`tirishga vaqtim yo`q \n Quyidagilardan birini tanlang!! \n 👇🏼👇🏼👇🏼",build_keyboard(keyboard))
                    elif "voice" in update['message']:
                        sendMessage (chatId,"Ovozli habarga hozircha javob bera olmayman!!")
                    elif "location" in update['message']:
                        sendMessage (chatId,"Lokatsiya yubormang !!")
                    elif "voisavasdfdsgsce" != update['message']:
                        sendMessage (chatId, "Xarhil narsa jo`natmang!!")
                    offset = update["update_id"] + 1
        else:
            print("Error in API response:", data["description"])
    else:
        print("Failed to make the API request.")

    time.sleep(0.1) 

    
    print(dcu_info('119201029745'))

 ['Zafar ShETK',
  '27220' ,
    'NS DVZ-2 35/10 kV', 
    'ТОШЛОК', 
    '666', 
    'DCU', 
    '119201029745', 
    'Offline',
      '19/05/2022 19:04:59',
        'UZMOBILE',
          '40.335285', 
          '69.24172667',
            '92.63.204.30',
              '2697',
                'hes-fep-1-group1-0.hes-hs.prod.svc.cluster.local', 
                '899989900260899054',
                  '', 
                  '',
                    '',
                      '']
