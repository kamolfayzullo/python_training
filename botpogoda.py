import json
import time
import requests
import urllib
import datetime as dt



a =  {'update_id': 412296220,
      'message': {'message_id': 252, 'from': {'id': 171319245, 'is_bot': False, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'language_code': 'ru'},
                  'chat': {'id': 171319245, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'type': 'private'},
                  'date': 1690806776, 'text': 'Salom'}}


bot_token = '6129894724:AAEZc_cSdJCOJWTnypyPtLgfOPuUXA08IZM'
base_url = f'https://api.telegram.org/bot{bot_token}/'



offset = None
while True:
    response = requests.get(base_url + f"getUpdates?offset={offset}")
    if response.ok:
        data = response.json()
        #print('data:',data)
        if data["ok"]:
            if data["result"]:
                for update in data["result"]:
                    timestamp=update['message']['date']

                    readable_date=dt.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                    print(timestamp,readable_date)

                    offset = update["update_id"] + 1
        else:
            print("Error in API response:", data["description"])
    else:
        print("Failed to make the API request.")
    time.sleep(1)



# import json
# import time
# import requests
# import datetime as dt


# botToken ="6129894724:AAEZc_cSdJCOJWTnypyPtLgfOPuUXA08IZM"
# botUrl =f"https://api.telegram.org/bot{botToken}/"

# offset = None
# while True:
#     response = requests.get(botUrl + f"getUpdates?offset={offset}")
#     if response.ok:
#         data =response.json()
#         if data["ok"]:
#             for update in data:
#                 print(update)
#         else:
#             print ("Xatolik JSON file da")
            
#     else:
#         print ("Xatolik API murojatida")
 
