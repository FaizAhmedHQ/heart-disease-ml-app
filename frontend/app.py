import streamlit as st
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Heart Disease Detection",
    page_icon="💖",
    layout="centered"
)

# ---------------- FORCE LIGHT MODE ----------------
st.markdown("""
<style>

/* Remove Streamlit dark background completely */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ffd1dc, #fff0f5) !important;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

[data-testid="stToolbar"] {
    background: transparent !important;
}

[data-testid="stSidebar"] {
    background: #fff0f5 !important;
}

/* Main block container */
.block-container {
    padding: 2rem;
    background: transparent !important;
}

/* Title */
.main-title {
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    color: #b30059;
}

.subtitle {
    text-align: center;
    color: #800040;
    margin-bottom: 25px;
    font-size: 18px;
}

/* Card */
.card {
    background-color: white;
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0px 10px 30px rgba(255, 0, 102, 0.25);
}

/* Button */
.stButton > button {
    background-color: #ff4d88;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    border: none;
}

.stButton > button:hover {
    background-color: #e6005c;
}

/* Make input labels visible */
label {
    color: #7a003c !important;
    font-weight: 600;
    font-size: 15px;
}

/* Streamlit widget labels */
.stSelectbox label,
.stNumberInput label,
.stTextInput label {
    color: #7a003c !important;
}


</style>
""", unsafe_allow_html=True)


# ---------------- TITLE ----------------
st.markdown("<div class='main-title'>💖 Heart Disease Detection</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI-Powered Clinical Prediction System</div>", unsafe_allow_html=True)

# ---------------- FORM CARD ----------------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 1, 120)
        sex = st.selectbox("Sex", [0,1], format_func=lambda x: "Female" if x==0 else "Male")
        chest_pain = st.selectbox("Chest Pain Type (0-3)", [0,1,2,3])
        resting_bp = st.number_input("Resting Blood Pressure")
        cholesterol = st.number_input("Cholesterol")
        fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0,1])

    with col2:
        resting_ecg = st.selectbox("Resting ECG (0-2)", [0,1,2])
        max_hr = st.number_input("Max Heart Rate")
        ex_angina = st.selectbox("Exercise Induced Angina", [0,1])
        st_depression = st.number_input("ST Depression")
        st_slope = st.selectbox("ST Slope (0-2)", [0,1,2])
        vessels = st.selectbox("Major Vessels (0-3)", [0,1,2,3])
        thal = st.selectbox("Thalassemia (1=Normal,2=Fixed,3=Reversible)", [1,2,3])

    if st.button("💗 Predict Now"):
        payload = {
            "Age": age,
            "Sex": sex,
            "Chest_Pain_Type": chest_pain,
            "Resting_Blood_Pressure": resting_bp,
            "Cholesterol": cholesterol,
            "Fasting_Blood_Sugar": fasting_bs,
            "Resting_ECG": resting_ecg,
            "Max_Heart_Rate": max_hr,
            "Exercise_Induced_Angina": ex_angina,
            "ST_Depression": st_depression,
            "ST_Slope": st_slope,
            "Num_Major_Vessels": vessels,
            "Thalassemia": thal
        }

        res = requests.post(
            "https://heart-disease-ml-app-mgbt.onrender.com/predict",
            json=payload
        )

        if res.status_code == 200:
            result = res.json()
            if result["prediction"] == 1:
                st.markdown("<div class='error-box'>⚠️ Heart Disease Detected</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='success-box'>✅ No Heart Disease Detected</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
