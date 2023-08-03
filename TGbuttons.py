import json
import time
import requests
import urllib
import datetime as dt
#bot manzil
bot_token = '6129894724:AAEZc_cSdJCOJWTnypyPtLgfOPuUXA08IZM'
base_url = f'https://api.telegram.org/bot{bot_token}/'

 


Input=[]

#Knopkalar
keyboard=[['Valyuta'],['🌦Ob-Havo']]
keyboard1=[['🇺🇿➡️🇺🇸'],['🇺🇸➡️🇺🇿']]
keyboard2=[['Qayta Boshlash']]


# def getLatLon():
#     response = requests.get("https://ipinfo.io/json")
#     geodata=response.json()['loc']
#     lat=float(geodata.split(',')[0])
#     lon=float(geodata.split(',')[1])
#     return lat,lon

# lat,lon=getLatLon()
# #knopka yasaydi

#dumps???
def build_keyboard(keyboard):
    reply_markup = {"keyboard":keyboard,"one_time_keyboard":True,"resize_keyboard":True,
                    "input_field_placeholder":"Kiriting"}
    return json.dumps(reply_markup)


#xabar yuboradi
def sendMessage(chatId,text,reply_markup=None):
    messageUrl=base_url+f"sendMessage?chat_id={chatId}&text={text}"
    if reply_markup:
        messageUrl = messageUrl +  "&reply_markup={}".format(reply_markup)
    requests.get(messageUrl)

valyuta=None
type1 = None
havo = None


def kurs():
    urlbank = requests.get('https://nbu.uz/uz/exchange-rates/json/')
    kursmalumot = urlbank.json()
    for i in kursmalumot:
        if i["title"] == "AQSh dollari":
            kurssoliw = i['nbu_buy_price']
    return kurssoliw

kursqiymat = float(kurs())

 


#xabar qabul qiladi
offset = None
while True:
    response = requests.get(base_url + f"getUpdates?offset={offset}")
    if response.ok:
        data = response.json()
        #print('data:',data)
        if data["ok"]:
            if data["result"]:
                for update in data["result"]:
                    chatId = update['message']["chat"]["id"]
                    if "text" in update:
                        malumot = update["message"]["text"]
                        if malumot=='/start' or malumot== 'Qayta Boshlash':
                            valyuta=None
                            type1=None
                            havo = None
                            sendMessage (chatId,"Assalomu alaykum ushbu botda ob-havo yoki valyuta kurslarini bilishingiz mumkin",build_keyboard(keyboard))
                        elif malumot == '🌦Ob-Havo':
                            havo = "havo"
                            sendMessage (chatId,"Location yuboring",build_keyboard(keyboard2))
                            valyuta=None
                            type1=None
                        
                        elif malumot == 'Valyuta':
                            sendMessage (chatId,"Tanlang \n So`mni dollarga aylantiramizmi? \n Dollarni so`mga aylantiramizmi?",build_keyboard(keyboard1))
                            valyuta='Valyuta'
                        elif malumot =='🇺🇿➡️🇺🇸':
                            type1='🇺🇿➡️🇺🇸'
                            sendMessage (chatId,"Qancha miqdor USD teng bo`lishini bilish uchun summa kiriting(UZS) !")
                        elif malumot =='🇺🇸➡️🇺🇿':
                            type1='🇺🇸➡️🇺🇿'
                            sendMessage (chatId,"Sotish uchun summa kiriting(USD) \n cent bo`lsa nuqta (.) bilan kiriting !")
                        elif valyuta=='Valyuta' and type1=='🇺🇿➡️🇺🇸':
                            try:
                                qiymat=float(malumot)
                                sendMessage (chatId,str(round((qiymat/kursqiymat),2))+' $ ga teng',build_keyboard(keyboard2))
                            except:
                                sendMessage (chatId,"Xato Malumot kirtdiz qaytadan raqam kiriting")
                                
                        elif valyuta=='Valyuta' and type1=='🇺🇸➡️🇺🇿':
                            try:
                                qiymat=float(malumot)
                                sendMessage (chatId,str(round((qiymat*kursqiymat),2))+' Som ga teng',build_keyboard(keyboard2))
                            except:
                                sendMessage (chatId,"Xato Malumot kirtdiz qaytadan raqam kiriting")
                        else:
                            sendMessage (chatId,"Xato Malumot kirtdiz !")
                            valyuta=None
                            type1=None
                            offset = update["update_id"] + 1
                    elif "location" in update:
                        sendMessage (chatId,"Lokatsiya yubordingiz")
                        #print (malumot
                        # sendMessage (chatId,"",build_keyboard(keyboard))
                        
                        offset = update["update_id"] + 1
        else:
            print("Error in API response:", data["description"])
    else:
        print("Failed to make the API request.")

    time.sleep(0.1)  

# {'update_id': 412296259, 
#  'message': {'message_id': 319,
#               'from': {'id': 171319245, 
#                        'is_bot': False, 
#                        'first_name': 'Fayzullo', 'last_name': 'Kamol',
#                          'username': 'kamolfayzullo', 'language_code': 'ru'},
#                          'chat': {'id': 171319245, 'first_name': 'Fayzullo', 'last_name': 'Kamol',
#                                    'username': 'kamolfayzullo', 
#                                   'type': 'private'}, 
#                                   'date': 1690872478, 
#                                   'text': 'salom hammaga'}}

#"message":{"message_id":674,
# "from":{"id":171319245,"is_bot":false,"first_name":"Fayzullo","last_name":"Kamol","username":"kamolfayzullo",
# "language_code":"ru"},
# "chat":{"id":171319245,"first_name":"Fayzullo","last_name":"Kamol","username":"kamolfayzullo","type":"private"},
# "date":1690965950,
# "location":{"latitude":41.305307,"longitude":69.279673}}}]}
sdgbkmdofhbmdfob
Nuriddinga rahmat



