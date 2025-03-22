# 🚗 Vehicle Silhouette Classification

## 📘 Project Description

This project focuses on building a classification model that can distinguish between different types of vehicles based on geometric features extracted from their silhouettes.
The request comes from a car repair chain named **Prospect Auto**, which wants to classify buses, vans, and cars using image-based features.

---

## 📊 Data Description

The dataset contains only numerical features, each extracted from the silhouette of a vehicle seen from different angles. These features are all geometric in nature.

### 🚙 Vehicle Classes

- 🚌 **Bus** (a double-decker bus)
- 🚐 **Van** (a Chevrolet van)
- 🚗 **Car** (either a Saab 9000 or an Opel Manta)

This specific selection was made to ensure clear visual differences between some classes (e.g., bus vs. car), while also including subtle differences (between the two car types).

### 🎯 Target Column

- `class`: Indicates the vehicle type (`bus`, `van`, or `car`)

### 🧮 Feature Columns

All remaining columns are numerical and describe silhouette geometry:

- `compactness`
- `circularity`
- `distance_circularity`
- `radius_ratio`
- `pr.axis_aspect_ratio`
- `max.length_aspect_ratio`
- `scatter_ratio`
- `elongatedness`
- `pr.axis_rectangularity`
- `max.length_rectangularity`
- `scaled_variance`, `scaled_variance.1`
- `scaled_radius_of_gyration`, `scaled_radius_of_gyration.1`
- `skewness_about`, `skewness_about.1`, `skewness_about.2`
- `hollows_ratio`

---

## ❓ Problem Statement

Prospect Auto has requested a model that can classify a vehicle into one of the three categories based on silhouette data.
Your task is to solve this as a **supervised classification problem** using the provided numerical features.

---

## 🔧 Project Workflow

This project follows a typical machine learning pipeline:

1. **📥 Import & Load Data**
   Import all necessary libraries, load the dataset, and read it into your environment.

2. **🔍 Exploratory Data Analysis (EDA)**
   Understand the data both visually and numerically: distributions, outliers, and correlations.

3. **🧼 Data Preprocessing**
   - Normalize and standardize features
   - Split the dataset into training and testing sets

4. **🤖 Model Building**
   Use classification algorithms like K-Nearest Neighbors, Random Forest, or Logistic Regression.

5. **📈 Model Evaluation**
   Assess model performance using metrics like:
   - Accuracy
   - Precision
   - Recall
   - F1-score

6. **📝 Conclusion**
   Summarize findings and determine whether the model is suitable for real-world deployment.

---

## 📎 Notes

- 📂 The dataset is publicly available *(Download link to be added)*
- 🐍 The entire project will be implemented in **Python**

---
