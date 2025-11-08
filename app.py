import streamlit as st

# streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube & fifth power")

# Get user input
n = st.number_input("enter an integer: ", value =1, step=1)

# calculate results
square = n**2
cube = n**3
fifth_power = n**5

# Display the results
st.write(f"The square fo {n} is : {square}")
st.write(f"The cube fo {n} is : {cube}")
st.write(f"The fifth_power fo {n} is : {fifth_power}")