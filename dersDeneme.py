# x,y,z="portakal","muz","kiraz"
# print(x)
# print(y)
# print(z)

# a=b=c="hilal "
# print(a)
# print(b)
# print(c)

# #koleksiyon acma
# meyveler=["elma","armut","yürü"]
# hilal,alper,filiz=meyveler
# print(hilal)
# print(alper)
# print(filiz)

# #print kullanımı
# x="python"
# y="nesne yönelimli"
# z="bir dildir."
# print(x,y,z) # vırgulle ayırırsak ard ardına cıktıları bırlestırır
# print(x+y+z) # + da kullanabılırız

# x=5
# y=10
# print(x+y)

#farklı turdekı bırden cok degıskenın cıktısını almak ıcın + yerıne , kullan

# x=5
# y="hilal"
# print(y,x)
# print("//////////")

# x="bir dildir"
# def fonk():
#     print("python "+x)
    
# fonk()

# def fonk():
#     global x
#     x="hilal"
    
# fonk()
# print("hava"+x)


#Bir fonksiyon içindeki global değişkenin
# değerini değiştirmek için global anahtar kelimeyi
#kullanarak değişkene bakın:

# x="muhtesem"
# def fonk():
#     global x
#     x="harika"
    
# fonk()
# print("hava"+x)

#Float, 10'un gücünü belirtmek için "e" ile gösterilen bilimsel sayılar da olabilir.
#Complex (Karmaşık Sayılar)
#Karmaşık sayılar sanal kısım olarak "j" ile yazılır:
# x = 3+5j
# y = 5j
# z = -5j
# print(type(x))
# print(type(y))
# print(type(z))

# x = 1 # int
# y = 2.8 # float
# z = 1j # complex
# a=float(x)
# print(a)
# b=int(y)
# print(b)
# c=complex(x)
# print(c)
# print(type(a))
# print(type(b))
# print(type(c))
# #NOT: Karmaşık sayıları başka bir sayı türüne dönüştüremezsiniz.
# import random
# print(random.randrange(1,10))

# #Üç tırnak kullanarak bir değişkene çok satırlı bir dize atayabilirsiniz:

# a = """Bu bir test verisidir,
# Bu bir test verisidir,
# Bu bir test verisidir,
# Bu bir test verisidir."""
# print(a)

# #Ancak Python'un bir karakter veri türü yoktur, tek bir karakter yalnızca 1 uzunluğunda birdizedir 
# for x in "muz":
#  print(x)
 
# txt="hilal tabak ınsan"
# print("hilal" in txt)

# b = "Merhaba Bandırma!"
# print(b[2:])

# b = "Merhaba Bandırma!"
# print(b[-5:-2]) 

# a = "    Merhaba Trakya!    "
# print(a.strip())

# a = "Merhaba, Tekirdağ!"
# print(a.split(","))

# Yas = 28
# txt = "Benim adım İpek, yaşım: " , Yas
# print(txt)

# yas = 28
# txt = " Benim adım İpek, yaşım: {}"
# print(txt.format(yas))


# txt = "Biz toplumda \"Yazılım Mühendisi\" olarak biliniriz."
# print(txt)

# print(bool("Merhaba"))
# print(bool(15))

# x = "Merhaba"
# y = 15
# print(bool(x))
# print(bool(y))

# #Boş dizeler dışında herhangi bir dize True'dur.
# #0 dışında herhangi bir sayı True'dur.

# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))

# #Python ayrıca, bir nesnenin belirli bir veri türünde olup olmadığını belirlemek için
# #kullanılabilen isinstance() işlevi gibi bir boole değeri döndüren 
# #birçok yerleşik işleve sahiptir:
# x="hilal"
# print(isinstance(x,str))

# #Verileri depolamak için 4 yerlesık verı turu vardır
# #Listeler-Tuple-Set-Dictionary

# #LİSTELER
# #kÖSELİ PARANTEZ KULLANILIR
# #OGELERİ SIRALIDIR ,DEGISTIRILEBILIR VE YENILENEN DEGERLERE IZIN VERIR
# #OGELER İNDEKSLENİR 
# #SIRALARNIR DEDIGIMIZDE OGELERIN BELIRLI SIRALARA SAHIP OLDUGU VE SIRANIN DEGISTIRILEMEYECEGI ANLAMINA GELIR
# #BİR LİSTEYE YENI OGELER EKLERSEK YENI OGELER LISTENIN SONUNA EKLENIR YANI OGELERIN SIRASI DEGISMEZ


# #OGELERI DEGISTIREBILIR VE KALDIRABILIRIZ
# #AYNİ DEGERE SAHIP OGELERE SAHIP OLABILIRİZ

# listem = ["elma", "muz", "kiraz", "elma", "kiraz"]
# print(listem)


# #LİSTE YAPMAK ICIN CIFT PARANTEZ

# buListe=list(["elma","armut",80])
# print(buListe)

# #Tuple, sıralı ve değişmez bir koleksiyondur. Yinelenen üyelere izin verir.
# #Set, sırasız, değiştirilemez* ve indekslenmemiş bir koleksiyondur. Çift üye yok.
# #Sözlük, sıralı** ve değiştirilebilir bir koleksiyondur. Çift üye yok

# #*Set öğeleri değiştirilemez, ancak istediğiniz zaman öğeleri kaldırabilir ve/veya ekleyebilirsiniz.

# buListe =["elma", "muz", "kiraz", "portakal", "kivi", "kavun", "mango"]
# print(buListe [-4:-1])

# buListe = ["elma", "muz", "kiraz", "portakal", "kivi", "mango"]
# buListe[1:3] = ["frenk üzümü", "karpuz"]
# print(buListe)


# buListe = ["elma", "muz", "kiraz"]
# buListe.insert(2, "karpuz")
# print(buListe)

# buListe = ["elma", "muz", "kiraz"]
# tropikal = ["mango", "ananas", "papaya"]
# buListe.extend(tropikal)
# print(buListe)

# buListe = ["elma", "muz", "kiraz"]
# for i in range(len(buListe)):
#  print(buListe[i])

# buListe = ["elma", "muz", "kiraz"]
# [print(x) for x in buListe ]

# buListe = ["elma", "muz", "kiraz"]
# i = 0
# while i < len(buListe):
#     print(buListe[i])
#     i = i + 1


meyveler = ["elma", "muz", "kiraz", "kivi", "mango"]
yeniListe = []
for x in meyveler:
    if "a" in x:
        yeniListe.append(x)
print(yeniListe)
