import streamlit as st
import random
import time

# पेज सेटअप - बिल्कुल प्रो ऐप जैसा
st.set_page_config(page_title="MAHESH GAME ZONE", layout="wide", initial_sidebar_state="collapsed")

# स्टाइलिंग (Professional Dark Theme)
st.markdown("""
    <style>
    .main { background: linear-gradient(180deg, #1a1a1d 0%, #000000 100%); color: white; }
    .stButton>button { background: linear-gradient(90deg, #ff4b2b, #ff416c); color: white; border: none; border-radius: 10px; font-weight: bold; }
    .game-box { border: 1px solid #333; padding: 15px; border-radius: 15px; background: #252525; text-align: center; margin-bottom: 20px; }
    .balance-box { background: #333; padding: 10px; border-radius: 50px; text-align: center; border: 1px solid gold; color: gold; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

# डेटाबेस (बैलेंस)
if 'balance' not in st.session_state:
    st.session_state.balance = 100

# --- हैडर ---
st.markdown("<h1 style='text-align: center; color: white;'>🎰 MAHESH 66 LOTTERY 🎰</h1>", unsafe_allow_html=True)
st.markdown(f"<div class='balance-box'>💰 वॉलेट बैलेंस: ₹{st.session_state.balance}</div>", unsafe_allow_html=True)
st.write("##")

# --- एडमिन पैनल (SIDEBAR) ---
with st.sidebar:
    st.header("👑 Admin Panel")
    pin = st.text_input("Secret PIN", type="password")
    if pin == "7860":
        amt = st.number_input("Add Money", step=100)
        if st.button("Update Now"):
            st.session_state.balance += amt
            st.success("Balance Added!")
            st.rerun()

# --- गेम्स का ग्रिड (जैसे आपकी फोटो में था) ---
st.write("### 🔥 शीर्ष खेल (Top Games)")
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="game-box">', unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/aviator-background-with-airplane_1017-43224.jpg", use_container_width=True)
    if st.button("🚀 AVIATOR (PLAY)"):
        st.session_state.active_game = "aviator"
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="game-box">', unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/casino-glitter-banner_1017-23116.jpg", use_container_width=True)
    if st.button("🎰 SATTA KING (PLAY)"):
        st.session_state.active_game = "satta"
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# --- असली गेम लॉजिक (यही गेम खोलेंगे) ---
if 'active_game' in st.session_state:
    if st.session_state.active_game == "aviator":
        st.subheader("🛫 Aviator Live")
        bet = st.number_input("बैट की रकम", min_value=10, step=10)
        if st.button("Start Flight"):
            if st.session_state.balance < bet:
                st.error("Balance Low!")
            else:
                st.session_state.balance -= bet
                placeholder = st.empty()
                crash = round(random.uniform(1.2, 5.0), 2)
                curr = 1.0
                while curr < crash:
                    curr += 0.1
                    placeholder.metric("Multiplier", f"{round(curr, 2)}x")
                    time.sleep(0.2)
                    if st.button("CASH OUT"):
                        st.session_state.balance += (bet * curr)
                        st.success(f"Winner! Received: ₹{round(bet*curr, 2)}")
                        break
                else:
                    placeholder.error(f"💥 CRASHED AT {crash}x")

    elif st.session_state.active_game == "satta":
        st.subheader("🎲 Satta King (1-10)")
        s_bet = st.number_input("Bet Amount", min_value=10, key="satta_bet")
        num = st.number_input("Choose Number (1-10)", 1, 10)
        if st.button("Show Result"):
            if st.session_state.balance < s_bet:
                st.error("Low Balance!")
            else:
                win_n = random.randint(1, 10)
                if num == win_n:
                    st.session_state.balance += (s_bet * 9)
                    st.balloons()
                    st.success(f"Winner! Number was {win_n}")
                else:
                    st.session_state.balance -= s_bet
                    st.error(f"Lost! Number was {win_n}")

# --- रिचार्ज सेक्शन ---
st.write("---")
with st.expander("💳 रिचार्ज / Deposit"):
    st.write("UPI ID: **8824558142-2@ibl**")
    st.markdown('<a href="https://wa.me/918824558142"><button style="width:100%; background:green; color:white; border-radius:10px; padding:10px;">व्हाट्सएप पर स्क्रीनशॉट भेजें</button></a>', unsafe_allow_html=True)
