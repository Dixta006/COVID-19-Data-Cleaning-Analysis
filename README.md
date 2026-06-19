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

## 📊 Analysis Performed

- Highest COVID-19 Cases
- Lowest COVID-19 Cases
- Highest Death Count
- Highest Vaccination Rate
- Average Cases
- Total Deaths

---

## 📈 Results

After applying cleaning techniques:

✅ Missing values removed

✅ Dataset quality improved

✅ Ready for further analysis and visualization

---

## 📸 Project Screenshots

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


## 👩‍💻 Author

**Dixita Jamwal**

Data Science & Analytics Enthusiast
