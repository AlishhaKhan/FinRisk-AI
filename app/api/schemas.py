from pydantic import BaseModel, Field
from typing import Dict, List

# Credit Risk Request Schema
class CreditRiskRequest(BaseModel):
    customer_id: str = Field(..., example="CUST-88392")
    annual_income: float = Field(..., example=75000.0)
    debt_to_income: float = Field(..., example=0.28)
    employment_years: float = Field(..., example=6.5)
    open_credit_lines: int = Field(..., example=4)
    delinquencies_2yrs: int = Field(..., example=0)
    credit_inquiries_6m: int = Field(..., example=1)
    repayment_score: float = Field(..., example=710.0)

# Credit Risk Response Schema
class CreditRiskResponse(BaseModel):
    customer_id: str
    approval_status: str
    risk_score: float
    default_probability: float
    recommendation: str
    feature_importance: Dict[str, float]

# Fraud Detection Request Schema
class FraudDetectionRequest(BaseModel):
    transaction_id: str = Field(..., example="TXN-99104")
    amount: float = Field(..., example=1450.0)
    velocity_1h: int = Field(..., example=4)
    is_international: int = Field(..., example=1)
    distance_from_home_km: float = Field(..., example=350.0)
    merchant_risk_rating: float = Field(..., example=4.2)
    failed_pin_attempts: int = Field(..., example=1)

# Fraud Detection Response Schema
class FraudDetectionResponse(BaseModel):
    transaction_id: str
    is_fraudulent: bool
    fraud_score: float
    risk_level: str
    risk_factors: List[str]