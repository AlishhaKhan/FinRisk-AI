from fastapi import APIRouter, HTTPException
from app.api.schemas import (
    CreditRiskRequest, 
    CreditRiskResponse, 
    FraudDetectionRequest, 
    FraudDetectionResponse
)
from app.services.evaluator import evaluate_credit_risk, evaluate_fraud_risk

router = APIRouter()

@router.post("/predict-credit-risk", response_model=CreditRiskResponse, summary="Evaluate Credit Application Risk")
def predict_credit_risk(request: CreditRiskRequest):
    """
    Accepts applicant financial metrics and predicts approval probability, 
    credit score, and SHAP-based feature importance.
    """
    try:
        return evaluate_credit_risk(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Credit Risk Evaluation Error: {str(e)}")

@router.post("/detect-fraud", response_model=FraudDetectionResponse, summary="Detect Real-Time Transaction Fraud")
def detect_fraud(request: FraudDetectionRequest):
    """
    Processes real-time transaction metadata to calculate anomaly score, 
    risk severity level, and specific fraud indicators.
    """
    try:
        return evaluate_fraud_risk(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Fraud Detection Engine Error: {str(e)}")