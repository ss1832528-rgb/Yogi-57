import streamlit as st
import random
import time

# पेज सेटिंग
st.set_page_config(page_title="MAHESH AVIATOR ZONE", layout="wide")

# डेटाबेस (बैलेंस)
if 'balance' not in st.session_state:
    st.session_state.balance = 50 # शुरुआती बैलेंस

# --- स्टाइलिंग ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #ff4b4b; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- हैडर ---
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🚀 MAHESH AVIATOR ZONE 🚀</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>💰 वॉलेट बैलेंस: ₹{st.session_state.balance}</h3>", unsafe_allow_html=True)

# --- एडमिन पैनल (साइडबार) ---
with st.sidebar:
    st.header("👑 एडमिन पैनल")
    pin = st.text_input("सीक्रेट पिन", type="password")
    if pin == "7860":
        amt = st.number_input("बैलेंस ऐड करें", step=50)
        if st.button("Update Balance"):
            st.session_state.balance += amt
            st.success("बैलेंस जुड़ गया!")
            st.rerun()

# --- गेम सेलेक्शन (ग्रिड) ---
st.write("### 🔥 लोकप्रिय खेल (Popular Games)")
c1, c2 = st.columns(2)

with c1:
    # एविएटर की वर्किंग फोटो
    st.image("https://raw.githubusercontent.com/Yogi-57/ss1832528-rgb/main/aviator_img.jpg", caption="AVIATOR CRASH", use_container_width=True)
    if st.button("AVIATOR खेलें"):
        st.session_state.game = "aviator"

with c2:
    st.image("https://img.freepik.com/free-vector/casino-banner-design_1017-23117.jpg", caption="SATTA KING", use_container_width=True)
    if st.button("SATTA KING खेलें"):
        st.session_state.game = "satta"

st.write("---")

# --- एविएटर गेम चालू करना ---
if 'game' in st.session_state and st.session_state.game == "aviator":
    st.subheader("🛫 Aviator (Live)")
    bet = st.number_input("बैट की रकम (₹)", min_value=10, step=10)
    
    if st.button("🚀 उड़ाएं (Start Flight)"):
        if st.session_state.balance < bet:
            st.error("भाई पहले रिचार्ज करो!")
        else:
            st.session_state.balance -= bet
            crash = round(random.uniform(1.1, 4.0), 2)
            val = 1.0
            p_holder = st.empty()
            
            while val < crash:
                val += 0.1
                p_holder.metric("Multiplier", f"{round(val, 2)}x")
                time.sleep(0.2)
                if st.button("CASH OUT NOW"): # कैश आउट का लॉजिक
                    win = bet * val
                    st.session_state.balance += win
                    st.success(f"मौज हो गई! ₹{round(win, 2)} जीत गए!")
                    break
            else:
                p_holder.error(f"💥 CRASHED AT {crash}x")
