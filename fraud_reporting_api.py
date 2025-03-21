from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import pandas as pd
import os
import uvicorn

app = FastAPI(
    title="📝 Fraud Reporting API",
    description="API for reporting and retrieving fraud cases.",
    version="1.0"
)

# File where reports will be saved
REPORT_FILE = "reported_frauds.csv"

# Fraud Report Schema
class FraudReport(BaseModel):
    transaction_id: str
    reason: str
    reporter_name: str
    reporter_contact: str

# Endpoint to report a fraud
@app.post("/report-fraud")
async def report_fraud(report: FraudReport):
    report_data = report.dict()

    # Check if the report file exists
    if os.path.exists(REPORT_FILE):
        df = pd.read_csv(REPORT_FILE)
        df = df.append(report_data, ignore_index=True)
    else:
        df = pd.DataFrame([report_data])

    df.to_csv(REPORT_FILE, index=False)

    return {
        "message": "Fraud reported successfully ✅",
        "report": report_data
    }

# Endpoint to get all fraud reports
@app.get("/fraud-reports")
async def get_fraud_reports():
    if not os.path.exists(REPORT_FILE):
        return {"message": "No fraud reports found."}

    df = pd.read_csv(REPORT_FILE)
    return df.to_dict(orient="records")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)