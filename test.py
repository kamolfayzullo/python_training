import requests 
# response=requests.get('https://nbu.uz/uz/exchange-rates/json/')

# for i in response.json():

#     if i["title"]== 'AQSh dollari':
#         dollrKursi = i["cb_price"]




def kurs():
    urlbank = requests.get('https://nbu.uz/uz/exchange-rates/json/')
    kursmalumot = urlbank.json()
    for i in kursmalumot:
        if i["title"] == "AQSh dollari":
            kurssotiw = i['nbu_cell_price']
            kurssoliw = i['nbu_buy_price']
    return kurssoliw
        
print (kurs())






