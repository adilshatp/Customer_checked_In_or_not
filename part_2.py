# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 22:45:24 2022

@author: ACER
"""

import pandas as pd
import streamlit as st
import matplotlib.image as mp
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageOps
import numpy as np
import requests
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder

image = mp.imread("checkin.png")
st.image(image)
st.write("""
         Customer wheather checked in or not
         """
         )

st.sidebar.header('Enter input')

def user_input_features():
    Nationality=st.sidebar.selectbox("Nationality",["prt", "deu", "fra", "other", "irl", "esp", "bel", "nld", "aut", "ita", "usa", "che", "gbr", "bra", "can", "swe"])
    Age=st.sidebar.number_input("Age",0,110)
    DaysSinceCreation=st.sidebar.number_input("DaysSinceCreation",0,10000)
    AverageLeadTime=st.sidebar.number_input("AverageLeadTime",0,1000)
    LodgingRevenue=st.sidebar.number_input("LodgingRevenue",0,10000)
    OtherRevenue=st.sidebar.number_input('OtherRevenue',0,1000)
    BookingsCanceled=st.sidebar.number_input("BookingsCanceled",0,10)
    BookingsNoShowed=st.sidebar.selectbox("BookingsNoShowed",[0,1,2,3])
    PersonsNights=st.sidebar.number_input("PersonsNights",0,100)
    DistributionChannel=st.sidebar.selectbox("DistributionChannel",[0,1,2,3])
    SRHighFloor=st.sidebar.selectbox("SRHighFloor", [0,1])
    SRLowFloor=st.sidebar.selectbox("SRLowFloor",[0,1])
    SRAccessibleRoom=st.sidebar.selectbox("SRAccessibleRoom",[0,1])
    SRMediumFloor=st.sidebar.selectbox("SRMediumFloor", [0,1])
    SRBathtub=st.sidebar.selectbox("SRBathtub", [0,1])
    SRShower=st.sidebar.selectbox("SRShower", [0,1])
    SRCrib=st.sidebar.selectbox("SRCrib", [0,1])
    SRKingSizeBed=st.sidebar.selectbox("SRKingSizeBed", [0,1])
    SRTwinBed=st.sidebar.selectbox("SRTwinBed", [0,1])
    SRNearElevator=st.sidebar.selectbox("SRNearElevator", [0,1])
    SRAwayFromElevator=st.sidebar.selectbox("SRAwayFromElevator", [0,1])
    SRNoAlcoholInMiniBar=st.sidebar.selectbox("SRNoAlcoholInMiniBar", [0,1])
    SRQuietRoom=st.sidebar.selectbox("SRQuietRoom", [0,1])
    
    data={"Nationality":Nationality,
          "Age":Age,
          "DaysSinceCreation":DaysSinceCreation,
          "AverageLeadTime":AverageLeadTime,
          "LodgingRevenue":LodgingRevenue,
          "OtherRevenue":OtherRevenue,
          "BookingsCanceled":BookingsCanceled,
          "BookingsNoShowed":BookingsNoShowed,
          "PersonsNights":PersonsNights,
          "DistributionChannel":DistributionChannel,
          "SRHighFloor":SRHighFloor,
          "SRLowFloor":SRLowFloor,
          "SRAccessibleRoom":SRAccessibleRoom,
          "SRMediumFloor":SRMediumFloor,
          "SRBathtub":SRBathtub,
          "SRShower":SRShower,
          "SRCrib":SRCrib,
          "SRKingSizeBed":SRKingSizeBed,
          "SRTwinBed":SRTwinBed,
          "SRNearElevator":SRNearElevator,
          "SRAwayFromElevator":SRAwayFromElevator,
          "SRNoAlcoholInMiniBar":SRNoAlcoholInMiniBar,
          "SRQuietRoom":SRQuietRoom}
    features=pd.DataFrame(data,index=[0])
    return features

df=user_input_features()


df5=pd.read_json('national.json')
le = LabelEncoder()
df5["label"] = " "
df5["label"] = le.fit_transform(df5["data_columns"])



df5 = df5.sort_values('label')
df5.reset_index(inplace=True)


x = df["Nationality"][0]
x = str(x)
def get_label(x):
    c = df5[df5["data_columns"] == x].index[0]
    return c


c = get_label(x)
df["Nationality"][0] = c


st.subheader("values")
st.write(df)   
    
submit=st.button('IN or OUT')

df = np.asarray(df).astype('float32')

model=tf.keras.models.load_model('customer_checkedin.h5')

prediction=model.predict(df)

#prediction = str(int(prediction[0]))

st.subheader("Result=")

st.write("CHECKED IN" if prediction == 1 else "NOT CHECKED IN")

 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    