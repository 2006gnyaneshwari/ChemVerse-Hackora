import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title="ChemVerse - A Virtual Lab", page_icon="🧪", layout="wide")
st.title("🧪 ChemVerse - A Virtual Lab")
st.caption("Real Board Practical - Salt Analysis | Acid-Base | Flame Test | Gas Tests - With Real Graphics")

# --- PERFECT GRAPHICS ENGINE - FIXED ---
def show_beaker(color="#03a9f4", text="Beaker", bubbles=2):
    b = "".join([f'<div style="position:absolute; left:{20+i*25}px; bottom:{20+i*10}px; width:12px; height:12px; background:rgba(255,255,255,0.9); border-radius:50%; animation:rise 2s infinite; animation-delay:{i*0.3}s"></div>' for i in range(bubbles)])
    html = f"""
    <style>
    @keyframes rise {{0%{{bottom:10px; opacity:1}} 100%{{bottom:170px; opacity:0}}}}
    @keyframes flicker {{0%{{transform:scale(1) translateY(0)}} 50%{{transform:scale(1.15) translateY(-5px)}} 100%{{transform:scale(1) translateY(0)}}}}
   .lab{{display:flex; justify-content:center; align-items:flex-end; height:250px; background:linear-gradient(180deg, #e0f7fa 0%, #ffffff 100%); border-radius:20px; border:3px solid #00acc1; position:relative; overflow:hidden; box-shadow: 0 8px 20px rgba(0,0,0,0.1)}}
   .beaker{{width:140px; height:180px; border:4px solid #37474f; border-top:none; border-radius:0 0 30px 30px; position:relative; background:rgba(255,255,255,0.6); margin:0 15px; box-shadow: inset 0 0 20px rgba(0,0,0,0.1)}}
   .liquid{{position:absolute; bottom:0; width:100%; border-radius:0 0 26px 26px; transition: all 1.5s ease;}}
    </style>
    <div class="lab">
        <div class="beaker"><div class="liquid" style="height:70%; background:{color}">{b}</div></div>
    </div>
    <center><b style="font-size:16px; margin-top:10px; display:block">{text}</b></center>
    """
    return html

def show_flame(flame_emoji="🔥", flame_name="Yellow Flame", bg_color="#ffeb3b", glow="#ff9800"):
    html = f"""
    <style>
    @keyframes flicker {{0%{{transform:scale(1)}} 50%{{transform:scale(1.2) rotate(2deg)}} 100%{{transform:scale(1)}}}}
   .flame-lab{{display:flex; justify-content:center; align-items:center; height:280px; background:radial-gradient(circle, #263238 0%, #000000 100%); border-radius:20px; border:3px solid {glow}; position:relative; overflow:hidden}}
   .flame-box{{font-size:80px; animation:flicker 0.2s infinite; filter: drop-shadow(0 0 30px {glow});}}
   .wire{{position:absolute; bottom:20px; font-size:20px; color:white}}
    </style>
    <div class="flame-lab">
        <div class="wire">🧫 Platinum Wire</div>
        <div class="flame-box">{flame_emoji}</div>
    </div>
    <center>
        <div style="background:{bg_color}; padding:10px; border-radius:10px; margin-top:10px; border:2px solid {glow}">
            <b style="font-size:18px; color:#000">{flame_name}</b>
        </div>
    </center>
    """
    return html

# --- 4 LABS ---
tab1, tab2, tab3, tab4 = st.tabs(["🧂 SALT ANALYSIS", "🧪 ACID-BASE TESTS", "🔥 FLAME TEST", "💨 GAS TESTS"])

with tab1:
    st.subheader("Salt Analysis - 6 Step Systematic Analysis")
    col1, col2 = st.columns([1,1])
    with col1:
        salt = st.selectbox("Select Unknown Salt", ["NaCl - Common Salt", "CuSO4 - Blue Salt", "Pb(NO3)2 - Lead Nitrate", "CaCO3 - Chalk", "NH4Cl - Ammonium Chloride", "FeSO4 - Green Vitriol", "BaCl2 - Barium Chloride", "Na2CO3 - Washing Soda"])
        details = {
            "NaCl - Common Salt": ("Cl-", "Na+", "#e1f5fe", "White AgCl ppt, soluble in NH4OH", "Golden yellow flame"),
            "CuSO4 - Blue Salt": ("SO4^2-", "Cu2+", "#03a9f4", "White BaSO4 ppt", "Deep blue with NH4OH, black CuO on heating"),
            "Pb(NO3)2 - Lead Nitrate": ("NO3-", "Pb2+", "#fff9c4", "Brown ring test +ve", "Yellow PbI2 with KI - Golden Rain!"),
            "CaCO3 - Chalk": ("CO3^2-", "Ca2+", "#f5f5f5", "CO2 effervescence, lime water milky", "Brick red flame"),
            "NH4Cl - Ammonium Chloride": ("Cl-", "NH4+", "#eeeeee", "White AgCl ppt", "NH3 gas with NaOH - pungent"),
            "FeSO4 - Green Vitriol": ("SO4^2-", "Fe2+", "#a5d6a7", "BaCl2 white ppt", "Green Fe(OH)2 → brown Fe(OH)3"),
            "BaCl2 - Barium Chloride": ("Cl-", "Ba2+", "#e8f5e9", "White AgCl", "Apple Green flame"),
            "Na2CO3 - Washing Soda": ("CO3^2-", "Na+", "#ffffff", "Brisk CO2 with acid", "Yellow flame"),
        }
        anion, cation, col, anion_conf, cation_conf = details[salt]
        st.markdown(f"**Anion:** `{anion}` | **Cation:** `{cation}`")
        if st.button("🔬 START FULL ANALYSIS", type="primary", use_container_width=True, key="salt_btn"):
            with st.status("Performing 6-step analysis...", expanded=True) as s:
                st.write("1️⃣ Physical: Noting color, smell...")
                time.sleep(0.4)
                st.write(f"2️⃣ Dry Heating: {cation} shows residue...")
                time.sleep(0.4)
                st.write(f"3️⃣ Flame Test: {cation_conf}")
                time.sleep(0.4)
                st.write(f"4️⃣ Dil HCl Test: {anion_conf}")
                time.sleep(0.4)
                st.write(f"5️⃣ Confirmatory: {anion} & {cation} confirmed!")
                s.update(label="Analysis Complete! ✅", state="complete")
            st.balloons()
            st.success(f"**RESULT: {salt} CONFIRMED**\n\nAnion: {anion} - {anion_conf}\n\nCation: {cation} - {cation_conf}")
            components.html(show_beaker(col, f"{salt} - {anion}/{cation}", bubbles=4), height=320)
    with col2:
        components.html(show_beaker(details[salt][2], f"Test Tube - {salt}", bubbles=3), height=320)
        st.table({"Step": ["1 Physical", "2 Dry Heat", "3 Flame", "4 Anion Test", "5 Cation Test"], "What to see": ["Color", "Residue", "Flame color", "Ppt/Gas", "Colored Ppt"]})

with tab2:
    st.subheader("Acid-Base & pH Tests - Real Indicator Colors")
    c1, c2 = st.columns(2)
    with c1:
        sol = st.selectbox("Select Solution", ["HCl - Strong Acid (pH 1)", "NaOH - Strong Base (pH 13)", "Vinegar - Weak Acid (pH 4)", "Baking Soda - Weak Base (pH 8)", "Lemon (pH 2)", "NaCl - Neutral (pH 7)", "Water (pH 7)"])
        ind = st.selectbox("Select Indicator", ["Blue Litmus", "Red Litmus", "Phenolphthalein", "Methyl Orange", "pH Paper", "Turmeric (Haldi)"])
        ph_map = {"HCl - Strong Acid (pH 1)":1, "NaOH - Strong Base (pH 13)":13, "Vinegar - Weak Acid (pH 4)":4, "Baking Soda - Weak Base (pH 8)":8, "Lemon (pH 2)":2, "NaCl - Neutral (pH 7)":7, "Water (pH 7)":7}
        ph = ph_map[sol]
        # Real indicator logic
        if ind=="Blue Litmus": col, res = ("#ef9a9a" if ph<7 else "#90caf9", "Blue→Red (Acid)" if ph<7 else "Stays Blue (Base)")
        elif ind=="Red Litmus": col, res = ("#90caf9" if ph>7 else "#ef9a9a", "Red→Blue (Base)" if ph>7 else "Stays Red (Acid)")
        elif ind=="Phenolphthalein": col, res = ("#f48fb1" if ph>8 else "#ffffff", "Pink in Base (>8), Colorless in Acid")
        elif ind=="Methyl Orange": col, res = ("#ffab91" if ph<3.1 else "#fff176" if ph>4.4 else "#ffcc80", "Red (<3.1) → Orange → Yellow (>4.4)")
        elif ind=="Turmeric (Haldi)": col, res = ("#b71c1c" if ph>8 else "#ffeb3b", "Yellow→Reddish Brown in Base")
        else: col, res = ("#ef5350" if ph<=2 else "#ff7043" if ph<=4 else "#ffca28" if ph<=6 else "#66bb6a" if ph==7 else "#29b6f6", f"pH {ph} Color")

        if st.button("🧪 TEST", type="primary", key="ab_btn", use_container_width=True):
            components.html(show_beaker(col, f"{ind} → {res} | pH {ph}", bubbles=5), height=320)
            time.sleep(0.5)
            if ph<7: st.error(f"**ACIDIC** - {res} | pH={ph}")
            elif ph>7: st.success(f"**BASIC** - {res} | pH={ph}")
            else: st.info(f"**NEUTRAL** - {res} | pH={ph}")
    with c2:
        components.html(show_beaker("#e1bee7", "Indicator Test Tube", bubbles=2), height=320)
        st.table({"Indicator": ["Phenolphthalein", "Methyl Orange", "Litmus", "Turmeric"], "Acid": ["Colorless", "Red", "Red", "Yellow"], "Base": ["Pink", "Yellow", "Blue", "Brown-Red"]})

with tab3:
    st.subheader("Flame Test - Real Glowing Flames")
    f1, f2 = st.columns([1,1])
    with f1:
        metal = st.selectbox("Select Salt for Flame Test", ["Sodium (NaCl) - Golden Yellow", "Potassium (KCl) - Lilac Purple", "Calcium (CaCl2) - Brick Red", "Barium (BaCl2) - Apple Green", "Strontium (SrCl2) - Crimson Red", "Copper (CuSO4) - Bluish Green", "Lead (Pb) - Pale White"])
        flame_data = {
            "Sodium (NaCl) - Golden Yellow": ("🟡", "Golden Yellow Flame - Na+ Confirmed - Persistent", "#ffeb3b", "#ff9800"),
            "Potassium (KCl) - Lilac Purple": ("🟣", "Lilac / Light Violet - K+ Confirmed (Blue Glass)", "#ce93d8", "#9c27b0"),
            "Calcium (CaCl2) - Brick Red": ("🟠", "Brick Red Flame - Ca2+ Confirmed", "#ff8a65", "#bf360c"),
            "Barium (BaCl2) - Apple Green": ("🟢", "Apple Green / Grassy Green - Ba2+ Confirmed", "#a5d6a7", "#2e7d32"),
            "Strontium (SrCl2) - Crimson Red": ("🔴", "Crimson Red - Sr2+ - Fireworks Red", "#ef5350", "#b71c1c"),
            "Copper (CuSO4) - Bluish Green": ("🔵", "Bluish Green with HCl - Cu2+ Confirmed", "#4dd0e1", "#006064"),
            "Lead (Pb) - Pale White": ("⚪", "Pale Bluish White - Pb2+", "#b0bec5", "#37474f"),
        }
        if st.button("🔥 PERFORM FLAME TEST", type="primary", use_container_width=True, key="flame_btn"):
            emoji, name, bg, glow = flame_data[metal]
            components.html(show_flame(emoji, name, bg, glow), height=360)
            st.balloons()
            st.success(f"**{name}**\n\nThis flame color confirms {metal.split()[0]} ion present!")
            time.sleep(0.3)
    with f2:
        components.html(show_flame("🔥", "Select metal and click TEST", "#263238", "#00acc1"), height=360)
        st.markdown("#### 🔥 Chart for Viva")
        st.table({"Ion": ["Na+", "K+", "Ca2+", "Ba2+", "Sr2+", "Cu2+"], "Color": ["Golden Yellow", "Lilac", "Brick Red", "Apple Green", "Crimson", "Bluish Green"], "Through Blue Glass": ["Yellow", "Pink", "Light Green", "Green", "Purple", "Blue"]})

with tab4:
    st.subheader("Gas Evolution & Confirmatory Tests")
    g1, g2 = st.columns(2)
    with g1:
        gas = st.selectbox("Select Gas Test", ["CO2 - Lime Water Milky Test", "H2 - Pop Test (Acid+Metal)", "NH3 - Pungent, Red Litmus Blue", "O2 - Glowing Splint Reignites", "Cl2 - Bleaches Moist Litmus", "Brown Ring - For Nitrate NO3-", "BaCl2 Test - For Sulphate SO4^2-"])
        if st.button("💨 PERFORM GAS TEST", key="gas_btn", type="primary"):
            if "CO2" in gas:
                components.html(show_beaker("#e0f2f1", "Lime Water Turns MILKY - CO2 Confirmed! CaCO3 ppt", bubbles=6), height=320)
                st.success("Ca(OH)2 + CO2 → CaCO3↓ (milky) | Excess CO2 → Clear (Ca(HCO3)2) | CONFIRMS CO3^2-")
            elif "H2" in gas:
                components.html(show_beaker("#fff3e0", "POP Sound! H2 Confirmed!", bubbles=8), height=320)
                st.success("Zn + 2HCl → ZnCl2 + H2↑ | H2 + flame → POP! | CONFIRMS ACID + METAL")
            elif "NH3" in gas:
                components.html(show_beaker("#f3e5f5", "NH3 - Pungent Smell - Red Litmus→Blue", bubbles=3), height=320)
                st.success("NH4Cl + NaOH → NH3↑ (pungent) + H2O | Turns red litmus blue | CONFIRMS NH4+")
            elif "Brown Ring" in gas:
                components.html(show_beaker("#8d6e63", "Brown Ring at Junction - NO3- Confirmed!", bubbles=0), height=320)
                st.success("NO3- + FeSO4 + conc H2SO4 → Brown ring [Fe(NO)(H2O)5]SO4 | CONFIRMS NITRATE")
            else:
                components.html(show_beaker("#e1f5fe", f"{gas} - Positive! ✅", bubbles=2), height=320)
                st.success(f"{gas} - Positive Test! ✅")
    with g2:
        st.markdown("**Other Confirmatory Tests**")
        st.info("""
        - **AgNO3 Test (Cl-):** AgNO3 + Cl- → AgCl White ppt (soluble in NH4OH)
        - **BaCl2 Test (SO4^2-):** BaCl2 + SO4^2- → BaSO4 White ppt (insoluble in acid)
        - **Lead Acetate (S2-):** Black ppt PbS
        - **KI Test (Pb2+):** Pb2+ + 2KI → PbI2 Yellow ppt (Golden Rain)
        """)
        st.image("https://cdn-icons-png.flaticon.com/512/1087/1087815.png", width=80, caption="Real Lab Apparatus")

st.divider()
st.success("🏆 ChemVerse - A Virtual Lab | 10 Salts + 7 pH + 7 Flames + 7 Gases = 31 Experiments | With Real Animated Graphics | Built for Hackora")
