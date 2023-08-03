import json
import time
import requests
import urllib

bot_token = '6129894724:AAEZc_cSdJCOJWTnypyPtLgfOPuUXA08IZM'
base_url = f'https://api.telegram.org/bot{bot_token}/'


def get_updates(offset=None):
    url = base_url + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    response = requests.get(url)
    content = response.content.decode("utf8")
    js = json.loads(content)
    return js
def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def sendVoice (chatId,voice):
    messageUrl=base_url+f"sendVoice?chat_id={chatId}&voice={voice}"
    requests.get(messageUrl)


def sendMessage(chatId,text):
    messageUrl=base_url+f"sendMessage?chat_id={chatId}&text={text}"
    requests.get(messageUrl)


#output





myId = 171319245



def handle_updates(updates):
    for update in updates["result"]:
        # print(update)
        print(update['message'].keys())
        chatId = update['message']["chat"]["id"]
        if 'text' in update['message'].keys():
            response=requests.get('https://nbu.uz/uz/exchange-rates/json/')
            summa = update['message']["text"]
            print(summa,chatId)
            if summa == "/start":
                sendMessage ( chatId,"Assalomualaykum ushbu BOT summa kiritsangiz uni real vaqtdagi dollar kursiga o`girib beradi")
            else:              
                try: 
                    summa = float(summa)
                    for i in response.json():
                        print (i)
                        if i["title"]== 'AQSh dollari':
                            Kursi = i["cb_price"]
                            Oliw = i['nbu_buy_price']
                            Sotiw =i['nbu_cell_price']
                            vaqt = i["date"]
                    Kursi = float(Kursi)
                    Oliw = float(Oliw)
                    Sotiw = float(Sotiw)
                    natija = summa /  Kursi
                    javob = (str(vaqt) + "🗓 kun holatiga"
                        "\n" "Qabul qilindi💸: " + str(round(summa)) + "🇺🇿 UZS" "\n"  "Bu summa " +str(round(natija,2)) + " 🇺🇸💲$")
                    sendMessage ( chatId,javob)
                except:
                    sendMessage ( chatId,"Raqam Kiriting Bratt!")    
        else:
            sendVoice (chatId,"AwACAgIAAxkBAAOnZMOVkKkTCRFy4_m7a5pcpb4_hMQAAnszAAJvliBKRgsBeoAMe4UvBA")















def main():  
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.1)
if __name__ == '__main__':
    main()

