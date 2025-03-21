import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Baby AI gets the storybook 📖
df = pd.read_csv('transactions_final.csv')

# Baby AI picks the clues 🔍
df_encoded = pd.get_dummies(df, columns=['transaction_channel'])

X = df_encoded[[
    'transaction_amount',
    'transaction_payment_mode_anonymous',
    'payment_gateway_bank_anonymous',
    'transaction_channel_ATM',
    'transaction_channel_POS',
    'transaction_channel_Online'
]]

# Baby AI looks at the truth (fraud or not) ✅ ❌
y = df['is_fraud_reported']

# Split into practice test (80% learn, 20% test!) 🎓
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Baby AI learns with Random Forest magic trees 🌳✨
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save baby AI’s brain 🧠
joblib.dump(model, 'fraud_model.pkl')

print("✅ Baby AI trained and saved! 🎉 It's ready to catch frauds!")

