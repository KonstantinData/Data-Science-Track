# Importing necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Generating a sample dataset to simulate email spam detection
# In practice, you'd use pd.read_csv('spambase.data') or another real dataset
np.random.seed(42)
num_samples = 1000
data = pd.DataFrame(
    {
        "keyword_free": np.random.randint(0, 2, num_samples),
        "num_links": np.random.randint(0, 10, num_samples),
        "subject_length": np.random.randint(10, 50, num_samples),
        "num_special_chars": np.random.randint(0, 10, num_samples),
        "is_spam": np.random.randint(
            0, 2, num_samples
        ),  # Target variable (0: Not Spam, 1: Spam)
    }
)

# Defining features (X) and the target variable (y)
X = data.drop("is_spam", axis=1)  # Features
y = data["is_spam"]  # Target

# Splitting the dataset into traing and test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Creating and training the logistig regression model
model = LogisticRegression(max_iter=10000, random_state=42)
model.fit(X_train, y_train)

# making predictions on the test set

y_pred = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Printing evaluation metrics
print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)
