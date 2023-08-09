# import requests 
# import datetime as dt
# import countryCode
# # response=requests.get('https://nbu.uz/uz/exchange-rates/json/')

# # for i in response.json():

# #     if i["title"]== 'AQSh dollari':
# #         dollrKursi = i["cb_price"]




# # def kurs():
# #     urlbank = requests.get('https://nbu.uz/uz/exchange-rates/json/')
# #     kursmalumot = urlbank.json()
# #     for i in kursmalumot:
# #         if i["title"] == "AQSh dollari":
# #             kurssotiw = i['nbu_cell_price']
# #             kurssoliw = i['nbu_buy_price']
# #     return kurssoliw
        
# # print (kurs())





# # def kurs():
# #     urlbank = requests.get('https://nbu.uz/uz/exchange-rates/json/')
# #     kursmalumot = urlbank.json()
# #     for i in kursmalumot:
# #         if i["title"] == "AQSh dollari":
# #             kurssotiw = i['nbu_cell_price']
# #             kurssoliw = i['nbu_buy_price']
# #     return kurssoliw
        
# # print (kurs())


# #def handle_updates(updates):
#     # for update in updates["result"]:
#     #     # print(update)
#     #     coordinat = (update['message']['location'])
# longtude =69
# latude =41
# #print (longtude , latude)
# response=requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latude}&lon={longtude}&appid=a6ffc8b3cadf6c0445beba80ac186b62&lang=ru&units=metric/json/')
# print  (response.json())

# # malumot = format["sys"]["country"]
# # for davlat in countryCode:
# #     if malumot == davlat["code"]:
# #         davlatnomi = davlat["country"]
# #         print (davlatnomi)
a = [{"CommunicationPointNo.":"190125648",
"DeviceType":"DCU",
"ESPCode":22206,
"ESP":"Bandixon TETK",
"Biriktirilgan hodim":"Mansurov Jahongir",
"Hodim raqami:":"+998946655858",
"TP":"134",
"InstallationAddress":"Бандиханское ЭСП",
"DeviceNo.":"129205019086","Location":{"Longitude":904189,"Latitude":-23.67135888}}]

print (a)
  