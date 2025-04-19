
import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔁")
st.title("🔁 Unit Converter - Temperature")

# Temperature units
units = ["Celsius", "Fahrenheit", "Kelvin"]

# User input
value = st.number_input("Enter the temperature value:", value=0.0)
from_unit = st.selectbox("From Unit:", units)
to_unit = st.selectbox("To Unit:", units)

def temp_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

# Conversion
if st.button("Convert"):
    result = temp_converter(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
