import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report
import warnings
warnings.filterwarnings('ignore')

# ── 1. Load ───────────────────────────────────────────────────────────────────
train = pd.read_csv('train.csv')
test  = pd.read_csv('test.csv')

TARGET = 'approved'

# ── 2. Split features / target ────────────────────────────────────────────────
X_train = train.drop(columns=[TARGET])
y_train = (train[TARGET] > 0).astype(int)
X_test  = test.drop(columns=[TARGET])
y_test  = (test[TARGET]  > 0).astype(int)

# ── 3. Encode categoricals ────────────────────────────────────────────────────
cat_cols = X_train.select_dtypes(include='object').columns.tolist()
for col in cat_cols:
    le = LabelEncoder()
    combined = pd.concat([X_train[col], X_test[col]]).astype(str).str.strip()
    le.fit(combined)
    X_train[col] = le.transform(X_train[col].astype(str).str.strip())
    X_test[col]  = le.transform(X_test[col].astype(str).str.strip())

X_train = X_train.fillna(X_train.median(numeric_only=True))
X_test  = X_test.fillna(X_train.median(numeric_only=True))

# ── 4. Train Gradient Boosting Classifier ─────────────────────────────────────
gb = GradientBoostingClassifier(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=4,
    subsample=0.8,
    min_samples_leaf=10,
    random_state=42
)
gb.fit(X_train, y_train)

# ── 5. Evaluate ───────────────────────────────────────────────────────────────
y_pred      = gb.predict(X_test)
y_pred_prob = gb.predict_proba(X_test)[:, 1]

print("=" * 50)
print("  GRADIENT BOOSTING — Classification (approved)")
print("=" * 50)
print(f"  Accuracy : {accuracy_score(y_test, y_pred):.4f}")
print(f"  ROC-AUC  : {roc_auc_score(y_test, y_pred_prob):.4f}")
print()
print(classification_report(y_test, y_pred, target_names=['Not Approved', 'Approved']))