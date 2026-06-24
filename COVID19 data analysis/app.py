import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="COVID-19 Analytics Dashboard",
    page_icon="🦠",
    layout="wide"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(135deg,#EAF4FF,#F8FBFF);
}

/* Headings */
h1,h2,h3,h4,h5,h6{
    color:#0F172A !important;
    font-weight:bold !important;
}

/* Text */
p,label{
    color:#1E293B !important;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#0F172A,#1E3A8A);
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* KPI Cards */
.metric-card{
    background:white;
    border-radius:18px;
    padding:20px;
    text-align:center;
    box-shadow:0px 4px 12px rgba(0,0,0,0.12);
}

.metric-title{
    color:#334155 !important;
    font-size:18px;
    font-weight:600;
}

.metric-value{
    color:#2563EB !important;
    font-size:32px;
    font-weight:bold;
}

/* Buttons */
.stButton button{
    background:#2563EB !important;
    color:white !important;
    border:none;
    border-radius:10px;
    font-weight:bold;
}

.stDownloadButton button{
    background:#16A34A !important;
    color:white !important;
    border:none;
    border-radius:10px;
    font-weight:bold;
}

/* Select Box */
.stSelectbox div[data-baseweb="select"]{
    background:white !important;
    color:black !important;
}

/* Dropdown */
div[role="option"]{
    color:black !important;
}

/* Tables */
[data-testid="stDataFrame"]{
    background:white !important;
}

/* Success */
.stSuccess{
    color:#065F46 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------

df = pd.read_csv("covid_2500_dataset.csv")

# ---------------- HEADER ----------------

st.markdown("""
<h1 style='text-align:center'>
🦠 COVID-19 Analytics Dashboard
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h4 style='text-align:center'>
Data Cleaning • Analytics • Visualization
</h4>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- SIDEBAR ----------------

st.sidebar.title("🦠 Dashboard Menu")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "📋 Dataset",
        "🧹 Data Cleaning",
        "📈 Visualizations",
        "📊 Statistics"
    ]
)

country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + sorted(df["Country"].dropna().unique())
)

if country != "All":
    df_filtered = df[df["Country"] == country]
else:
    df_filtered = df

# ---------------- HOME ----------------

if page == "🏠 Home":

    st.subheader("📊 Key Metrics")

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
        <div class="metric-title">Total Cases</div>
        <div class="metric-value">
        {int(df_filtered['Cases'].fillna(0).sum()):,}
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
        <div class="metric-title">Total Deaths</div>
        <div class="metric-value">
        {int(df_filtered['Deaths'].fillna(0).sum()):,}
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
        <div class="metric-title">Avg Vaccination %</div>
        <div class="metric-value">
        {round(df_filtered['Vaccinated'].fillna(0).mean(),2)}
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
        <div class="metric-title">Missing Values</div>
        <div class="metric-value">
        {int(df_filtered.isnull().sum().sum())}
        </div>
        </div>
        """, unsafe_allow_html=True)

    st.success("✅ Dashboard Running Successfully")

# ---------------- DATASET ----------------

elif page == "📋 Dataset":

    st.subheader("📋 Dataset Preview")

    st.dataframe(
        df_filtered,
        use_container_width=True
    )

# ---------------- CLEANING ----------------

elif page == "🧹 Data Cleaning":

    st.subheader("🧹 Manual Cleaning")

    manual_df = df_filtered.dropna()

    st.write("Rows Before Cleaning:", len(df_filtered))
    st.write("Rows After Cleaning:", len(manual_df))

    st.dataframe(manual_df.head())

    st.subheader("📌 Mean Imputation")

    mean_df = df_filtered.copy()

    for col in ["Cases","Deaths","Vaccinated"]:
        mean_df[col] = mean_df[col].fillna(mean_df[col].mean())

    st.dataframe(mean_df.head())

    st.subheader("📌 Median Imputation")

    median_df = df_filtered.copy()

    for col in ["Cases","Deaths","Vaccinated"]:
        median_df[col] = median_df[col].fillna(median_df[col].median())

    st.dataframe(median_df.head())

    st.subheader("📌 Mode Imputation")

    mode_df = df_filtered.copy()

    for col in ["Cases","Deaths","Vaccinated"]:
        mode_df[col] = mode_df[col].fillna(mode_df[col].mode()[0])

    st.dataframe(mode_df.head())

# ---------------- VISUALIZATIONS ----------------

elif page == "📈 Visualizations":

    st.subheader("📈 COVID Cases by Country")

    cases = df.groupby("Country")["Cases"].sum().reset_index()

    fig1 = px.bar(
        cases,
        x="Country",
        y="Cases",
        color="Country",
        title="Total Cases by Country"
    )

    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("☠️ Death Distribution")

    deaths = df.groupby("Country")["Deaths"].sum().reset_index()

    fig2 = px.pie(
        deaths,
        names="Country",
        values="Deaths",
        title="Death Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("💉 Vaccination Analysis")

    vacc = df.groupby("Country")["Vaccinated"].mean().reset_index()

    fig3 = px.line(
        vacc,
        x="Country",
        y="Vaccinated",
        markers=True,
        title="Vaccination Percentage"
    )

    st.plotly_chart(fig3, use_container_width=True)

# ---------------- STATISTICS ----------------

elif page == "📊 Statistics":

    st.subheader("📊 Statistical Summary")

    st.dataframe(df.describe())

    st.subheader("🏆 Highest Cases")

    st.write(df.loc[df["Cases"].idxmax()])

    st.subheader("📉 Lowest Cases")

    st.write(df.loc[df["Cases"].idxmin()])

    csv = df.to_csv(index=False)

    st.download_button(
        label="⬇️ Download Dataset",
        data=csv,
        file_name="covid_cleaned_dataset.csv",
        mime="text/csv",
        use_container_width=True
    )

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown("""
<h3 style='text-align:center;color:#2563EB'>
🚀 Developed by Dixita Jamwal
</h3>
""", unsafe_allow_html=True)