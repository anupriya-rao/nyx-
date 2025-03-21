import pandas as pd
import numpy as np
import random
from datetime import datetime

def random_dates(start, end, n=100):
    start_u = start.timestamp()
    end_u = end.timestamp()
    return [datetime.fromtimestamp(random.uniform(start_u, end_u)) for _ in range(n)]

n = 1000
df = pd.DataFrame({
    'transaction_id': [f'TX{i:04}' for i in range(n)],
    'transaction_amount': np.random.randint(10, 10000, size=n),
    'transaction_date': random_dates(datetime(2024, 1, 1), datetime(2025, 3, 20), n),
    'transaction_channel': np.random.choice(['Online', 'POS', 'ATM'], size=n),
    'transaction_payment_mode_anonymous': np.random.choice([0, 1, 2], size=n),
    'payment_gateway_bank_anonymous': np.random.choice([0, 1, 2], size=n),
    'payer_browser_anonymous': np.random.choice([0, 1], size=n),
    'payer_email_anonymous': [f"user{i}@domain.com" for i in range(n)],
    'payee_ip_anonymous': [f"192.168.1.{i%255}" for i in range(n)],
    'payer_mobile_anonymous': np.random.randint(1000000000, 9999999999, size=n),
    'payee_id_anonymous': np.random.randint(1000, 9999, size=n),
    'is_fraud_predicted': np.random.choice([0, 1], size=n, p=[0.85, 0.15]),
    'is_fraud_reported': np.random.choice([0, 1], size=n, p=[0.9, 0.1]),
})

df.to_csv('transactions_final.csv', index=False)
print("✅ Sample data generated: transactions_final.csv")

