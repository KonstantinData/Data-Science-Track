import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Task 1 Import LogisticRegression from sklearn.linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Create a sample dataset
data = {
    "Age": [22, 25, 47, 52, 46, 56, 55, 60, 62, 61],
    "Income": [15, 20, 35, 55, 40, 60, 45, 80, 90, 85],
    "Purchased": [0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
}

# Convert to a pandas DataFrame
df = pd.DataFrame(data)

# Split the dataset into features (X) and target (y)
X = df[["Age", "Income"]]  # Features: Age and Income
# Task 2: use column indicating whether the customer purchased the product as target
y = df["Purchased"]  # Target: Purchased


# Split the data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Task 3: Train a Logistic Regression model
log_reg = LogisticRegression(random_state=42)
log_reg.fit(X_train, y_train)

# Task 4: Make predictions on the test set
y_pred = log_reg.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(class_report)
