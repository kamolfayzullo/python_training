import json
import time
import requests
import urllib
import datetime as dt
from countryCode import country_codes

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


#Kurs qiymati
def kurs():
    urlbank = requests.get('https://nbu.uz/uz/exchange-rates/json/')
    kursmalumot = urlbank.json()
    for i in kursmalumot:
        if i["title"] == "AQSh dollari":
            kurssoliw = i['nbu_buy_price']
    return kurssoliw
kursqiymat = float(kurs())

#Ob-Havo

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
                        malumot = update["message"]["text"]              
                        if malumot == "/start":
                            sendMessage (chatId,"Assalomualaykum!😎 \nUshbu BOT yordamida quyidagilarni bilib olasiz \n -Valyuta🤑 Kursi \n -Ob-Havo🌦 ma`lumotlari",build_keyboard(keyboard))                 
                        elif malumot == 'Ortga':
                            havo = None
                            valyuta = None
                            type1 = None
                            sendMessage (chatId,"Endi qaysi amal?",build_keyboard(keyboard))    
                        elif malumot == 'Valyuta':
                            havo = None
                            valyuta="valyuta"
                            sendMessage (chatId,"Tanlang! \n '🇺🇿➡️🇺🇸' so`m dollargami? \n '🇺🇸➡️🇺🇿' dollar so`mgami?",build_keyboard(keyboard1))
                        elif malumot == '🇺🇿➡️🇺🇸':
                            havo = None
                            type1 = "uzs"
                            sendMessage (chatId,"Summa kiriting so`mda")
                        elif malumot =='🇺🇸➡️🇺🇿':
                            havo = None
                            type1 = "suz"
                            sendMessage (chatId,"Summa kiriting dollarda")
                        elif valyuta=="valyuta" and type1 == "uzs":
                            try:
                                qiymat = float(malumot)
                                sendMessage(chatId,f"{qiymat} so`m \n {round((qiymat / kursqiymat),2)} dollarga teng",build_keyboard(keyboard2))
                            except:
                                sendMessage(chatId,"Xato ma`lumot yubordiz")
                        elif valyuta=="valyuta" and type1 == "suz":
                            try:
                                qiymat = float(malumot)
                                sendMessage(chatId,f"{qiymat} dollar \n {round((qiymat * kursqiymat),2)} so`mga teng",build_keyboard(keyboard2))
                            except:
                                sendMessage(chatId,"Xato ma`lumot yubordiz")            
                        elif malumot == '🌦Ob-Havo':
                            havo = "havo"
                            sendMessage(chatId,"Lokatsiya jo`nating",build_keyboard(keyboard2))
                        elif malumot != "sdvjnsdkvsdkskhbvdkshbvsdbigsdykassjvnhsdbvhsdvjsdb":
                            sendMessage(chatId,"So`z yozmang siz bilan gaplashib o`tirishga vaqtim yo`q \n Quyidagilardan birini tanlang!! \n 👇🏼👇🏼👇🏼",build_keyboard(keyboard))
                    elif "voice" in update['message']:
                        sendMessage (chatId,"Ovozli habarga hozircha javob bera olmayman!!")
                    elif "location" in update['message']:
                        #print (update)
                        if havo == "havo":
                            longtude = update['message']['location']['longitude']
                            latude = update['message']['location']['latitude']
                            print (longtude,latude)
                            response=requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latude}&lon={longtude}&appid=a6ffc8b3cadf6c0445beba80ac186b62&lang=ru&units=metrics/')
                            obhavo = response.json()
                            davlat = str(obhavo["sys"]["country"])
                            #print (davlat)
                            for i in country_codes:
                                if i['code'] == davlat:
                                    davlatnomi = i["country"]
                                    #print (davlatnomi)
                                    sendMessage(chatId,f"Siz {davlatnomi} {obhavo['name']}dasiz \n Harorat {obhavo['main']['temp']} ga teng")
                                # for i in country_codes:
                                #     if i == davlat:
                                #         davlatnomi = i["country"]
                                #         print (davlatnomi)
                                        #sendMessage (chatId,f"Siz {davlatnomi} {obhavo['coord']['name']}  ni tanladingiz havo harorati {obhavo['coord']['main']['temp']} ga teng")
                    elif "voisavasce" != update['message']:
                        sendMessage (chatId, "Xarhil narsa jo`natmang!!")

                    offset = update["update_id"] + 1
        else:
            print("Error in API response:", data["description"])
    else:
        print("Failed to make the API request.")

    time.sleep(0.1) 


