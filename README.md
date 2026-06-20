# 🦠 COVID-19 Data Cleaning and Preprocessing

## 📌 Project Overview

This project demonstrates data cleaning and preprocessing techniques on a COVID-19 dataset containing missing values.

The objective is to identify, analyze, and handle missing data using both manual and automatic cleaning methods.

---

## 🎯 Objectives

- Detect missing values in a dataset
- Perform manual cleaning using row deletion
- Perform automatic cleaning using:
  - Mean Imputation
  - Median Imputation
  - Mode Imputation
- Compare different cleaning techniques
- Generate cleaned datasets for analysis

---

## 🛠️ Technologies Used

- Python
- Google Colab
- Pandas
- NumPy

---

## 📂 Dataset Features

| Column | Description |
|----------|------------|
| Country | Country Name |
| Cases | COVID-19 Cases |
| Deaths | COVID-19 Deaths |
| Vaccinated | Vaccination Percentage |

---

## 🔍 Missing Value Detection

```python
df.isnull().sum()
```

The dataset contains multiple missing values represented as NaN.

---

## 🧹 Manual Cleaning

Rows containing missing values were removed using:

```python
df.dropna()
```

Advantages:
- Simple implementation
- Removes incomplete records

Disadvantages:
- Data loss

---

## 🤖 Automatic Cleaning

### Mean Imputation

```python
df.fillna(df.mean())
```

### Median Imputation

```python
df.fillna(df.median())
```

### Mode Imputation

```python
df.fillna(df.mode().iloc[0])
```

Advantages:
- Preserves data
- Improves dataset completeness

---


## 📈 Results

After applying cleaning techniques:

✅ Missing values removed

✅ Dataset quality improved

✅ Ready for further analysis and visualization

---

## 📸 colab work (coding)

### Original Dataset

<img width="1919" height="956" alt="Screenshot 2026-06-19 121426" src="https://github.com/user-attachments/assets/409a8823-92e7-4a38-852f-bbd7c4da711d" />


### Missing Values Detection

<img width="1223" height="856" alt="Screenshot 2026-06-19 121518" src="https://github.com/user-attachments/assets/e92d0aa5-17d9-423c-927b-a1fba19a80ae" />


### Manual Cleaning

<img width="1898" height="976" alt="Screenshot 2026-06-19 105948" src="https://github.com/user-attachments/assets/c9388175-93ac-4372-adae-1f0e3f51156c" />


### Mean Imputation

<img width="1342" height="846" alt="Screenshot 2026-06-19 121735" src="https://github.com/user-attachments/assets/0ed30ae0-ed84-4926-be2b-e5ae07e5572d" />

### Automatic Cleaning
<img width="892" height="866" alt="Screenshot 2026-06-19 121825" src="https://github.com/user-attachments/assets/4c4bc144-44d8-4b32-b9d4-4afd8b25b580" />

---

# 🖥️ Interactive Dashboard

After data cleaning and preprocessing, an interactive dashboard was developed using Streamlit and Plotly for data visualization and analysis.

## 🚀 Dashboard Features

- Interactive KPI Cards
- Country-wise Filtering
- Missing Value Analysis
- Manual Cleaning Visualization
- Mean Imputation Analysis
- Median Imputation Analysis
- Mode Imputation Analysis
- COVID-19 Cases Analysis
- Death Distribution Analysis
- Vaccination Analysis
- Statistical Summary
- Download Cleaned Dataset

---

## 📊 Dashboard Screenshots

### Dashboard Home Page
<img width="1919" height="1079" alt="Screenshot 2026-06-20 145839" src="https://github.com/user-attachments/assets/0179458f-2339-4fc9-a7ae-77f221d60697" />

### Missing Values Analysis
<img width="1501" height="684" alt="Screenshot 2026-06-20 145911" src="https://github.com/user-attachments/assets/11d8f7b6-9562-445a-b5cb-6e8cbf8425b8" />


### Cases by Country
<img width="1390" height="691" alt="Screenshot 2026-06-20 145955" src="https://github.com/user-attachments/assets/c632a5eb-912f-4b6c-b841-8283a270d3c5" />


### Death Distribution
<img width="1431" height="666" alt="Screenshot 2026-06-20 150410" src="https://github.com/user-attachments/assets/395d4a9a-834e-48ef-a1f8-ce69290a383a" />


### Vaccination Analysis
<img width="1556" height="714" alt="Screenshot 2026-06-20 150034" src="https://github.com/user-attachments/assets/64c30d8e-78a7-421d-b7dd-e2b4ed7f8c2a" />



---

## 🛠 Dashboard Technologies Used

- Streamlit
- Plotly
- Pandas
- Python

---

## ▶️ Run Dashboard Locally

```bash
pip install streamlit pandas plotly
python -m streamlit run app.py
```

---

## 📂 Dashboard Files

```text
COVID19-DATA-ANALYSIS/
│
├── app.py
├── covid_2500_dataset.csv
├── requirements.txt
├── README.md
└── screenshots/
```
## 👩‍💻 Author

**Dixita Jamwal**

Data Science & Analytics Enthusiast
