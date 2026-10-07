import streamlit as st

# ---------------------------------------------------------
# AI SMART HEALTH MONITOR
# Academic Demonstration Prototype
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Smart Health Monitor",
    page_icon="🏥",
    layout="centered"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a, #172554, #312e81);
        color: white;
    }

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #dbeafe;
        margin-bottom: 30px;
    }

    .card {
        background: rgba(255, 255, 255, 0.10);
        border-radius: 18px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid rgba(255,255,255,0.15);
    }

    .result-normal {
        background: #14532d;
        padding: 22px;
        border-radius: 18px;
        text-align: center;
        margin-top: 20px;
    }

    .result-warning {
        background: #854d0e;
        padding: 22px;
        border-radius: 18px;
        text-align: center;
        margin-top: 20px;
    }

    .result-danger {
        background: #991b1b;
        padding: 22px;
        border-radius: 18px;
        text-align: center;
        margin-top: 20px;
    }

    .metric-title {
        font-size: 18px;
        font-weight: bold;
    }

    .metric-value {
        font-size: 30px;
        font-weight: bold;
    }

    .footer {
        text-align: center;
        color: #cbd5e1;
        font-size: 13px;
        margin-top: 35px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">🏥 AI Smart Health Monitor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-Based Smart Health Monitoring & Emergency Alert System'
    '</div>',
    unsafe_allow_html=True
)

st.info(
    "Enter the patient's health readings. "
    "The prototype will classify the current risk level."
)

# ---------------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------------

st.subheader("📊 Enter Health Readings")

col1, col2 = st.columns(2)

with col1:
    heart_rate = st.number_input(
        "❤️ Heart Rate (BPM)",
        min_value=30,
        max_value=220,
        value=82,
        step=1
    )

    spo2 = st.number_input(
        "🫁 SpO₂ (%)",
        min_value=50,
        max_value=100,
        value=98,
        step=1
    )

with col2:
    temperature = st.number_input(
        "🌡️ Temperature (°C)",
        min_value=30.0,
        max_value=45.0,
        value=36.7,
        step=0.1,
        format="%.1f"
    )

    age = st.number_input(
        "👤 Age",
        min_value=1,
        max_value=120,
        value=20,
        step=1
    )

# ---------------------------------------------------------
# ANALYSIS FUNCTION
# ---------------------------------------------------------

def analyze_health(heart_rate, spo2, temperature):
    """
    Simple rule-based risk classification
    for academic demonstration.
    """

    emergency = False
    warning = False
    reasons = []

    # SpO2 analysis
    if spo2 < 90:
        emergency = True
        reasons.append("Very low SpO₂")
    elif spo2 < 94:
        warning = True
        reasons.append("Low SpO₂")

    # Heart rate analysis
    if heart_rate < 50 or heart_rate > 120:
        emergency = True
        reasons.append("Abnormal heart rate")
    elif heart_rate < 60 or heart_rate > 100:
        warning = True
        reasons.append("Heart rate outside typical resting range")

    # Temperature analysis
    if temperature >= 39.0 or temperature < 35.0:
        emergency = True
        reasons.append("Abnormal body temperature")
    elif temperature >= 38.0:
        warning = True
        reasons.append("Elevated temperature")

    # Final classification
    if emergency:
        return "EMERGENCY", reasons

    if warning:
        return "WARNING", reasons

    return "NORMAL", ["No abnormal risk detected in this prototype"]


# ---------------------------------------------------------
# ANALYZE BUTTON
# ---------------------------------------------------------

st.markdown("---")

if st.button("🔍 Analyze Health", use_container_width=True):

    status, reasons = analyze_health(
        heart_rate,
        spo2,
        temperature
    )

    # -----------------------------------------------------
    # DISPLAY HEALTH READINGS
    # -----------------------------------------------------

    st.subheader("📋 Health Analysis")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""
            <div class="card">
                <div class="metric-title">❤️ Heart Rate</div>
                <div class="metric-value">{heart_rate} BPM</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="card">
                <div class="metric-title">🫁 SpO₂</div>
                <div class="metric-value">{spo2}%</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class="card">
                <div class="metric-title">🌡️ Temperature</div>
                <div class="metric-value">{temperature:.1f} °C</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # -----------------------------------------------------
    # RESULT
    # -----------------------------------------------------

    if status == "NORMAL":

        st.markdown(
            """
            <div class="result-normal">
                <h2>🟢 NORMAL</h2>
                <p>No abnormal risk detected in this prototype.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif status == "WARNING":

        st.markdown(
            """
            <div class="result-warning">
                <h2>🟠 WARNING</h2>
                <p>Some readings require attention.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.warning("⚠️ Please review the following readings.")

    else:

        st.markdown(
            """
            <div class="result-danger">
                <h2>🔴 EMERGENCY</h2>
                <p>Potentially concerning readings detected.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.error(
            "🚨 Emergency Alert: Please seek appropriate medical "
            "attention immediately."
        )

    # -----------------------------------------------------
    # REASONS
    # -----------------------------------------------------

    st.subheader("🔎 Analysis Details")

    for reason in reasons:
        st.write("•", reason)

    # -----------------------------------------------------
    # EMERGENCY ALERT
    # -----------------------------------------------------

    if status == "EMERGENCY":

        st.markdown("---")

        st.subheader("🚨 Emergency Alert System")

        st.error(
            "Emergency condition detected. "
            "This prototype can be extended to notify "
            "family members, caregivers, or emergency services."
        )

    # -----------------------------------------------------
    # DEMO INFORMATION
    # -----------------------------------------------------

    st.markdown("---")

    st.caption(
        f"Patient Age: {age} years | "
        f"Heart Rate: {heart_rate} BPM | "
        f"SpO₂: {spo2}% | "
        f"Temperature: {temperature:.1f} °C"
    )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="footer">
        AI Smart Health Monitor | Academic Demonstration Prototype<br>
        This system is not a medical diagnostic device.
    </div>
    """,
    unsafe_allow_html=True
)
