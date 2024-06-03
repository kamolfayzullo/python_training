#import psycopg2 #pythondan postgresqlga boglashga ishlatiladgan library
import json
import time
import requests
import urllib
import datetime as dt




#bot manzil
bot_token = '6129894724:AAEZc_cSdJCOJWTnypyPtLgfOPuUXA08IZM'
base_url = f'https://api.telegram.org/bot{bot_token}/'


#Yordamchi

offset = None


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

#Knopkalar2
inbord2=[[{'text':'Konsentrator' ,   'callback_data':'DCU'},{'text':'Xisoblagich' ,   'callback_data':'METER'}]]
inbord1=[[{'text':'Qoraqalpog`iston',       'callback_data':'35000'},
        {'text':'Andijon',                  'callback_data':'03000'}],
         [{'text':'Buxoro',                 'callback_data':'06000'},
         {'text':'Jizzax',                  'callback_data':'08000'}],
         [{'text':'Qashqadaryo',            'callback_data':'10000'},
         {'text':'Navoiy',                  'callback_data':'12000'}],
         [{'text':'Namangan',               'callback_data':'14000'},
         {'text':'Samarqand',               'callback_data':'18000'}],
         [{'text':'Surxondaryo',            'callback_data':'22000'},
         {'text':'Sirdaryo',                'callback_data':'24000'}],
         [{'text':'Toshkent',               'callback_data':'27000'},
         {'text':"Farg‘ona",                'callback_data':'30000'}],
         [{'text':'Xorazm',                 'callback_data':'33000'},
         {'text':'Toshkent shahar',         'callback_data':'26000'}]]

inbord35000=[[{'text':' Amudaryo ',     'callback_data':'35204'},
{'text':' Bo‘zatov ',                   'callback_data':'35214'}],
[{'text':' Qorao‘zak ',                 'callback_data':'35211'},
{'text':' Mo‘ynoq ',                    'callback_data':'35222'}],
[{'text':' To‘rtko‘l ',                 'callback_data':'35233'},
{'text':' Xo‘jayli ',                   'callback_data':'35236'}],
[{'text':' Beruniy ',                   'callback_data':'35207'},
{'text':' Qonliko‘l ',                  'callback_data':'35218'}],
[{'text':' Kegeyli ',                   'callback_data':'35212'},
{'text':' Qo‘ng‘irot ',                 'callback_data':'35215'}],
[{'text':' Nukus ',                     'callback_data':'35225'},
{'text':' Nukus ',                      'callback_data':'35401'}],
[{'text':" Ellikqal'a ",                'callback_data':'35250'},
{'text':' Chimboy ',                    'callback_data':'35240'}],
[{'text':' Taxiatosh ',                 'callback_data':'35411'},
{'text':' Shumanay ',                   'callback_data':'35243'}],
[{'text':' Taxtako‘pir ',               'callback_data':'35230'}],
[{'text':'Ortga',               'callback_data':'00000'}]]

inbord03000=[[{'text':' Oltinko‘l ', 'callback_data':'03202'},
{'text':' Andijon ', 'callback_data':'03203'}],
[{'text':' Kuyganyor ', 'callback_data':'03204'},
{'text':' Baliqchi ', 'callback_data':'03206'}],
[{'text':' Chinobod ', 'callback_data':'03207'},
{'text':' Bo‘ston ', 'callback_data':'03209'}],
[{'text':' Buloqboshi ', 'callback_data':'03210'},
{'text':' Jalaquduq ', 'callback_data':'03211'}],
[{'text':' Izboskan ', 'callback_data':'03214'},
{'text':' Ulug‘nor ', 'callback_data':'03217'}],
[{'text':' Qo‘rg‘ontepa ', 'callback_data':'03220'},
{'text':' Asaka ', 'callback_data':'03224'}],
[{'text':' Marhamat ', 'callback_data':'03227'},
{'text':' Shahrixon ', 'callback_data':'03230'}],
[{'text':' Shahrixon ', 'callback_data':'03231'},
{'text':' Paxtaobod ', 'callback_data':'03232'}],
[{'text':' Xo‘jaobod ', 'callback_data':'03236'},
{'text':' Andijon Yangi ', 'callback_data':'03401'}],
[{'text':' Andijon Eski ', 'callback_data':'03404'},
{'text':' Asaka ', 'callback_data':'03405'}],
[{'text':' Xonobod ', 'callback_data':'03408'},
{'text':' Andijon Bobur ', 'callback_data':'03403'}],
[{'text':'Ortga',               'callback_data':'00000'}]]

inbord06000=[[{'text':' Qorako‘l ', 'callback_data':'06230'},
{'text':' Shofirkon ', 'callback_data':'06258'}],
[{'text':' Kogon ', 'callback_data':'06219'},
{'text':' Peshku ', 'callback_data':'06240'}],
[{'text':' Buxoro ', 'callback_data':'06401'},
{'text':' Olot ', 'callback_data':'06204'}],
[{'text':' Vobkent ', 'callback_data':'06212'},
{'text':' Jondor ', 'callback_data':'06246'}],
[{'text':' Buxoro ', 'callback_data':'06207'},
{'text':' G‘ijduvon ', 'callback_data':'06215'}],
[{'text':' Qoraulbozor ', 'callback_data':'06232'},
{'text':' Romiton ', 'callback_data':'06242'}],
[{'text':'Ortga',               'callback_data':'00000'}]]

inbord30000=[[{'text':' Bog‘dod ', 'callback_data':'30209'},
{'text':' Dang‘ara ', 'callback_data':'30236'}],
[{'text':' Oltiariq ', 'callback_data':'30203'},
{'text':' O‘zbekiston ', 'callback_data':'30230'}],
[{'text':' Qo‘shtepa ', 'callback_data':'30206'},
{'text':' Toshloq ', 'callback_data':'30227'}],
[{'text':' Farg‘ona ', 'callback_data':'30401'},
{'text':' Qirguli ', 'callback_data':'30403'}],
[{'text':' Uchko‘prik ', 'callback_data':'30221'},
{'text':' Rishton ', 'callback_data':'30224'}],
[{'text':' Marg‘ilon ', 'callback_data':'30412'},
{'text':' Quvasoy ', 'callback_data':'30408'}],
[{'text':' Yozyovon ', 'callback_data':'30242'},
{'text':' Buvayda ', 'callback_data':'30212'}],
[{'text':' Furqat ', 'callback_data':'30238'},
{'text':' Farg‘ona ', 'callback_data':'30233'}],
[{'text':' Quva ', 'callback_data':'30218'},
{'text':' So‘x ', 'callback_data':'30226'}],
[{'text':' Qo‘qon ', 'callback_data':'30405'},
{'text':' Beshariq ', 'callback_data':'30215'}],
[{'text':'Ortga',               'callback_data':'00000'}]]

inbord08000=[[{'text':' Paxtakor ', 'callback_data':'08228'},
{'text':' Yangiobod ', 'callback_data':'08237'}],
[{'text':' Baxmal ', 'callback_data':'08204'},
{'text':' Forish ', 'callback_data':'08235'}],
[{'text':' Do‘stlik ', 'callback_data':'08215'},
{'text':' Arnasoy ', 'callback_data':'08201'}],
[{'text':' Zomin ', 'callback_data':'08218'},
{'text':' Mirzacho‘l ', 'callback_data':'08223'}],
[{'text':' Zarbdor ', 'callback_data':'08220'},
{'text':' Sh.Rashidov ', 'callback_data':'08212'}],
[{'text':' G‘allaorol ', 'callback_data':'08209'},
{'text':' Jizzax ', 'callback_data':'08402'}],
[{'text':' Zafarobod ', 'callback_data':'08225'}],
[{'text':'Ortga',               'callback_data':'00000'}]]

inbord14000=[[{'text':' Uychi ', 'callback_data':'14229'},
{'text':' Uchqo‘rg‘on ', 'callback_data':'14234'}],
[{'text':' Namangan  (Markaz)', 'callback_data':'14404'},
{'text':' Namangan  (Do‘stlik)', 'callback_data':'14402'}],
[{'text':' Yangiqo‘rg‘on ', 'callback_data':'14242'},
{'text':' Namangan  (Istiqbol)', 'callback_data':'14405'}],
[{'text':' Chust ', 'callback_data':'14237'},
{'text':' Chortoq ', 'callback_data':'14236'}],
[{'text':' Kosonsoy ', 'callback_data':'14207'},
{'text':' To‘raqo‘rg‘on ', 'callback_data':'14224'}],
[{'text':' Norin ', 'callback_data':'14216'},
{'text':' Mingbuloq ', 'callback_data':'14204'}],
[{'text':' Namangan ', 'callback_data':'14212'},
{'text':' Pop ', 'callback_data':'14219'}],
[{'text':'Ortga',               'callback_data':'00000'}]]

inbord12000=[[{'text':' Zarafshon ', 'callback_data':'12408'},
{'text':' Karmana ', 'callback_data':'12234'}],
[{'text':' Qiziltepa ', 'callback_data':'12216'},
{'text':' Konimex ', 'callback_data':'12211'}],
[{'text':' Tomdi ', 'callback_data':'12244'},
{'text':' Xatirchi ', 'callback_data':'12251'}],
[{'text':' G‘azg‘on ', 'callback_data':'12412'},
{'text':' Nurota ', 'callback_data':'12238'}],
[{'text':' Navoiy ', 'callback_data':'12401'},
{'text':' Navbahor ', 'callback_data':'12230'}],
[{'text':' Uchquduq ', 'callback_data':'12248'}],
[{'text':'Ortga',               'callback_data':'00000'}]]

inbord10000=[[{'text':' Chiroqchi ', 'callback_data':'10242'},
{'text':' Qarshi ', 'callback_data':'10401'}],
[{'text':' Ko‘kdala ', 'callback_data':'10240'},
{'text':' Yakkabog‘ ', 'callback_data':'10250'}],
[{'text':' Shahrisabz ', 'callback_data':'10246'},
{'text':' Shahrisabz ', 'callback_data':'10245'}],
[{'text':' Kasbi ', 'callback_data':'10237'},
{'text':' Nishon ', 'callback_data':'10235'}],
[{'text':' Muborak ', 'callback_data':'10234'},
{'text':' Mirishkor ', 'callback_data':'10233'}],
[{'text':' Kitob ', 'callback_data':'10232'},
{'text':' Baxoriston ', 'callback_data':'10231'}],
[{'text':' Koson ', 'callback_data':'10229'},
{'text':' Qarshi ', 'callback_data':'10224'}],
[{'text':' Qamashi ', 'callback_data':'10220'},
{'text':' Dehqonobod ', 'callback_data':'10212'}],
[{'text':' G‘uzor ', 'callback_data':'10207'}],
[{'text':'Ortga',               'callback_data':'00000'}]]

inbord18000=[[{'text':' Pastdarg‘om  (Go‘zalkent)', 'callback_data':'18228'},
{'text':' Narpay ', 'callback_data':'18218'}],
[{'text':' Samarqand  (Bog‘ishamol)', 'callback_data':'18408'},
{'text':' Nurobod ', 'callback_data':'18235'}],
[{'text':' Paxtachi ', 'callback_data':'18230'},
{'text':' Qoradaryo ', 'callback_data':'18214'}],
[{'text':' Kattaqo‘rg‘on ', 'callback_data':'18215'},
{'text':' Samarqand  (Temiryo‘l)', 'callback_data':'18405'}],
[{'text':' Samarqand  (Siyob)', 'callback_data':'18407'},
{'text':' Tayloq ', 'callback_data':'18238'}],
[{'text':' Urgut ', 'callback_data':'18236'},
{'text':' Payariq  (Chelak)', 'callback_data':'18226'}],
[{'text':' Dehqonobod ', 'callback_data':'18239'},
{'text':' Jomboy ', 'callback_data':'18209'}],
[{'text':' Samarqand  (Do‘stlik)', 'callback_data':'18233'},
{'text':' Oqdaryo ', 'callback_data':'18203'}],
[{'text':' Samarqand  (Zarafshon)', 'callback_data':'18234'},
{'text':' Ishtixon ', 'callback_data':'18212'}],
[{'text':' Qo‘shrabod ', 'callback_data':'18216'},
{'text':' Bulung‘ur ', 'callback_data':'18206'}],
[{'text':' Pastdarg‘om ', 'callback_data':'18227'},
{'text':' Payariq ', 'callback_data':'18224'}],
[{'text':'Ortga',               'callback_data':'00000'}]]

inbord24000=[[{'text':' Oqoltin ', 'callback_data':'24206'},
{'text':' Boyovut ', 'callback_data':'24212'}],
[{'text':' Sayxunobod ', 'callback_data':'24216'},
{'text':' Guliston ', 'callback_data':'24220'}],
[{'text':' Sardoba ', 'callback_data':'24226'},
{'text':' Mirzaobod ', 'callback_data':'24228'}],
[{'text':' Sirdaryo ', 'callback_data':'24231'},
{'text':' Xovos ', 'callback_data':'24235'}],
[{'text':' Guliston ', 'callback_data':'24401'},
{'text':' Shirin ', 'callback_data':'24410'}],
[{'text':' Yangiyer ', 'callback_data':'24413'}],
[{'text':'Ortga',               'callback_data':'00000'}]]

inbord22000=[[{'text':' Angor ', 'callback_data':'22202'},
{'text':' Boysun ', 'callback_data':'22204'}],
[{'text':' Bandixon ', 'callback_data':'22206'},
{'text':' Muzrabod ', 'callback_data':'22207'}],
[{'text':' Denov ', 'callback_data':'22210'},
{'text':' Denov ', 'callback_data':'22211'}],
[{'text':' Jarqo‘rg‘on ', 'callback_data':'22212'},
{'text':' Qiziriq ', 'callback_data':'22215'}],
[{'text':' Sariosiyo ', 'callback_data':'22217'},
{'text':' Termez ', 'callback_data':'22220'}],
[{'text':' Sherobod ', 'callback_data':'22223'},
{'text':' Sho‘rchi ', 'callback_data':'22226'}],
[{'text':' Termez ', 'callback_data':'22401'},
{'text':' Oltinsoy ', 'callback_data':'22201'}],
[{'text':' Qumqo‘rg‘on ', 'callback_data':'22214'},
{'text':' Uzun ', 'callback_data':'22221'}],
[{'text':'Ortga',               'callback_data':'00000'}]]

inbord27000=[[{'text':' Qibray ', 'callback_data':'27248'},
{'text':' Bo‘ka ', 'callback_data':'27228'}],
[{'text':' Yuqorichirchiq ', 'callback_data':'27239'},
{'text':' Oxangaron ', 'callback_data':'27415'}],
[{'text':' Parkent ', 'callback_data':'27249'},
{'text':' Bo‘stonliq ', 'callback_data':'27224'}],
[{'text':' Angren ', 'callback_data':'27407'},
{'text':' Chirchiq ', 'callback_data':'27419'}],
[{'text':' Zangiota ', 'callback_data':'27238'},
{'text':' Zafar ', 'callback_data':'27220'}],
[{'text':' Quyichirchiq ', 'callback_data':'27233'},
{'text':' Nurafshon ', 'callback_data':'27401'}],
[{'text':' Piskent ', 'callback_data':'27250'},
{'text':' Yangiyo‘l ', 'callback_data':'27424'}],
[{'text':' Yangiyo‘l ', 'callback_data':'27259'},
{'text':' Toshkent ', 'callback_data':'27237'}],
[{'text':' O‘rtachirchiq ', 'callback_data':'27253'},
{'text':' Chinoz ', 'callback_data':'27256'}],
[{'text':' Oqqo‘rg‘on ', 'callback_data':'27206'},
{'text':' Olmaliq ', 'callback_data':'27404'}],
[{'text':' Oxangaron ', 'callback_data':'27212'},
{'text':' Bekobod ', 'callback_data':'27413'}],
[{'text':'Ortga',               'callback_data':'00000'}]]

inbord26000=[[{'text':' Olmazor ', 'callback_data':'26280'},
{'text':' Mirobod ', 'callback_data':'26273'}],
[{'text':' Yashnobod ', 'callback_data':'26290'},
{'text':' Yakkasaroy ', 'callback_data':'26287'}],
[{'text':' Bektemir ', 'callback_data':'26264'},
{'text':' Shayxontohur ', 'callback_data':'26277'}],
[{'text':' Yunusobod ', 'callback_data':'26266'},
{'text':' Sergeli ', 'callback_data':'26283'}],
[{'text':' Mirzo Ulug‘bek ', 'callback_data':'26269'},
{'text':' Chilonzor ', 'callback_data':'26294'}],
[{'text':' Uchtepa ', 'callback_data':'26262'},
{'text':' Yangihayot ', 'callback_data':'26292'}],
[{'text':'Ortga',               'callback_data':'00000'}]]

inbord33000=[[{'text':' Xiva ', 'callback_data':'33226'},
{'text':' Xiva ', 'callback_data':'33406'}],
[{'text':' Ugranch ', 'callback_data':'33217'},
{'text':' Urganch ', 'callback_data':'33401'}],
[{'text':' Gurlan ', 'callback_data':'33208'},
{'text':' Qo‘shko‘pir ', 'callback_data':'33212'}],
[{'text':"Tuproqqal'a", 'callback_data':'33402'},
{'text':' Xazorasp ', 'callback_data':'33220'}],
[{'text':' Xonqa ', 'callback_data':'33223'},
{'text':' Shovot ', 'callback_data':'33230'}],
[{'text':' Yangiariq ', 'callback_data':'33233'},
{'text':' Yangibozor ', 'callback_data':'33236'}],
[{'text':' Bog‘ot ', 'callback_data':'33204'}],
[{'text':'Ortga',               'callback_data':'00000'}]]








#ikkinchi turdagi keyboard
def inline_keyboard(inbord):
    reply_markup={'inline_keyboard':inbord}
    return json.dumps(reply_markup)

#xabar yuboradi
def sendMessage(chatId,text,reply_markup=None):
    messageUrl=base_url+f"sendMessage?chat_id={chatId}&text={text}"
    if reply_markup:
        messageUrl = messageUrl +  "&reply_markup={}".format(reply_markup)
    requests.get(messageUrl)




#Kelgan smsni obrobotka
while True:
    response = requests.get(base_url + f"getUpdates?offset={offset}")
    if response.ok:
        data = response.json()
        if data["ok"]:
            if data["result"]:
                for update in data["result"]:
                    #print (update)
                    if 'message' in update:
                        chatId = update['message']["chat"]["id"]
                        if "/start" in update['message']["text"]:
                            print(update)
                            sendMessage(chatId,"Bot ga hush kelibsiz!! \n Ushbu bot yordamida siz lokatsiya haqida ma`lumot olishingiz mumkin \n Buning uchun siz o`zingiga kerak bo`lgan hududni tanlang")
                            sendMessage(chatId,"Qaysi Viloyatni tanlaysiz?",inline_keyboard(inbord1))
                            # print (update['message']["text"])
                        elif update != 'dsvdsvsdbdsb':
                            sendMessage(chatId,"xatolik")                            
                    elif 'callback_query' in update:
                        print('knopka')
                        print(update)
                        chatId =update['callback_query']['message']["chat"]["id"]
                        callbackdata = update['callback_query']['data']
                        if '03000' in update['callback_query']['data']:
                            sendMessage(chatId,"O`zingizga kerakli bo`lgan tumanni tanlang!",inline_keyboard(inbord03000))   
                        if '06000' in update['callback_query']['data']:
                            sendMessage(chatId,"O`zingizga kerakli bo`lgan tumanni tanlang!",inline_keyboard(inbord06000)) 
                        if '30000' in update['callback_query']['data']:
                            sendMessage(chatId,"O`zingizga kerakli bo`lgan tumanni tanlang!",inline_keyboard(inbord30000)) 
                        if '08000' in update['callback_query']['data']:
                            sendMessage(chatId,"O`zingizga kerakli bo`lgan tumanni tanlang!",inline_keyboard(inbord08000))    
                        if '14000' in update['callback_query']['data']:
                            sendMessage(chatId,"O`zingizga kerakli bo`lgan tumanni tanlang!",inline_keyboard(inbord14000)) 
                        if '12000' in update['callback_query']['data']:
                            sendMessage(chatId,"O`zingizga kerakli bo`lgan tumanni tanlang!",inline_keyboard(inbord12000)) 
                        if '10000' in update['callback_query']['data']:
                            sendMessage(chatId,"O`zingizga kerakli bo`lgan tumanni tanlang!",inline_keyboard(inbord10000)) 
                        if '35000' in update['callback_query']['data']:
                            sendMessage(chatId,"O`zingizga kerakli bo`lgan tumanni tanlang!",inline_keyboard(inbord35000)) 
                        if '18000' in update['callback_query']['data']:
                            sendMessage(chatId,"O`zingizga kerakli bo`lgan tumanni tanlang!",inline_keyboard(inbord18000)) 
                        if '24000' in update['callback_query']['data']:
                            sendMessage(chatId,"O`zingizga kerakli bo`lgan tumanni tanlang!",inline_keyboard(inbord24000)) 
                        if '22000' in update['callback_query']['data']:
                            sendMessage(chatId,"O`zingizga kerakli bo`lgan tumanni tanlang!",inline_keyboard(inbord22000)) 
                        if '27000' in update['callback_query']['data']:
                            sendMessage(chatId,"O`zingizga kerakli bo`lgan tumanni tanlang!",inline_keyboard(inbord27000)) 
                        if '26000' in update['callback_query']['data']:
                            sendMessage(chatId,"O`zingizga kerakli bo`lgan tumanni tanlang!",inline_keyboard(inbord26000)) 
                        if '33000' in update['callback_query']['data']:
                            sendMessage(chatId,"O`zingizga kerakli bo`lgan tumanni tanlang!",inline_keyboard(inbord33000)) 
                        if '00000' in update['callback_query']['data']:
                            sendMessage(chatId,"O`zingizga kerakli bo`lgan tumanni tanlang!",inline_keyboard(inbord1)) 
                        elif "METER" in update['callback_query']['data']:
                        
                            sendMessage(chatId,"Xozircha Xisoblagichlar haqida ma`lumot yubora olmaymiz")          
                    elif 'callback_query' in update:
                        #print('knopka') 
                        chatId =update['callback_query']['message']["chat"]["id"]
                        callbackdata = update['callback_query']['data']
                        a = region(str(callbackdata))
                        sending_text='Katta Xolamn rayonlari \n'
                        for q in a:
                            sending_text=sending_text+q[0]+' - '+q[1]+'\n'
                        sendMessage(chatId,sending_text)
                        sendMessage(chatId,"Qaysi hudud",inline_keyboard(inbord1))
                    offset = update["update_id"] + 1
        else:
            print("Error in API response:", data["description"])
    else:
        print("Failed to make the API request.")
    time.sleep(0.1) 
# #keladigan oddiy sms    
        #       if "text" in update['message']:
        # {'update_id': 412296779, 
        #  'message': {'message_id': 1789, 'from': {'id': 171319245, 'is_bot': False, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'language_code': 'ru'},
        #               'chat': {'id': 171319245, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'type': 'private'},
        #                 'date': 1695030771, 
        #                 'text': '/start', 
        #                 'entities': [{'offset': 0, 'length': 6, 'type': 'bot_command'}]}}
    

# #Inline knopkadan kegan sms
    #             if "text" in update['callback_query']['message']:
    # {'update_id': 412296771, 
    #  'callback_query': {'id': '735810555401851063',
    #                      'from': {'id': 171319245, 'is_bot': False, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'language_code': 'ru'}, 
    #                      'message': {'message_id': 1780, 'from': {'id': 6129894724, 'is_bot': True, 'first_name': 'Requests Test Bot', 'username': 'reqtest_bot'}, 
    #                                  'chat': {'id': 171319245, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'type': 'private'}, 
    #                                  'date': 1695022887, 
    #                                  'text': 'Ushbu BOT sizga Konsentratorlar haqida ma`lumot beradi! \n Bunin uchun siz o`z hududingizni tanlang', 
    #                                  'reply_markup': {'inline_keyboard': [[{'text': '1', 'callback_data': 'bir'}, 
    #                                                                        {'text': '2', 'callback_data': 'ikki'},
    #                                                                          {'text': '3', 'callback_data': 'uch'}],
    #                                                                            [{'text': '4', 'callback_data': 'tort'},
    #                                                                              {'text': '5', 'callback_data': 'besh'},
    #                                                                                {'text': '6', 'callback_data': 'olti'}]]}}, 
    #                                                                                'chat_instance': '5323233157514262773',
    #                                                                                  'data': 'olti'}}


    


# ['Zafar ShETK',                      #1 ESP
#  '27220' ,                           #2 ESP Code
#    'NS DVZ-2 35/10 kV',              #Substation
#    'ТОШЛОК',                         #Feeder
#    '666',                            #TR
#    'DCU',                            #dev_type
#    '119201029745',                   #dev_no
#    'Offline',                        #Status
#      '19/05/2022 19:04:59',          #on_off_time
#        'UZMOBILE',                   #com_operatot
#          '40.335285',                #latititude
#          '69.24172667',              #Longtitude
#            '92.63.204.30',           #dev_ip
#              '2697',                 #dev_port
#                'hes-fep-1-group1-0.hes-hs.prod.svc.cluster.local',  #server_ip 
#                '899989900260899054',   #sim_no SSID
#                  '',                   #manager_name
#                  '',                   #manager_phone
#                    '',                 #phone_no
#                      '']               #account_id

#{'update_id': 412296856
# , 'message': {'message_id': 1948,
# 'from': {'id': 171319245, 'is_bot': False, 
# 'first_name': 'Fayzullo', 
# 'last_name': 'Kamol', 'username': 'kamolfayzullo',
# 'language_code': 'ru'}, 'chat': {'id': 171319245, 'first_name': 'Fayzullo', 'last_name': 'Kamol', 'username': 'kamolfayzullo', 'type': 'private'}, 
# 'date': 1696524005, 'text': '123'}}



input ()