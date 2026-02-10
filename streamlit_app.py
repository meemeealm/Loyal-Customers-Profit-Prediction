import streamlit as st
import pickle

@st.cache_resource
def load_pipeline():
    with open('model.bin', 'rb') as f_in:
        return pickle.load(f_in)

pipeline = load_pipeline()

st.title("Loyal Customers: Potential Profit Predictor")

# UI Inputs
customer_name = st.text_input("Customer Name", value="Write Customer's Name!")
sub_category = st.selectbox("Sub Category", ["Health Drinks", "Dals & Pulses", "Soft Drinks", "Cookies", "Fresh Vegetables", "Edible Oil & Ghee","Chicken"])
city = st.selectbox("City", ["Vellore", "Chennai", "Madurai", "Nagercoil", "Ramanadhapuram", "Kanyakumari"])
sales = st.number_input("Sales", min_value=0, value=10)
discount = st.number_input("Discount", min_value=0, value=4)

if st.button("Predict Profit"):

    input_data = {
        "Customer Name": customer_name,
        "Sub Category": sub_category,
        "City": city,
        "Sales": sales,
        "Discount": discount
    }
    
    prediction = pipeline.predict([input_data])
    
    st.metric("Estimated Profit", f"${float(prediction[0]):,.2f}")