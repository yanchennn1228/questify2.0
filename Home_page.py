# Home page for users to select Beginner or Regular
import streamlit as st

st.markdown("""
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {padding-top: 2rem;}
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(to top, #141E30, #243B55);
        color: white;
    }
    h1, h2, h3 {
        text-align: center;
    }
    div.stButton > button {
        width: 100%;
        height: 80px;
        font-size: 26px;
        font-weight: 700;
        border-radius: 14px;
        border: none;
        background-color: #1f1f1f;
        color: white;
        box-shadow: 0 0 15px rgba(255,255,255,0.15);
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #2e2e2e;
        box-shadow: 0 0 25px rgba(255,255,255,0.3);
    }
</style>
""", unsafe_allow_html=True)

st.title("🏋️ Welcome to Questify!")
st.markdown("<h3 style='text-align:center; color:#aab4c8;'>ActiveSG Gym Check-In</h3>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.write("Please select your user type to proceed:")

col1, col2 = st.columns(2)

with col1:
    if st.button("🌱 BEGINNER", key="beginner_btn", use_container_width=True):
        st.switch_page("pages/1_Beginners_Interface.py")

with col2:
    if st.button("🔥 REGULAR", key="regular_btn", use_container_width=True):
        st.switch_page("pages/2_Regulars_Interface.py")

if st.button("Return Wristband"):
    st.switch_page("pages/4_Return_Wristband.py")
