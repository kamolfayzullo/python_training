import sqlite3
import json
import time
import requests

#bot manzil
bot_token = '6671112279:AAEg5YkmX4FvHRDQ2tmo-pIm-1TFkIpAL1k'
base_url = f'https://api.telegram.org/bot{bot_token}/'



#sms yuborw
def sendMessage(chatId,text,reply_markup=None):
    messageUrl=base_url+f"sendMessage?chat_id={chatId}&text={text}"
    if reply_markup:
        messageUrl = messageUrl +  "&reply_markup={}".format(reply_markup)
    requests.get(messageUrl)





offset = None
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
                offset = update["update_id"] + 1
        else:
            print("Error in API response:", data["description"])
    else:
        print("Failed to make the API request.")
    time.sleep(0.1) 




print (str(response))

bot_token = '6671112279:AAEg5YkmX4FvHRDQ2tmo-pIm-1TFkIpAL1k'
base_url = f'https://api.telegram.org/bot6671112279:AAEg5YkmX4FvHRDQ2tmo-pIm-1TFkIpAL1k/getUpdates?'


#### sms
{"update_id":534266311,
 "message":
    {"message_id":7,
     "from":
         {"id":171319245,
          "is_bot":false,
          "first_name":"Fayzullo",
          "last_name":"Kamol",
          "username":"kamolfayzullo",
          "language_code":"ru"},
         "chat":{"id":171319245,
                 "first_name":"Fayzullo",
                 "last_name":"Kamol",
                 "username":"kamolfayzullo",
                 "type":"private"},
         "date":1705906316,
         "text":"saasf"}}

{"ok":true,"result":[{"update_id":534266316,
"message":{"message_id":12,
           "from":{"id":171319245,"is_bot":false,"first_name":"Fayzullo","last_name":"Kamol","username":"kamolfayzullo","language_code":"ru"},
           "chat":{"id":171319245,"first_name":"Fayzullo","last_name":"Kamol","username":"kamolfayzullo","type":"private"},
           "date":1705908914,
           "animation":{"file_name":"happy-tears.mp4","mime_type":"video/mp4","duration":2,"width":320,"height":320,
                        "file_id":"CgACAgQAAxkBAAMMZa4asptoz1nWSgFJcxBt5GWSN0oAAnMDAALEaiVSijnjxfNu6KA0BA",
                        "file_unique_id":"AgADcwMAAsRqJVI","file_size":98196},
           "document":{"file_name":"happy-tears.mp4","mime_type":"video/mp4",
                       "file_id":"CgACAgQAAxkBAAMMZa4asptoz1nWSgFJcxBt5GWSN0oAAnMDAALEaiVSijnjxfNu6KA0BA",
                       "file_unique_id":"AgADcwMAAsRqJVI","file_size":98196}}},
                     {"update_id":534266317,
                      
"message":{"message_id":13,"from":{"id":171319245,"is_bot":false,"first_name":"Fayzullo",
                                   "last_name":"Kamol","username":"kamolfayzullo","language_code":"ru"},
           "chat":{"id":171319245,"first_name":"Fayzullo","last_name":"Kamol","username":"kamolfayzullo","type":"private"},
           "date":1705908921,"voice":{"duration":1,"mime_type":"audio/ogg",
                                      "file_id":"AwACAgIAAxkBAAMNZa4aufUgcNNE1ZtRT_UjQZi80TcAAqw_AAJQAAFxSYAqgaKyPWzUNAQ",
                                      "file_unique_id":"AgADrD8AAlAAAXFJ",
                                      "file_size":5953}}},
                     {"update_id":534266318,
                      
"message":{"message_id":14,"from":{"id":171319245,"is_bot":false,"first_name":"Fayzullo","last_name":"Kamol","username":"kamolfayzullo","language_code":"ru"},"chat":{"id":171319245,"first_name":"Fayzullo","last_name":"Kamol","username":"kamolfayzullo","type":"private"},"date":1705908927,"document":{"file_name":"\u0413\u0440\u0430\u0444\u0438\u043a \u043e\u0431\u0445\u043e\u0434\u0430 \u041e\u0422\u041a \u043c\u0435\u0434\u0438\u0430\u043f\u0430\u0440\u043a.3.xlsx","mime_type":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet","file_id":"BQACAgIAAxkBAAMOZa4av7Lx3mnxnrEgn1yhqzhZItYAAq0_AAJQAAFxSeB7qSv0Kfy6NAQ","file_unique_id":"AgADrT8AAlAAAXFJ","file_size":23701}}},{"update_id":534266319,
"message":{"message_id":15,"from":{"id":171319245,"is_bot":false,"first_name":"Fayzullo","last_name":"Kamol","username":"kamolfayzullo","language_code":"ru"},"chat":{"id":171319245,"first_name":"Fayzullo","last_name":"Kamol","username":"kamolfayzullo","type":"private"},"date":1705908945,"location":{"latitude":41.305429,"longitude":69.279676}}},{"update_id":534266320,
"message":{"message_id":16,"from":{"id":171319245,"is_bot":false,"first_name":"Fayzullo","last_name":"Kamol","username":"kamolfayzullo","language_code":"ru"},"chat":{"id":171319245,"first_name":"Fayzullo","last_name":"Kamol","username":"kamolfayzullo","type":"private"},"date":1705908987,"contact":{"phone_number":"998998805453","first_name":"Aaaaaa","user_id":134048533}}}]}