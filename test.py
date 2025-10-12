
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Scientific Visualization", divider="gray")

# URL to the CSV file
url = "https://raw.githubusercontent.com/atiqahfsl-oli25/Tutorial-1/refs/heads/main/arts_faculty_data.csv"

# Read the CSV file
try:
    df_url = pd.read_csv(url)
    print(df_url.head())  # Show first few rows
except Exception as e:
    print(f"An error occurred while reading the CSV file from the URL: {e}")
else:
    # Check if 'Gender' column exists
    if 'Gender' in df_url.columns:
        # Count occurrences of each gender
        gender_counts = df_url['Gender'].value_counts().reset_index()
        gender_counts.columns = ['Gender', 'Count']

        # Create interactive pie chart using Plotly
        fig = px.pie(
            gender_counts,
            names='Gender',
            values='Count',
            title='Distribution of Gender in Arts Faculty',
            hole=0.3  # Set to 0 for full pie, or >0 for donut chart
        )
        fig.update_traces(textinfo='percent+label')  # Show label and percentage
        fig.show()
    else:
        print("The column 'Gender' was not found in the dataset.")
