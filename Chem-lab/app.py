import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title="ChemVerse - A Virtual Lab", page_icon="🧪", layout="wide")

st.title("🧪 ChemVerse - A Virtual Lab")
st.caption("Real graphics. Real reactions. Zero risk. | A Virtual Lab for Every School")

# --- REAL GRAPHICS HTML GENERATOR ---
def reaction_graphics_html(reaction_id):
    # Base beaker + animation CSS
    base_css = """
    <style>
   .lab { display:flex; justify-content:center; align-items:flex-end; height:260px; background: linear-gradient(#e6f7ff, #fff); border-radius:20px; border:2px solid #00acc1; position:relative; overflow:hidden; }
   .beaker { width:140px; height:180px; border:4px solid #333; border-top:none; border-radius:0 0 30px 30px; position:relative; background:rgba(255,255,255,0.6); margin:0 40px; }
   .liquid { position:absolute; bottom:0; width:100%; border-radius:0 0 26px 26px; transition: all 1s; }
   .bubble { position:absolute; width:10px; height:10px; background:rgba(255,255,255,0.8); border-radius:50%; animation: rise 2s infinite; }
    @keyframes rise { 0% { bottom:10px; opacity:1; transform:translateX(0); } 100% { bottom:160px; opacity:0; transform:translateX(20px); } }
    @keyframes fire { 0% { transform:scale(1) translateY(0); } 50% { transform:scale(1.2) translateY(-10px); } 100% { transform:scale(1) translateY(0); } }
   .flame { position:absolute; bottom:140px; left:50%; font-size:50px; animation: fire 0.3s infinite; }
   .ppt { position:absolute; width:8px; height:8px; border-radius:50%; animation: fall 1.5s linear infinite; }
    @keyframes fall { 0% { top:20px; } 100% { top:150px; } }
    </style>
    """

    if reaction_id == "fire": # Sodium + Water
        return base_css + """
        <div class="lab">
            <div class="beaker"><div class="liquid" style="height:60%; background:#03a9f4;"></div><div class="bubble" style="left:20px;"></div><div class="bubble" style="left:50px; animation-delay:0.5s;"></div></div>
            <div class="flame">🔥</div>
            <div class="beaker" style="background:rgba(255,235,59,0.8);"><div class="liquid" style="height:70%; background:#ffeb3b;"></div></div>
        </div>
        <center><b style="color:red;">🔥 Violent Exothermic! H2 gas burning!</b></center>
        """
    if reaction_id == "co2": # Baking Soda + Vinegar
        bubbles = "".join([f'<div class="bubble" style="left:{10+i*15}px; animation-delay:{i*0.2}s; width:{8+i%3}px; height:{8+i%3}px;"></div>' for i in range(10)])
        return base_css + f"""
        <div class="lab" style="background: linear-gradient(#f3e5f5, #fff);">
            <div class="beaker"><div class="liquid" style="height:70%; background:#e1bee7;">{bubbles}</div></div>
            <div style="font-size:40px; margin-bottom:100px;">🎈</div>
        </div>
        <center><b>🫧 CO2 bubbles rising fast! Balloon inflating!</b></center>
        """
    if reaction_id == "yellow": # Pb + KI
        ppt = "".join([f'<div class="ppt" style="left:{20+i*10}px; background:gold; animation-delay:{i*0.1}s;"></div>' for i in range(10)])
        return base_css + f"""
        <div class="lab" style="background:#fffde7;">
            <div class="beaker"><div class="liquid" style="height:80%; background:#fff9c4;">{ppt}</div></div>
        </div>
        <center><b style="color:goldenrod;">✨ Golden Yellow Precipitate (PbI2) forming! Most Beautiful!</b></center>
        """
    if reaction_id == "white": # AgNO3 + NaCl
        ppt = "".join([f'<div class="ppt" style="left:{20+i*10}px; background:white; border:1px solid #999; animation-delay:{i*0.1}s;"></div>' for i in range(12)])
        return base_css + f"""
        <div class="lab"><div class="beaker"><div class="liquid" style="height:80%; background:rgba(200,230,255,0.5);">{ppt}</div></div></div>
        <center><b>⚪ White Curdy Precipitate (AgCl)!</b></center>
        """
    if reaction_id == "blue_green": # CuSO4 + Fe
        return base_css + """
        <div class="lab">
            <div class="beaker"><div class="liquid" style="height:75%; background:#4fc3f7; animation: colorChange 3s forwards;" id="liq"></div></div>
        </div>
        <style>@keyframes colorChange { 0% { background:#2196f3; } 100% { background:#81c784; } }</style>
        <center><b>🔵 Blue → 🟢 Green! Copper coating on Iron!</b></center>
        """
    # Default - gas / pop
    return base_css + """
    <div class="lab"><div class="beaker"><div class="liquid" style="height:70%; background:#c8e6c9;"></div>
    <div class="bubble" style="left:30px;"></div><div class="bubble" style="left:60px; animation-delay:0.3s;"></div><div class="bubble" style="left:90px; animation-delay:0.6s;"></div>
    </div></div><center><b>💨 Gas bubbles! Pop test!</b></center>
    """

CHEMICALS = ["Sodium (Na)", "Water (H2O)", "HCl - Acid", "NaOH - Base", "CuSO4 - Blue", "Iron (Fe)", "Zinc (Zn)", "Baking Soda", "Vinegar", "Limestone (CaCO3)", "Silver Nitrate (AgNO3)", "Salt (NaCl)", "Potassium Iodide (KI)", "Lead Nitrate (Pb(NO3)2)"]

def get_reaction(c1, c2):
    s = {c1, c2}
    if s == {"Sodium (Na)", "Water (H2O)"}: return ("2Na + 2H2O → 2NaOH + H2 🔥", "Violent fire, H2 pop test, exothermic", "HIGH", "fire")
    if s == {"Baking Soda", "Vinegar"}: return ("NaHCO3 + CH3COOH → CO2 ↑", "CO2 fountain, balloon inflates", "SAFE", "co2")
    if s == {"Lead Nitrate (Pb(NO3)2)", "Potassium Iodide (KI)"}: return ("Pb(NO3)2 + 2KI → PbI2 (yellow) ↓", "Golden yellow precipitate, Golden Rain!", "VIRTUAL ONLY", "yellow")
    if s == {"Silver Nitrate (AgNO3)", "Salt (NaCl)"}: return ("AgNO3 + NaCl → AgCl (white) ↓", "White curdy precipitate, test for chloride", "MEDIUM", "white")
    if s == {"CuSO4 - Blue", "Iron (Fe)"}: return ("CuSO4 + Fe → FeSO4 + Cu", "Blue fades to green, copper coating", "SAFE", "blue_green")
    if s == {"HCl - Acid", "NaOH - Base"}: return ("HCl + NaOH → NaCl + H2O", "Neutralization pH 7, warm", "SAFE", "default")
    if s == {"Limestone (CaCO3)", "HCl - Acid"}: return ("CaCO3 + HCl → CO2 ↑", "Fizzes, lime water milky", "SAFE", "co2")
    if s == {"Zinc (Zn)", "CuSO4 - Blue"}: return ("Zn + CuSO4 → ZnSO4 + Cu", "Blue to colorless, displacement", "SAFE", "blue_green")
    if s == {"CuSO4 - Blue", "NaOH - Base"}: return ("CuSO4 + NaOH → Cu(OH)2 (blue ppt)", "Pale blue precipitate", "SAFE", "white")
    return None

c1, c2 = st.columns([1, 1.3])
with c1:
    st.subheader("1️⃣ Select Chemicals")
    chemA = st.selectbox("Beaker A", CHEMICALS, index=0)
    chemB = st.selectbox("Beaker B", CHEMICALS, index=1)
    st.write("")
    res = get_reaction(chemA, chemB)
    if res:
        st.success(f"**Equation:** {res[0]}")
        st.caption(res[1])

with c2:
    st.subheader("2️⃣ Reaction Chamber - Real Graphics!")
    placeholder = st.empty()
    placeholder.markdown(reaction_graphics_html("default"), unsafe_allow_html=True)

    if st.button("🧪 MIX - START REAL REACTION", type="primary", use_container_width=True):
        r = get_reaction(chemA, chemB)
        if r:
            with st.spinner("Pouring... Reacting..."):
                time.sleep(1)
            # Show real graphics!
            placeholder.empty()
            with placeholder:
                components.html(reaction_graphics_html(r[3]), height=320)
            st.balloons()
            st.success(f"**{r[0]}**")
            st.info(f"**Observation:** {r[1]} | Safety: {r[2]}")
        else:
            components.html(reaction_graphics_html("default"), height=320)
            st.warning("No reaction. Try Sodium+Water (Fire) or Lead Nitrate+KI (Golden Yellow!)")

st.divider()
st.markdown("### 🏆 Why Real Graphics?")
st.write("Before: Only text. Now: **Real beaker, liquid color change, bubbles rising animation, fire flicker, yellow precipitate falling** — all with CSS, no images needed, works on any phone!")

# --- REAL IMAGES OF APPARATUS ---
st.markdown("#### 🔬 Real Lab Apparatus")
a1, a2, a3, a4 = st.columns(4)
with a1: st.image("https://cdn-icons-png.flaticon.com/512/1087/1087815.png", caption="Beaker")
with a2: st.image("https://cdn-icons-png.flaticon.com/512/3037/3037828.png", caption="Test Tube")
with a3: st.image("https://cdn-icons-png.flaticon.com/512/2761/2761557.png", caption="Conical Flask")
with a4: st.image("https://cdn-icons-png.flaticon.com/512/3063/3063362.png", caption="Bunsen Burner")
