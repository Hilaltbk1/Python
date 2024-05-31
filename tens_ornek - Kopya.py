import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
import tensorflow as tf

dataFrame=pd.read_csv("C:/Users/hilal/OneDrive/Masaüstü/python/__pycache__/bisiklet_fiyatlari.csv")
# result=dataFrame.head()
# print(result)
# sbn.pairplot(dataFrame)
# plt.show()

#veriyi test/train olarak 
from sklearn.model_selection import train_test_split
#train_test_split (4 arguman alır,x_train,xtest,ytrain,ytest test_Size ister yuzde kacı test ıcın kullanılacak)
#y=wx+b
#y-> label
#x->featur (ozellik)
y=dataFrame["Fiyat"].values #numpy arrraye cevırdık,values demessek pandas serısı olarak alır ,dersek numpy
x=dataFrame[["BisikletOzellik1","BisikletOzellik2"]].values

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.33,random_state=15)

# print(x_train.shape) #670,2
# print(x_test.shape) # 330,2
# print(y_test.shape) #330, 

#scaling ölceklendırme

from sklearn.preprocessing import MinMaxScaler
#minmax sınıfından obje olusturmalıyız
scaler=MinMaxScaler()
scaler.fit(x_train)
#satırı, ölçekleyici modelini eğitim setine sığdırır. Bu işlem modelin
#verilerin minimum ve maksimum değerlerini öğrenmesini sağlar.

x_train=scaler.transform(x_train)
# satırı, ölçekleyici modelini kullanarak eğitim setini ölçeklendirir. Bu işlem
# sonucu eğitim setindeki değerler 0 ile 1 aralığına düşürülür.
x_test=scaler.transform(x_test)
# satırı, aynı ölçekleyici modelini kullanarak test setini de ölçeklendirir. 
# Böylece test seti de aynı aralığa ölçeklenmiş olur.
# print(x_test)

from tensorflow.python.keras.models import Sequential   
#modelımızın sınıfı ve ıcerısınde katmanlarla calısacagız onu belırtıyoruz 
from tensorflow.python.keras.layers import Dense
#katmanlarla calısmak ıcın 

model=Sequential()

model.add(Dense(4,activation="relu"))
model.add(Dense(4,activation="relu"))
model.add(Dense(4,activation="relu"))

model.add(Dense(1)) # cıktı kısmı 1noron vermemız yeterlı olur
model.compile(optimizer="rmsprop")#compıle edıyor calısmaya hazır hale getırıyor,optimizer parametres ıalıyor ve lose alıyor
#buyuk verı setımız varsa verılerı 200 er 300 er vermek mantıklıdır bench olarak ayarlayabılırız 
#ıpoke secmelıyız tum  verı setlerınden 1 kez gecılırse 1 olmus oluyor 
#cok fazla secılırse overfıttınge yol acabılır sadece kendı verı setındekı elemanlar dogru cıksın dıye ogrenmeye baslaayabılır
model.fit(x_train,y_train,epochs=250)

