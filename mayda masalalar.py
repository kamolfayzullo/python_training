# import math as fayzullo

# yosh = input ("tug`ilgan yilingizni kiriting ") 
# print ('Sizning yoshingiz :'+str(2023-int(yosh)))



# son_1 = input ("1-sonni kiriting ")
# son_2 = input ("2-sonni kiriting ")
# print ("natija " + str(int(son_1) + int(son_2)))

# ism = input ("Ismingizni kiriting :") 
# familiya = input ("Familiyasini kiriting :") 
# print ( ism.capitalize() +" " + familiya.capitalize())


# TomoniUzinlig = input ("Tomoni uzligini kiriting :  ")
# P = 4 * float(TomoniUzinlig)
# S = float(TomoniUzinlig) * float(TomoniUzinlig)
# print  ("Kvadratning perimetri " + str(P) + " ga teng")
# print ("Kvadratning yuzas " + str(S) + " ga teng ")

# #--------------------##

# Balandlig = input ("To`rtburchak balandligini kiriting :  ")
# Uzunlik = input ("To`rtburchak uzunligini kiriting : ")

# P = 2 * (float(Balandlig) + float(Uzunlik))
# S = float(Balandlig) * float(Uzunlik)
# print  ("Kvadratning perimetri " + str(P) + " ga teng")
# print ("Kvadratning yuzasi " + str(S) + " ga teng ")

# D = input ("Aylana diametrini kiriting :  ")
# L = 3.14 * int(D)
# print ("Kvadratning yuzas " + str(L) + " ga teng ")

# #kdhsbvksdbjkv##


# kubuzunligi = input ("Kub qirrasining uzunligini kiriting :" )
# V = float(kubuzunligi) **3
# S = 6 * (float(kubuzunligi)**2) 
# print("Kubning hajmi" + str(V) + "va uning sirtining yuzasi" + str(S) + "ga teng.")



# uzunligi = input ("Kub qirrasining uzunligini kiriting :" )
# balandligi = input ("Kub qirrasining balandligini kiriting :" )
# kengligi = input ("Kub qirrasining kengligini kiriting :" )
# V = float(uzunligi) * float(balandligi) * float(kengligi)
# S = (4 * (float(uzunligi) + float(balandligi))) + ( 2 * float(balandligi) + float(kengligi) ) 
# print ("Kubning hajmi" + str(V) + "va uning sirtining yuzasi" + str(S) + "ga teng.")


# #Berilgan R radiusga ko’ra doira aylanasining uzunligi L va uning yuzi S hisoblansin.

# R = input ("Radiusni kiriting " )
# Pi = 3.14
# L = (2 * float(R)) * Pi
# S = float(R) * Pi

# print ("Aylananing uzunligi" + str(round(L)) + "va uning yuzi" +  str(round(S)) + "ga teng")


# Ikkita a va b sonlar berilgan. Ularning o’rta arifmetigi hisoblansin.

# son1 = input("Birinchi sooni kiriting " )
# son2 = input("Ikkinchi sooni kiriting " )
# OAqiymat = (float(son1) + float(son2)) / 2
# print ("O`rta arifmetik qiymat " + str(round(float(OAqiymat))) + "ga teng")

# 9Ikkita manfiy bo`lmagan a va b sonlar berilgan. Ularning o’rta geometrigi hisoblansin.

# son1 = input("Birinchi sooni kiriting " )
# son2 = input("Ikkinchi sooni kiriting " )
# if float(son1) > 0 and float(son2) > 0 :  
#     OAqiymat =  (float(son1) * float(son2)) 
#     yangi_son=fayzullo.sqrt(OAqiymat)
#     print ("Ildiz qiymat " + str(round(yangi_son)) + "ga teng")
# else : 
#     print ("Musbat son kiriting!")


# 10 Ikkita nolga teng bo`lmagan a va b sonlari berilgan.
#  Ularning yig`indisi, ayirmasi, ko`paytmasi va bo`linmasi hisoblansin.

# son1 = input("Birinchi sonni kiritng ")
# son2 = input("Ikkinchi sonni kiritng ")
# if float(son1) != 0 and float(son2) != 0: 
#      yigindi = (float(son1)) + (float(son2))
#      ayirma = (float(son1)) - (float(son2))
#      bolinma = (float(son1)) / (float(son2))
#      kopaytma = (float(son1)) * (float(son2))
#      print ("Ularning yig`indisi " + str(yigindi) +" ga, ayirmasi," + str(ayirma) + " ga, ko`paytmasi " 
#         + str(kopaytma) + "ga  va bo`linmasi" + str(bolinma) + "ga teng")
# else :
#      print ("0 ga teng bo`lmasin") 

#     11 Ikkita nolga teng bo`lmagan sonlar berilgan.
#      Ularning yig`indisi, ayirmasi, ko`paytmasi va ularning bo`linmasining moduli hisoblansin.

# son1 = input("Birinchi sonni kiritng ")
# son2 = input("Ikkinchi sonni kiritng ")

# yigindi = (float(son1)) + (float(son2))
# ayirma = (float(son1)) - (float(son2))
# kopaytma = (float(son1)) * (float(son2))
# bolinma = (float(son1)) / (float(son2))
# if bolinma > 0:
#     bolinma=bolinma * (-1)
#     print ("Ularning yig`indisi " + str(yigindi) +" ga, ayirmasi," + str(ayirma) + " ga, ko`paytmasi " 
#    + str(kopaytma) + "ga  va bo`linmasi" + str(bolinma) + " ga tengIF")


# else:  print ("Ularning yig`indisi " + str(yigindi) +" ga, ayirmasi," + str(ayirma) + " ga, ko`paytmasi " 
#     + str(kopaytma) + " ga  va bo`linmasi " + str(bolinma) + " ga tengELSE")




# To`g`ri burchakli uchburchak  a va b katetlari berilgan.
# Uning gipotenuzasi C hamda perimetri P hisoblansin.  

# son1 = input("Birinchi sonni kiritng ")
# son2 = input("Ikkinchi sonni kiritng ")
# katet1 = float(son1)
# katet2 = float(son2)
# tomon3 = fayzullo.sqrt (((katet1)**2) + ((katet2)**2))

# p = katet1 + katet2 + tomon3

# print  ("Uning gipotenuzasi" + str(tomon3) + "ga hamda perimetri " + str(p) + "ga teng")


# Radiuslari R1 va R2 bo`lgan (R1>R2) hamda markazi umumiy
# 2 ta doira berilgan. Birinchi doiraning yuzi S1,
# ikkinchi doiraning yuzi S2 hamda tashqi doiraning
# ichida va ichki doiraning tashqarisida joylashgan yuza S3 (S3=S1-S2) hisoblansin. 


# Radius1 = input("R1 ni kiriting ")
# Radius2 = input("R2 ni kiriting ")
# Pi = 3.14
# S1 = Pi * (float(Radius1) **2)
# S2 = Pi * (float(Radius2) **2)
# S3 = S1 - S2

# print ("Birinchi doiraning yuzi " + str(round(S1)) + "ga, ikkinchi doiraning yuzi " + str(round(S2)) + 
#       "ga, hamda tashqi doiraning ichida va ichki doiraning tashqarisida joylashgan yuza " + str(round(S3)) + "ga teng")



# 14 Doiraning aylana uzunligi L berilgan. Uning radiusi R va yuzi S hisoblansin.

# aylanaUzinligi = input("Aylana Uzinligini kiriting: ")
# pi = 3.14
# R = (float(aylanaUzinligi) / pi) / 2
# S = (R**2) * pi
# print ("Uning radiusi " + str(R) + "ga teng va va yuzi " + str(S) +"ga teng")

# 15 Doiraning yuzi S berilgan. Uning diametri D va aylana uzunligi L  hisoblansin. 


# S = input("Doira yuzini kiriting : ")
# pi = 3.14
# D = fayzullo.sqrt(float(S))
# L = D * pi
# print ("Javob" + str(D) + "shu")


# print ("Uning diametri " + str(D) + "   ga teng va va uzunligi " + str(L) +" ga teng")

# 16 Sonlar o’qida berilgan x1 va x2 nuqtalar orasidagi masofa (x2-x1) hisoblansin.

# son1 = input ("x1 ni kiriting :")
# son2 = input ("x2 ni kiriting :")
# x1 = float(son1)
# x2 = float(son2)
# masofa = x2 - x1
# print ("sonlar orasidagi masofa " + str(round(masofa)) + " ga teng")

# 17 Sonlar o’qida A, B, C nuqtalar berilgan. AC va BC 
# kesmalar uzunligi va ularning yig`indisi hisoblansin.
       

# son1 = input ("A nuqtadagi sonni kiriting:")
# son2 = input ("B nuqtadagi sonni kiriting:")
# son3 = input ("C nuqtadagi sonni kiriting:")

# A = float(son1)
# B = float(son2)
# C = float(son3)

# AC = C - A
# BC = C - B

# ACBC = AC + BC
# print ("AC = " + str(round(AC)) + " ga BC = " + str(round(BC)) + " ga teng va ularning yig`indisi "
#         + str(round(ACBC)) + " ga teng")

# 18 Sonlar o’qida A, B, C nuqtalar berilgan.(Bu yerda C nuqta A va B nuqtalar orasida yotadi deb hisoblanadi) 
# AC va BC kesmalar uzunliklari hamda ularning ko`paytmasi hisoblansin. 


# son1 = input ("A nuqtadagi sonni kiriting:")
# son2 = input ("B nuqtadagi sonni kiriting:")
# son3 = input ("C nuqtadagi sonni kiriting:")

# A = float(son1)
# B = float(son2)
# C = float(son3)

# AC = C - A
# BC = B - C

# ACBC = AC * BC
# print ("AC = " + str(round(AC)) + " ga BC = " + str(round(BC)) + " ga teng va ularning ko`paytmasi "
#         + str(round(ACBC)) + " ga teng")



# 19 To`g`ri burchakli to`rtburchakning qarama-qarshi uchlari
#  (x1,y1) va (x2,y2) lar berilgan. To`g`ri to`rtburchakning
#  tomonlari koordinata o`qlariga parallel deb hisoblanib, uning perimetri va yuzasi hisoblansin.  

# x1 = input ("X1 sonni kiriting :")
# y1 = input ("Y1 sonni kiriting :")
# x2 = input ("X2 sonni kiriting :")
# y2 = input ("Y2 sonni kiriting :")

# uzunligi = float(x2) - float(x1)
# balandligi = float(y2) - float(y1)
# P = 2 * (uzunligi + balandligi)
# S = uzunligi * balandligi

# print ("P = " + str(P) + "S = " + str(S))



# 20 Tekislikda koordinatalari bilan berilgan ikki nuqta orasidagi masofa hisoblab topilsin.


# x1 = input ("X1 sonni kiriting :")
# y1 = input ("Y1 sonni kiriting :")
# x2 = input ("X2 sonni kiriting :")
# y2 = input ("Y2 sonni kiriting :")

# xx = float(x2) - float(x1)
# yy = float(y2) - float(y1)

# cc = xx **2 + yy **2

# javob = fayzullo.sqrt(cc)

# print ("javob " + str(javob) + " : ")

# 21 Uchburchakning uchlarining koordinatalari berilgan. 
# Ular (x1,y1), (x2,y2), (x3,y3) hisoblanadi. Ikki nuqta orasidagi 
# masofani topish formulasi va Geron formulasidan foydalanib uning perimetri hamda yuzasi hisoblansin. 

# x1 = int(input ("X1 sonni kiriting :"))
# y1 = int(input ("Y1 sonni kiriting :"))
# x2 = int(input ("X2 sonni kiriting :"))
# y2 = int(input ("Y2 sonni kiriting :"))
# x3 = int(input ("X3 sonni kiriting :"))
# y3 = int(input ("Y3 sonni kiriting :"))

# if    x2 > x1 and x2 > x3:
#     asos = x2
#     #print ("if")


# else:   
#     asos = x3
#     #print ("else")

  
# if    y2 > y1 and y2 > y3:
#     baland = y2
#     #print ("if")


# else:   
#     baland = y3
#     #print ("else")


# uzunlik = asos - x1
# buy = baland - y1

# katet = fayzullo.sqrt( uzunlik**2 + buy**2)

# P = uzunlik + buy + katet
# S = (uzunlik * buy) / 2

# print ("P = " + str(P) +
#        "S = " + str(S) + " ")


# 22 A va B o`zgaruvchilardagi qiymatlarni almashtiradigan programma tuzilsin.

# A = input ("A raqamni kiriting")
# B = input ("B raqamni kiriting")

# C = A
# A = B
# B = C

# print ("A = " + str(A)
#        + "B = " +str(B))

# 23 A, B va C o`zgaruvchilarining qiymatlari quyidagicha almashtirilsin:
#  A→B, B→C, C→A va chiqarilsin. 


# A = input ("A raqamni kiriting")2   
# B = input ("B raqamni kiriting")4
# C = input ("C raqamni kiriting")6

# D = A
# A = B
# B = C
# C = D

# print ("A = " + str(A)
#        + "B = " +str(B) + "C = " +str(C) )


# 25 x ning berilgan qiymatida y=3x6-6x3-7 qiymati hisoblansin.

# x = float(input("x raqamni kiriting : "))
# raqam = 0 * x
# if raqam != 0:
#     print ("raqam kiriting bowqa narsa emas")

# y = ((3 * (x **6)) - (6 * (x **3))) - 7

# print ("Javob " + str(y))

#     raqam kiritiw +++++++++++++++++++++++++++++++++++++++++++  
#     +++++++++++++++++++++++++++++++
#    ++++++++++++++++++++++++++++++

# x = (input ("Raqam kiriting "))

# raqam = float(x) * 0
# if raqam != 0:  
#     print ("raqam kiritilmadi")

# else:
#     print ("raqam kiritildi")



# 26 x ning berilgan qiymatida y=4(x-3)6-7(x-3)3+2 qiymati hisoblansin.

# x = float( input("x sonni kiriting"))

# y = (4*((x - 3)**6))-(7*((x - 3)**3))+2

# print("y = " + str(y))


# A soni berilgan. A2, A4, A5 ketma-ketlik uchun yordamchi 
# o`zgaruvchilardan foydalanib 3 ta ko`paytirish amalini bajarib, 
# A5 hisoblansin   va barcha A ning ko`rsatilgan darajalari ekranga chiqarilsin.  


# a = float(input(" A raqamni kiriting "))

# A2 = a**2
# A4 = a**4
# A5 = a**5

# print ("A ning 2 darajasi " + str(A2) + "ga teng" + 
#        "A ning 4 darajasi " + str(A4) + "ga teng" +
#        "A ning 5 darajasi " + str(A5) + "ga teng")

 
# a = str(input(" Javobni kiriting "))
# match a: 
#     case "A": 
#         print("To`g`gri todin")
#     case other:
#         print("chichyordin")




# 29 α burchak (0<α<360°) gradusda berilgan. Unga mos radian qiymat topilsin.

# a = float(input("Gradusni kiriting :"))

# radi = 6.28 / 360
# radians = a * radi

# print ("radians " + str(radians) + " ga teng")


# 30 α burchak (0<α<2π) radianda berilgan. Uning gradusdagi qiymati topilsin.

# radians = float(input("Gradusni kiriting :"))

# radi = 360 / 6.28
# gradus = radians * radi 

# print ("gradus " + str(gradus) + " ga teng")







#      unnamed block
# a=5
# b=4
# print(a+b)
# procedure
# def test_procedure(a,b):
#     print(a+b)


# test_procedure(4,5)
# test_procedure(10,8)

# def test_function(a,b):
#     y=a+b
#     return y
# x=test_function(4,5)
# print(x+8)


#Passport seriya topiw-------------------------------------
# def passseriya(a,b):
#     fio ="Ismiz " + a + " Familyangiz " + b
#     return fio

# name = input ("Ismingizni kiriting :").capitalize()
# familiya = input ("Familiyangizni kiriting :").capitalize()
# yow = input ("Yoshingizni kiriting :")

# try:
#     yow = float(yow)
#     yili = 2023 - yow
#     q = name[0]
#     w = familiya[0]
#     e = yili
#     ism = passseriya (name,familiya)   
#     print (str(ism) + " tug`ilgan yilingiz :" + str(yili) + " yil" + '\n' +
#         "Sizga mos passport seriya" + str(q) + str(w) + str(round(e)))
# except Exception as error:
#     print ("yowingizga raqam kiritmadingiz")
#     print(error)


#-------------------------------------------------------------------------------------------
# def xuysan (s,b) :
#     yow = s + b
#     return yow

# yow = a + b
# yow 

# ism = input("ism kiriting :")

# bow = ism[0,3]

# print("bow harf " + str(ism)
      


      
# yow = input("Yoshingiz kiriting :")

# try:

#     yow = float(yow)
#     yili = 2023 - yow
#     q = name[0]
#     w = familiya[0]
#     e = yili
#     ism = passseriya (name,familiya)   
#     print (str(ism) + " tug`ilgan yilingiz :" + str(yili) + " yil" + '\n' +
#         "Sizga mos passport seriya" + str(q) + str(w) + str(round(e)))
# except Exception as error:
#     print ("yowingizga raqam kiritmadingiz")





# a = str(input(" Javobni kiriting "))
# match a: 
#     case "A": 
#         print("To`g`gri todin")
#     case other:
#         print("chichyordin")

# TOPWIRIQ________________________________________________________

# x = input ("Xisoblagich raqamini kiriting : ")
# uzunlik = int(len(x))

# if uzunlik in [12,9,10]:
          
#     0

# else:
#     print  ("notugri")

# boshraqam = int(x[0:3])

# if boshraqam in [111,123,124,"EX-",1212,1211,]:

#     pass
# else:
#     print  ("notugri2")



# print (str(boshraqam))

#////////////////////////////////////////////////////

# x = input ("raqam kirit :")

# bowi = x[0:3]

# print(str(bowi))





# mevalar = ["anor", "uzum", "nok", "gilos", "hurmo"]
# for meva in mevalar:
#     print(meva)
#     if meva == "nok":
#         break
#___________________________________________________________________________#
#Unli va Undosh harflarni sanash
# ism = input ("Ism kiriting: ")
# ism2 = ism.lower()
# unlilar = 0
# for i in ism2:
#     #print (i)
#     if i in ["a","e","i","o","u"]:
#         #print ("unli harflar bor")
#         unlilar=unlilar + 1

# #print (unlilar)

# undoshlar = len(ism) - unlilar
# print ("Unli harflar soni: " + str(unlilar) + " ta" + '\n' + "Undosh harflar soni: " + str(undoshlar) + " ta")

#___________________________________________________________________________#

#qoldiq bn masofa o`lchash`
# soni = 0
# for a in range (999):
#   if a%9 == 0:
#     soni = soni + 1

# print (soni)


#______________________________________________________________________________#

#Unlini urniga berilgan raqam kiritilinsin
# ism = input ("Ism kiriting: ")
# ism2 = ism.lower()
# raqam = input ("Raqam kiriting: ")
# natija = ""
# for i in ism2:
#     if i in ['a','e','o','i',"u"]:
#         natija=natija+str(raqam)
#     else:
#         natija=natija+i

# print (natija)

#______________________________________________________________________________#
# 0-dan 333 gacha bolgan son ichida 3 raqamidan nechta?


# son = 333
# soni = 0
# for a in range(son+1):
#     b = (str(a))
#     for h in b:
#      if h in ("2"):
#       soni= soni + 1
# print (soni)

#_________________________________________________________________________________#

 
# mevalar = ["a", "b", "c"]
# dictionary data type
# mening_malumotim = {
#     "ismi": "Fayzullo",
#     "familyasi": "Kamol",
#     "yoshi": 26,
#     "yoqtrgan_mevalari": ["olma", "banan", "tarvuz"],
# }

# print(dir(mening_malumotim))

# # .keys()
# print(mening_malumotim.keys())
# # .values()
# print(mening_malumotim.values())

# klyuich yozsez valueslar chqadi
# print(mening_malumotim["yoqtrgan_mevalari"])
# print(mening_malumotim.get("yoqtrgan_mevalari"))


# print(len(mening_malumotim))

# mening_malumotim.pop("yoqtrgan_mevalari")
# print(mening_malumotim)

# print(mening_malumotim.items())


# new_dictionary = dict(name="Fayzullo", yoshi=26, familyasi="Kamol")
# print(new_dictionary)

#__________________________________________________________________________________________#

# Dictionary
# nma ma`lumot surasa javobi chiqsin
# mening_malumotim = {
#     "ismi": "Fayzullo",
#     "familyasi": "Kamol",
#     "yoshi": 26,
#     "yoqtrgan_mevalari": ["olma", "banan", "tarvuz"],
# }

# mevalar = mening_malumotim.get("yoqtrgan_mevalari")

# savol = input("nma ma`lumot kerak? ").lower()



# if savol in ["ism"]:
#     print (mening_malumotim.get("ismi"))
# elif savol in ["familya","familyasi"]:
#     print (mening_malumotim["familyasi"])
# elif savol in ["yosh","yoshi"]: 
#     print (mening_malumotim["yoshi"])
# elif savol in ["meva","mevalar"]:
#     son = 1
#     for i in mevalar:     
#       print (str(son) + "." + (i))
#       son = son + 1


#________________________________________________________________________#















 
#print (str(i))




































