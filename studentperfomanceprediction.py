# ------------------------------
# Debugged KNN code for studentperformance.xlsx
# ------------------------------

import pandas as pd
import os
import sklearn
import openpyxl  # required for pandas to read Excel
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ------------------------------
# Step 1: Define the full path to your Excel file
# Replace this with your actual path
excel_file = r"C:\Users\STUDENTS.DESKTOP-345CQH4\Desktop\SkyTechIncentiveSystem\studentperfomance.xlsx"

# Step 2: Load the Excel data safely
try:
    data = pd.read_excel(excel_file, engine='openpyxl')
except FileNotFoundError:
    print("Error: Excel file not found! Check your file path.")
    exit()

# Step 3: Display the first few rows
print("First 5 rows of the dataset:")
print(data.head())

# Step 4: Encode Final_Result labels (PASS=1, FAIL=0)
data['Final_Result'] = data['Final_Result'].map({'PASS': 1, 'FAIL': 0})

# Step 5: Split data into features and target
X = data.drop('Final_Result', axis=1)
y = data['Final_Result']

# Step 6: Split into training and testing sets (80%-20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Train a KNN classifier with k=3
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Step 8: Evaluate the model
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f"\nAccuracy: {accuracy}")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(class_report)

# Step 9: Test K values from 1 to 5
print("\nAccuracy for different K values:")
for k in range(1, 6):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred_k = knn.predict(X_test)
    accuracy_k = accuracy_score(y_test, y_pred_k)
    print(f"K={k}, Accuracy: {accuracy_k}")

# Step 10: Plot Accuracy vs K values
k_values = range(1, 6)
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred_k = knn.predict(X_test)
    accuracy_k = accuracy_score(y_test, y_pred_k)
    accuracies.append(accuracy_k)

plt.plot(k_values, accuracies, marker='o')
plt.xlabel('K Values')
plt.ylabel('Accuracy')
plt.title('KNN Accuracy vs K Values')
plt.show()