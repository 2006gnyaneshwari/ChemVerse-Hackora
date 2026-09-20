import streamlit as st
import random
import time

st.set_page_config(page_title="ChemVerse - Virtual Lab", page_icon="🧪", layout="wide")

lang = st.sidebar.selectbox("Language / ಭಾಷೆ / भाषा", ["English", "ಕನ್ನಡ", "हिन्दी"])
T = {
 "English": {"title":"🧪 ChemVerse - Lab for Every School","sub":"No chemicals. No risk. Just pure science.","react":"Do Reaction","quiz":"Quiz Mode","cert":"Get Certificate"},
 "ಕನ್ನಡ": {"title":"🧪 ಕೆಮ್‌ವರ್ಸ್ - ಪ್ರತಿ ಶಾಲೆಗೂ ಒಂದು ಲ್ಯಾಬ್","sub":"ರಾಸಾಯನಿಕವಿಲ್ಲ. ಅಪಾಯವಿಲ್ಲ. ಶುದ್ಧ ವಿಜ್ಞಾನ.","react":"ಪ್ರತಿಕ್ರಿಯೆ ಮಾಡಿ","quiz":"ಕ್ವಿಜ್ ಮೋಡ್","cert":"ಪ್ರಮಾಣಪತ್ರ ಪಡೆಯಿರಿ"},
 "हिन्दी": {"title":"🧪 केमवर्स - हर स्कूल के लिए लैब","sub":"कोई केमिकल नहीं। कोई खतरा नहीं। सिर्फ विज्ञान।","react":"प्रतिक्रिया करो","quiz":"क्विज़ मोड","cert":"प्रमाणपत्र प्राप्त करें"}
}[lang]

st.markdown(f"# {T['title']}\n### {T['sub']}")
st.markdown("---")

reactions = {
    "Sodium + Water (Highly Reactive!)": {"eq": "2Na + 2H2O → 2NaOH + H2 ↑ + 🔥", "color": "#ff8c00", "effect": "fire", "info": "Most reactive metal - stored in kerosene!"},
    "Limestone Heating (Decomposition)": {"eq": "CaCO3 --heat--> CaO + CO2 ↑", "color": "#f0f0f0", "effect": "bubbles", "info": "Thermal Decomposition - you asked earlier"},
    "Silver Chloride (Photo Decomposition)": {"eq": "2AgCl --sunlight--> 2Ag + Cl2", "color": "#c0c0c0", "effect": "smoke", "info": "Least reactive? No, but light sensitive"},
    "Mercury + Acid (Hg = Hydrargyrum)": {"eq": "Hg + 4HNO3 → Hg(NO3)2 + 2NO2 + 2H2O", "color": "#d9d9d9", "effect": "smoke", "info": "Hg = Liquid Silver - only liquid metal"},
    "Water Electrolysis": {"eq": "2H2O --electricity--> 2H2 + O2", "color": "#87ceeb", "effect": "bubbles", "info": "Current flows fastest in Silver, then Copper"},
}

col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader(f"🧫 {T['react']}")
    choice = st.selectbox("Select Reaction:", list(reactions.keys()))
    r = reactions[choice]
    if st.button(f"🔬 START {T['react'].upper()}", use_container_width=True):
        st.balloons()
        beaker = st.empty()
        for i in range(6):
            h = 15 + i*14
            emoji = "🔥" if r['effect']=='fire' else "🫧" if r['effect']=='bubbles' else "💨"
            beaker.markdown(f"""
            <div style='height:220px; width:160px; border:4px solid #222; border-radius:0 0 25px 25px; margin:auto; position:relative; overflow:hidden; background:white; box-shadow: 0 10px 20px rgba(0,0,0,0.2);'>
                <div style='position:absolute; bottom:0; width:100%; height:{h}%; background:{r['color']}; transition:0.4s;'></div>
                <div style='position:absolute; top:{50-i*5}%; width:100%; text-align:center; font-size:{30+i*3}px;'>{emoji}</div>
            </div>
            """, unsafe_allow_html=True)
            time.sleep(0.25)
        st.success(f"**Equation:** `{r['eq']}`")
        st.info(f"**Concept:** {r['info']}")

# --- FIXED QUIZ - No more bug ---
with col2:
    st.subheader(f"🧠 {T['quiz']}")
    if "quiz_q" not in st.session_state:
        st.session_state.quiz_q = random.choice([
            {"q":"Current flows fastest in which element?","o":["Copper","Silver","Gold","Aluminium"],"a":"Silver"},
            {"q":"Hg full form?","o":["Hydrargyrum","Hydrogenium","High Gas","Hard Glue"],"a":"Hydrargyrum"},
            {"q":"Least reactive element?","o":["Na","Ne","F","K"],"a":"Ne"},
            {"q":"Decomposition by sunlight?","o":["Thermal","Photo","Electro","All"],"a":"Photo"},
            {"q":"Only liquid metal at room temp?","o":["Na","Hg","Br","Fe"],"a":"Hg"},
        ])
    q = st.session_state.quiz_q
    st.write(f"**Q: {q['q']}**")
    ans = st.radio("Choose:", q['o'], key="ans", label_visibility="collapsed")

    c1, c2 = st.columns(2)
    if c1.button(T['cert'], use_container_width=True):
        if ans == q['a']:
            st.success("✅ Correct!")
            st.markdown(f"""
            <div style='border:3px double green; padding:20px; text-align:center; background:#f0fff0;'>
                <h2>🏆 CHEMVERSE CERTIFICATE</h2>
                <p>Awarded for Excellence in Virtual Chemistry</p>
                <p><b>Topic: {choice}</b></p>
                <p>Question: {q['q']} = {q['a']}</p>
                <p>HACKORA 2026 - Team of 2 - Dod Ballapur</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error(f"Wrong! Correct is {q['a']}")
    if c2.button("Next Question", use_container_width=True):
        del st.session_state.quiz_q
        st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("**Conductivity Ranking (Your Q):**\n1. Silver (100%)\n2. Copper (97%)\n3. Gold (76%)\n4. Al (60%)")
st.sidebar.markdown("**Team:**\n- Dev 1: Builder\n- Dev 2: Pitch")
st.sidebar.caption("Pitch: *We built a lab for every school that doesn't have one.*")