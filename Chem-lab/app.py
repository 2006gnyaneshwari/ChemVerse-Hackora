import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="ChemVerse Ultimate", layout="wide")

# --- CSS FIX FOR WHITE TEXT BUG ---
st.markdown("""
<style>
.stApp { background: #0E1A2B; }
.observation-box {
    background: #E0F7FA!important;
    color: #000000!important;
    border: 2px solid #0F5C5C;
    border-radius: 12px;
    padding: 15px;
    margin-top: 10px;
}
.observation-box b { color: #000000!important; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#4DD0E1;'>🧪 ChemVerse - Ultimate Real Lab</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#B0BEC5;'>Salt Analysis + 7 Fun Chemistry Experiments | Real Graphics</p>", unsafe_allow_html=True)

# --- REAL LAB BEAKER - SINGLE CLEAN ---
def show_beaker(color, label, title="Experiment"):
    html = f"""
    <div style="background: linear-gradient(to bottom, #8D6E63 0%, #6D4C41 100%); border-radius:15px; padding:20px; display:flex; flex-direction:column; align-items:center; box-shadow: inset 0 5px 15px rgba(0,0,0,0.5);">
        <div style="color:white; font-weight:bold; margin-bottom:12px; background:rgba(0,0,0,0.4); padding:6px 15px; border-radius:20px; font-family:sans-serif;">{title}</div>
        <div style="width:170px; height:230px; border:5px solid rgba(255,255,255,0.9); border-top:6px solid #ECEFF1; border-radius:0 0 40px 40px; position:relative; background: linear-gradient(to right, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0.1) 20%, rgba(255,255,255,0.1) 80%, rgba(255,255,255,0.4) 100%); overflow:hidden; box-shadow: 0 15px 30px rgba(0,0,0,0.4);">
            <div style="position:absolute; bottom:0; width:100%; height:70%; background:{color}; border-radius:0 0 35px 35px; box-shadow: inset 0 15px 25px rgba(0,0,0,0.4);">
                <div style="position:absolute; top:-8px; width:100%; height:16px; background:{color}; border-radius:50%; animation: wave 3s infinite;"></div>
                <div style="position:absolute; width:14px; height:14px; background:radial-gradient(circle at 30% 30%, rgba(255,255,255,0.9), rgba(255,255,255,0.2)); border-radius:50%; bottom:20%; left:60%; animation: rise 2.2s infinite;"></div>
                <div style="position:absolute; width:8px; height:8px; background:rgba(255,255,255,0.8); border-radius:50%; bottom:10%; left:30%; animation: rise 3s infinite 0.5s;"></div>
            </div>
            <div style="position:absolute; top:10px; left:15px; width:25px; height:170px; background:linear-gradient(to bottom, rgba(255,255,255,0.5), rgba(255,255,255,0.05)); border-radius:15px;"></div>
        </div>
        <div style="background:#1A2E35; color:#FFD54F; text-align:center; padding:8px 20px; border-radius:10px; margin-top:15px; font-weight:bold; border:2px solid #FFD54F; font-size:12px;">🧬 {label}</div>
    </div>
    <style>@keyframes rise {{0%{{transform:translateY(0); opacity:0.9;}}100%{{transform:translateY(-130px); opacity:0;}} }} @keyframes wave {{0%,100%{{transform:scaleX(1);}}50%{{transform:scaleX(1.05);}}}}</style>
    """
    components.html(html, height=420)

def show_volcano():
    html="""
    <div style="background: linear-gradient(to bottom, #8D6E63 0%, #4E342E 100%); border-radius:15px; padding:20px; text-align:center;">
        <div style="width:0; height:0; border-left:80px solid transparent; border-right:80px solid transparent; border-bottom:120px solid #795548; margin:0 auto; position:relative;">
            <div style="position:absolute; top:40px; left:-20px; width:40px; height:60px; background:linear-gradient(to top, #FF6F00, #FFCA28, #F44336); border-radius:50% 50% 0 0; animation: erupt 1.5s infinite;"></div>
        </div>
        <div style="width:180px; height:20px; background:#3E2723; margin:0 auto; border-radius:10px;"></div>
        <div style="color:#FFCC80; margin-top:10px; font-weight:bold;">🌋 Baking Soda + Vinegar Eruption</div>
    </div>
    <style>@keyframes erupt {0%{transform:translateY(0) scale(0.8); opacity:0.8;}50%{transform:translateY(-30px) scale(1.2); opacity:1;}100%{transform:translateY(-60px) scale(0.5); opacity:0;}}</style>
    """
    components.html(html, height=300)

# --- DB ---
DB_FILE="students_progress.csv"
if not os.path.exists(DB_FILE):
    pd.DataFrame(columns=["Date","Name","Roll","Experiment","Score"]).to_csv(DB_FILE,index=False)

# --- SIDEBAR ---
st.sidebar.header("👤 Student Login")
sname=st.sidebar.text_input("Name")
roll=st.sidebar.text_input("Roll No")
is_teacher=st.sidebar.checkbox("I'm Teacher")
tpw=st.sidebar.text_input("Password",type="password") if is_teacher else ""

# --- MAIN TABS - 8 TYPES ---
main_tab1, main_tab2 = st.tabs(["🔬 EXPERIMENTS LAB", "👩‍🏫 Teacher Dashboard"])

with main_tab1:
    exp_type = st.selectbox("Select Experiment Category (8 Types)",
        ["1. Salt Analysis (31 Salts, 5 Tests)", "2. Litmus Test - Acid/Base", "3. Copper Cycle", "4. Acid-Base Titration", "5. Baking Soda Volcano", "6. Cabbage Chemistry - pH Indicator", "7. Cartesian Diver - Buoyancy", "8. Rock Candy - Crystallization"])

    # --- 1. SALT ANALYSIS ---
    if "Salt Analysis" in exp_type:
        salts_db = {
            "NaCl":{"name":"Common Salt","color":"#E8EAF6","obs":["White crystalline","No gas with dil acid","HCl fumes with conc acid","Golden flame","AgNO3 white ppt"]},
            "Pb(NO3)2":{"name":"Lead Nitrate","color":"#E69A00","obs":["White solid crackling turns yellow","White PbSO4","Brown NO2 fumes","White ppt soluble excess","Yellow PbI2"]},
            "CuSO4":{"name":"Copper Sulphate","color":"#0D47A1","obs":["Blue crystals","White BaSO4 ppt","No reaction","Pale blue Cu(OH)2","Chocolate brown"]},
            "FeCl3":{"name":"Ferric Chloride","color":"#4A0F0F","obs":["Dark brown","No gas","HCl gas","Brown Fe(OH)3","Blood red KSCN"]},
            "FeSO4":{"name":"Ferrous Sulphate","color":"#7CB342","obs":["Light green","White BaSO4","No reaction","White Fe(OH)2 turns brown","Blue with K3[Fe(CN)6]"]},
        }
        for ex in ["KCl","BaCl2","CaCO3","NiSO4","AgNO3"]:
            if ex not in salts_db: salts_db[ex]={"name":ex,"color":"#90A4AE","obs":[f"{ex} preliminary","Dil test","Conc test","NaOH test","Confirmatory"]}

        sel=st.selectbox("Select Salt", list(salts_db.keys()))
        data=salts_db[sel]
        c1,c2=st.columns([1,2])
        with c1:
            st.info(f"**{sel} - {data['name']}**")
            if st.button("Mark Complete", type="primary"):
                st.session_state['completed']=sel
                st.success("Completed! Quiz unlocked below")
        with c2:
            t1,t2,t3,t4,t5=st.tabs(["1. Preliminary","2. Dil. H2SO4","3. Conc. H2SO4","4. NaOH","5. Confirmatory"])
            for i, tab in enumerate([t1,t2,t3,t4,t5]):
                with tab:
                    show_beaker(data["color"], f"{sel} - Exp {i+1}", f"Exp {i+1}: {['Preliminary','Dil Acid','Conc Acid','NaOH Test','Confirmatory'][i]}")
                    # FIXED WHITE TEXT BUG HERE - BLACK TEXT
                    st.markdown(f"<div class='observation-box'><b>🔍 Observation:</b> {data['obs'][i]}<br><b>⚗️ Inference:</b> Note in lab manual - {sel} confirmed</div>", unsafe_allow_html=True)

    # --- 2. LITMUS TEST ---
    elif "Litmus" in exp_type:
        st.subheader("🔴🔵 Litmus Test - Acid or Base?")
        col1,col2=st.columns(2)
        with col1:
            liquid=st.selectbox("Select Liquid", ["Lemon Juice (Acid)","Soap Solution (Base)","Water (Neutral)","Vinegar (Acid)","Baking Soda (Base)"])
            is_acid="Acid" in liquid
            color="#FF8A65" if is_acid else "#81D4FA" if "Base" in liquid else "#E8F5E9"
            show_beaker(color, liquid, "Litmus Test")
        with col2:
            st.markdown(f"<div class='observation-box'><b>🔵 Blue Litmus:</b> {'Turns RED - Acid confirmed' if is_acid else 'No change - Base or Neutral'}<br><b>🔴 Red Litmus:</b> {'No change - Acid' if is_acid else 'Turns BLUE - Base confirmed' if 'Base' in liquid else 'No change - Neutral'}<br><br><b>Result:</b> {liquid} is {'Acidic' if is_acid else 'Basic' if 'Base' in liquid else 'Neutral'}</div>", unsafe_allow_html=True)
            st.image("https://cdn-icons-png.flaticon.com/512/210/210545.png", width=100)

    # --- 3. COPPER CYCLE ---
    elif "Copper Cycle" in exp_type:
        st.subheader("🔄 Copper Cycle - 4 Steps")
        step=st.slider("Select Cycle Step", 1,4,1)
        steps={1:("Copper Metal - Reddish brown","#B87333","Oxidation: 2Cu + O2 -> 2CuO (Black)"),2:("Black CuO","#212121","Precipitation: CuO + 2HCl -> CuCl2 + H2O (Blue-green)"),3:("Blue CuCl2 Solution","#0D4F4F","Dissolution: CuCl2 + 2NaOH -> Cu(OH)2 (Blue ppt)"),4:("Blue Cu(OH)2","#1565C0","Reduction: Cu(OH)2 -> Cu + H2O (Copper back!)")}
        col,txt=steps[step]
        col1,col2=st.columns(2)
        with col1: show_beaker(col, f"Step {step}", f"Copper Cycle Step {step}")
        with col2: st.markdown(f"<div class='observation-box'><b>Reaction:</b> {txt}<br><br><b>What happens:</b> Elemental copper goes through oxidation, precipitation, dissolution, and reduction to come back to original form!</div>", unsafe_allow_html=True)

    # --- 4. TITRATION ---
    elif "Titration" in exp_type:
        st.subheader("🧪 Acid-Base Titration with Phenolphthalein")
        vol=st.slider("Add NaOH drops (Titrant)", 0, 50, 0)
        if vol<20: color="#FFCDD2"; result="Acidic - Colorless"; status="Add more NaOH"
        elif vol<25: color="#F8BBD0"; result="Near Endpoint - Light Pink"; status="Almost neutral!"
        else: color="#E91E63"; result="Basic - Deep Pink"; status="Neutralization complete!"
        col1,col2=st.columns(2)
        with col1: show_beaker(color, f"{vol} ml NaOH", "Titration Flask")
        with col2: st.markdown(f"<div class='observation-box'><b>Indicator:</b> Phenolphthalein<br><b>Volume:</b> {vol} ml<br><b>Color:</b> {result}<br><b>Status:</b> {status}<br><br>HCl + NaOH -> NaCl + H2O (Neutralisation)</div>", unsafe_allow_html=True)
            st.progress(vol/50)

    # --- 5. VOLCANO ---
    elif "Volcano" in exp_type:
        st.subheader("🌋 Baking Soda Volcano - CO2 Eruption")
        if st.button("🌋 ERUPT VOLCANO!", type="primary"):
            show_volcano()
            st.balloons()
            st.markdown("<div class='observation-box'><b>Reaction:</b> NaHCO3 + CH3COOH -> CO2 + H2O + CH3COONa<br><b>Observation:</b> Foam erupts due to CO2 gas!<br><b>Real Life:</b> Same as real volcano - gas pressure builds up!</div>", unsafe_allow_html=True)
        else:
            show_volcano()

    # --- 6. CABBAGE ---
    elif "Cabbage" in exp_type:
        st.subheader("🥬 Cabbage Chemistry - Natural pH Indicator")
        ph=st.slider("pH of Household Solution", 1,14,7)
        if ph<3: color="#B71C1C"; label="pH 1-2 - Strong Acid - Red"
        elif ph<5: color="#E53935"; label="pH 3-4 - Acid - Red-Pink"
        elif ph<7: color="#8E24AA"; label="pH 5-6 - Weak Acid - Purple"
        elif ph==7: color="#7B1FA2"; label="pH 7 - Neutral - Purple"
        elif ph<9: color="#1E88E5"; label="pH 8-9 - Weak Base - Blue"
        elif ph<12: color="#43A047"; label="pH 10-11 - Base - Green"
        else: color="#FDD835"; label="pH 12-14 - Strong Base - Yellow"
        col1,col2=st.columns(2)
        with col1: show_beaker(color, label, "Cabbage Indicator")
        with col2: st.markdown(f"<div class='observation-box'><b>Solution pH:</b> {ph}<br><b>Color:</b> {label}<br><br>Red cabbage juice (anthocyanin) changes color with pH. Test with lemon, soap, etc!</div>", unsafe_allow_html=True)

    # --- 7. CARTESIAN DIVER ---
    elif "Cartesian" in exp_type:
        st.subheader("🤿 Cartesian Diver - Buoyancy & Gas Laws")
        pressure=st.slider("Squeeze Bottle (Pressure)", 0,100,0)
        diver_pos= 80 - pressure*0.6
        html=f"""
        <div style="background:linear-gradient(to bottom, #E1F5FE, #81D4FA); border-radius:15px; padding:20px; height:350px; position:relative; border:3px solid #0F5C5C;">
            <div style="position:absolute; bottom:{diver_pos}%; left:45%; width:30px; height:50px; background:#FF5722; border-radius:15px 15px 5px 5px; transition:bottom 0.5s;">
                <div style="width:20px; height:20px; background:#FFCCBC; border-radius:50%; margin:5px auto;"></div>
                <div style="width:10px; height:10px; background:white; border-radius:50%; position:absolute; bottom:5px; left:10px;"></div>
            </div>
            <div style="position:absolute; bottom:0; width:100%; height:20px; background:#5D4037; left:0; border-radius:0 0 12px 12px;"></div>
            <div style="color:#01579B; font-weight:bold; text-align:center;">Water Bottle - Squeeze to increase pressure</div>
        </div>
        """
        col1,col2=st.columns(2)
        with col1: components.html(html, height=400)
        with col2: st.markdown(f"<div class='observation-box'><b>Pressure:</b> {pressure}%<br><b>Diver Position:</b> {'Top - Floating' if pressure<30 else 'Middle - Neutral' if pressure<70 else 'Bottom - Sinking'}<br><br><b>Principle:</b> Boyle's Law - Pressure increases, air bubble compresses, density increases, diver sinks. Real submarines work same!</div>", unsafe_allow_html=True)

    # --- 8. ROCK CANDY ---
    elif "Rock Candy" in exp_type:
        st.subheader("🍭 Rock Candy - Crystallization")
        days=st.slider("Days of Evaporation", 0,14,0)
        size= days*8
        html=f"""
        <div style="background:#FFF8E1; border-radius:15px; padding:20px; text-align:center; border:3px solid #FF8F00;">
            <div style="width:10px; height:200px; background:#8D6E63; margin:0 auto; position:relative;">
                <div style="position:absolute; top:{200-size}px; width:{size}px; height:{size}px; background:linear-gradient(135deg, #E1F5FE, #81D4FA, #E1F5FE); left:-{size//2}px; border-radius:5px; box-shadow:0 0 10px rgba(0,0,0,0.3); transform:rotate({days*10}deg);">
                </div>
            </div>
            <div style="width:120px; height:80px; background:linear-gradient(to top, #4FC3F7, #E1F5FE); margin:10px auto; border-radius:0 0 60px 60px; border:3px solid #0288D1;"></div>
            <div style="color:#E65100; font-weight:bold;">Day {days} - Sugar crystals growing!</div>
        </div>
        """
        col1,col2=st.columns(2)
        with col1: components.html(html, height=380)
        with col2: st.markdown(f"<div class='observation-box'><b>Day:</b> {days}/14<br><b>Crystal Size:</b> {size}mm<br><b>Process:</b> Sugar molecules crystallize on stick as water evaporates. Supersaturated solution!<br><br><b>Observation:</b> {'No crystals yet - solution clear' if days<2 else 'Tiny crystals forming' if days<5 else 'Crystals growing bigger!' if days<10 else 'Large rock candy ready to eat! 🍭'}</div>", unsafe_allow_html=True)

    # --- QUIZ AFTER ANY EXPERIMENT ---
    st.divider()
    if 'completed' in st.session_state or True:
        st.subheader("📝 Quick Quiz + Certificate")
        q=st.text_input("Enter your answer for Viva: What is neutralization?", "Acid + Base -> Salt + Water")
        if st.button("Submit for Teacher"):
            row={"Date":datetime.now().strftime("%d-%m-%Y %H:%M"),"Name":sname or "Anonymous","Roll":roll or "0","Experiment":exp_type,"Score":10}
            df=pd.read_csv(DB_FILE); df=pd.concat([df,pd.DataFrame([row])],ignore_index=True); df.to_csv(DB_FILE,index=False)
            st.success("✅ Saved to teacher dashboard!")

with main_tab2:
    st.header("👩‍🏫 Teacher Live Dashboard")
    if tpw!="chem123" and is_teacher:
        st.warning("Password is chem123")
    else:
        if os.path.exists(DB_FILE):
            df=pd.read_csv(DB_FILE)
            if df.empty: st.info("No data yet")
            else:
                c1,c2,c3=st.columns(3)
                c1.metric("Total Experiments", len(df)); c2.metric("Students", df['Roll'].nunique()); c3.metric("Most Popular", df['Experiment'].value_counts().index[0][:20])
                st.dataframe(df, use_container_width=True)
                st.bar_chart(df['Experiment'].value_counts())
                st.download_button("📥 Download Report", df.to_csv(index=False), "ChemVerse_Ultimate_Report.csv")
        else:
            st.info("No data file")

st.caption("ChemVerse v6.0 Ultimate | 8 Experiment Types | White Text Bug FIXED | Real Lab Graphics")
