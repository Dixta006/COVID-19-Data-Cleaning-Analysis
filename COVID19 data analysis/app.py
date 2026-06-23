import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="COVID-19 Analytics Dashboard",
    page_icon="🦠",
    layout="wide"
)

# Load Dataset
df = pd.read_csv("covid_2500_dataset.csv")

# Title
st.title("🦠 COVID-19 Analytics Dashboard")
st.markdown("### Data Cleaning & Analysis Project")

# Sidebar
st.sidebar.header("Filters")

country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + sorted(df["Country"].dropna().unique())
)

if country != "All":
    df_filtered = df[df["Country"] == country]
else:
    df_filtered = df

# KPI Cards
st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Cases",
    f"{int(df_filtered['Cases'].fillna(0).sum()):,}"
)

col2.metric(
    "Total Deaths",
    f"{int(df_filtered['Deaths'].fillna(0).sum()):,}"
)

col3.metric(
    "Average Vaccination %",
    round(df_filtered['Vaccinated'].fillna(0).mean(), 2)
)

col4.metric(
    "Missing Values",
    int(df_filtered.isnull().sum().sum())
)

# Dataset Preview
st.subheader("📋 Dataset Preview")
st.dataframe(df_filtered)

# Missing Values Analysis
st.subheader("🔍 Missing Values Analysis")

missing = df_filtered.isnull().sum().reset_index()
missing.columns = ["Column", "Missing Values"]

fig_missing = px.bar(
    missing,
    x="Column",
    y="Missing Values",
    color="Column",
    title="Missing Values by Column"
)

st.plotly_chart(fig_missing, use_container_width=True)

# Manual Cleaning
st.subheader("🧹 Manual Cleaning")

manual_df = df_filtered.dropna()

st.write("Rows Before Cleaning:", len(df_filtered))
st.write("Rows After Cleaning:", len(manual_df))

st.dataframe(manual_df.head())

# Mean Imputation
st.subheader("📌 Mean Imputation")

mean_df = df_filtered.copy()

for col in ["Cases", "Deaths", "Vaccinated"]:
    mean_df[col] = mean_df[col].fillna(mean_df[col].mean())

st.dataframe(mean_df.head())

# Median Imputation
st.subheader("📌 Median Imputation")

median_df = df_filtered.copy()

for col in ["Cases", "Deaths", "Vaccinated"]:
    median_df[col] = median_df[col].fillna(median_df[col].median())

st.dataframe(median_df.head())

# Mode Imputation
st.subheader("📌 Mode Imputation")

mode_df = df_filtered.copy()

for col in ["Cases", "Deaths", "Vaccinated"]:
    mode_df[col] = mode_df[col].fillna(mode_df[col].mode()[0])

st.dataframe(mode_df.head())

# Cases by Country
st.subheader("📈 Total Cases by Country")

country_cases = df.groupby("Country")["Cases"].sum().reset_index()

fig_cases = px.bar(
    country_cases,
    x="Country",
    y="Cases",
    color="Country",
    title="COVID Cases by Country"
)

st.plotly_chart(fig_cases, use_container_width=True)

# Death Distribution
st.subheader("☠️ Death Distribution")

country_deaths = df.groupby("Country")["Deaths"].sum().reset_index()

fig_deaths = px.pie(
    country_deaths,
    names="Country",
    values="Deaths",
    title="Death Distribution"
)

st.plotly_chart(fig_deaths, use_container_width=True)

# Vaccination Analysis
st.subheader("💉 Vaccination Analysis")

vacc = df.groupby("Country")["Vaccinated"].mean().reset_index()

fig_vacc = px.line(
    vacc,
    x="Country",
    y="Vaccinated",
    markers=True,
    title="Vaccination Percentage"
)

st.plotly_chart(fig_vacc, use_container_width=True)

# Statistics
st.subheader("📊 Statistical Summary")
st.dataframe(df.describe())

# Highest Cases
st.subheader("🏆 Country with Highest Cases")
st.write(df.loc[df["Cases"].idxmax()])

# Lowest Cases
st.subheader("📉 Country with Lowest Cases")
st.write(df.loc[df["Cases"].idxmin()])

# Download Button
st.subheader("⬇️ Download Cleaned Dataset")

csv = mean_df.to_csv(index=False)

st.download_button(
    label="Download Cleaned Dataset",
    data=csv,
    file_name="covid_cleaned_dataset.csv",
    mime="text/csv"
)

st.markdown("---")
st.markdown("### Developed by Dixita Jamwal 🚀")