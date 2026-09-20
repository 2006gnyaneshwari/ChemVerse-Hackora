import streamlit as st
import time
import random

st.set_page_config(page_title="ChemVerse - Lab for Every School", page_icon="🧪", layout="wide")

# --- LANGUAGES ---
LANG = {
    "English": {"select": "Select Experiment", "start": "🧪 START REACTION", "equation": "Equation", "obs": "Observation", "risk": "Safety", "quiz": "Take Quiz", "certificate": "Get Certificate"},
    "Kannada": {"select": "ಪ್ರಯೋಗ ಆಯ್ಕೆಮಾಡಿ", "start": "🧪 ಪ್ರತಿಕ್ರಿಯೆ ಪ್ರಾರಂಭಿಸಿ", "equation": "ಸಮೀಕರಣ", "obs": "ವೀಕ್ಷಣೆ", "risk": "ಸುರಕ್ಷತೆ", "quiz": "ರಸಪ್ರಶ್ನೆ", "certificate": "ಪ್ರಮಾಣಪತ್ರ"},
    "Hindi": {"select": "प्रयोग चुनें", "start": "🧪 प्रतिक्रिया शुरू करें", "equation": "समीकरण", "obs": "अवलोकन", "risk": "सुरक्षा", "quiz": "क्विज़ लें", "certificate": "प्रमाण पत्र"}
}

# --- 6 EXPERIMENTS ---
REACTIONS = {
    "Sodium + Water (Highly Reactive!) 🔥": {
        "equation": "2Na + 2H₂O → 2NaOH + H₂ ↑",
        "obs": "Sodium floats, moves rapidly, fizzes violently and catches fire. Highly Exothermic! Produces Hydrogen gas which burns with pop sound. Temp > 100°C.",
        "risk": "🔴 HIGH RISK - Never try without teacher. Burns skin.",
        "emoji": "🔥💥", "color": "orange"
    },
    "Acid + Base - Neutralization 🧫": {
        "equation": "HCl + NaOH → NaCl + H₂O + Heat",
        "obs": "pH changes from 1 (acid) to 7 (neutral). Solution becomes warm. Salt water formed. Indicator turns from pink to colorless. Most important reaction in daily life.",
        "risk": "🟢 SAFE - Neutralization removes acidity",
        "emoji": "💧", "color": "green"
    },
    "Copper Sulphate + Iron (Displacement) 🔵➡️🟤": {
        "equation": "CuSO₄ (blue) + Fe → FeSO₄ (green) + Cu (brown)",
        "obs": "Blue colour fades to light green! Iron nail gets copper coating. Fe is more reactive than Cu. This proves reactivity series. 5 min process.",
        "risk": "🟢 SAFE - Classic Class 10th experiment",
        "emoji": "🔵➡️🟤", "color": "blue"
    },
    "Baking Soda + Vinegar (CO₂ Fountain) 🎈": {
        "equation": "NaHCO₃ + CH₃COOH → CO₂ ↑ + H₂O + CH₃COONa",
        "obs": "Massive bubbling! CO₂ gas produced inflates balloon. Used in baking, fire extinguisher, volcano model. Lime water turns milky with this gas.",
        "risk": "🟢 VERY SAFE - Can do at home",
        "emoji": "🎈🫧", "color": "purple"
    },
    "Magnesium + HCl (Hydrogen Test) ✨": {
        "equation": "Mg + 2HCl → MgCl₂ + H₂ ↑ (Pop test)",
        "obs": "Magnesium ribbon disappears with fast bubbles. Hydrogen gas burns with 'pop' sound. Fastest reaction in syllabus. Light white precipitate.",
        "risk": "🟡 MEDIUM - H₂ is flammable, wear goggles",
        "emoji": "💨✨", "color": "silver"
    },
    "Limestone Test - Acid Test for Carbonate 🪨": {
        "equation": "CaCO₃ + 2HCl → CaCl₂ + CO₂ ↑ + H₂O",
        "obs": "Limestone chips fizz heavily! Same reaction in caves formation. CO₂ turns lime water milky - confirmatory test for carbonate rocks.",
        "risk": "🟢 SAFE - Geologists use this daily",
        "emoji": "🪨💨", "color": "yellow"
    }
}

# --- SIDEBAR ---
with st.sidebar:
    st.title("🧪 ChemVerse")
    st.markdown("**Lab for Every School**")
    lang_choice = st.selectbox("Language / ಭಾಷೆ / भाषा", ["English", "Kannada", "Hindi"])
    t = LANG[lang_choice]
    st.divider()
    st.info(f"Total Experiments: **{len(REACTIONS)}**\n\nWorks on any phone!\nNo chemicals needed.")
    st.divider()
    st.markdown("**Tech:** Python + Streamlit\n**For:** Rural Schools")

# --- MAIN ---
st.title("🧪 ChemVerse - Lab for Every School")
st.caption("No chemicals. No risk. Just pure science. | ರಾಸಾಯನಿಕಗಳಿಲ್ಲ, ಅಪಾಯವಿಲ್ಲ | कोई केमिकल नहीं, कोई खतरा नहीं")
st.divider()

col1, col2 = st.columns([1, 1.5])

with col1:
    st.subheader(f"1️⃣ {t['select']}")
    selected = st.selectbox("Choose", list(REACTIONS.keys()), label_visibility="collapsed")
    data = REACTIONS[selected]

    st.markdown(f"### {t['equation']}")
    st.code(data['equation'], language="chemistry")

    st.markdown(f"### {t['risk']}")
    if "HIGH" in data['risk']:
        st.error(data['risk'])
    elif "MEDIUM" in data['risk']:
        st.warning(data['risk'])
    else:
        st.success(data['risk'])

with col2:
    st.subheader("2️⃣ Reaction Chamber")
    st.markdown(f"<div style='background-color:#f0f2f6; padding:30px; border-radius:15px; text-align:center; border: 2px dashed {data['color']};'><h1 style='font-size:60px;'>{data['emoji']}</h1><p>Ready to react: <b>{selected}</b></p></div>", unsafe_allow_html=True)
    st.write("")
    if st.button(t['start'], use_container_width=True, type="primary"):
        with st.status(f"Reacting {selected}...", expanded=True) as status:
            st.write("Mixing chemicals...")
            time.sleep(0.8)
            st.write("Observing reaction...")
            bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                bar.progress(i+1)
            time.sleep(0.5)
            status.update(label="Reaction Complete! ✅", state="complete", expanded=False)

        st.balloons()
        st.success(f"**{t['obs']}:** {data['obs']}")
        st.toast(f"Reaction Success: {selected}", icon="🧪")

st.divider()

# --- BONUS SECTIONS FOR JUDGES ---
c1, c2 = st.columns(2)
with c1:
    with st.expander("📊 Q? Conductivity Ranking (Why Silver > Copper?) - Click to Show Judges"):
        st.markdown("""
        **Top Conductors:**
        1. **Silver (Ag) - 100%** - Best, but costly
        2. **Copper (Cu) - 97%** - Used in all wires (cheap + best)
        3. **Gold (Au) - 76%** - Never rusts, used in satellites
        4. **Aluminium (Al) - 61%** - Light, used in overhead lines

        **Concept Taught:** Conductivity depends on free electrons!
        """)

with c2:
    with st.expander(f"🎯 {t['quiz']} - Interactive"):
        q = st.radio("Which is the only liquid metal at room temp?", ["Iron", "Mercury (Hg)", "Sodium", "Gold"])
        if st.button("Submit Answer"):
            if q == "Mercury (Hg)":
                st.success("Correct! Hg is liquid! You earned a Certificate 🎓")
                st.markdown(f"### {t['certificate']}")
                st.code(f"Certificate of Excellence\nAwarded to: Science Explorer\nFor completing ChemVerse Lab\nDate: 2026", language="text")
                st.balloons()
            else:
                st.error("Try again! Hint: Thermometers use it...")

st.markdown("<center><small>Built for Hackathon | 1 Link = Lab for 10,000 Schools | No chemicals needed</small></center>", unsafe_allow_html=True)
