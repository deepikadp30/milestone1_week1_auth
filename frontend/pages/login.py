import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000"

# Page title
st.set_page_config(page_title="Login Page", layout="centered")
st.title("🔑 Login Page")

# Session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.profile = None

# If user is already logged in → show profile page
if st.session_state.logged_in:
    st.success(f"Welcome, {st.session_state.profile['username']}! 🎉")

    st.subheader("👤 Profile Details")
    st.write(f"🆔 ID: {st.session_state.profile['id']}")
    st.write(f"📧 Email: {st.session_state.profile['email']}")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.profile = None
        st.rerun()

else:
    # Login form
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            # Call FastAPI backend
            response = requests.post(
                f"{API_URL}/login",
                params={"username": username, "password": password}
            )

            if response.status_code == 200:
                st.session_state.logged_in = True
                st.session_state.profile = response.json()
                st.rerun()  # refresh page to show profile
            else:
                st.error("❌ Invalid username or password")
