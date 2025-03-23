import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate random data using NumPy
np.random.seed(42)  # For reproducibility
dates = pd.date_range(start="2024-01-01", periods=30)  # 30 days of data
values = np.random.randint(10, 100, size=30)  # Random values between 10 and 100

# Create a Pandas DataFrame
df = pd.DataFrame({"Date": dates, "Value": values})

# Print first 5 rows
print("Sample Data:\n", df.head())

# Plot the data using Matplotlib
plt.figure(figsize=(10, 5))
plt.plot(
    df["Date"], df["Value"], marker="o", linestyle="-", color="b", label="Random Values"
)

# Customize the plot
plt.xlabel("Date")
plt.ylabel("Value")
plt.title("Random Data Visualization")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)

# Show the plot
plt.show()
