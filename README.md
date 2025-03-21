🚨 Fraud Detection System

Overview

This system provides a comprehensive fraud detection solution with a Streamlit dashboard and FastAPI backends for real-time and batch prediction, as well as fraud reporting capabilities.
Components
1. Streamlit Dashboard (streamlit_app.py)
A user-friendly dashboard for monitoring and interacting with the fraud detection system.

Features:

Real-time transaction monitoring
Historical data visualization
Fraud statistics and metrics
Filter transactions by date, payer, payee, or transaction ID
Integration with batch processing API
Real-time fraud prediction
Fraud reporting capability

2. Batch Fraud Detection API (batch_api.py)
Processes multiple transactions in a single request.
Endpoints:

POST /batch-fraud-detection: Analyzes multiple transactions for fraud patterns

3. Real-Time Fraud Detection API (realtime_api.py)
Provides immediate fraud analysis for individual transactions.
Endpoints:

POST /real-time-fraud-detection: Checks if a single transaction is fraudulent

4. Fraud Reporting API (reporting_api.py)
Handles user-reported fraud cases.
Endpoints:

POST /report-fraud: Submit a fraud report
GET /fraud-reports: Retrieve all reported frauds

5. Data Generation Script (generate_data.py)
Creates sample transaction data for testing and demonstration.
Installation
Prerequisites

Python 3.8+
pip

Setup

Clone the repository

bashCopygit clone https://github.com/yourusername/fraud-detection-system.git
cd fraud-detection-system

Create a virtual environment

bashCopypython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install required packages

bashCopypip install -r requirements.txt

Generate sample data

bashCopypython generate_data.py
Usage
Running the Dashboard
bashCopystreamlit run streamlit_app.py
Access the dashboard at http://localhost:8501
Running the APIs
In separate terminal windows:

Batch API

bashCopypython batch_api.py

Real-Time API

bashCopypython realtime_api.py

Reporting API

bashCopypython reporting_api.py
API Documentation
After starting the APIs, access their interactive documentation:

Batch API: http://localhost:8000/docs
Real-Time API: http://localhost:8002/docs
Reporting API: http://localhost:8001/docs

Project Structure
Copyfraud-detection-system/
│
├── streamlit_app.py         # Streamlit dashboard
├── batch_api.py             # Batch processing API
├── realtime_api.py          # Real-time detection API
├── reporting_api.py         # Fraud reporting API
├── generate_data.py         # Sample data generator
├── transactions_final.csv   # Generated sample data
├── reported_frauds.csv      # User-reported frauds
├── requirements.txt         # Project dependencies
└── README.md                # This file
Requirements

streamlit==1.22.0
fastapi==0.95.1
uvicorn==0.22.0
pandas==2.0.1
plotly==5.14.1
pydantic==1.10.7
requests==2.29.0
numpy==1.24.3

Future Enhancements

Integration with a trained ML model for more accurate fraud detection
User authentication and authorization
Email/SMS alerts for detected fraud
Expanded dashboard with additional visualizations
API key authentication for the backend services

License
MIT

Contact
For questions or support, please contact: anupriyarao75@gmail.com
