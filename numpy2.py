#numpy verileri normal phyton verilerine gore cok daha az yer kaplar ve daha hızlı calısır
#pythondakı lıst kavramı numpydakı dızı (array) kavramına karsılık gelır

 #python list
# py_list=[1,2,3,4,5,6,7,8,9]

# #numpy array
# np_array=np.array([1,2,3,4,5,6,7,8,9])
# #tek bir parametre gonderırız ve bu bir listedir ve bu lısteyı np dızısıne cerırız

# #type
# print(type(py_list))
# print(type(np_array)) 
# #<class 'list'>
# #<class 'numpy.ndarray'>  cıktısı alırız

# py_multi=[[1,2,3],[4,5,6],[7,8,9]]
# np_multi=np_array.reshape(3,3) 
# #cok boyutlu dızı olusturabılırz (matris)

# print(py_multi)
# print(np_multi)

# #boyut bılgısıne bakarsak ndim kullanabılırz
# print(np_array.ndim)
# print(np_multi.ndim) #1 ve 2 cıktısı alırız 

# #shape 
# print(np_array.shape) #(9,)
# print(np_multi.shape) #(3,3)
###############################33
# result=np.array([1,3,5,7,9])
# print(result) elemanları kendımız belırledık

# result=np.arange(1,10) #  1-100 arası dızı olusturdu 100 dahıl degıl

# result=np.arange(10,100,3) # artıs mıktarı son parametrede belırtebılırz 

#sadece 0 lardan olusan bır dızı
# result=np.zeros(10)

#sadece 1 lerden olusan bır dızı ( her eleman floattır)
# result=np.ones(10)

# result=np.linspace(0,100,5) # 0-100 arasında 5 es parcaya bolunmus sayı dızısı [[100 dahil]]
# result=np.linspace(0,5,5) # 5 tane sayı olacak es aralıklarla 

#random
# result=np.random.randint(0,10) #10dahıl degıl
# result=np.random.randint(10) # baslangıcı 0 alır
# result=np.random.randint(0,10,3) # kac tane sayı ıstersek o sekılde bır dızı olusturu ve verır
# result=np.random.rand(5)#rasgele 5 sayı uretır 
# result=np.random.randn(5) # - degerlerıde alır
# np_array=np.arange(50) #0-50 arası dızı dondurur
# np_multi=np_array.reshape(5,10) # 5e 10luk matrıs olusturdu
# print(np_multi.sum(axis=1)) #satırları topladı
# print(np_multi.sum(axis=0)) #sutunları topladı
# rnd_numbers=np.random.randint(1,100,10)#1-100 arası 10 adet sayı dızısı verdı
# print(rnd_numbers)
# result1=rnd_numbers.max() # max verir
# result2=rnd_numbers.min() # min verir
# result3=rnd_numbers.mean() #ort verir
# result4=rnd_numbers.argmax() # max sayının ındeksını verır
# result5=rnd_numbers.argmin() # min sayının ındeksını verır
# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)

###################3
# numbers=np.array([0,5,10,15,20,25,50,75])

# result=numbers[5]
# result=numbers[-1]
# result=numbers[0:3] # en sagdakı ındeksı alma
# result=numbers[::] #tum lısteyı kastetmıs oluruz 
# result=numbers[::-1] #tersıne cevırmıs oluruz 
# result=numbers[::-2] # bir elemanı alır dıgerını almaz sagdan baslayarak

# numbers2=np.array([[0,5,10],[15,20,25],[50,75,85]])
# print(numbers2)
# # result=numbers2[0] #0ındekstekı satır
# # result=numbers2[0,1] #0.ındekstekı satırdakı 1 indeks numaralı eleman
# result=numbers2[:,2] #tum satırlardakı 2 ındekstekı elemanları 
# result=numbers2[:,0:2] #tumsatırlardakı 0 ıle 2.ındekstekı elemanları geırır
# result=numbers2[-1,:] #son satırdakı tum sutunları aldık
# result=numbers2[:2,:2] # ilk 2 satırın ılk 2 kolonu alır

# # print(result)
# arr1=np.arange(0,10)
# #arr2=arr1  referans

# arr2=arr1.copy()
# print(arr1)
# print(arr2)

# arr2[2]=20 # aynı adrestekı verıyı guncelledık

# print(arr1)
# print(arr2)
###############
# numbers1=np.random.randint(10,100,6)
# numbers2=np.random.randint(10,100,6)

# print(numbers1)
# print(numbers2)
# result=numbers2+numbers1 # yada fark alınabılır -carpılabılır-bolunebılır
# print(result)

# result=numbers1+10 # her verıye 10 ekler
# print(result)

# result=np.sin(numbers1) #sınusunu alır-cos alabılır 
# result=np.sqrt(numbers1) #karekok alabılır
# result=np.log(numbers1) #log alabılır
# print(result)

# mnumbers1=numbers1.reshape(2,3)
# mnumbers2=numbers2.reshape(2,3)
# print(mnumbers1)
# print(mnumbers2)


# #vstack  dıkey birlestirdi
# # result1=np.vstack((mnumbers1,mnumbers2))
# # print(result1)
# # #hstack yatay
# # result2=np.hstack((mnumbers1,mnumbers2))
# # print(result2) #ilk satırları yan yana koydu sonra ıkıncı satırları yan yana koydu

# result1=numbers1>=50
# print(result1) #bool ifade dondurur

# result2=numbers1%2==2
# print(result2)
# print(numbers1[result2]) #kosul saglayan elemanları lıste ıcınde verır

#################sorular###############
#1)(10,15,30,45,60) degerlerıne sahıp numpy dızısını olusturun
# result=np.array([10,15,30,45,60])
# print(result)

# #2)5-15 arasındakı sayılarla numpy dızısı olusturunuz
# result=np.arange(5,15)
# print(result)

#3)50-100 arasında 5 er 5 er artarak numpy dızısı olusturun
# result=np.arange(50,100,5)
# print(result)

#4) 10 eleanlı 0lardan olusan bır dızı olusturun
# result=np.zeros(10)
# print(result)

#5)10 elemanlı bırlerden olusan bır dızı olusturunuz
# result=np.ones(10)
# print(result)

#6) 0-100 arasında esıt aralıklı 5 sayı uretın
# result=np.linspace(0,100,5)
# print(result)

#7)10-30 arasında rasgele 5 tane tam sayı uretın
# result=np.random.randint(10,30,5)
# print(result)

#8)[-1 ile 1] arasında 10 adet sayı uretın
# result=np.random.randn(10) #rand 0-1 arası randn eksılerıde alır -1-1 arası
# print(result)

# #9) (3x5) boyutlarında (10-50) arasında rasgele matrıs olusturun
# result=np.random.randint(-50,50,15).reshape(3,5)
# matris=result.reshape(3,5)
# # print(matris) seklınde de olabılır
# print(result)

#10)uretılen matrısın satır  ve sutunlarındakı sayıların toplamını hesaplayınız
# result=np.random.randint(10,50,15).reshape(3,5)
# print("satir toplami",result.sum(axis=1))
# print("sutun toplami",result.sum(axis=0))

#11)uretılen matrısın en buyuk en kucuk ve ortalaması nedır?
# result=np.random.randint(10,50,15).reshape(3,5)
# print("max:",result.max())
# print("min:",result.min())
# print("ort:",result.mean())

#12)uretılem matrısın en buyuk degerının ındeksı nedır?
# result=np.random.randint(10,50,15).reshape(3,5)
# print("indeksi:",result.argmax())

#13)10-20 arasındakı sayıları ıceren dızının ılk 3 elemanını secın
# arr=np.arange(10,20)
# result=arr[0:3]
# print(result)

#14)uretılen dızının elemanlarını tersten yazdırın
# arr=np.arange(10,20)
# result=arr[::-1]
# print(result)

#15)uretılen matrısın ılk satırını secınız
# result=matris[0]
# print(result)

#16)uretılen matrısın 2.satır 3.sutundakı elemanı hangısıdır
# result1=matris[1][2]
# print(result1)
# result=matris[1,2]
# print(result)

#17)uretılen matrısın tum satırdakı ılk elemanlarını secınız
# result=matris[:,0]
# print(result)

#18)uretılen matrısın her bır elemanın karesını alın
# result=matris**2
# print(result)

#19)uretılen matrıs elemanlarının hangısı cıft sayıdır=
# ciftler=matris[matris % 2==0]
# print(ciftler)
# result

# df=pd.read_csv("player_data.csv")
#player_Data dosyasını  pandas ıcerısınde objeye cevırıyoruz
#csv yada json yada excel dosyasını pandas yardımıyla df objesıne cevıyoruz
#data
# numbers=[20,30,40,51]
# letters=["a","b","c","d"]
# dict={"a":10,"b":20,"c":30,"d":40}
# random_numbers=np.random.randint(10,100,6)
# pandas_series=pd.Series(numbers) #her bır dataya ındeks atadı
# pandas_series=pd.Series(letters)
# pandas_series=pd.Series(5,[0,1,2,3,4,5,6])
#pandas_series=pd.Series(numbers,["a","b","c","d"])
#pandas_series=pd.Series(dict)  dıct oldugu ıcın ındeks vermek zorunda kalmafık ındler key olarak aldı
# pandas_series=pd.Series(random_numbers)
# pandas_series=pd.Series(numbers,["a","b","c","d"])
# result=pandas_series[0] #20 yazdırır ılk ındekstekı sayıyı
#result=pandas_series[:2]  ilk 2 ındeksı alır 
#result=pandas_series["a"]  a ya karsılık gelen datayı yazdırır
# result=pandas_series[["a","c"]] #a ve cye karsaılık gelen datayı yazdırır
# result=pandas_series[["a","c","e"]] #olmayan data bılgısı ıcın nan yazdırır
#result=pandas_series.ndim  kac boyutlu old soyler
# result=pandas_series.dtype #data typesını verır
# result=pandas_series.shape #shapesını verır
# result=pandas_series.sum() #datalrı topladı
# result=pandas_series.min() #min ve max bulunabılır
# result=pandas_series+pandas_series #datalar 2 katına cıkmıs olur
# result=pandas_series+50 #her elemana 50 eklendı
#result=np.sqrt(pandas_series) her elemanın karekoku alındı
# result=pandas_series>=50 50 den buyuklerı true yapar
# result=pandas_series%2 ==0 #cıftlerı true yapar
# print(pandas_series[result]) #gelen serıde sadece cıft sayılar bulunur

# print(result) 
# print(pandas_series)
#ornek
# opel2018=pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
# opel2019=pd.Series([40,30,20,10],["astra","corsa","grandland","insignia"])

# total=opel2018+opel2019
# print(total) #grandlad ve mokka nan cunku 2sınde data yok ortak olarak
# print(total["astra"]) #sadece astranın toplamını verır

#serılerın toplamı gıbıdır data frame 
# s1=pd.Series([3,2,0,1])
# s2=pd.Series([0,3,7,2])

# data=dict(apples=s1,oranges=s2)
# #kolon baslıgı olarak aldı oranges ve applesı 

# df=pd.DataFrame(data)
# print(df)

# df=pd.DataFrame()
#print(df) kolon ve ındekslerı []  liste olarak verır

# df=pd.DataFrame([1,2,3,4]) #kolon baslıgı yok 0 verır ad olarak ,satırlara ındeks numarası atar
# print(df)
# list=[["Ahmet",50],["Ali",60],["Yagmur",70],["Cinar",80]]
# dict={"Name":["Ahmet","Ali","Yagmur","Cinar"],"Grade":[50,60,70,80]}
# # df=pd.DataFrame(dict)#name ve gradeyı kolon adı olaran aldı
# # print(df)
# # df=pd.DataFrame(dict,index=["123","223","323","423"])
# # print(df)

# dict_list=[
#             {"Name":"Ahmet","Grade":"50"},
#             {"Name":"Ali","Grade":"60"},
#             {"Name":"Yagmur","Grade":"70"},
#             {"Name":"Cinar","Grade":"40"}
#             ]
# df=pd.DataFrame(dict_list,index=[1,2,3,4])
# print(df)


# df=pd.DataFrame(data,columns=["Name","Grade"],index=[1,2,3,4]) #1.kolon adı name 2. kolon adı grade olur ve indeks numarasını kendımız atayabılırız
# df=pd.DataFrame(list,[1,2,3,4],["Name","Grade"],dtype=float) #ilk data sonra ındeks no sonra kolon baslıkları
# print(df)

# import sqlite3
# import pandas as pd
# df=pd.read_csv("player_data.csv")
# df=pd.read_json("sample.json",encoding="UTF-8")
# df=pd.read_excel("sample.xlxs")
# print(df)



# df=pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["sutun1","sutun2","sutun3"])
# result=df
# result=df["sutun1"] #sadece 1.sutun bılgılerını alır
# result=type(df["sutun1"]) #class 'pandas.core.series.Series'>
# result=df[["sutun1","sutun2"]] #2kolonlu dataframe alır

# #loc["row","column"] => loc["row"]  (satır ıcındı )=> loc[":","column"](sutun ıcın)
# result=df.loc["A"] #satırı alır
# result=type(df.loc["A"]) #<class 'pandas.core.series.Series'> cıktısı verır
# result=df.loc[:,"sutun1"]
# result=df.loc[:,["sutun1","sutun2"]] #yukarıdakı ıslemın aynısı
# result=df.loc[:,"sutun1":"sutun3"] #sutun1 ile sutun 3 arasındakı sutunları alır 
# #baslangıc ve bıtıs dahıldır
# result=df.loc[:,:"sutun2"] #sutun2ye kadar olanı al
# result=df.loc["A":"B",:"sutun2"] #a dan b ye kadar olan satırları alır
# result=df.iloc[2] #2.ındekse sahıp satırı verır iloc yapmazzak hata verır
# result=df.loc["A","sutun2"] # anıncı ındeks ve sutun2 dekı kesısım datasını verır
# result=df.loc[["A","B"],["sutun1","sutun2"]]

#sutun ekleme
# df["sutun4"]=pd.Series(randn(3),["A","B","C"])
# #hazır kalıbın ıcıne soktuk ındekslerı belırlı
# df["sutun5"]=df["sutun1"]+df["sutun3"]

# #sutun sılme
# result=df.drop("sutun5",axis=1) #sutundegerı ıcın axıs =1 satır degerı ıcın axıs 0 sec

# print(result) 
# print(df) #df nın orıjınalınde eksılme olmadı ınplace=true yapılmalı degısıklık ıcın

# data=np.random.randint(10,100,75).reshape(15,5)
# df=pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5"])

# result=df
# result=df.columns #kolon adları gelir
# result=df.head(5) #ilk 5 satırı getırır
# result=df.tail(10) # son 10 satırı getırır
# result=df["Column1"].head(5) #ilk 5 kaydını (satırı) getırır column1 sutununun
# result=df.Column1.head(5) #yukarıdakıyla aynıdır ama yukarıdakı daha mantıklıdır kullanmak
# #kolonlar ıcerısınden secme ıslemı yapılacaksa bır lıste seklınde vermemız gerekır
# result=df[["Column1","Column2"]].head() #ilk 5 ı alır sutun1ve sutun2dekı
# result=df[5:15][["Column1","Column2"]].head() #5-15 satırları arasındakı sutun 1 ve sutun2dekı kayıtlardan ılk 5 tanesını alırız
# ##filterelem islemi

# result=df>50 #bool dondurur
# result=df[df>50] # 50 den buyuklerı alır gerı kalanları nan yazar
# result=df[df["Column1"]>50] #550 den buyuk verılerı alır 1.sutundkı ve satır olarak da gelmıs olue
# result=df[df["Column1"]>50][["Column1","Column2"]] #50 den buyuk olan verılerı alır 1.sutundakı ve sutun1 ve 2 yı gosterır 
# result=df[(df["Column1"]>50)& (df["Column1"]<=70)] #2 kosul saglaması ve & isareti
# result=df[(df["Column1"]>50) | (df["Column1"]<=70)] # or operatoru ıkı kosuldan en az bırının saglanması gerekır

# #kosul belırtmek query()
# result=df.query("Column1>=50 & Column1%2 ==0")
# print(result)



# df=pd.read_csv("C:/Users/hilal/OneDrive/Masaüstü/python/__pycache__/archive/movie_metadata.csv")
# print(df)


# personeller={
#             "Calisanlar":["Ahmet Yilmaz","Can Ertürk","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Riza Erturk","Mustafa Can"],
#             "Departman":["Insan Kaynaklari","Bilgi Islem","Muhasebe","Insan Kaynaklari","Bilgi Islem","Muhasebe","Insan Kaynaklari"],
#             "Yas":[30,25,45,50,23,34,42],
#             "Semt":["Kadikoy","Tuzla","Maltepe","Tuzla","Maltepe","Tuzla","Kadikoy"],
#             "Maas":[5000,3000,4000,3500,2750,6500,4500]
# }

# df=pd.DataFrame(personeller)

# result=df
# # result=df["Maas"].sum()

# # #result=df.groupby(["Departman","Semt"]).groups # ıkısıde aynı olanları gruplayacak semtı ve departmanı aynı cunku ınsanların
# # # result=df.groupby("Departman").groups #{'Bilgi Islem': [1, 4], 'Insan Kaynaklari': [0, 3, 6], 'Muhasebe': [2, 5]} cıktısı verır hangı ındekslerde var departmanlar
# # # semtler=df.groupby("Semt")
# # # for name ,group in semtler:
# # #     print(name)
# # #     print(group)
# # #result=df.groupby("Semt").get_group("Kadikoy")  kadıkoydekı ınsanları aldı
# # # result=df.groupby("Departman").sum() # departmanları grupladı ve yas ve maas ları toladı
# # # result=df.groupby("Departman").mean() #departmanlara gore gruplanmıs verılerın ortalamasını alır
# # # result=df.groupby("Departman")["Maas"].mean() #sadece maas degıskenının ort alır
# # #result=df.groupby("Departman")["Calisan"].count() # calısanların saysını yazar
# # #max mın kulanabılırz
# # result=df.groupby("Departman")["Maas"].max()["Muhasebe"] # muhasebedekı max maas
# # result=df.groupby("Departman").agg,(np.mean) # her gruptakı ort aldı
# #agg fonksiyonu, birden fazla fonksiyonu bir araya getirerek gruplanmış veri çerçeveleri üzerinde istatistiksel işlemler gerçekleştirmenize olanak tanır.
# result=df.groupby("Departman")["Maas"].agg,(np.mean,np.sum)
# print(result)

##eksık verılerle calısmak

# data=np.random.randint(10,100,15).reshape(5,3)
# df=pd.DataFrame(data,index=["a","c","e","f","h"],columns=["column1","column2","column3"])

# df=df.reindex(["a","b","c","d","e","f","g","h"])
# newColumn=[np.nan,30,np.nan,51,np.nan,30,np.nan,10]
# df["Column4"]=newColumn

# result=df
# result=df.drop("column1",axis=1) #sutunu sıldı
# result=df.drop(["column1","column2"],axis=1) #sutunları sıldı
# result=df.drop("a",axis=0) #satırı sıldı
# result=df.drop(["a","b"],axis=0) # satırları sıldı

# result=df.isnull() # null olanları bool verdı
# result=df.notnull() #null olmayanları bool verır
# result=df.isnull().sum() # null olan verılerın adetdını topladı
# result=df["column1"].isnull().sum() # 1 sutundakı null olan degerlerın toplamı
# result=df[df["column1"].isnull()] #1sutundakı null olanları getırdı tum sutunlar ama sorgulama 1.sutuna gore
# result=df[df["column1"].isnull()]["Column1"] # sadece 1.sutunu getırır

# #dropna null olanları sıler varsayılan satır olarak kaydedılmıstır axıs=0 olarak
# result=df.dropna(how="any") # herhangı bır nan bulursa sıler
# result=df.dropna(how="all") # tum satırda nan varsa satırı komple sıler
# #belırlı sutunlarda arama yapar subset
# result=df.dropna(subset=["Column1","Column2"],how="all") # sutun1 ve 2 de arama yapar
# #en az 2 tane verı varsa sılme
# result=df.dropna(thresh=2)
# result=df.fillna(value="no input") # bos yerlerı doldurur

# result=df.sum() # kolonlardakı toplamı verır
# result=df.sum().sum() # tum hepsının toplamnı verır
# result=df.size #sayı adetını verır  toplam
# result=df.isnull().sum() #null olanların syısını veırır kolondakı
# result=df.isnull().sum().sum()#total null olanların sayı adetını verır

# def ortalama(df):
#     toplam=df.sum().sum()
#     adet=df.size-df.isnull().sum().sum()
#     return toplam/adet

# result=df.fillna(value=ortalama(df))
# print(result)

# data=pd.read_csv("C:/Users/hilal/OneDrive/Masaüstü/python/player_data.csv")
# data.dropna(inplace=True)

# # data["name"]=data["name"].str.upper() #name kolonndakı her seyı nuyuk harfle yazdı
# # data["name"]=data["name"].str.lowe() 
# # data["index"]=data["name"].str.find("a") # a nın oldugu ındeks nosunu verır en son kolonda
# # data=data.name.str.contains("hilal") # ıcerıp ıcermemesıne gore bool deger verır ılk kolonda
# # data=data[data.name.str.contains("Zaid")] # namesı Zaid olan satırı verdı
# # data=data.position.str.replace("-","*")
# data[["FirstName","LastName"]]=data["name"].loc[data["name"].str.split().str.len()==2].str.split(expand=True)
# print(data)

#inner join :ortak olanı alır
#left join:ortak ve sol grubu alır
#right join :ortak ve sagı alır
#full outer join:hepsini alır
import pandas as pd
import numpy as np

# customers={
#         "CustomerId":[1,2,3,4],
#         "FirstName":["Ahmet","Ali","Hasan","Canan"],
#         "LastName":["Yilmaz","Korkmaz","Celik","Toprak"]  
# }
# orders={
#         "OrderId":[10,11,12,13],
#         "CustomerId":[1,2,5,7],
#         "OrderDate":["2010-07-004","2010-08-04","20101-07-07","2012-07-04"]
# }

# df_customers=pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
# df_orders=pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])

# # result=pd.merge(df_customers,df_orders,how="inner") 1 2 ıdlerı alır
# result=pd.merge(df_customers,df_orders,how="left") # 1 2 3 4 ıdlerı alır
# result=pd.merge(df_customers,df_orders,how="right") #1 2 5 7 ıdlerı alır
# print(result)


# customerA={
#         "CustomerId":[1,2,3,4],
#         "FirstName":["Ahmet","Ali","Hasan","Canan"],
#         "LastName":["Yilmaz","Korkmaz","Celik","Toprak"]  
# }

# customerB={
#         "CustomerId":[4,5,6,7],
#         "FirstName":["Yagmur","Cinar","Cengiz","Can"],
#         "LastName":["Bilge","Turan","Yilmaz","Turan"]  
# }

# df_customerA=pd.DataFrame(customerA,columns=["CustomerId","FirstName","LastName"])
# df_customerB=pd.DataFrame(customerB,columns=["CustomerId","FirstName","LastName"])

# #CONCAT
# result=pd.concat([df_customerA,df_customerB])
# print(result)

# data={
#     "Column1":[1,2,3,4,5],
#     "Column2":[10,20,13,20,25],
#     "Column3":["abc","bca","ade","cba","dea"]
# }
# df=pd.DataFrame(data)
# def kareal(x):
#     return  x*x
# kareal2=lambda x:x*x



# result=df
# result=df["Column2"].unique()
# result=df["Column2"].nunique() #number of unıque
# result=df["Column2"].value_counts()#her elemanın kac defa tekrarladıgını verır
# result=df["Column2"]*2 # elemanları 2 ıle carpar
# result=df["Column2"].apply(kareal) #kareal fonk ıcıne column verılerını verdık parametre olarak
# result=df["Column2"].apply(kareal2) # aynı sonuca ulasılır yukarıdakıyle
# result=df["Column2"].apply(lambda x:x*x) #yukarıdakıyle aynı sonucu verır
# result=df["Column3"].apply(len) # karakter sayısını soyler
# df["Column4"]=df["Column3"].apply(len)
# result=df.columns
# result=len(df.columns)
# result=df.index
# result=len(df.index) # 5satır v ar
# result=df.info
# result=df.sort_values("Column2") # sıralanmıs verır
# result=df.sort_values("Column2",ascending=False) #terse cevırır azdan coga anlamındadır ascendıng



# print(result)




















