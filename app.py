
import streamlit as st
import random
import time

# पेज सेटिंग
st.set_page_config(page_title="MAHESH AVIATOR ZONE", layout="wide")

# डेटाबेस (बैलेंस और गेम स्टेट)
if 'balance' not in st.session_state:
    st.session_state.balance = 0
if 'multiplier' not in st.session_state:
    st.session_state.multiplier = 1.0

# --- स्टाइलिंग (फोटो जैसा दिखने के लिए) ---
st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: white; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #ff4b4b; color: white; }
    .game-card { border: 1px solid #444; padding: 10px; border-radius: 15px; text-align: center; background: #262626; }
    </style>
    """, unsafe_allow_html=True)

# --- हैडर और बैलेंस ---
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🚀 MAHESH AVIATOR ZONE 🚀</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>💰 वॉलेट बैलेंस: ₹{st.session_state.balance}</h3>", unsafe_allow_html=True)

# --- एडमिन पैनल (साइडबार) ---
with st.sidebar:
    st.header("👑 एडमिन कंट्रोल")
    pin = st.text_input("पिन डालें", type="password")
    if pin == "7860":
        add_money = st.number_input("पैसे जोड़ें", step=100)
        if st.button("बैलेंस अपडेट करें"):
            st.session_state.balance += add_money
            st.success("पैसे जुड़ गए!")
            st.rerun()

# --- मुख्य गेम ग्रिड (फोटो की तरह) ---
st.write("### 🔥 सभी गेम्स (All Games)")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="game-card">', unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/aviator-background-with-airplane_1017-43224.jpg", width=150)
    if st.button("AVIATOR (Live)"): st.session_state.game = "aviator"
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="game-card">', unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/casino-glitter-banner_1017-23116.jpg", width=150)
    if st.button("SATTA KING"): st.session_state.game = "satta"
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="game-card">', unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/colourful-wheel-fortune-concept_23-2148601831.jpg", width=150)
    if st.button("MINES"): st.session_state.game = "mines"
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# --- एविएटर गेम लॉजिक ---
if 'game' in st.session_state and st.session_state.game == "aviator":
    st.subheader("🛫 Aviator (Crash Game)")
    bet = st.number_input("अपनी बैट लगाएं (₹)", min_value=10, step=10)
    
    col_play, col_cashout = st.columns(2)
    
    if col_play.button("🚀 उड़ाएं (Start)"):
        if st.session_state.balance < bet:
            st.error("बैलेंस कम है!")
        else:
            st.session_state.balance -= bet
            crash_point = round(random.uniform(1.0, 5.0), 2)
            current = 1.0
            placeholder = st.empty()
            
            for i in range(1, 100):
                current += 0.1
                if current >= crash_point:
                    placeholder.error(f"💥 CRASHED at {crash_point}x")
                    break
                placeholder.metric("Multiplier", f"{round(current, 2)}x")
                time.sleep(0.1)
                st.session_state.temp_mult = current
                
    if col_cashout.button("💰 Cash Out"):
        win = bet * st.session_state.get('temp_mult', 1.0)
        st.session_state.balance += win
        st.success(f"निकासी सफल! आप ₹{round(win, 2)} जीते।")
        st.rerun()

# --- पेमेंट सेक्शन ---
st.write("---")
with st.expander("💳 रिचार्ज (Add Money)"):
    st.write("UPI ID: 8824558142-2@ibl")
    st.markdown(f'<a href="https://wa.me/918824558142?text=भाई_रिचार्ज_करो"><button style="background:green;color:white;width:100%;border-radius:10px;">व्हाट्सएप पर स्क्रीनशॉट भेजें</button></a>', unsafe_allow_html=True)
    
