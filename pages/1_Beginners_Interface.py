import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Beginner Check-In", page_icon="💪", layout="centered")

st.markdown("""
<style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {padding-top: 1rem;}

    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }

    h1, h2, h3 { text-align: center; }

    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(255,255,255,0.08) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        border-radius: 10px !important;
    }

    div.stButton > button {
        width: 100%;
        height: 55px;
        font-size: 22px;
        font-weight: 700;
        border-radius: 14px;
        border: none;
        background: linear-gradient(to right, #6a11cb, #2575fc);
        color: white;
        box-shadow: 0 0 20px rgba(101, 17, 203, 0.5);
        transition: all 0.3s ease;
        margin-top: 10px;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 30px rgba(101, 17, 203, 0.8);
    }

    .card {
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 16px;
        padding: 20px 25px;
        margin: 15px 0;
        backdrop-filter: blur(10px);
    }

    .wristband {
        display: inline-block;
        padding: 12px 40px;
        border-radius: 50px;
        font-size: 28px;
        font-weight: bold;
        letter-spacing: 3px;
        box-shadow: 0 0 25px currentColor;
        margin: 10px auto;
    }

    .tip-box {
        background: rgba(255,255,255,0.05);
        border-left: 4px solid #6a11cb;
        border-radius: 8px;
        padding: 12px 16px;
        margin-top: 8px;
        font-size: 14px;
        color: #ccc;
    }

    .confirm-card {
        background: linear-gradient(135deg, rgba(106,17,203,0.3), rgba(37,117,252,0.3));
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
    }

    .detail-row {
        display: flex;
        justify-content: space-between;
        padding: 8px 0;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# ── Workout config ───────────────────────────────────────
workout_config = {
    "Chest/Shoulder": {
        "colour": "#FF4B4B",
        "zone": "Free Weights",
        "emoji": "💪",
        "tip": "Great choice for beginners! Start with light weights and focus on form. Chest press, shoulder press, and tricep pushdowns are perfect starting points.",
    },
    "Back/Biceps": {
        "colour": "#2ECC71",
        "zone": "Machines",
        "emoji": "🏋️",
        "tip": "Machines are ideal for beginners — they guide your movement safely. Try the lat pulldown, seated row, and bicep curl machine.",
    },
    "Legs": {
        "colour": "#3498DB",
        "zone": "Squat Racks",
        "emoji": "🦵",
        "tip": "Focus on bodyweight squats first before adding weight. Lunges and leg press are also great beginner-friendly exercises.",
    },
    "Cardio": {
        "colour": "#F1C40F",
        "zone": "Cardio Zone",
        "emoji": "🔥",
        "tip": "A cardio workout is great for building a base! Combine simple compound movements like squats, rows, and presses with some light cardio.",
    },
}

# ── Header ───────────────────────────────────────────────
st.markdown("""
<div style='text-align:center; padding: 10px 0 5px 0;'>
    <span style='font-size:60px;'>💪</span>
    <h1 style='margin:0; font-size:36px; background: linear-gradient(to right, #a78bfa, #60a5fa);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
        WELCOME BEGINNERS
    </h1>
</div>
""", unsafe_allow_html=True)

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if not st.session_state.submitted:

    # Personal details
    
    st.markdown("#### 👤 Personal Details")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name", placeholder="e.g. Jane Doe")
    with col2:
        gym_id = st.text_input("GYM ID", placeholder="e.g. GYM-1234")
    st.markdown("</div>", unsafe_allow_html=True)

    # Workout details
    st.markdown("#### 🏋️ Workout Details")
    workout = st.selectbox("Workout Type", list(workout_config.keys()))

    config = workout_config[workout]
    gym_zone = config["zone"]

    # Live beginner tip
    st.markdown(f"""
    <div class='tip-box'>
        {config['emoji']} <strong>Beginner Tip:</strong> {config['tip']}<br><br>
        📍 <strong>Your Assigned Zone:</strong> {gym_zone}
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Timing
    st.markdown("#### ⏱️ Session Timing")
    col3, col4 = st.columns(2)
    with col3:
        start_time = st.time_input("Start Time", value=datetime.now().time())
    with col4:
        duration = st.slider("Duration (minutes)", 15, 180, 60, step=15)

    start_dt = datetime.combine(datetime.today(), start_time)
    end_dt = start_dt + timedelta(minutes=duration)
    st.markdown(f"""
    <p style='text-align:center; color:#aaa; margin-top:8px;'>
        🕐 Session: <strong style='color:white'>{start_time.strftime('%I:%M %p')}</strong>
        → <strong style='color:white'>{end_dt.strftime('%I:%M %p')}</strong>
        &nbsp;|&nbsp; ⏳ <strong style='color:white'>{duration} min</strong>
    </p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    workout_zone_map = {
    "Chest/Shoulder": "Free Weights",
    "Back/Biceps": "Machines",
    "Legs": "Squat Racks",
    "Cardio": "Cardio Zone"
}
gym_zone = workout_zone_map[workout]
st.title('Wristband Colour:')    
workout_colour_map = {
    "Chest/Shoulder": "Red",
    "Back/Biceps": "Green",
    "Legs": "Blue",
    "Cardio": "Yellow"
}
if workout == "Chest/Shoulder":
    wristband_colour = workout_colour_map.get(workout, "Red")
elif workout == "Back/Biceps":
    wristband_colour = workout_colour_map.get(workout, "Green")
elif workout == "Legs":
    wristband_colour = workout_colour_map.get(workout, "Blue")
elif workout == "Cardio":
    wristband_colour = workout_colour_map.get(workout, "Yellow")

st.markdown(
    f"""
    <div style="
        color:{wristband_colour};
        font-weight:bold;
        font-size:50px;
        text-align: center
    ">
        {wristband_colour}
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(f"""
<div style="
    background-color: #1f1f1f;
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    color: white;
    box-shadow: 0 0 25px {wristband_colour};
    border: 2px solid {wristband_colour};
    transition: 0.3s;
    width: auto
">
    🏢 Assigned Zone: {gym_zone}
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* Premium Kiosk Submit Button */
div.stButton > button {
    width: 100%;
    height: 50px;
    font-size: 30px;
    font-weight: 700;
    border-radius: 14px;
    border: none;
    background-color: #1f1f1f;   
    color: white;
    box-shadow: 0 0 15px rgba(255,255,255,0.15);
    transition: all 0.3s ease;
}


</style>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Submit"):
    if not name or not gym_id:
        st.error("⚠️ Please fill in your Full Name and GYM ID before submitting.")
    else:
        st.switch_page("pages/3_Wristband_Pairing.py")

st.markdown("<br>", unsafe_allow_html=True)
if st.button("⬅️ Back to Home"):
    st.switch_page("Home_page.py")
