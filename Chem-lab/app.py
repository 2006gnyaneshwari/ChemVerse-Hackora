import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title="ChemVerse - A Virtual Lab", page_icon="🧪", layout="wide")
st.title("🧪 ChemVerse - A Virtual Lab")
st.caption("Real Board Lab - Dark Real Chemical Colors")

def show_beaker(color="#0D47A1", text="Beaker", bubbles=3):
    # DARK STRONG COLORS
    b = "".join([f'<div style="position:absolute; left:{20+i*28}px; bottom:{20+i*10}px; width:12px; height:12px; background:rgba(255,255,255,0.95); border-radius:50%; animation:rise 2s infinite; animation-delay:{i*0.3}s; box-shadow:0 0 5px white"></div>' for i in range(bubbles)])
    html = f"""
    <style>
    @keyframes rise {{0%{{bottom:10px; opacity:1}} 100%{{bottom:170px; opacity:0}}}}
    @keyframes flicker {{0%{{transform:scale(1)}} 50%{{transform:scale(1.15)}} 100%{{transform:scale(1)}}}}
  .lab{{display:flex; justify-content:center; align-items:flex-end; height:260px; background:linear-gradient(180deg, #e0f7fa 0%, #ffffff 100%); border-radius:20px; border:3px solid #006064; position:relative; overflow:hidden; box-shadow:0 8px 25px rgba(0,0,0,0.2)}}
  .beaker{{width:150px; height:190px; border:4px solid #212121; border-top:none; border-radius:0 0 35px 35px; position:relative; background:rgba(255,255,255,0.3); margin:0 15px; box-shadow:inset 0 0 25px rgba(0,0,0,0.15)}}
  .liquid{{position:absolute; bottom:0; width:100%; border-radius:0 0 32px 32px; transition:1.5s; opacity:0.95; box-shadow:inset 0 10px 20px rgba(0,0,0,0.2)}}
    </style>
    <div class="lab">
        <div class="beaker"><div class="liquid" style="height:75%; background:{color}; border-top:3px solid rgba(0,0,0,0.2)">{b}</div></div>
    </div>
    <center><b style="font-size:16px; margin-top:12px; display:block; background:#263238; color:white; padding:6px 12px; border-radius:8px">{text}</b></center>
    """
    return html

def show_flame(flame_emoji="🔥", flame_name="Yellow Flame", bg_color="#FFEB3B", glow="#FF6F00"):
    html = f"""
    <style>
    @keyframes flicker {{0%{{transform:scale(1)}} 50%{{transform:scale(1.25) rotate(2deg)}} 100%{{transform:scale(1)}}}}
  .flame-lab{{display:flex; justify-content:center; align-items:center; height:290px; background:radial-gradient(circle, #212121 0%, #000000 100%); border-radius:20px; border:4px solid {glow}; position:relative; overflow:hidden; box-shadow:0 0 30px {glow}}}
  .flame-box{{font-size:90px; animation:flicker 0.18s infinite; filter:drop-shadow(0 0 35px {glow}) drop-shadow(0 0 60px {bg_color})}}
    </style>
    <div class="flame-lab"><div class="flame-box">{flame_emoji}</div></div>
    <center><div style="background:{bg_color}; padding:12px; border-radius:12px; margin-top:12px; border:3px solid {glow}; box-shadow:0 4px 15px rgba(0,0,0,0.3)"><b style="font-size:19px; color:#000">{flame_name}</b></div></center>
    """
    return html

tab1, tab2, tab3, tab4 = st.tabs(["🧂 SALT ANALYSIS", "🧪 ACID-BASE", "🔥 FLAME TEST", "💨 GAS TESTS"])

with tab1:
    st.subheader("Salt Analysis - Dark Real Colors")
    col1, col2 = st.columns([1,1])
    with col1:
        salt = st.selectbox("Select Unknown Salt", ["NaCl - Common Salt", "CuSO4 - Blue Salt", "Pb(NO3)2 - Lead Nitrate", "CaCO3 - Chalk", "NH4Cl - Ammonium Chloride", "FeSO4 - Green Vitriol", "BaCl2 - Barium Chloride", "Na2CO3 - Washing Soda"])
        details = {
            "NaCl - Common Salt": ("Cl-", "Na+", "#B0BEC5", "White AgCl ppt", "Golden yellow flame"), # dark greyish
            "CuSO4 - Blue Salt": ("SO4^2-", "Cu2+", "#0D47A1", "White BaSO4 ppt", "Deep blue with NH4OH"), # DARK BLUE
            "Pb(NO3)2 - Lead Nitrate": ("NO3-", "Pb2+", "#F9A825", "Brown ring test", "Yellow PbI2 - Golden Rain!"), # DARK YELLOW
            "CaCO3 - Chalk": ("CO3^2-", "Ca2+", "#EEEEEE", "CO2 effervescence", "Brick red flame"),
            "NH4Cl - Ammonium Chloride": ("Cl-", "NH4+", "#78909C", "White AgCl ppt", "NH3 gas pungent"),
            "FeSO4 - Green Vitriol": ("SO4^2-", "Fe2+", "#2E7D32", "BaCl2 white ppt", "Green Fe(OH)2 → brown"), # DARK GREEN
            "BaCl2 - Barium Chloride": ("Cl-", "Ba2+", "#A5D6A7", "White AgCl", "Apple Green flame"),
            "Na2CO3 - Washing Soda": ("CO3^2-", "Na+", "#FFFFFF", "Brisk CO2", "Yellow flame"),
        }
        anion, cation, col, anion_conf, cation_conf = details[salt]
        st.markdown(f"**Anion:** `{anion}` | **Cation:** `{cation}`")
        if st.button("🔬 START ANALYSIS", type="primary", use_container_width=True, key="salt_btn"):
            with st.status("Analyzing...", expanded=True) as s:
                st.write("1️⃣ Physical 2️⃣ Dry Heating 3️⃣ Flame 4️⃣ Anion 5️⃣ Cation")
                time.sleep(0.8)
                s.update(label="Confirmed! ✅", state="complete")
            st.balloons()
            st.success(f"**{salt} CONFIRMED** | {anion_conf} | {cation_conf}")
            components.html(show_beaker(col, f"{salt} - DARK COLOR", bubbles=5), height=330)
    with col2:
        # Show dark color immediately
        components.html(show_beaker(details[salt][2], f"{salt} - REAL DARK COLOR", bubbles=4), height=330)

with tab2:
    st.subheader("Acid-Base - DARK Indicator Colors")
    c1, c2 = st.columns(2)
    with c1:
        sol = st.selectbox("Solution", ["HCl - Strong Acid (pH 1)", "NaOH - Strong Base (pH 13)", "Vinegar - Weak Acid (pH 4)", "Baking Soda - Weak Base (pH 8)", "Lemon (pH 2)", "NaCl - Neutral (pH 7)"])
        ind = st.selectbox("Indicator", ["Blue Litmus", "Red Litmus", "Phenolphthalein", "Methyl Orange", "pH Paper", "Turmeric"])
        ph_map = {"HCl - Strong Acid (pH 1)":1, "NaOH - Strong Base (pH 13)":13, "Vinegar - Weak Acid (pH 4)":4, "Baking Soda - Weak Base (pH 8)":8, "Lemon (pH 2)":2, "NaCl - Neutral (pH 7)":7}
        ph = ph_map[sol]
        # DARK COLORS NOW
        if ind=="Blue Litmus": col, res = ("#B71C1C" if ph<7 else "#0D47A1", "Blue→RED (Acid)" if ph<7 else "Stays DARK BLUE (Base)")
        elif ind=="Red Litmus": col, res = ("#0D47A1" if ph>7 else "#B71C1C", "Red→DARK BLUE (Base)" if ph>7 else "Stays DARK RED (Acid)")
        elif ind=="Phenolphthalein": col, res = ("#AD1457" if ph>8 else "#FAFAFA", "DARK PINK in Base, Colorless in Acid") # dark pink #AD1457
        elif ind=="Methyl Orange": col, res = ("#BF360C" if ph<3.1 else "#F9A825", "DARK RED in Acid, DARK YELLOW in Base") # dark red, dark yellow
        elif ind=="Turmeric": col, res = ("#3E2723" if ph>8 else "#F9A825", "DARK Brown-Red in Base, DARK Yellow in Acid")
        else: col, res = ("#B71C1C" if ph<=2 else "#E65100" if ph<=4 else "#F9A825" if ph<=6 else "#2E7D32" if ph==7 else "#0D47A1", f"pH {ph}")

        if st.button("🧪 TEST", type="primary", key="ab_btn", use_container_width=True):
            components.html(show_beaker(col, f"{ind} → {res} | pH {ph} - DARK", bubbles=6), height=330)
            if ph<7: st.error(f"ACIDIC - {res}")
            elif ph>7: st.success(f"BASIC - {res}")
            else: st.info(f"NEUTRAL - {res}")
    with c2:
        components.html(show_beaker("#4A148C", "DARK Indicator - Real Lab Color", bubbles=2), height=330)
        st.markdown("**DARK COLORS = REAL LAB**")
        st.write("Acid: Dark Red | Base: Dark Blue | Phenolphthalein: Dark Pink #AD1457")

with tab3:
    st.subheader("Flame Test - DARK Background, Bright Flames")
    f1, f2 = st.columns([1,1])
    with f1:
        metal = st.selectbox("Select Salt", ["Sodium (NaCl) - Golden Yellow", "Potassium (KCl) - Lilac", "Calcium (CaCl2) - Brick Red", "Barium (BaCl2) - Apple Green", "Strontium (SrCl2) - Crimson Red", "Copper (CuSO4) - Bluish Green"])
        flame_data = {
            "Sodium (NaCl) - Golden Yellow": ("🟡", "Golden Yellow - Na+ - DARK YELLOW FLAME", "#FFC400", "#FF6F00"),
            "Potassium (KCl) - Lilac": ("🟣", "Lilac Purple - K+ - DARK PURPLE", "#7B1FA2", "#4A148C"),
            "Calcium (CaCl2) - Brick Red": ("🟠", "Brick Red - Ca2+ - DARK RED", "#BF360C", "#3E2723"),
            "Barium (BaCl2) - Apple Green": ("🟢", "Apple Green - Ba2+ - DARK GREEN", "#2E7D32", "#1B5E20"),
            "Strontium (SrCl2) - Crimson Red": ("🔴", "Crimson Red - Sr2+ - DARK CRIMSON", "#B71C1C", "#880E4F"),
            "Copper (CuSO4) - Bluish Green": ("🔵", "Bluish Green - Cu2+ - DARK BLUE-GREEN", "#006064", "#004D40"),
        }
        if st.button("🔥 PERFORM FLAME TEST", type="primary", use_container_width=True, key="flame_btn"):
            emoji, name, bg, glow = flame_data[metal]
            components.html(show_flame(emoji, name, bg, glow), height=380)
            st.balloons()
            st.success(name)
    with f2:
        components.html(show_flame("🔥", "Click TEST - See DARK Glowing Flame", "#263238", "#00E5FF"), height=380)

with tab4:
    st.subheader("Gas Tests - Dark Colors")
    gas = st.selectbox("Gas Test", ["CO2 - Lime Water Milky", "H2 - Pop Test", "NH3 - Pungent", "Brown Ring - Nitrate"])
    if st.button("💨 TEST GAS", key="gas_btn", type="primary"):
        if "CO2" in gas:
            components.html(show_beaker("#E0E0E0", "MILKY WHITE - CO2 Confirmed! CaCO3 DARK WHITE PPT", bubbles=7), height=330)
            st.success("MILKY = CaCO3 ppt - DARK WHITE!")
        elif "H2" in gas:
            components.html(show_beaker("#FFE0B2", "POP! - H2 - Colorless but bubbles DARK", bubbles=9), height=330)
            st.success("POP sound!")
        elif "NH3" in gas:
            components.html(show_beaker("#CE93D8", "NH3 - Pungent - Dark Purple vapors", bubbles=4), height=330)
            st.success("NH3 confirmed!")
        else:
            components.html(show_beaker("#5D4037", "Brown Ring - DARK BROWN RING at junction", bubbles=0), height=330)
            st.success("Brown ring - Nitrate confirmed - DARK BROWN!")

st.success("✅ DARK COLORS FIXED - Now looks like real chemicals, not water!")
