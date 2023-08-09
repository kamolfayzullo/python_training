import json
import time
import requests
import urllib
import datetime as dt

#bot manzil
bot_token = '6129894724:AAEZc_cSdJCOJWTnypyPtLgfOPuUXA08IZM'
base_url = f'https://api.telegram.org/bot{bot_token}/'


#Knopkalar
keyboard=[['Valyuta'],['🌦Ob-Havo']]
keyboard1=[['🇺🇿➡️🇺🇸'],['🇺🇸➡️🇺🇿']]
keyboard2=[['Ortga']]


#build keyboard
def build_keyboard(keyboard):
    reply_markup = {"keyboard":keyboard,"one_time_keyboard":True,"resize_keyboard":True,
                    "input_field_placeholder":"Quyidagilardan birini tanlang! So`z yozmang"}
    return json.dumps(reply_markup)


#xabar yuboradi
def sendMessage(chatId,text,reply_markup=None):
    messageUrl=base_url+f"sendMessage?chat_id={chatId}&text={text}"
    if reply_markup:
        messageUrl = messageUrl +  "&reply_markup={}".format(reply_markup)
    requests.get(messageUrl)


#Location Json format





#Yordamchi 
valyuta=None
type1 = None
havo = None
offset = None


#xabar qabul qiladi
while True:
    response = requests.get(base_url + f"getUpdates?offset={offset}")
    if response.ok:
        data = response.json()
        if data["ok"]:
            if data["result"]:
                for update in data["result"]:
                    chatId = update['message']["chat"]["id"]
                    if "text" in update['message']:
                        sendMessage (chatId,"norm")

                    offset = update["update_id"] + 1
        else:
            print("Error in API response:", data["description"])
    else:
        print("Failed to make the API request.")

    time.sleep(0.1) 

    {'update_id': 412296727,
      'message': {'message_id': 1698,
                   'from': {'id': 171319245, 'is_bot': False, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'language_code': 'ru'}, 
                   'chat': {'id': 171319245, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'type': 'private'},
                     'date': 1691394739,
                       'forward_from': {'id': 171319245, 'is_bot': False, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'language_code': 'ru'},
                         'forward_date': 1691167586,
                           'location': {'latitude': 46.597528, 'longitude': 9.316791}}}