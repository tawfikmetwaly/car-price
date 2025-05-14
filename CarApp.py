import joblib
import pandas as pd
import streamlit as st

# Load Model
model = joblib.load('rf_model.sav')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Build Streamlit
st.cache_data.clear()
st.title('Car Price Predection 🚗💵')
st.image("design.jpg",use_container_width =True)

list_Cars = ['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
       'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
       'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
       'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
       'Ambassador', 'Ashok', 'Isuzu', 'Opel']

fuel_types = ['Diesel', 'Petrol', 'LPG', 'CNG']

owner_types = ['First Owner', 'Second Owner', 'Third Owner','Fourth & Above Owner','Test Drive Car']

Seller_Types = ['Individual', 'Dealer', 'Trustmark Dealer']

transmission_types = ['Manual', 'Automatic']

seats_types = [2, 4, 5, 6, 7, 8, 9, 10, 14]

with st.container(height=1000):
 st.header('Enter Car Details')
 col1 , col2 = st.columns(2)
 with col1:
  st.write("### Brand of Car")
  name = st.selectbox("You selected:",list_Cars)

  st.write("### Type of Owner")
  owner = st.selectbox("You selected:",owner_types)

  st.write("### Type of Transmission")
  transmission = st.selectbox("You selected:",transmission_types)

  st.write("### Type of Fuel⛽")
  fuel = st.selectbox("You selected:",fuel_types)

  st.write("### Type of Sellers")
  seller_type = st.selectbox("You selected:",Seller_Types)
 with col2:
   st.write("### KM Driven of Car")
   km_driven = st.text_input(label="You Enter:")

   st.write("### Mileage of Car")
   mileage = st.slider("You selected:",0,40,20)

  
   st.write("### Age of Car")
   age = st.slider("You selected:",0,40,3)

   st.write("### Engine of Car (CC)")
   engine = st.slider("You selected:",0,4000,1200)

   st.write("### Max Power of Car (hp)")
   max_power = st.slider("You selected:",0,1000,120)

 st.write("### Number of Seat 💺")
 seats = st.selectbox("You selected:",seats_types)

name_to_encode = ['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault', 'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz', 'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus', 'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force', 'Ambassador', 'Ashok', 'Isuzu', 'Opel']

encoded_name = [20, 26, 10, 11, 28, 9, 25, 19, 27, 4, 6, 14, 21, 22, 2, 29, 3, 23, 17, 13, 16, 18, 30, 5, 15, 7, 8, 0, 1, 12, 24]
convert_name = dict(zip(name_to_encode, encoded_name))

fuel_to_encode = ['Diesel', 'Petrol', 'LPG', 'CNG']
encoded_fuel = [1, 3, 2, 0]
convert_fuel = dict(zip(fuel_to_encode,encoded_fuel))

seller_to_encode = ['Individual', 'Dealer', 'Trustmark Dealer']
encoded_saller = [1, 0, 2]
convert_saller = dict(zip(seller_to_encode,encoded_saller))

transmission_to_encode = ['Manual', 'Automatic']
encoded_transmission = [1, 0]
convert_transmission = dict(zip(transmission_to_encode,encoded_transmission))

owner_to_encode = ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car']
encoded_owner = [0, 2, 4, 1, 3]
convert_owner = dict(zip(owner_to_encode,encoded_owner))


try:
 df = pd.DataFrame({
          'age':[age],
          'km_driven':[float(km_driven)],
          'fuel':convert_fuel[fuel],
          'seller_type':convert_saller[seller_type],
          'transmission':convert_transmission[transmission],
          'owner':convert_owner[owner],
          'mileage':[mileage],
          'engine':[engine],
          'max_power':[max_power],
          'seats':[seats],
          'Brand':convert_name[name],
          },index=[0],
          )
except ValueError:
    st.error("Please ensure all numerical fields are correctly filled! ❌")


with st.sidebar:
 st.write("# Prediction Price of Car")
 st.info("The prediction is based on 97% accuracy ✔️")
 button = st.button("Predict Price",type='primary')
 if button:
   st.markdown("---")
   price = model.predict(df)
   price = price[0]
   formatted_price = f"{price:,.2f}" 
   st.write(f"## The Predicted Price is {formatted_price}")