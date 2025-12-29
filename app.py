
import streamlit as st
import random

# पेज की सेटिंग
st.set_page_config(page_title="महेश मल्टी-गेम पैलेस", page_icon="🎰", layout="wide")

# डेटाबेस (बैलेंस)
if 'balance' not in st.session_state:
    st.session_state.balance = 0

# --- साइडबार मेनू (यहाँ से गेम बदलेंगे) ---
with st.sidebar:
    st.header("👑 महेश भाई (Admin)")
    pincode = st.text_input("एडमिन पिन डालें", type="password")
    if pincode == "7860":
        amount = st.number_input("बैलेंस बढ़ाएं/घटाएं", step=10)
        if st.button("बैलेंस अपडेट करें"):
            st.session_state.balance += amount
            st.success("बैलेंस अपडेट हो गया!")
            st.rerun()
    
    st.write("---")
    st.header("🎮 गेम चुनें")
    game_choice = st.radio("कौन सा गेम खेलना है?", ["सट्टा किंग (1-10)", "सिक्का उछालें (Heads/Tails)", "कलर प्रेडिक्शन (Red/Green)"])

# --- मुख्य वेबसाइट हैडर ---
st.markdown(f"<h1 style='text-align: center;'>🎰 {game_choice} 🎰</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center; color: gold;'>आपका बैलेंस: ₹{st.session_state.balance}</h3>", unsafe_allow_html=True)
st.write("---")

# --- पैसे जमा करने का बटन ---
with st.expander("💰 पैसे जमा करने के लिए यहाँ क्लिक करें"):
    st.write("UPI ID: 8824558142-2@ibl")
    wa_link = "https://wa.me/918824558142?text=भाई_पैसे_ऐड_करो"
    st.markdown(f'<a href="{wa_link}"><button style="background:green;color:white;padding:10px;width:100%;">व्हाट्सएप पर स्क्रीनशॉट भेजें</button></a>', unsafe_allow_html=True)

# ------------------------------------------------------------------
# गेम 1: सट्टा किंग
# ------------------------------------------------------------------
if game_choice == "सट्टा किंग (1-10)":
    bet = st.number_input("बाजी की रकम (₹)", min_value=10, step=10, key="bet1")
    guess = st.number_input("अपना नंबर चुनें (1-10)", min_value=1, max_value=10, key="guess1")
    
    if st.button("🎰 गेम शुरू करें"):
        if st.session_state.balance < bet:
            st.error("बैलेंस कम है!")
        else:
            win_num = random.randint(1, 10)
            st.info(f"नंबर निकला: {win_num}")
            if guess == win_num:
                st.session_state.balance += (bet * 9)
                st.balloons()
                st.success("बधाई हो! आप जीत गए!")
            else:
                st.session_state.balance -= bet
                st.error("आप हार गए।")

# ------------------------------------------------------------------
# गेम 2: सिक्का उछालें (Heads/Tails)
# ------------------------------------------------------------------
elif game_choice == "सिक्का उछालें (Heads/Tails)":
    bet = st.number_input("बाजी की रकम (₹)", min_value=10, step=10, key="bet2")
    side = st.selectbox("अपना पक्ष चुनें", ["Heads", "Tails"])
    
    if st.button("🪙 सिक्का उछालें"):
        if st.session_state.balance < bet:
            st.error("बैलेंस कम है!")
        else:
            result = random.choice(["Heads", "Tails"])
            st.info(f"नतीजा: {result}")
            if side == result:
                st.session_state.balance += bet
                st.success("जीत गए! पैसा डबल!")
            else:
                st.session_state.balance -= bet
                st.error("हार गए।")

# ------------------------------------------------------------------
# गेम 3: कलर प्रेडिक्शन
# ------------------------------------------------------------------
elif game_choice == "कलर प्रेडिक्शन (Red/Green)":
    bet = st.number_input("बाजी की रकम (₹)", min_value=10, step=10, key="bet3")
    color = st.selectbox("रंग चुनें", ["Red", "Green", "Violet"])
    
    if st.button("🎨 रिजल्ट देखें"):
        if st.session_state.balance < bet:
            st.error("बैलेंस कम है!")
        else:
            result = random.choice(["Red", "Green", "Violet"])
            st.info(f"रंग निकला: {result}")
            if color == result:
                st.session_state.balance += (bet * 2)
                st.success("सही अंदाजा! आप जीत गए!")
            else:
                st.session_state.balance -= bet
                st.error("गलत अंदाजा।")
