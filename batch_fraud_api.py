import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import random
import uvicorn

app = FastAPI(title="🚀 Fraud Detection Batch API")

# Transaction format
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

class BatchRequest(BaseModel):
    transactions: List[Transaction]

# Dummy fraud detection logic
def detect_fraud(transaction):
    fraud_score = random.uniform(0, 1)
    is_fraud = fraud_score > 0.7
    fraud_reason = "High Risk Pattern" if is_fraud else "Low Risk"
    return {
        "is_fraud": is_fraud,
        "fraud_score": round(fraud_score, 2),
        "fraud_reason": fraud_reason
    }

@app.post("/batch-fraud-detection")
async def batch_fraud_detection(batch_request: BatchRequest):
    transactions = batch_request.transactions
    if not transactions:
        raise HTTPException(status_code=400, detail="No transactions provided.")

    results = {}
    for txn in transactions:
        txn_data = txn.dict()
        detection = detect_fraud(txn_data)
        results[txn.transaction_id] = detection

    return {"results": results}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
