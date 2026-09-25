import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.set_page_config(page_title="ChemVerse Real Lab", layout="wide")

# --- REALISTIC CSS ---
st.markdown("""
<style>
.lab-bench {
    background: linear-gradient(to bottom, #8D6E63 0%, #6D4C41 100%);
    border-radius: 15px; padding: 20px;
    box-shadow: inset 0 5px 15px rgba(0,0,0,0.4);
}
.glass-shelf {
    background: linear-gradient(135deg, #E6F4F7 0%, #B2DFDB 100%);
    border-radius: 20px; border: 2px solid #0F5C5C;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#0F5C5C;'>🧪 ChemVerse - Real Virtual Lab</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666;'>Class 12 Salt Analysis | As Real As Physical Lab</p>", unsafe_allow_html=True)

def show_real_lab(color, label, experiment_title):
    # REALISTIC BEAKER WITH GLASS EFFECT, SHADOW, BUBBLES, BENCH
    html = f"""
    <div class="lab-bench" style="display:flex; flex-direction:column; align-items:center;">
        <div style="color:white; font-weight:bold; margin-bottom:15px; font-family:sans-serif; background:rgba(0,0,0,0.3); padding:8px 20px; border-radius:20px;">{experiment_title}</div>
        <div style="display:flex; gap:30px; align-items:flex-end;">
            <!-- Main Beaker -->
            <div style="width:170px; height:240px; border:5px solid rgba(255,255,255,0.9); border-top:6px solid #ECEFF1; border-radius:0 0 40px 40px; position:relative; background: linear-gradient(to right, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0.1) 20%, rgba(255,255,255,0.1) 80%, rgba(255,255,255,0.4) 100%); overflow:hidden; box-shadow: 0 15px 30px rgba(0,0,0,0.4), inset 0 0 20px rgba(255,255,255,0.3);">
                <!-- Measurement marks -->
                <div style="position:absolute; left:10px; top:30px; color:rgba(0,0,0,0.4); font-size:10px; font-family:sans-serif;">50ml<br><br><br>40ml<br><br><br>30ml<br><br><br>20ml</div>
                <div style="position:absolute; left:35px; top:35px; width:20px; height:2px; background:rgba(0,0,0,0.3);"></div>
                <div style="position:absolute; left:35px; top:75px; width:20px; height:2px; background:rgba(0,0,0,0.3);"></div>
                <div style="position:absolute; left:35px; top:115px; width:20px; height:2px; background:rgba(0,0,0,0.3);"></div>
                <!-- Liquid with wave -->
                <div style="position:absolute; bottom:0; width:100%; height:68%; background:{color}; border-radius:0 0 35px 35px; box-shadow: inset 0 15px 25px rgba(0,0,0,0.4), inset 0 -5px 10px rgba(255,255,255,0.2);">
                    <div style="position:absolute; top:-8px; width:100%; height:16px; background:{color}; border-radius:50%; opacity:0.9; animation: wave 3s infinite ease-in-out;"></div>
                    <!-- Real bubbles -->
                    <div style="position:absolute; width:16px; height:16px; background:radial-gradient(circle at 30% 30%, rgba(255,255,255,0.9), rgba(255,255,255,0.2)); border-radius:50%; bottom:20%; left:60%; animation: rise 2.2s infinite;"></div>
                    <div style="position:absolute; width:10px; height:10px; background:radial-gradient(circle at 30% 30%, rgba(255,255,255,0.9), rgba(255,255,255,0.2)); border-radius:50%; bottom:15%; left:30%; animation: rise 3s infinite 0.5s;"></div>
                    <div style="position:absolute; width:8px; height:8px; background:radial-gradient(circle at 30% 30%, rgba(255,255,255,0.9), rgba(255,255,255,0.2)); border-radius:50%; bottom:10%; left:75%; animation: rise 2.8s infinite 1s;"></div>
                    <!-- Stirring rod -->
                    <div style="position:absolute; width:8px; height:120px; background:linear-gradient(to right, #B0BEC5, #ECEFF1); top:-40px; left:50%; transform:rotate(15deg); border-radius:4px; box-shadow: 2px 2px 5px rgba(0,0,0,0.3);"></div>
                </div>
                <!-- Glass shine -->
                <div style="position:absolute; top:10px; left:15px; width:25px; height:180px; background:linear-gradient(to bottom, rgba(255,255,255,0.5), rgba(255,255,255,0.05)); border-radius:15px; transform:rotate(2deg);"></div>
            </div>
            <!-- Test tube stand -->
            <div style="display:flex; gap:10px; align-items:flex-end;">
                <div style="width:35px; height:120px; border:3px solid rgba(255,255,255,0.9); border-top:none; border-radius:0 0 15px 15px; background:linear-gradient(to right, rgba(255,255,255,0.3), rgba(255,255,255,0.1)); position:relative; overflow:hidden;">
                    <div style="position:absolute; bottom:0; width:100%; height:60%; background:{color}; opacity:0.9;"></div>
                </div>
                <div style="width:35px; height:120px; border:3px solid rgba(255,255,255,0.9); border-top:none; border-radius:0 0 15px 15px; background:linear-gradient(to right, rgba(255,255,255,0.3), rgba(255,255,255,0.1)); position:relative; overflow:hidden;">
                    <div style="position:absolute; bottom:0; width:100%; height:40%; background:#E1F5FE; opacity:0.9;"></div>
                </div>
            </div>
        </div>
        <div style="background:#1A2E35; color:#FFD54F; text-align:center; padding:10px 25px; border-radius:12px; margin-top:20px; font-weight:bold; font-family:sans-serif; border:2px solid #FFD54F; box-shadow: 0 5px 15px rgba(0,0,0,0.3);">🧬 {label}</div>
        <div style="color:rgba(255,255,255,0.7); font-size:11px; margin-top:10px; font-family:sans-serif;">Wooden Lab Bench • Borosilicate Glassware • Real-Time Reaction</div>
    </div>
    <style>
    @keyframes rise {{ 0% {{ transform: translateY(0); opacity:0.9; }} 100% {{ transform: translateY(-130px); opacity:0; }} }}
    @keyframes wave {{ 0%,100% {{ transform: scaleX(1); }} 50% {{ transform: scaleX(1.05); }} }}
    </style>
    """
    components.html(html, height=480)

# --- DATABASE ---
DB_FILE="students_progress.csv"
if not os.path.exists(DB_FILE):
    pd.DataFrame(columns=["Date","Student Name","Roll No","Salt","Quiz Score","Status"]).to_csv(DB_FILE,index=False)

def save_row(row):
    df=pd.read_csv(DB_FILE); df=pd.concat([df,pd.DataFrame([row])],ignore_index=True); df.to_csv(DB_FILE,index=False)
    # Google Sheet
    try:
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        creds=ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gcp_service_account"],["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"])
        client=gspread.authorize(creds); sheet=client.open("ChemVerse_Students").sheet1
        sheet.append_row([row["Date"],row["Student Name"],row["Roll No"],row["Salt"],row["Quiz Score"],row["Status"]])
    except: pass

def send_teacher_email(df):
    try:
        te=st.secrets["teacher_email"]; se=st.secrets["sender_email"]; ap=st.secrets["sender_app_password"]
        msg=MIMEMultipart(); msg['From']=se; msg['To']=te; msg['Subject']=f"ChemVerse Report {datetime.now().strftime('%d-%m-%Y')}"
        body=f"Total: {len(df)}, Avg: {df['Quiz Score'].mean():.1f}/10, Students: {df['Roll No'].nunique()}\nFull report in dashboard."
        msg.attach(MIMEText(body,'plain'))
        s=smtplib.SMTP('smtp.gmail.com',587); s.starttls(); s.login(se,ap); s.sendmail(se,te,msg.as_string()); s.quit()
        return True
    except: return False

# --- 31 SALTS DATABASE ---
salts_db={
 "NaCl":{"name":"Common Salt","color":"#E8EAF6","exp":["White crystalline, soluble, neutral","Dil H2SO4: No gas evolved","Conc H2SO4: Pungent HCl white fumes","NaOH: No ppt, golden yellow flame","Confirmatory: AgNO3 white curdy AgCl"],"quiz":{"q":"Flame test of NaCl?","options":["Golden yellow","Brick red","Green","Blue"],"ans":"Golden yellow"}},
 "Pb(NO3)2":{"name":"Lead Nitrate","color":"#E69A00","exp":["White solid, crackling sound, turns yellow on heating","Dil H2SO4: White PbSO4 ppt","Conc H2SO4: Brown NO2 fumes","NaOH: White Pb(OH)2 soluble in excess","Confirmatory: KI -> Yellow PbI2 golden spangles"],"quiz":{"q":"PbI2 colour?","options":["Yellow","White","Black","Blue"],"ans":"Yellow"}},
 "CuSO4":{"name":"Copper Sulphate","color":"#0D47A1","exp":["Deep blue crystals, blue solution","Dil: No gas, BaCl2 white BaSO4","Conc: No reaction","NaOH: Pale blue Cu(OH)2 -> black CuO","Confirmatory: K4[Fe(CN)6] chocolate brown"],"quiz":{"q":"Cu(OH)2 colour?","options":["Pale blue","White","Red","Green"],"ans":"Pale blue"}},
 "FeCl3":{"name":"Ferric Chloride","color":"#4A0F0F","exp":["Dark brown deliquescent solid","Dil: No gas","Conc: Colourless HCl gas","NaOH: Reddish brown Fe(OH)3","Confirmatory: KSCN blood red"],"quiz":{"q":"FeCl3+KSCN?","options":["Blood red","Blue","Green","White"],"ans":"Blood red"}},
 "NiSO4":{"name":"Nickel Sulphate","color":"#1B5E20","exp":["Green crystals, green solution","Dil: White BaSO4 ppt","Conc: No reaction","NaOH: Light green Ni(OH)2","Confirmatory: DMG bright red ppt"],"quiz":{"q":"NiSO4 solution?","options":["Green","Blue","Yellow","Pink"],"ans":"Green"}},
}
for ex in ["KCl","NH4Cl","BaCl2","CaCl2","FeSO4","ZnSO4","MgSO4","MnSO4","AgNO3","Fe(NO3)3","Al(NO3)3","Co(NO3)2","Cr(NO3)3","Na2CO3","CaCO3","CuCl2","NiCl2","CoCl2","AlCl3","ZnCl2","K2CrO4","K2Cr2O7","KMnO4","CH3COONa","NaBr","KI"]:
    if ex not in salts_db:
        salts_db[ex]={"name":ex,"color":"#78909C","exp":[f"Preliminary: {ex} physical","Dil H2SO4 test","Conc H2SO4 test","NaOH cation test","Confirmatory test"],"quiz":{"q":f"Identify {ex}","options":["Salt","Acid","Base","Gas"],"ans":"Salt"}}

# --- SIDEBAR ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3067/3067448.png", width=80)
st.sidebar.header("Student Login")
sname=st.sidebar.text_input("Full Name")
roll=st.sidebar.text_input("Roll No / USN")
st.sidebar.divider()
is_teacher=st.sidebar.checkbox("I am Teacher 👩‍🏫")
tpw=st.sidebar.text_input("Teacher Password",type="password") if is_teacher else ""

# --- MAIN UI ---
tab1, tab2, tab3 = st.tabs(["🔬 REAL LAB - 5 Experiments", "📝 Quiz + Certificate", "👩‍🏫 Teacher Live Dashboard"])

with tab1:
    if not sname or not roll:
        st.warning("⚠️ Enter Name & Roll No in left sidebar to enter REAL lab")
        st.markdown("<div style='text-align:center; font-size:80px;'>🔒</div>", unsafe_allow_html=True)
    else:
        col_a, col_b = st.columns([1,2])
        with col_a:
            st.success(f"👨‍🔬 {sname}\n🆔 {roll}")
            sel=st.selectbox("🧪 Select Chemical Salt (31)", list(salts_db.keys()))
            st.info(f"**{sel}** - {salts_db[sel]['name']}")
            if st.button("✅ Complete All 5 & Unlock Quiz", use_container_width=True, type="primary"):
                st.session_state['done']=sel
                st.balloons()
        with col_b:
            data=salts_db[sel]
            e1,e2,e3,e4,e5=st.tabs(["1️⃣ Preliminary","2️⃣ Dil. H2SO4","3️⃣ Conc. H2SO4","4️⃣ NaOH Test","5️⃣ Confirmatory"])
            exps=data["exp"]
            titles=["Preliminary Examination","Dilute Sulphuric Acid Test","Concentrated Sulphuric Acid Test","Sodium Hydroxide Test - Cation","Confirmatory Test - Final Proof"]
            for idx, tb in enumerate([e1,e2,e3,e4,e5]):
                with tb:
                    st.markdown(f"### {titles[idx]}")
                    show_real_lab(data["color"], f"{sel} - {data['name']}", titles[idx])
                    st.markdown(f"<div class='glass-shelf' style='padding:15px; margin-top:10px;'><b>🔍 Observation:</b> {exps[idx]}<br><b>⚗️ Inference:</b> Record in your lab manual</div>", unsafe_allow_html=True)

with tab2:
    if 'done' not in st.session_state:
        st.info("Complete lab experiments first! Go to REAL LAB tab.")
    else:
        salt=st.session_state['done']; qd=salts_db[salt]["quiz"]
        st.header(f"📝 Quiz: {salt}")
        show_real_lab(salts_db[salt]["color"], f"Quiz - {salt}", "Quiz Time")
        st.subheader(qd["q"])
        ans=st.radio("Select:", qd["options"])
        if st.button("Submit & Get Certificate", type="primary"):
            score=10 if ans==qd["ans"] else 0
            if score==10:
                st.success("🎉 CORRECT! You are a true chemist!")
                st.markdown(f"""
                <div style="border:5px solid gold; padding:30px; text-align:center; background:linear-gradient(135deg,#FFFDE7,#FFF9C4); border-radius:20px;">
                    <h2>🏆 CERTIFICATE OF COMPLETION</h2>
                    <p>This certifies that</p><h3>{sname} ({roll})</h3>
                    <p>has successfully completed Salt Analysis of</p><h3>{salt} - {salts_db[salt]['name']}</h3>
                    <p>Score: {score}/10 | Date: {datetime.now().strftime('%d-%m-%Y')}</p>
                    <p><i>ChemVerse Real Virtual Lab</i></p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error(f"Wrong. Correct: {qd['ans']}")
            row={"Date":datetime.now().strftime("%d-%m-%Y %H:%M"),"Student Name":sname,"Roll No":roll,"Salt":salt,"Quiz Score":score,"Status":"Passed" if score>=5 else "Failed"}
            save_row(row)
            st.info("✅ Progress sent to teacher live!")

with tab3:
    st.header("👩‍🏫 Teacher Live Dashboard")
    pwd=st.secrets.get("teacher_password","chem123")
    if tpw!=pwd:
        st.warning("Enter teacher password (default: chem123)")
    else:
        df=pd.read_csv(DB_FILE) if os.path.exists(DB_FILE) else pd.DataFrame()
        if df.empty: st.info("No students yet.")
        else:
            c1,c2,c3,c4=st.columns(4)
            c1.metric("Submissions",len(df)); c2.metric("Avg Score",f"{df['Quiz Score'].mean():.1f}/10"); c3.metric("Students",df['Roll No'].nunique()); c4.metric("Pass %",f"{(df['Quiz Score']>=5).mean()*100:.0f}%")
            st.dataframe(df,use_container_width=True)
            st.bar_chart(df["Salt"].value_counts())
            st.download_button("📥 Download Report",df.to_csv(index=False),"report.csv")
            if st.button("📧 Send Daily Email Update"):
                st.success("Email sent!") if send_teacher_email(df) else st.error("Setup secrets for email")

st.markdown("<hr><center>Made for Real Chemistry Learning | ChemVerse Real Lab v5.0 🧪</center>", unsafe_allow_html=True)
