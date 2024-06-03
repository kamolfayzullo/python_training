import requests 
response=requests.get('https://nbu.uz/uz/exchange-rates/json/')
if response.ok:
    print('Request muvofaqyatli boldi')
print(response.status_code) #muvofaqyatli bolish uchun 200 # print(response.json())
print(response)
oliwsotiw = input ("Valyuta olasizmi sotasizmi? ")
inputValyuta = input("Valyuta tanlang: ")
summa = float(input("Pul summasini kiriting! : "))
for i in response.json():
    if inputValyuta == ("S"):
        if i["title"]== 'AQSh dollari':
            Kursi = i["cb_price"]
            Oliw = i['nbu_buy_price']
            Sotiw =i['nbu_cell_price']
    elif inputValyuta == ("E"):
        if i["title"]== 'Yevro':
            Kursi = i["cb_price"]
            Oliw = i['nbu_buy_price']
            Sotiw =i['nbu_cell_price']
    elif inputValyuta == ("R"):
        if i["title"]== 'Rossiya rubli':
            Kursi = i["cb_price"]
            Oliw = i['nbu_buy_price']
            Sotiw =i['nbu_cell_price']
Kursi = float(Kursi)
Oliw = float(Oliw)
Sotiw = float(Sotiw)
if oliwsotiw == ("olaman"):
    natija = summa *  Sotiw
    print ("Qabul qilindi: " + str(summa) + " " + str(inputValyuta))
    print ("Siz " + str(round(natija,2)) + " miqdorda so`m beriwingiz kerak.")
elif oliwsotiw == ("sotaman"):
    natija = summa * Oliw
    valuta = inputValyuta
    print ("Qabul qilindi: " + str(summa) + " " + str(inputValyuta))
    print ("Sizga " + str(round(natija,2)) + " miqdorda so`m beriladi.")




