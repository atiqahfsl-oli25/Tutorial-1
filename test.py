
import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit page config
st.set_page_config(page_title="Gender Distribution", layout="centered")

# Title of the app
st.title("🎓 Arts Faculty Gender Distribution")

# Load data
url = "https://raw.githubusercontent.com/atiqahfsl-oli25/Tutorial-1/refs/heads/main/arts_faculty_data.csv"

# Try reading the CSV file
try:
    df_url = pd.read_csv(url)
    st.subheader("📋 Raw Data Preview")
    st.dataframe(df_url.head())  # Show first few rows
except Exception as e:
    st.error(f"❌ An error occurred while reading the CSV file: {e}")
else:
    if 'Gender' in df_url.columns:
        # Count gender values
        gender_counts = df_url['Gender'].value_counts().reset_index()
        gender_counts.columns = ['Gender', 'Count']

        # Plotly Pie Chart
        st.subheader("📊 Gender Distribution Pie Chart")
        fig = px.pie(
            gender_counts,
            names='Gender',
            values='Count',
            title='Distribution of Gender in Arts Faculty',
            hole=0.3  # Optional: donut chart
        )
        fig.update_traces(textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠️ The column 'Gender' was not found in the dataset.")

# Example: Load your dataset (replace this with your own)
# df_url = pd.read_csv("https://raw.githubusercontent.com/atiqahfsl-oli25/Tutorial-1/refs/heads/main/arts_faculty_data.csv")

st.title("Comparison of S.S.C (GPA) by Gender")

    # Plotly boxplot
    fig = px.box(
        df_url,
        x='Gender',
        y='S.S.C (GPA)',
        color='Gender',
        title='Comparison of S.S.C (GPA) by Gender',
        labels={'Gender': 'Gender', 'S.S.C (GPA)': 'S.S.C (GPA)'},
        points='all'  # shows individual data points
    )

    # Display plot
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Please upload a CSV file to generate the boxplot.")


