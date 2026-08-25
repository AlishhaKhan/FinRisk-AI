# 🛡️ FinRisk AI
> **Enterprise Real-Time Credit Assessment & Transaction Fraud Engine**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![XGBoost](https://img.shields.io/badge/XGBoost-232F3E?style=for-the-badge&logo=xgboost)](https://xgboost.readthedocs.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

FinRisk AI is an enterprise-grade financial risk intelligence platform designed to address two core banking challenges simultaneously: **intelligent automated credit underwriting** and **real-time transaction fraud monitoring**. 

Featuring a high-performance decoupled architecture, CreditShield AI provides real-time ML scoring alongside Explainable AI (SHAP) to satisfy strict regulatory audit standards.

---

## ✨ Key Capabilities

- **⚡ Instant Credit Risk Underwriting:** Evaluates applicant income, debt-to-income ratio, credit history length, and employment metrics to output instant approval probabilities and risk bands.
- **🚨 Real-Time Fraud Monitoring Feed:** Continuous transaction stream processor detecting velocity anomalies, geolocation jumps, and high-risk amount patterns.
- **🔬 Regulatory Explainable AI (XAI):** Integrated SHAP (SHapley Additive exPlanations) visual breakdown for every score, providing complete transparency into why an application was approved or flagged.
- **📊 Executive Operations Dashboard:** Feature-rich Streamlit application with interactive risk gauge charts, dynamic transaction feeds, and model impact graphs.
- **🔌 Enterprise REST API:** Low-latency FastAPI engine with automated OpenAPI / Swagger documentation ready for core banking system integrations.

---
## 📸 Interface Showcase
**1. Credit Applicant Evaluator Dashboard**
Evaluates applicant profile metrics, displays real-time CreditShield gauge scores, and shows feature importance breakdown for transparent credit decisions.
<img width="1917" height="918" alt="finrisk1" src="https://github.com/user-attachments/assets/4e00abe3-45cc-455f-860e-c07b8b1a7925" />

**2. Decision Explainability & Risk Analysis**
Visual representation of decision parameters and underlying risk metrics calculated by the Machine Learning inference engine.
<img width="1919" height="917" alt="finrisk2" src="https://github.com/user-attachments/assets/55580761-7bbd-4ffd-b163-702c1fac2275" />

**3. Real-Time Transaction Fraud Detector**
Simulates transaction streaming inputs and scans anomalies such as velocity spikes, location discrepancies, and merchant risk ratings.
<img width="1919" height="918" alt="finrisk3" src="https://github.com/user-attachments/assets/cc281394-76d8-47ed-bca4-9ca03fe6f758" />

**4. Interactive Live Fraud Stream & Analytics**
Overview of real-time transaction processing feed with dynamic status flagging (PASS / FLAGGED) for security operations.
<img width="1920" height="917" alt="finrisk4" src="https://github.com/user-attachments/assets/f6638317-e9e8-451e-92fe-640fca202f6a" /> 

---

## 🏗 System Architecture

```text
┌─────────────────────────────────────────────────────────┐
│              FinRisk AI Infrastructure                  │
└────────────────────────────┬────────────────────────────┘
                             │
             ┌───────────────┴───────────────┐
             ▼                               ▼
┌─────────────────────────┐     ┌─────────────────────────┐
│    Streamlit Frontend   │     │   FastAPI Core Engine   │
│ ─────────────────────── │     │ ─────────────────────── │
│ • Applicant Evaluator   │◄───►│ • /predict-credit-risk  │
│ • Live Fraud Dashboard  │ JSON│ • /detect-fraud         │
│ • SHAP Explainability   │ REST│ • Automated Swagger UI  │
└─────────────────────────┘     └────────────┬────────────┘
                                             │
                                             ▼
                                ┌─────────────────────────┐
                                │   Scikit / XGBoost ML   │
                                │ ─────────────────────── │
                                │ • Synthetic Data Engine │
                                │ • Feature Scoring Model │
                                └─────────────────────────┘
