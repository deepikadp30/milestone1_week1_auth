import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Text Morph", page_icon="📝", layout="centered")

# --- Hero Section ---
st.title("📝 Text Morph")
st.subheader("Transform your text with AI-powered summarization and analysis")

st.markdown(
    """
    Welcome to **Text Morph** 🚀  
    A powerful AI application that lets you **summarize, transform, and analyze text** effortlessly.  
    Get started by creating your account or logging in below.  
    """
)

# --- Navigation ---
choice = st.radio("Navigation", ["🏠 Home", "🔑 Login", "📝 Sign Up"], horizontal=True)

# --- Home Section ---
if choice == "🏠 Home":
    st.image("https://cdn-icons-png.flaticon.com/512/2910/2910768.png", width=150)
    st.info("👉 Use the navigation above to **Sign Up** or **Login** and start using Text Morph.")

# --- Redirect to Login Page ---
elif choice == "🔑 Login":
    st.success("➡ Redirecting to Login Page...")
    st.switch_page("pages/login.py")

# --- Redirect to Signup Page ---
elif choice == "📝 Sign Up":
    st.success("➡ Redirecting to Sign Up Page...")
    st.switch_page("pages/signup.py")
