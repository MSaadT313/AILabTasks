import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# ── Load data ─────────────────────────────
train = pd.read_csv('train.csv')
test  = pd.read_csv('test.csv')

TARGET = 'approved'

# ── Split features / target ───────────────
X_train = train.drop(columns=[TARGET])
y_train = train[TARGET]

X_test  = test.drop(columns=[TARGET])
y_test  = test[TARGET]

# ── Convert target to binary ──────────────
y_train = (y_train > 0).astype(int)
y_test  = (y_test > 0).astype(int)

# ── Encode categorical columns ────────────
cat_cols = X_train.select_dtypes(include='object').columns

for col in cat_cols:
    le = LabelEncoder()
    
    combined = pd.concat([X_train[col], X_test[col]]).astype(str)
    le.fit(combined)

    X_train[col] = le.transform(X_train[col].astype(str))
    X_test[col]  = le.transform(X_test[col].astype(str))

# ── Fill missing values ───────────────────
X_train = X_train.fillna(X_train.median(numeric_only=True))
X_test  = X_test.fillna(X_train.median(numeric_only=True))

# ── Train model ───────────────────────────
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# ── Predict ───────────────────────────────
y_pred = model.predict(X_test)

# ── Accuracy ONLY ──────────────────────────
acc = accuracy_score(y_test, y_pred)

print("=" * 40)
print("ACCURACY RESULT")
print("=" * 40)
print(f"Accuracy: {acc:.4f}")