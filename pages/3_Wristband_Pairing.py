import streamlit as st
import pandas as pd
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

st.title("🎽 Wristband Numbers")

numbers = list(range(1, 31))
taken = load_wristbands()

choice = st.selectbox("Input your wristband number according to the colour allocated:", numbers)

if st.button("✅ Confirm"):
    taken = load_wristbands()  # re-read to avoid race conditions
    if choice in taken:
        st.error(f"❌ Number {choice} is already taken! Please choose another.")
    else:
        taken.append(choice)
        save_wristbands(taken)
        st.success(f"✅ Number {choice} assigned!")
        st.rerun()

st.divider()

# Stats
taken = load_wristbands()
taken_count = len(taken)
available_count = len(numbers) - taken_count

col1, col2 = st.columns(2)
with col1:
    st.metric("✅ Available", available_count)
with col2:
    st.metric("❌ Taken", taken_count)

st.subheader("Number Status:")

# Build 6-row × 5-col grid
rows = []
for i in range(0, len(numbers), 5):
    row = []
    for num in numbers[i : i + 5]:
        if num in taken:
            row.append(f"❌ {num}")
        else:
            row.append(f"✅ {num}")
    rows.append(row)

df = pd.DataFrame(rows)
st.dataframe(
    df,
    hide_index=True,
    use_container_width=True,
    column_config={i: st.column_config.Column(label="", width="small") for i in df.columns},
)

st.markdown("<br>", unsafe_allow_html=True)
if st.button("⬅️ Back to Home"):
    st.switch_page("Home_page.py")
