import streamlit as st

st.title("👋 Interactive Greeting App")

# Text input for the user's name
name = st.text_input("Enter your name:")

# Button to trigger greeting
if st.button("Greet Me"):
    if name.strip() == "":
        st.warning("Please enter a valid name!")
    else:
        st.success(f"Hello, {name}! Welcome to the app 😊")