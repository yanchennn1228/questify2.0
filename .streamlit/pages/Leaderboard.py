import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gym Leaderboard", layout="wide")

st.markdown("""
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {padding-top: 0rem;}
    </style>
""", unsafe_allow_html=True)



st.markdown("""
<style>
.stApp {
    /* Blue gradient background */
    background: linear-gradient(135deg, #1e3c72, #2a5298);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

h1, h2 { text-align: center; }

/* Circle section */
.circle-row { display: flex; justify-content: space-around; margin-bottom: 30px; }
.circle { width: 170px; height: 170px; border-radius: 50%; display: flex; flex-direction: column;
          align-items: center; justify-content: center; font-weight: bold; box-shadow: 0 0 15px rgba(255,255,255,0.2); }
.gold { background: linear-gradient(145deg,#FFD700,#ffcc00); color:black; }
.green { background: linear-gradient(145deg,#00c9a7,#00e6c3); color:black; }
.blue { background: linear-gradient(145deg,#3a7bd5,#00d2ff); color:black; }

/* Leaderboard rows */
.row { padding: 12px; border-radius: 12px; margin-bottom: 8px; display:flex; justify-content:space-between; }
.top1 { background: #FFD700; color:black; } 
.top2 { background: #C0C0C0; color:black; } 
.top3 { background:#CD7F32; color:black; } 
.normal { background:#1f2937; }
</style>
""", unsafe_allow_html=True)


st.title("🏆 GYM LEADERBOARD")

# --------------------------
# Data
# --------------------------
df = pd.DataFrame({
    "Name": ["Alex", "Jordan", "Chris", "Taylor", "Sam"],
    "Hours": [32, 27, 21, 18, 14],
    "Prev": [26,26,19,15,6],
    "Streak":[8,5,10,4,6]
})
df["Rank"] = df["Hours"].rank(ascending=False, method="first").astype(int)
df["Imp"] = df["Hours"] - df["Prev"]

top = df.loc[df["Hours"].idxmax()]
streak = df.loc[df["Streak"].idxmax()]
improve = df.loc[df["Imp"].idxmax()]

# --------------------------
# Circles in one horizontal row
# --------------------------
st.markdown(f"""
<div class="circle-row">
    <div class="circle gold">
        <div>👑 TOP PERFORMER</div>
        <div>{top['Name']}</div>
        <div>{top['Hours']} hrs</div>
    </div>
    <div class="circle green">
        <div>🔥 HIGHEST STREAK</div>
        <div>{streak['Name']}</div>
        <div>{streak['Streak']} days</div>
    </div>
    <div class="circle blue">
        <div>🚀 MOST IMPROVED</div>
        <div>{improve['Name']}</div>
        <div>+{improve['Imp']} hrs</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------------
# Top 5 leaderboard
# --------------------------
st.markdown("## 📊 Top 5 Rankings")
for _, r in df.sort_values("Rank").head(5).iterrows():
    style = "top1" if r["Rank"]==1 else "top2" if r["Rank"]==2 else "top3" if r["Rank"]==3 else "normal"
    st.markdown(f"<div class='row {style}'>#{r['Rank']} - {r['Name']}  {r['Hours']} hrs |🔥 {r['Streak']} days</div>" , unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
if st.button("⬅️ Back to Home"):
    st.switch_page("Home_page.py")
