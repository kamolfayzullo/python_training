import json
import time
import requests
import urllib
import datetime as dt
from countryCode import country_codes

#bot manzil
bot_token = '6473562141:AAEolg-naoNdusP6rppQ_eIhQgZc1V9M71s'
base_url = f'https://api.telegram.org/bot{bot_token}/'


#Knopkalar
keyboard=[['Rasxod'],['Kirim']]
keyboard1=[['Oylik'],['Boshqa']]
keyboard2=[['so`m'],['dollar']]



#hisob uchun







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


#Kurs qiymati keremas xozrcha
# def kurs():
#     urlbank = requests.get('https://nbu.uz/uz/exchange-rates/json/')
#     kursmalumot = urlbank.json()
#     for i in kursmalumot:
#         if i["title"] == "AQSh dollari":
#             kurssoliw = i['nbu_buy_price']
#     return kurssoliw
# kursqiymat = float(kurs())

#Ob-Havo
yigindi = a + 0
#Yordamchi 
kirim=None
summa = None
if summa != None:
    a = summa 
else:
    pass


#xabar qabul qiladi
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

