import numpy as np
import streamlit as st
import pickle

load_model = pickle.load(open('model_car_pred.pkl', 'rb'))

def car_prediction(input_data):
     input_data_as_numpy_array = np.asarray(input_data)

   
     input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Predict
     prediction = load_model.predict(input_data_reshaped)
     return f"Predicted Car Value: ${prediction}"

st.title("Car Value Prediction")

vehicle_age = st.number_input("Vehicle Age", min_value=0)
km_driven = st.number_input("KM Driven", min_value=0)
mileage = st.number_input("Mileage")
engine = st.number_input("Engine (cc)")
seats = st.number_input("Seats", min_value=1)

seller_type = st.selectbox("Seller Type", ["Dealer", "Individual", "Trustmark Dealer"])
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

if st.button("Predict Price"):
     
    features = [
        vehicle_age,
        km_driven,
        mileage,
        engine,
        seats
    ]
    
    seller = [0, 0, 0]
    if seller_type == "Dealer":
        seller[0] = 1
    elif seller_type == "Individual":
        seller[1] = 1
    else:
        seller[2] = 1
    fuel = [0, 0, 0, 0, 0]
    fuel_map = ["CNG", "Diesel", "Electric", "LPG", "Petrol"]
    fuel[fuel_map.index(fuel_type)] = 1

    # transmission encoding (2 columns)
    trans = [0, 0]
    if transmission == "Automatic":
        trans[0] = 1
    else:
        trans[1] = 1
    final_input = features + seller + fuel + trans
    final_input = np.array(final_input).reshape(1, -1)

    prediction = load_model.predict(final_input)

    st.success(f"Estimated Price: ₹ {prediction[0]:,.2f}")
