# -*- coding: utf-8 -*-
"""ML Terapan - Proyek 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gY5QB3_m6Q0al3JY4pdjtF-b1DQzwKpu

# Proyek Pertama : Predictive Analytics

## Import Libraries
"""

# Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Libraries for preprocessing
from sklearn.preprocessing import StandardScaler

# Libraries for splitting the data
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

# Libraries for modeling
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Libraries for evaluation
from sklearn.metrics import accuracy_score, classification_report

"""## Load Dataset"""

url = 'https://raw.githubusercontent.com/Ardizza/Machine-Learning-Terapan/main/heart.csv'
df = pd.read_csv(url)

# Tampilkan 5 baris pertama dari dataset
print(df.head())

"""## Eksplorasi Data"""

# Informasi dataset
print(df.info())

# Statistik deskriptif
print(df.describe())

# Visualisasi data
sns.countplot(x='target', data=df)
plt.title('Distribution of Target Variable')
plt.show()

sns.pairplot(df, hue='target')
plt.show()

# Visualisasi korelasi antar fitur
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap Korelasi Fitur')
plt.show()

"""## Data Preparation"""

# Tidak ada missing values pada dataset ini
df.isnull().sum()

# Pisahkan fitur dan target
X = df.drop('target', axis=1)
y = df['target']

# Normalisasi data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data menjadi training dan testing set
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

"""## Modeling"""

# Modeling - Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

print("Logistic Regression Accuracy:", accuracy_score(y_test, y_pred_lr))
print(classification_report(y_test, y_pred_lr))

# Modeling - Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

print("Random Forest Accuracy:", accuracy_score(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))

# Hyperparameter Tuning for Random Forest
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [5, 10, 15],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=3, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

print("Best parameters found:", grid_search.best_params_)
best_rf = grid_search.best_estimator_
y_pred_best_rf = best_rf.predict(X_test)

print("Best Random Forest Accuracy:", accuracy_score(y_test, y_pred_best_rf))
print(classification_report(y_test, y_pred_best_rf))

# Evaluasi model terbaik
print("Best Random Forest Accuracy:", accuracy_score(y_test, y_pred_best_rf))
print("Best Random Forest Classification Report:\n", classification_report(y_test, y_pred_best_rf))
print("Best parameters found:", grid_search.best_params_)

# Tahap 5: Kesimpulan
print("Logistic Regression Accuracy:", accuracy_score(y_test, y_pred_lr))
print("Random Forest Accuracy:", accuracy_score(y_test, y_pred_rf))
print("Best Random Forest Accuracy:", accuracy_score(y_test, y_pred_best_rf))

print("\nKesimpulan: Model Random Forest dengan hyperparameter tuning memberikan akurasi terbaik dalam memprediksi penyakit jantung pada dataset ini.")