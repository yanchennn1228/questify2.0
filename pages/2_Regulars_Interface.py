import streamlit as st
from datetime import datetime

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
        background: linear-gradient(to top, #141E30, #243B55);
        color: white;
    }
    h1, h2, h3 {
        text-align: center;
    }
    div.stButton > button {
        width: 100%;
        height: 50px;
        font-size: 22px;
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

st.title("Welcome Regular! 🔥")
st.write("Please fill in the details below:")

name = st.text_input("Full Name:")
gym_id = st.text_input("GYM ID:")

st.write("Please choose your workout today:")
workout = st.selectbox("Workout Type:", ["Push", "Pull", "Legs", "Full Body"])
gym_zone = st.selectbox("Gym Zone:", ["Free Weights", "Squat Racks", "Machines", "Cardio Zone"])
start_time = st.time_input("Start Time:", value=datetime.now(), key="start_time")
duration = st.slider("Available for (minutes):", 15, 180, 60, step=15)

# Wristband colour
workout_colour_map = {
    "Push": "Red",
    "Pull": "Green",
    "Legs": "Blue",
    "Full Body": "Yellow",
}
wristband_colour = workout_colour_map[workout]

st.markdown("<br>", unsafe_allow_html=True)
st.title("Wristband Colour:")
st.markdown(
    f"""
    <div style="
        color:{wristband_colour};
        font-weight:bold;
        font-size:50px;
        text-align:center;
    ">
        {wristband_colour}
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div style="
        background-color: #1f1f1f;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: white;
        box-shadow: 0 0 25px {wristband_colour};
        border: 2px solid {wristband_colour};
        margin-top: 20px;
    ">
        🏢 Selected Zone: {gym_zone}
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Submit"):
    if not name or not gym_id:
        st.error("⚠️ Please fill in your Full Name and GYM ID before submitting.")
    else:
        st.success(f"✅ Welcome back {name}! Head to **{gym_zone}** and grab your **{wristband_colour}** wristband.")

st.markdown("<br>", unsafe_allow_html=True)
if st.button("⬅️ Back to Home"):
    st.switch_page("Home_page.py")
