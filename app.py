import streamlit as st
import pandas as pd
import pickle

# load trained model
model = pickle.load(open("model.pkl","rb"))

st.title("Stock Valuation Prediction App")
st.write("""
This application predicts whether a stock is **Undervalued** or **Overvalued**
based on financial indicators such as Assets, Net Income, Liabilities,
Debt Ratio, CPI, Unemployment Rate, and Stock Price.
""")


st.write("Predict whether a stock is Undervalued or Overvalued")

year = st.number_input("Year",2010,2035,2024)
assets = st.number_input("Assets")
netincome = st.number_input("Net Income")
liabilities = st.number_input("Liabilities")
debt = st.number_input("Debt Ratio")
cpi = st.number_input("CPI")
unrate = st.number_input("Unemployment Rate")
close = st.number_input("Stock Price")

if st.button("Predict"):

    data = pd.DataFrame([[year,assets,netincome,liabilities,debt,cpi,unrate,close]],
    columns=[
    "year",
    "Assets",
    "NetIncomeLoss",
    "Liabilities",
    "DebtRatio",
    "CPIAUCSL",
    "UNRATE",
    "Close"
    ])

    prediction = model.predict(data)

    st.subheader("Prediction Result")

    if prediction[0] == "Undervalued":
        st.success("Stock is UNDERVALUED")
    else:
        st.error("Stock is OVERVALUED")
