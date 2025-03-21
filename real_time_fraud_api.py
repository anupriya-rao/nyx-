from fastapi import FastAPI
from pydantic import BaseModel
import random
import uvicorn

# FastAPI instance
app = FastAPI(
    title="⚡ Real-Time Fraud Detection API",
    description="Check if a single transaction is fraudulent in real time!",
    version="1.0"
)

# Transaction schema
class Transaction(BaseModel):
    transaction_id: str
    transaction_amount: float
    transaction_date: str
    transaction_channel: str
    transaction_payment_mode_anonymous: int
    payment_gateway_bank_anonymous: int
    payer_browser_anonymous: int
    payer_email_anonymous: str
    payee_ip_anonymous: str
    payer_mobile_anonymous: str
    payee_id_anonymous: str

# Dummy fraud detection function (Replace with ML model later)
def detect_fraud(transaction):
    fraud_score = random.uniform(0, 1)  # Random score between 0 and 1
    is_fraud = fraud_score > 0.7        # Threshold for fraud detection
    fraud_reason = "Suspicious behavior detected" if is_fraud else "Transaction seems safe"

    return {
        "transaction_id": transaction["transaction_id"],
        "is_fraud": is_fraud,
        "fraud_score": round(fraud_score, 2),
        "fraud_reason": fraud_reason
    }

# API endpoint to detect fraud in real time
@app.post("/real-time-fraud-detection")
async def real_time_fraud_detection(transaction: Transaction):
    transaction_data = transaction.dict()
    detection_result = detect_fraud(transaction_data)

    return {
        "message": "Real-time fraud analysis complete 🚀",
        "result": detection_result
    }

# Run server directly
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)