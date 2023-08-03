# import requests
# bot_token='6129894724:AAEZc_cSdJCOJWTnypyPtLgfOPuUXA08IZM'
# base_url=f'https://api.telegram.org/bot{bot_token}/'
# my_id=171319245


# def send_message(chat_id,text):
#     message_url=base_url+f'sendMessage?chat_id={chat_id}&text={text}'
#     requests.get(message_url)


# send_message(my_id,'sanga nima ')

#________________________________________________________________________________#

#https://api.telegram.org/bot<token>/METHOD_NAME
#Telegramga message jonatiw
import time
import requests
botToken = "6129894724:AAEZc_cSdJCOJWTnypyPtLgfOPuUXA08IZM"
baseAdres = f"https://api.telegram.org/bot{botToken}/"
myId = 171319245
def sendMessage(chatId,text):
    messageUrl=baseAdres+f"sendMessage?chat_id={chatId}&text={text}"
    requests.get(messageUrl)
response=requests.get('https://nbu.uz/uz/exchange-rates/json/')
# print(dir(response))
# if response.ok==True:
if response.ok:
    print('Request muvofaqyatli boldi')

print(response.status_code) #muvofaqyatli bolish uchun 200

# print(response.json())
print(response)
for i in response.json():  
    if i["title"]== 'AQSh dollari':     
            SKursi = i["cb_price"]
    elif i["title"]== 'Yevro':
            EKursi = i["cb_price"]
    elif i["title"]== 'Rossiya rubli':
            RKursi = i["cb_price"]

          
natija = 'AQSh dollari ' + str(SKursi) + "\n" + 'EURO ' + str(EKursi) + "\n" + "Rubl" + str(RKursi)


sendMessage (myId,natija)


    