from users.models import *
from .models import Car,TestCar

def user_type(username):
    users = Users.objects.filter(username=username)
    for i in users:
        return i.user_type

# def predict_the_price(algorithm,x_train_,y_train_,x_test_,y_test_):
    # algorithm.fit(x_train_,y_train_)
    # predicts=algorithm.predict(x_test_)
    # print(predicts[:5])

# data= pd.DataFrame(list(Car.objects.all().values()))

# # print(type(data))
# data = data.drop(['name','Pin_No','id','user_id','image_link','image'],axis=1)
# # data.info()
# data.fuel.replace(regex={"Petrol":"0","Diesel":"1","CNG":"2","Electric":"3","LPG":"4"},inplace=True)
# data.seller_type.replace(regex={"Dealer":"0","Individual":"1","Trustmark 0":"2"},inplace=True)
# data.seller_type.replace(regex={"Dealer":"0","Individual":"1","Trustmark 0":"2"},inplace=True)
# data.transmission.replace(regex={"Manual":"0","Automatic":"1"},inplace=True)
# data.owner.replace(regex={"First Owner":"0","Second Owner":"1","Third Owner":"3","Fourth & Above Owner":"4","Test Drive Car":"5"},inplace=True)
# # set(data['transmission'])

# data[["fuel","seller_type","transmission","owner"]]=data[["fuel","seller_type","transmission","owner"]].astype(int)

# y=data.selling_price
# x=data.drop(["selling_price"],axis=1)

# # data.info()

# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

# # print("x train: ",x_train.shape)
# # print("x test: ",x_test.shape)
# # print("y train: ",y_train.shape)
# # print("y test: ",y_test.shape)

# lr = LinearRegression()
# predict_the_price(lr,x_train,y_train,x_test,y_test)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

def predict_the_price(algorithm,x_train_,y_train_,x_test_):
    algorithm.fit(x_train_,y_train_)

    # print(x_train_.info())
    # print(x_test_.info())
  
    predicts=algorithm.predict(x_test_)
    return predicts[-1]

def price_predictor(data,test):
    data = data.drop(['name','id','user_id','image_link','image','Pin_No'],axis=1)

    data.fuel.replace(regex={"Petrol":"0","Diesel":"1","CNG":"2","Electric":"3","LPG":"4"},inplace=True)
    data.seller_type.replace(regex={"Dealer":"0","Individual":"1","Trustmark 0":"2"},inplace=True)
    data.seller_type.replace(regex={"Dealer":"0","Individual":"1","Trustmark 0":"2"},inplace=True)
    data.transmission.replace(regex={"Manual":"0","Automatic":"1"},inplace=True)
    data.owner.replace(regex={"First Owner":"0","Second Owner":"1","Third Owner":"3","Fourth & Above Owner":"4","Test Drive Car":"5"},inplace=True)

    data[["fuel","seller_type","transmission","owner"]]=data[["fuel","seller_type","transmission","owner"]].astype(int)


    y=data.selling_price
    x=data.drop(["selling_price"],axis=1)

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

    test = test.drop(['id'],axis=1)
    try:
        test = test.drop(['name','user_id','image_link','image','Pin_No'],axis=1)
    except:
        pass

    # print(data.info())


    test.fuel.replace(regex={"Petrol":"0","Diesel":"1","CNG":"2","Electric":"3","LPG":"4"},inplace=True)
    test.seller_type.replace(regex={"Dealer":"0","Individual":"1","Trustmark 0":"2"},inplace=True)
    test.seller_type.replace(regex={"Dealer":"0","Individual":"1","Trustmark 0":"2"},inplace=True)
    test.transmission.replace(regex={"Manual":"0","Automatic":"1"},inplace=True)
    test.owner.replace(regex={"First Owner":"0","Second Owner":"1","Third Owner":"3","Fourth & Above Owner":"4","Test Drive Car":"5"},inplace=True)

    test[["fuel","seller_type","transmission","owner"]]=test[["fuel","seller_type","transmission","owner"]].astype(int)

    # print(test.info())
    try:
        test = test.drop('selling_price',axis=1)
    except:
        pass

    x_test = test
    lr = LinearRegression()
    return predict_the_price(lr,x_train,y_train,x_test)
    
# train = pd.DataFrame(list(Car.objects.all().values()))
# test = pd.DataFrame(list(TestCar.objects.filter().values()))

# print(price_predictor(train,test))

# data = pd.DataFrame(list(Car.objects.all().values()))

# data = data.drop(['name','id','user_id','image_link','image','Pin_No'],axis=1)

# data.fuel.replace(regex={"Petrol":"0","Diesel":"1","CNG":"2","Electric":"3","LPG":"4"},inplace=True)
# data.seller_type.replace(regex={"Dealer":"0","Individual":"1","Trustmark 0":"2"},inplace=True)
# data.seller_type.replace(regex={"Dealer":"0","Individual":"1","Trustmark 0":"2"},inplace=True)
# data.transmission.replace(regex={"Manual":"0","Automatic":"1"},inplace=True)
# data.owner.replace(regex={"First Owner":"0","Second Owner":"1","Third Owner":"3","Fourth & Above Owner":"4","Test Drive Car":"5"},inplace=True)

# data[["fuel","seller_type","transmission","owner"]]=data[["fuel","seller_type","transmission","owner"]].astype(int)


# y=data.selling_price
# x=data.drop(["selling_price"],axis=1)

# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

# test = test.drop(['id'],axis=1)
# test.fuel.replace(regex={"Petrol":"0","Diesel":"1","CNG":"2","Electric":"3","LPG":"4"},inplace=True)
# test.seller_type.replace(regex={"Dealer":"0","Individual":"1","Trustmark 0":"2"},inplace=True)
# test.seller_type.replace(regex={"Dealer":"0","Individual":"1","Trustmark 0":"2"},inplace=True)
# test.transmission.replace(regex={"Manual":"0","Automatic":"1"},inplace=True)
# test.owner.replace(regex={"First Owner":"0","Second Owner":"1","Third Owner":"3","Fourth & Above Owner":"4","Test Drive Car":"5"},inplace=True)

# test[["fuel","seller_type","transmission","owner"]]=test[["fuel","seller_type","transmission","owner"]].astype(int)

# x_test = test
# lr = LinearRegression()
# predict_the_price(lr,x_train,y_train,x_test)
