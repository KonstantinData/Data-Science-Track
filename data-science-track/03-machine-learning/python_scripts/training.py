import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = {
    "Age": [22, 25, 47, 52, 46, 56, 55, 60, 62, 61],
    "Income": [15, 20, 35, 55, 40, 60, 45, 80, 90, 85],
    "Purchased": [0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
}

df = pd.DataFrame(data)

X = df.drop("Purchase", axis=1)
y = df["Purchase"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# model = LogisticRegression(max_iter=10000, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train)

y_pred = model.predict(y_test)

accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(class_report)
