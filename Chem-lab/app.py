import streamlit as st
import time
import random

st.set_page_config(page_title="ChemVerse - A Virtual Lab", page_icon="🧪", layout="wide")

# --- TITLE CHANGED AS YOU ASKED ---
st.markdown("""
<style>
.reaction-box {
    background: linear-gradient(135deg, #e0f7fa 0%, #ffffff 100%);
    padding: 30px; border-radius: 20px; text-align:center;
    border: 3px dashed #00acc1; min-height: 200px;
}
.beaker {
    display:inline-block; width:80px; height:100px;
    border:3px solid #333; border-radius: 0 0 20px 20px;
    margin:10px; line-height:100px; font-size:30px;
}
</style>
""", unsafe_allow_html=True)

# --- CHEMICALS ---
CHEMICALS = {
    "Sodium (Na)": {"emoji": "🟡", "type": "metal", "color": "#ffeb3b"},
    "Water (H₂O)": {"emoji": "💧", "type": "liquid", "color": "#03a9f4"},
    "Hydrochloric Acid (HCl)": {"emoji": "🧴", "type": "acid", "color": "#ffcc80"},
    "Sodium Hydroxide (NaOH)": {"emoji": "🧪", "type": "base", "color": "#f8bbd0"},
    "Copper Sulphate (CuSO₄)": {"emoji": "🔵", "type": "salt", "color": "#2196f3"},
    "Iron Nail (Fe)": {"emoji": "🔩", "type": "metal", "color": "#9e9e9e"},
    "Baking Soda (NaHCO₃)": {"emoji": "⚪", "type": "salt", "color": "#ffffff"},
    "Vinegar (CH₃COOH)": {"emoji": "🍶", "type": "acid", "color": "#dcedc8"},
    "Magnesium (Mg)": {"emoji": "✨", "type": "metal", "color": "#e0e0e0"},
    "Limestone (CaCO₃)": {"emoji": "🪨", "type": "carbonate", "color": "#fff9c4"},
}

# --- REACTION LOGIC ---
def get_reaction(c1, c2):
    combo = set([c1, c2])
    if combo == {"Sodium (Na)", "Water (H₂O)"}:
        return {"equation": "2Na + 2H₂O → 2NaOH + H₂ ↑ 🔥", "obs": "VIOLENT! Sodium floats, fizzes, catches fire! Exothermic, H₂ gas pop test. HIGHLY DANGEROUS in real lab!", "risk": "🔴 HIGH RISK", "anim": "🔥💥💨"}
    if combo == {"Hydrochloric Acid (HCl)", "Sodium Hydroxide (NaOH)"}:
        return {"equation": "HCl + NaOH → NaCl + H₂O + Heat", "obs": "Neutralization! Acid + Base = Salt + Water. pH becomes 7 (neutral). Solution becomes slightly warm. Indicator color disappears.", "risk": "🟢 SAFE", "anim": "💧➡️✨"}
    if combo == {"Copper Sulphate (CuSO₄)", "Iron Nail (Fe)"}:
        return {"equation": "CuSO₄ (blue) + Fe → FeSO₄ (green) + Cu (brown coating)", "obs": "DISPLACEMENT! Blue color fades to green! Iron gets copper coating. Fe is more reactive than Cu. Class 10 NCERT experiment.", "risk": "🟢 SAFE - Classic school experiment", "anim": "🔵➡️🟢 + 🟤"}
    if combo == {"Baking Soda (NaHCO₃)", "Vinegar (CH₃COOH)"}:
        return {"equation": "NaHCO₃ + CH₃COOH → CO₂ ↑ + H₂O + CH₃COONa", "obs": "CO₂ Fountain! Massive bubbling! Gas inflates balloon. CO₂ turns lime water milky. Used in volcano model & fire extinguisher.", "risk": "🟢 VERY SAFE - Home experiment", "anim": "🫧🎈💨"}
    if combo == {"Magnesium (Mg)", "Hydrochloric Acid (HCl)"}:
        return {"equation": "Mg + 2HCl → MgCl₂ + H₂ ↑ (Pop test)", "obs": "Magnesium disappears with fast bubbles! H₂ gas burns with POP sound. Fastest reaction. White salt left behind.", "risk": "🟡 MEDIUM - H₂ flammable", "anim": "✨💨💥"}
    if combo == {"Limestone (CaCO₃)", "Hydrochloric Acid (HCl)"}:
        return {"equation": "CaCO₃ + 2HCl → CaCl₂ + CO₂ ↑ + H₂O", "obs": "Limestone fizzes heavily! Test for carbonate rocks. Geologists use this. CO₂ turns lime water milky = confirmation.", "risk": "🟢 SAFE", "anim": "🪨💨🧪"}
    if combo == {"Limestone (CaCO₃)", "Vinegar (CH₃COOH)"}:
        return {"equation": "CaCO₃ + 2CH₃COOH → CO₂ ↑ + H₂O + (CH₃COO)₂Ca", "obs": "Slow fizzing! Weaker acid, same CO₂ gas but slower. Good for comparing strong vs weak acid.", "risk": "🟢 SAFE", "anim": "🪨🫧"}
    return None

# --- HEADER - TITLE CHANGED ---
st.markdown("# 🧪 ChemVerse - A Virtual Lab")
st.caption("No chemicals. No risk. Just pure science. | ರಾಸಾಯನಿಕಗಳಿಲ್ಲ, ಅಪಾಯವಿಲ್ಲ | कोई केमिकल नहीं, कोई खतरा नहीं")
st.info("💡 **How to use:** Select 2 chemicals from below → Drop them in Reaction Chamber → Click MIX!")
st.divider()

col1, col2 = st.columns([1, 1.3])

with col1:
    st.subheader("1️⃣ Select Chemicals")
    c1 = st.selectbox("Beaker 1 - Chemical A", list(CHEMICALS.keys()), index=0)
    c2 = st.selectbox("Beaker 2 - Chemical B", list(CHEMICALS.keys()), index=1)

    st.write("")
    st.markdown(f"""
    <div style="display:flex; justify-content:center;">
        <div class="beaker" style="background:{CHEMICALS[c1]['color']}">{CHEMICALS[c1]['emoji']}</div>
        <div style="line-height:120px; font-size:30px;">+</div>
        <div class="beaker" style="background:{CHEMICALS[c2]['color']}">{CHEMICALS[c2]['emoji']}</div>
    </div>
    <center><b>{c1}</b> + <b>{c2}</b></center>
    """, unsafe_allow_html=True)

    st.write("")
    reaction = get_reaction(c1, c2)
    if reaction:
        st.success(f"**Expected:** {reaction['equation']}")
    else:
        st.warning("⚠️ No reaction / Unknown combination - Try in real lab? But here it's safe to try!")

with col2:
    st.subheader("2️⃣ Reaction Chamber - Do it Manually!")

    chamber_placeholder = st.empty()
    chamber_placeholder.markdown(f"""
    <div class="reaction-box">
        <h1>🧫 Empty Chamber</h1>
        <p>Drop chemicals here</p>
        <h2>{CHEMICALS[c1]['emoji']} + {CHEMICALS[c2]['emoji']}</h2>
        <small>Ready to mix</small>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    mix_btn = st.button("🧪 MIX CHEMICALS - START REACTION", use_container_width=True, type="primary")

    if mix_btn:
        result = get_reaction(c1, c2)
        if result:
            with st.status(f"Mixing {c1} + {c2}...", expanded=True) as status:
                st.write("Pouring chemicals...")
                time.sleep(0.5)
                st.write("Molecules colliding...")
                prog = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    prog.progress(i+1)
                status.update(label="Reaction Complete! ✅", state="complete", expanded=False)

            chamber_placeholder.markdown(f"""
            <div class="reaction-box" style="background: linear-gradient(135deg, #fff3e0 0%, #ffffff 100%); border-color: #ff9800;">
                <h1 style="font-size:50px;">{result['anim']}</h1>
                <h3>{result['equation']}</h3>
                <p><b>Reaction Done!</b></p>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()
            st.success(f"**Observation:** {result['obs']}")
            if "HIGH" in result['risk']:
                st.error(f"**Safety:** {result['risk']} - In real lab, wear goggles & gloves!")
            else:
                st.info(f"**Safety:** {result['risk']}")
        else:
            chamber_placeholder.markdown(f"""
            <div class="reaction-box" style="background:#ffebee;">
                <h1>😶 No Reaction</h1>
                <p>{c1} + {c2} don't react at room temp</p>
                <p>Try another combination!</p>
            </div>
            """, unsafe_allow_html=True)
            st.warning("No visible reaction. Try: Sodium+Water, Acid+Base, CuSO₄+Iron...")

st.divider()
c1, c2 = st.columns(2)
with c1:
    with st.expander("📊 Q? Conductivity Ranking (Why Silver > Copper?)"):
        st.markdown("1. **Silver (Ag) 100%** - Best conductor\n2. **Copper (Cu) 97%** - Used in wires (cheap)\n3. **Gold (Au) 76%** - Never rusts, satellites\n4. **Aluminium (Al) 61%** - Light, overhead lines")
with c2:
    with st.expander("🎯 Take Quiz - Interactive"):
        q = st.radio("Which gas is produced when Baking Soda + Vinegar mix?", ["O₂", "H₂", "CO₂", "N₂"])
        if st.button("Submit"):
            if q == "CO₂":
                st.success("Correct! CO₂ inflates balloon! 🎈 Certificate: Science Explorer 2026")
                st.balloons()
            else:
                st.error("Hint: Lime water turns milky with this gas...")

st.markdown("<center><small>Built for Hackathon | A Virtual Lab - 1 Link = Lab for 10,000 Schools | No chemicals needed</small></center>", unsafe_allow_html=True)
