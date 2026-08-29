import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import sys
import os

# App folder ko Python Path mein add karna taake import ho sake
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services.evaluator import evaluate_credit_risk, evaluate_fraud_risk

# Streamlit Page Config
st.set_page_config(
    page_title="FinRisk AI Engine",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header Banner
st.markdown("""
    <div style="background-color: #1E293B; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #3B82F6; margin-bottom: 2rem;">
        <h1 style="color: #F8FAFC; margin: 0;">🛡️ FinRisk AI — Enterprise Engine</h1>
        <p style="color: #94A3B8; margin: 5px 0 0 0;">Real-Time Credit Underwriting & Transaction Anomaly Detection Engine</p>
    </div>
""", unsafe_allow_html=True)

# Navigation Sidebar
st.sidebar.title("💳 Navigation Module")
app_mode = st.sidebar.radio(
    "Select Interface Mode:",
    ["Credit Applicant Evaluator", "Real-Time Fraud Monitor"]
)

# ==========================================
# MODULE 1: CREDIT APPLICANT EVALUATOR
# ==========================================
if app_mode == "Credit Applicant Evaluator":
    st.subheader("📋 Applicant Risk Profile & Underwriting")
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.markdown("#### Input Applicant Metrics")
        cust_id = st.text_input("Customer ID", value="CUST-99201")
        annual_inc = st.number_input("Annual Income ($)", value=75000, step=2500)
        dti = st.slider("Debt-to-Income (DTI) Ratio", 0.05, 0.65, 0.28, 0.01)
        emp_years = st.slider("Employment History (Years)", 0.0, 35.0, 6.5, 0.5)
        open_lines = st.number_input("Open Credit Lines", value=4, min_value=1, max_value=20)
        delinq_2yrs = st.selectbox("Delinquencies (Past 2 Years)", [0, 1, 2, 3])
        inq_6m = st.number_input("Credit Inquiries (Past 6 Months)", value=1, min_value=0, max_value=10)
        repay_score = st.slider("Historical Bureau Score", 300, 850, 710)
        
        eval_btn = st.button("Evaluate Credit Risk", type="primary", use_container_width=True)

    with col2:
        if eval_btn:
            payload = {
                "customer_id": cust_id,
                "annual_income": float(annual_inc),
                "debt_to_income": float(dti),
                "employment_years": float(emp_years),
                "open_credit_lines": int(open_lines),
                "delinquencies_2yrs": int(delinq_2yrs),
                "credit_inquiries_6m": int(inq_6m),
                "repayment_score": float(repay_score)
            }
            
            try:
                # Direct Import Call (No API network delay!)
                data = evaluate_credit_risk(payload)
                
                status = data["approval_status"]
                status_color = "#22C55E" if status == "APPROVED" else ("#F59E0B" if status == "MANUAL REVIEW" else "#EF4444")
                
                st.markdown(f"""
                    <div style="background-color: #1E293B; padding: 1.2rem; border-radius: 8px; text-align: center; border: 1px solid {status_color};">
                        <h3 style="margin: 0; color: #94A3B8;">DECISION STATUS</h3>
                        <h1 style="color: {status_color}; margin: 5px 0;">{status}</h1>
                        <p style="color: #CBD5E1; margin: 0;">{data['recommendation']}</p>
                    </div>
                """, unsafe_allow_html=True)
                
                fig_gauge = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=data["risk_score"],
                    domain={'x': [0, 1], 'y': [0, 1]},
                    title={'text': "CreditShield Risk Score (300-850)", 'font': {'color': "white"}},
                    gauge={
                        'axis': {'range': [300, 850], 'tickcolor': "white"},
                        'bar': {'color': "#3B82F6"},
                        'steps': [
                            {'range': [300, 550], 'color': '#7F1D1D'},
                            {'range': [550, 700], 'color': '#78350F'},
                            {'range': [700, 850], 'color': '#14532D'}
                        ]
                    }
                ))
                fig_gauge.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={'color': "white"}, height=250)
                st.plotly_chart(fig_gauge, use_container_width=True)
                
                st.markdown("#### Decision Explainability (Feature Impact)")
                feat_imp = data["feature_importance"]
                df_imp = pd.DataFrame(list(feat_imp.items()), columns=['Feature', 'Importance']).sort_values(by='Importance', ascending=True)
                
                fig_bar = px.bar(df_imp, x='Importance', y='Feature', orientation='h', color='Importance', color_continuous_scale='Blues')
                fig_bar.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font={'color': "white"}, height=250)
                st.plotly_chart(fig_bar, use_container_width=True)
                
            except Exception as e:
                st.error(f"Error evaluating model: {e}")

# ==========================================
# MODULE 2: REAL-TIME FRAUD MONITOR
# ==========================================
else:
    st.subheader("🚨 Real-Time Transaction Anomaly Feed")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("#### Live Transaction Simulator")
        txn_id = st.text_input("Transaction ID", value="TXN-88219")
        amount = st.number_input("Transaction Amount ($)", value=3400.0)
        velocity = st.slider("Velocity (1 Hour Count)", 1, 15, 6)
        is_intl = st.radio("Is International?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        distance = st.number_input("Distance from Home (KM)", value=1200.0)
        merchant_risk = st.slider("Merchant Risk Rating (1-5)", 1.0, 5.0, 4.8)
        failed_pin = st.selectbox("Failed PIN Attempts", [0, 1, 2, 3], index=2)
        
        fraud_btn = st.button("Scan Transaction", type="primary", use_container_width=True)

    with col2:
        if fraud_btn:
            payload = {
                "transaction_id": txn_id,
                "amount": float(amount),
                "velocity_1h": int(velocity),
                "is_international": int(is_intl),
                "distance_from_home_km": float(distance),
                "merchant_risk_rating": float(merchant_risk),
                "failed_pin_attempts": int(failed_pin)
            }
            
            try:
                # Direct Import Call
                data = evaluate_fraud_risk(payload)
                
                is_fraud = data["is_fraudulent"]
                level = data["risk_level"]
                badge_color = "#EF4444" if is_fraud else "#22C55E"
                
                st.markdown(f"""
                    <div style="background-color: #1E293B; padding: 1.2rem; border-radius: 8px; border-left: 6px solid {badge_color}; margin-bottom: 1rem;">
                        <h4 style="margin: 0; color: #94A3B8;">FRAUD RISK LEVEL: <span style="color:{badge_color};">{level}</span></h4>
                        <h2 style="margin: 5px 0; color: white;">Anomaly Score: {data['fraud_score'] * 100:.1f}%</h2>
                        <p style="margin: 0; color: #CBD5E1;">Status: {'⚠️ BLOCKED / HIGH RISK' if is_fraud else '✅ APPROVED / LOW RISK'}</p>
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown("#### Detected Risk Factors")
                for factor in data["risk_factors"]:
                    if is_fraud:
                        st.warning(f"• {factor}")
                    else:
                        st.success(f"• {factor}")
                        
            except Exception as e:
                st.error(f"Error scanning transaction: {e}")

    st.markdown("---")
    st.markdown("#### Live Monitoring Stream (Simulated Enterprise Feed)")
    
    sample_feed = pd.DataFrame([
        {"Txn ID": "TXN-101", "Amount": "$120.00", "Velocity": 1, "Intl": "No", "Risk Score": "12%", "Status": "PASS"},
        {"Txn ID": "TXN-102", "Amount": "$4,500.00", "Velocity": 8, "Intl": "Yes", "Risk Score": "94%", "Status": "FLAGGED"},
        {"Txn ID": "TXN-103", "Amount": "$45.50", "Velocity": 2, "Intl": "No", "Risk Score": "5%", "Status": "PASS"},
        {"Txn ID": "TXN-104", "Amount": "$1,890.00", "Velocity": 5, "Intl": "Yes", "Risk Score": "81%", "Status": "FLAGGED"},
    ])
    
    def highlight_fraud(val):
        color = '#7F1D1D' if val == 'FLAGGED' else '#14532D'
        return f'background-color: {color}; color: white;'
    
    st.dataframe(sample_feed.style.map(highlight_fraud, subset=['Status']), use_container_width=True)