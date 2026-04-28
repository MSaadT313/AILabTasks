import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score

# ── 1. Load data ─────────────────────────────
train = pd.read_csv('train.csv')
test  = pd.read_csv('test.csv')

TARGET = 'approved_loan_amount'

# ── 2. Split features / target ───────────────
X_train = train.drop(columns=[TARGET])
y_train = train[TARGET]

X_test  = test.drop(columns=[TARGET])
y_test  = test[TARGET]

# ── 3. Binarise target (median split) ───────
median_val = y_train.median()

y_train = (y_train > median_val).astype(int)
y_test  = (y_test > median_val).astype(int)

# ── 4. Encode categorical columns ────────────
cat_cols = X_train.select_dtypes(include='object').columns

for col in cat_cols:
    le = LabelEncoder()

    combined = pd.concat([X_train[col], X_test[col]]).astype(str)
    le.fit(combined)

    X_train[col] = le.transform(X_train[col].astype(str))
    X_test[col]  = le.transform(X_test[col].astype(str))

# ── 5. Handle missing values ────────────────
X_train = X_train.fillna(X_train.median(numeric_only=True))
X_test  = X_test.fillna(X_train.median(numeric_only=True))

# ── 6. Feature scaling ──────────────────────
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# ── 7. Train Logistic Regression ────────────
model = LogisticRegression(
    max_iter=1000,
    class_weight='balanced',
    random_state=42
)

model.fit(X_train, y_train)

# ── 8. Predict ──────────────────────────────
y_pred = model.predict(X_test)

# ── 9. ONLY ACCURACY ────────────────────────
acc = accuracy_score(y_test, y_pred)

print("=" * 45)
print("LOGISTIC REGRESSION RESULT")
print("=" * 45)
print(f"Accuracy: {acc:.4f}")