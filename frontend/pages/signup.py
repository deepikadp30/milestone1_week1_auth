# signup.py
import streamlit as st
import requests

st.title("🔑 Sign Up for TextMorph")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Sign Up"):
    if username and email and password:
        response = requests.post(
            "http://127.0.0.1:8000/signup",
            params={"username": username, "email": email, "password": password}
        )

        if response.status_code == 200:
            st.success("✅ Account created successfully! Please login.")
        else:
            st.error(f"❌ {response.json()['detail']}")
    else:
        st.warning("Please fill in all fields.")
