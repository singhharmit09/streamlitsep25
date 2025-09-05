import streamlit as st
import numpy as np
import pandas as pd
import pickle
import sklearn

st.title("Car Resale Price Prediction")
df = pd.read_csv("cars24-car-price.csv")
st.write(df.head())

col1, col2 = st.columns(2)

fuel_type = col1.selectbox("Select the fuel type",["Diesel","Petrol","CNG","LPG","Electric"])
engine = col1.slider("Set the Engine Power",500,5000, step=100)
transmission_type=col2.selectbox("Select the Transmission Type",["Manual","Automatic"])
seats=col2.selectbox("Set the Number of Seats",[4,5,7,9,11])

encode_dict = {
    "fuel_type":{"Diesel": 1,"Petrol": 2, "CNG": 3, "LPG": 4, "Electric": 5},
    "seller_type":{"Dealer": 1, "Individual": 2, "Trustmark Dealer": 3},
    "transmission_type":{"Manual": 1, "Automatic": 2}
}

if st.button("Get Price"):
    encoded_fuel_type = encode_dict['fuel_type'][fuel_type]
    encoded_transmission_type = encode_dict['transmission_type'][transmission_type]
    input_car = [2012.0,2,120000,encoded_fuel_type,encoded_transmission_type,19.7,engine,46.3,seats]

    with open("car_pred", "rb") as f:
        car_pred = pickle.load(f)
    price = car_pred.predict([input_car])[0]
    st.header(np.round(price,2))



