import os
import pandas as pd
from xgboost import XGBClassifier

MODEL_DIR = os.path.join(os.path.dirname(__file__), "../models")

credit_model = XGBClassifier()
credit_model.load_model(os.path.join(MODEL_DIR, "credit_model.json"))

fraud_model = XGBClassifier()
fraud_model.load_model(os.path.join(MODEL_DIR, "fraud_model.json"))

def evaluate_credit_risk(data):
    input_df = pd.DataFrame([{
        'annual_income': data.annual_income,
        'debt_to_income': data.debt_to_income,
        'employment_years': data.employment_years,
        'open_credit_lines': data.open_credit_lines,
        'delinquencies_2yrs': data.delinquencies_2yrs,
        'credit_inquiries_6m': data.credit_inquiries_6m,
        'repayment_score': data.repayment_score
    }])
    
    prob_default = float(credit_model.predict_proba(input_df)[0][1])
    risk_score = round((1 - prob_default) * 850, 1)
    
    if prob_default < 0.35:
        status = "APPROVED"
        recommendation = "Low Risk - Standard Instant Approval"
    elif prob_default < 0.60:
        status = "MANUAL REVIEW"
        recommendation = "Medium Risk - Require Secondary Underwriting"
    else:
        status = "REJECTED"
        recommendation = "High Risk - Exceeds Default Threshold"
        
    importances = credit_model.feature_importances_
    features = list(input_df.columns)
    feat_imp = {feat: round(float(imp), 4) for feat, imp in zip(features, importances)}
    
    return {
        "customer_id": data.customer_id,
        "approval_status": status,
        "risk_score": risk_score,
        "default_probability": round(prob_default, 4),
        "recommendation": recommendation,
        "feature_importance": feat_imp
    }

def evaluate_fraud_risk(data):
    input_df = pd.DataFrame([{
        'amount': data.amount,
        'velocity_1h': data.velocity_1h,
        'is_international': data.is_international,
        'distance_from_home_km': data.distance_from_home_km,
        'merchant_risk_rating': data.merchant_risk_rating,
        'failed_pin_attempts': data.failed_pin_attempts
    }])
    
    fraud_prob = float(fraud_model.predict_proba(input_df)[0][1])
    is_fraud = fraud_prob >= 0.55
    
    if fraud_prob >= 0.75:
        level = "CRITICAL"
    elif fraud_prob >= 0.50:
        level = "HIGH"
    elif fraud_prob >= 0.25:
        level = "MODERATE"
    else:
        level = "LOW"
        
    factors = []
    if data.amount > 2000:
        factors.append("High Transaction Amount Threshold Exceeded")
    if data.velocity_1h > 3:
        factors.append("Abnormal Hourly Transaction Velocity")
    if data.is_international == 1:
        factors.append("Cross-Border Geolocation Jump Detected")
    if data.failed_pin_attempts > 0:
        factors.append("Failed PIN Verification Attempts")
    if not factors:
        factors.append("Normal Transaction Pattern Observed")
        
    return {
        "transaction_id": data.transaction_id,
        "is_fraudulent": is_fraud,
        "fraud_score": round(fraud_prob, 4),
        "risk_level": level,
        "risk_factors": factors
    }