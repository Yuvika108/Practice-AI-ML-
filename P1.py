## DAY - 1 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import streamlit as st

st.title("Hello, Streamlit!")
st.subheader("Welcome to your first Streamlit app.")
st.text("Streamlit makes it easy to create and share beautiful, custom web apps for machine learning and data science.")
st.write("This is a simple app to demonstrate Streamlit's capabilities.")

chai = st.selectbox("Choose your favorite chai flavor:", ["Masala Chai", "Ginger Chai", "Cardamom Chai", "Tulsi Chai"])
st.write(f"You chose: {chai}. \n\n Excellent choice! --> {chai} is delicious.")

## DAY - 2 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
st.title("Chai Maker App")

if st.button("Make Chai"):
    st.success("Your chai is being prepared! Enjoy your delicious cup of chai!")

extra_sugar = st.checkbox("Add extra sugar")
extra_milk = st.checkbox("Add extra milk")

if extra_sugar:
    st.write("Adding extra sugar to your chai!")

if extra_milk:
    st.write("Adding extra milk to your chai!")

tea_type = st.radio("Choose your tea base:", ["Milk", "Water", "Honey"])
st.write(f"You chose: {tea_type} as your tea base.")

flavor = st.selectbox("Choose your flavor", ["Adrak", "Elaichi", "Tulsi", "Masala"])
st.write(f"You chose: {flavor} flavor for your chai!")

sugar = st.slider("Select sugar level", 0, 5, 2)
st.write(f"You selected: {sugar} teaspoons of sugar for your chai.")

cups = st.number_input("How many cups of chai would you like?", min_value=1, max_value=10, value=1)
st.write(f"You want {cups} cup(s) of chai. \n\nGreat choice!")

name = st.text_input("Enter your name to personalize your chai:")
if name:
    st.write(f"Your chai is on the way, {name}!")

dob = st.date_input("Select your date of birth:")
st.write(f"You selected: {dob}. \n\nHappy Birthday in advance!")

## DAY - 3 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/16228436/pexels-photo-16228436/free-photo-of-a-table-with-a-tea-pot-and-a-candle-on-it.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="Masala Chai", width=200)
    vote1 = st.button("Vote for Masala Chai")

with col2:
    st.header("Ginger Chai")
    st.image("https://images.pexels.com/photos/16228436/pexels-photo-16228436/free-photo-of-a-table-with-a-tea-pot-and-a-candle-on-it.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="Ginger Chai", width=200)
    vote2 = st.button("Vote for Ginger Chai")

if vote1:
    st.success("Thanks for voting for Masala Chai!")
elif vote2:
    st.success("Thanks for voting for Ginger Chai!")

name = st.sidebar.text_input("Enter your name: ")
tea = st.sidebar.selectbox("Select your favorite tea:", ["Masala Chai", "Ginger Chai"])

st.write(f"{name} loves {tea}!")

with st.expander("Show Chai Making Instructions."):
    st.write("""
    1. Boil water and add tea leaves.
    2. Add spices (for Masala Chai) or ginger (for Ginger Chai).
    3. Let it simmer for a few minutes.
""")
    
st.markdown("### Welcome to the Chai App!")
st.markdown('> Blockquote ')
st.markdown("This app allows you to vote for your favorite chai and share your preferences. Enjoy your tea time! ☕")

## DAY - 4 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd

st.title("Chai Sale Dashboards")

file = st.file_uploader("Upload your Chai Sale CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df.head())

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())

if file:
    products = df['Product'].value_counts()
    selected_product = st.selectbox("Select a product to view sales", products.index)
    filtered_data = df[df['Product'] == selected_product]

    st.dataframe(filtered_data)
    st.subheader("Sales by Product")
    st.bar_chart(products)

## DAY - 5 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import requests

st.title("Live Currency Converter")
amt = st.number_input("Enter amount in INR", min_value=1)

target_currency = st.selectbox("Convert to", ["USD", "EUR", "GBP", "JPY"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][target_currency]

        if rate:
            converted_amt = amt * rate
            st.success(f"{amt} INR is approximately {converted_amt:.2f} {target_currency}")
        else:
            st.error("Currency not supported.")