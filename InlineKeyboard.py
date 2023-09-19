Javohiraka Askue operator, [18.09.2023 10:56]
import time
import sqlite3
import requests
import json

bot='6546508751:AAGW8bjV545JitadUTUvJkPm0hr_1S3qBtY'
adress=f'https://api.telegram.org/bot{bot}/'

keyboard=[['Konsentrator'],['Hisoblagich']]
keybor1=[[{
    'text':'1',
    'callback_data':'bir'
},{
    'text':'2',
    'callback_data':'ikki'
},{
    'text':'3',
    'callback_data':'uch'
}],[{
    'text':'4',
    'callback_data':'tort'
},{
    'text':'5',
    'callback_data':'besh'
},{
    'text':'6',
    'callback_data':'olti'
}],]

def inline_keyboard(keyboard):
    reply_markup={'inline_keyboard':keyboard}
    return json.dumps(reply_markup)
    

def build_keyboard(keyboard):
    reply_markup={'keyboard':keyboard,'one_time_keyboard':True,'resize_keyboard':True,'input_field_placeholder':'Quyidagilardan birini tanlang'}
    return json.dumps(reply_markup)


def sendmessage(chatid,text,reply_markup=None):
    texturl=adress+f'sendMessage?chat_id={chatid}&text={text}'
    if reply_markup:
        texturl=texturl+'&reply_markup={}'.format(reply_markup)
    requests.get(texturl)


offset=None
while True:
    response=requests.get(adress+f'getUpdates?offset={offset}')
    if response.ok:
        data=response.json()
        if data['ok']:
            if data['result']:
                for update in data['result']:
                    if 'message' in update:
                        chatid=update['message']['chat']['id']
                        if 'text' in update['message']:
                            text=update['message']['text']
                            sendmessage(chatid,'lalaku',inline_keyboard(keybor1))
                        
                    elif 'callback_query' in update:
                        chatid=update['callback_query']['message']['chat']['id']
                        data=update['callback_query']['data']
                        print(data)
                        sendmessage(chatid,'knopka bosding')
                        
                        
                        
                offset=update['update_id']+1       
    time.sleep(0.001)