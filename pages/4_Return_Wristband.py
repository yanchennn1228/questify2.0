import streamlit as st
import sys
import os

# Allow importing wristband_store from parent directory
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from wristband_store import load_wristbands, save_wristbands

st.markdown("""
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {padding-top: 1rem;}
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    .stApp {
    background: linear-gradient(to top, #141E30, #0B5FE8);
    color: white;
    }
    h1, h2, h3 {
        text-align: center;
    }
    div.stButton > button {
        width: 100%;
        height: 50px;
        font-size: 20px;
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

st.title("🔄 Return Wristband")
st.write("Select the wristband number you are returning:")

numbers = list(range(1, 31))
taken = load_wristbands()

if not taken:
    st.info("ℹ️ No wristbands are currently checked out.")
else:
    # Only show numbers that are currently taken
    choice = st.selectbox("Select wristband number to return:", sorted(taken))

    # Preview status
    st.markdown(
        f"""
        <div style="
            background-color: #1f1f1f;
            padding: 20px;
            border-radius: 16px;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            color: white;
            border: 2px solid #4CAF50;
            box-shadow: 0 0 20px #4CAF50;
            margin: 16px 0;
        ">
            Wristband #{choice} — Currently Checked Out
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("🎟️ Return & Dispense Token"):
        taken = load_wristbands()  # re-read before modifying
        if choice in taken:
            taken.remove(choice)
            save_wristbands(taken)
            st.success(f"✅ Wristband #{choice} returned! Your token has been dispensed. Thank you!")
            st.balloons()
            st.rerun()
        else:
            st.error("❌ This wristband was already returned or not checked out.")

st.markdown("<br>", unsafe_allow_html=True)
if st.button("⬅️ Back to Home"):
    st.switch_page("Home_page.py")
