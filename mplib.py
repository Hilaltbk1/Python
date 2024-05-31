import numpy as np
import matplotlib.pyplot  as plt

# yasListesi=[10,20,30,30,30,40,50,60,70,75]
# kiloListesi=[20,60,80,85,86,87,70,90,95,90]

# numpyYasListesi=np.array(yasListesi)
# numpyKiloListesi=np.array(kiloListesi)

# plt.plot(numpyYasListesi,numpyKiloListesi,"r")
# plt.xlabel("yas veriler")
# # x ve y eksenı adları
# plt.ylabel("kilo verileri")
# plt.title("Kilo nun yasa gore degısım grafıgı")
# #grafıgın adı
# #ilk yazılan x eksenını temsıl ederken dıger yazılan y eksenını temsıl eder
# #g green yanı cızımın rengını temsıl eder r deseydık red olurdu



# plt.show()
#numpyDizisi1=np.linspace(0,10,20)   aralarında esıt aralık olan 0-10 aralıgında 20 adet sayı
#numpyDizisi2=numpyDizisi1**2
# plt.plot(numpyDizisi1,numpyDizisi2,"r--")
#renk harf kodundan sonra -- koyarsak kesıklı olur 
# plt.plot(numpyDizisi1,numpyDizisi2,"r*-")
#*- eklersek ıse yıldızla ısaretlenmıs sekılde verır
#her yildiz bir veriyi temsil eder

#2 ayrı grafıgı bırlestırır aynı duzlemde verır yan yana ya da alt alta
# plt.subplot(1,2,1) # 1 sıra olacak,2kolon olacak ve suan 1..yı cızer
# plt.plot(numpyDizisi1,numpyDizisi2,"r*-")
# plt.subplot(1,2,2) # 1 sıra olacak,2kolon olacak ve suan 2 .yı cızer
# plt.plot(numpyDizisi2,numpyDizisi1,"g--")

#sımdıye kadar kutuphaneden nesne olusturmadan ılerledık sımdıden sonra ıse
#kutuphaneden obje olusturup o obje uzerınden ıslemler yapacagız 
#daha fazla kontrol ve ozellestırme getırır

#figur olusturacagız bos bır cızım yetı gıbı dusunebılırsın ıcerısınde grafık yok 
# benimFigure=plt.figure()
# #x ve y eksenı verılerı uoktur
# figureAxes=benimFigure.add_axes([0.4,0.4,0.5,0.5])
# #ılk sayı y eksenının baslangıc noktası 
# figureAxes.plot(numpyDizisi1,numpyDizisi2,"g")
# figureAxes.set_xlabel("x ekseni veri ismi")
# figureAxes.set_ylabel("y ekseni veri ismi")
# figureAxes.set_title("grafik adi")
# plt.show()


# figure2=plt.figure()

# eksen1=figure2.add_axes([0.1,0.1,0.9,0.9])
# eksen2=figure2.add_axes([0.1,0.1,0.3,0.3])
# #sayıları degıstırerek konumunu degıstırdık (nereden baslayacagı) ılk 2 parametrede

# eksen1.plot(numpyDizisi1,numpyDizisi2,"g")
# eksen1.set_xlabel("X Ekseni")
# eksen1.set_ylabel("Y Ekseni")
# eksen1.set_title("Ana grafik baslık")

# eksen2.plot(numpyDizisi2,numpyDizisi1,"g")
# eksen2.set_xlabel("X Ekseni")
# eksen2.set_ylabel("Y Ekseni")
# eksen2.set_title("Kucuk grafik baslık")
# plt.show()


# plt.subplot()
#bos bır alan ve eksen cıkarır yukarıdakınden ek olarak eksen de vardır
#tuple dondurur
#ilk figure ıkıncı olarak eksen dondurur
# (benimFigure,benimEksenler)=plt.subplots(nrows=1,ncols=2)
# # benimEksen.plot(numpyDizisi1,numpyDizisi2,"b")
# # plt.show()
# #print(type(benimEksen)) <class 'numpy.ndarray'> cıktısı verır
# for eksen in benimEksenler:
#     eksen.plot(numpyDizisi1,numpyDizisi2,"g")
#     eksen.set_xlabel("x ekseni ")
# plt.show()
# plt.tight_layout()


#veri gorsellestırme
# yeniFigure=plt.figure(dpi=100)
# #parametre verebilirz axes ı override edıyor ve figsize =deger verırsek
# #deger vermezzek with ve heighte gore olusturur
# #dpi= cozunurlugu kac pxel olacagı ıle ılgılı bır degıskendır
# #en bastan degılde grafıgı kaydetmeden once dpi belirtebiliriz
# #kaydetmek için yeniFigure.savefig("benimfigur.png",dpi=200)
# yeniEksen=yeniFigure.add_axes([0.1,0.1,0.9,0.9])

# yeniEksen.plot(numpyDizisi1,numpyDizisi1**2,label="Numpy dizisi**2")
# yeniEksen.plot(numpyDizisi1,numpyDizisi1**3,label="Numpy dizisi**3")
# yeniEksen.legend(loc=1)
# #legend in loc vererek yerını degıstırebılırz labelın
# #label=verinin acıklaması yada bırden fazla cızgı varsa onu acıklamak ıcın
# plt.show()

# numpyDizisi1=np.linspace(0,10,20)
# numpyDizisi2=numpyDizisi1**2


# # (benimFigur,benimEksen)=plt.subplots()
# # benimEksen.plot(numpyDizisi1,numpyDizisi2,color="#3A95A8")
# # benimEksen.plot(numpyDizisi2,numpyDizisi1,color="#C96F23")
# #rgb hex code yazıp renk kodlarına gore renk secebılırız grafıgımız ıcın
# #saydamlık katmak ıstersek alpha=degerini azaltıp yazabılırz color kısmından sonra 

# #grafık cızgılerını kalınlastırabılırz
# (yeniFigur,yeniEksen)=plt.subplots()
# yeniEksen.plot(numpyDizisi1,numpyDizisi1+2,color="blue",linewidth=8.0)
# yeniEksen.plot(numpyDizisi1,numpyDizisi1+3,color="yellow",linewidth=6.0)
# yeniEksen.plot(numpyDizisi1,numpyDizisi1+4,color="#C96F23",linestyle="-.")
# yeniEksen.plot(numpyDizisi1,numpyDizisi1+5,color="#C96F23",linestyle=":")
# yeniEksen.plot(numpyDizisi1,numpyDizisi1+6,color="#C96F23",linestyle="--")
# #eksen style cızgı cızgı yaptı -- ,: nokta nokta yapar -. da calısır
# #verilerin isaretlenmesi marker
# yeniEksen.plot(numpyDizisi1,numpyDizisi1+7,color="#000000",linestyle="-",marker="o",markersize="10 ",markerfacecolor="red")
# yeniEksen.plot(numpyDizisi1,numpyDizisi1+8,color="#000000",linestyle="--",marker="+",markersize="5")
# plt.show()

#scatter
# plt.scatter(numpyDizisi1,numpyDizisi2)
#veriler dagılmıssa bıraz
#histogram
# yeniDizi=np.random.randint(0,100,50)
# plt.hist(yeniDizi)
#boxplot
#standart sapmanın ne kadar oldugunu az oup olmadıgını anlamak ıcın kullanılabılır
# plt.boxplot(yeniDizi)
# plt.show()

# x=[1,2,3,4]
# y=[1,4,9,16]
# plt.plot(x,y,color="g",linestyle="--",linewidth="5",marker="o")
# #x dgerine karsılık gelen y degerını gosterır
# #1 2 3 4 x 1 4 9 16 ise y eksenındekı degerlerı gosterır
# plt.axis([0,6,0,20])
# #x in aralıgı 0-6 iken y nın aralıgı 0-20 olur
# plt.title("grafik baslıgı")
# plt.xlabel("x label")
# plt.ylabel("y label")

# x=np.linspace(0,2,100)

# plt.plot(x,x,label="linear",color="red")
# plt.plot(x,x**2,label="qudratic",color="blue")
# plt.plot(x,x**3,label="cubic",color="yellow")

# plt.xlabel("x label")
# plt.ylabel("y label")
# plt.title("grafık baslıgı")
# plt.legend()
#lagend actıgımız ıcın labeller yer aldı
#grafık uzerındekı alana axes dıyoeuz 
#0,0  0,1  1,0 1,1 gibi axes  
#grafik alanına axes dıyoruz ısaretlenecek alan

#duzleme bır kac tane grafık eklemek ıcın subplots kullanabılırz
# fig,axs=plt.subplots(3) 
#2parametresı verdıgımız ıcın 3 axes alanı olusturmus oluruz 

# axs[0].plot(x,x,color="red")
# axs[0].set_title("linear")

# axs[1].plot(x,x**2,color="green")
# axs[1].set_title("quadratic")

# axs[2].plot(x,x**3,color="yellow")
# axs[2].set_title("cubic")



# plt.tight_layout()
#grafikler arası boslugu duzeltır
 
# fig,axs=plt.subplots(2,2) # 2 satır 2 kolon anlamında 
# fig.suptitle("grafik basligi")

# axs[0,0].plot(x,x,color="red")
# axs[0,1].plot(x,x**2,color="blue")
# axs[1,0].plot(x,x**3,color="green")
# axs[1,1].plot(x,x**4,color="yellow")


# x=np.linspace(-10,9,20)
# y=x**3
# z=x**2

# figure=plt.figure()
#1) ornek
# add_axes() bu metot figur uzerıne eklenecek olan axes  alanın konumunu belırtır
# axes_cube=figure.add_axes([0.1,0.1,0.8,0.8])
#soldan ve alttan 0.2 saga kaymıs ve yukseklık 0.8 genıslık 0.8 ayarlamıs tamamını 1-1 kabul edersek
# axes_cube.plot(x,y,"b")
# axes_cube.set_xlabel("x asis")
# axes_cube.set_ylabel("y asis")
# axes_cube.set_title("cube")

# axes_square=figure.add_axes([0.15,0.6,0.25,0.3])
# axes_square.plot(x,z,"r")
# axes_square.set_xlabel("x asis")
# axes_square.set_ylabel("y asis")
# axes_square.set_title("square")

#2) ornek
# axes=figure.add_axes([0,0,1,1])
# axes.plot(x,z,label="square")
# axes.plot(x,y,label="cube")
# axes.legend(loc=1)
#lagendin konumunu loc ıle degıstırebılırz
#3)ornek
# fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(4,4))
# axes[0].plot(x,y)
# axes[0].set_title("square")

# axes[1].plot(x,z)
# axes[1].set_title("cube")

# plt.tight_layout()
# fig.savefig("figure1.png")
##////////stack Plot
# yil=[2011,2012,2013,2014,2015]

# oyuncu1=[8,10,12,7,9]
# oyuncu2=[7,12,5,15,21]
# oyuncu3=[18,20,22,25,19]

# #stack Plot grafıgı kullanacagız
# plt.plot([],[],color="y",label="oyuncu1")
# plt.plot([],[],color="r",label="oyuncu2")
# plt.plot([],[],color="b",label="oyuncu3")

# plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=["y","r","b"])
# plt.title("yıllara gore atılan gol sayısı grafıgı")
# plt.xlabel("yil")
# plt.ylabel("gol")
# plt.legend()
##///////////pasta grafıgı (pıe)
# goal_types="Penalti","Kaleye Atılan Sut","Serbest Vurus"
# goals=[12,35,7]
# colors=["y","r","b"]
# plt.pie(goals,labels=goal_types,colors=colors,shadow=True,explode=(0.05,0.05,0.05),autopct="%1.1f%%")
#autopct="%1.1f%%" yuzdelık dılım olarak ıfade eder ,shadow golge olup olmamasını kontrol eder

##///////// bar grafıgı
# plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5)
# plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi",width=.5)

# plt.legend()
# plt.xlabel("Gun")
# plt.ylabel("Mesafe (KM)")
# plt.title("Arac bilgileri")

## histogram
# yaslar=[22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
# yas_gruplari=[0,10,20,30,40,50,60,70,80,90,100]

# plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)
# plt.xlabel("yas gruplari")
# plt.ylabel("kisi sayisi")
# plt.title("histogram garafi")














plt.show()









