
import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit page config
st.set_page_config(page_title="Gender Distribution", layout="centered")

# Title of the app
st.title("🎓 Arts Faculty Gender Distribution")

# Load data
url = "https://raw.githubusercontent.com/atiqahfsl-oli25/Tutorial-1/refs/heads/main/arts_faculty_data.csv"

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="PLO 2", value=f"3.3", help="PLO 2: Cognitive Skill", border=True)
col2.metric(label="PLO 3", value=f"3.5", help="PLO 3: Digital Skill", border=True)
col3.metric(label="PLO 4", value=f"4.0", help="PLO 4: Interpersonal Skill", border=True)
col4.metric(label="PLO 5", value=f"4.3", help="PLO 5: Communication Skill", border=True)

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
    
# Boxplot S.S.C (GPA) by gender
        if 'S.S.C (GPA)' in df_url.columns:
            st.subheader("📈 Comparison of S.S.C (GPA) by Gender")
            fig_box = px.box(
                df_url,
                x='Gender',
                y='S.S.C (GPA)',
                color='Gender',
                title='Comparison of S.S.C (GPA) by Gender',
                points='all'
            )
            st.plotly_chart(fig_box, use_container_width=True)
        else:
            st.warning("⚠️ The column 'S.S.C (GPA)' was not found in the dataset.")

# Boxplot H.S.C (GPA) by gender 
        if 'H.S.C (GPA)' in df_url.columns:
            st.subheader("📈 Comparison of H.S.C (GPA) by Gender")
            fig_box = px.box(
                df_url,
                x='Gender',
                y='H.S.C (GPA)',
                color='Gender',
                title='Comparison of H.S.C (GPA) by Gender',
                points='all'
            )
            st.plotly_chart(fig_box, use_container_width=True)
        else:
            st.warning("⚠️ The column 'H.S.C (GPA)' was not found in the dataset.")
    else:
        st.warning("⚠️ The column 'Gender' was not found in the dataset.")

# Arts program distribution by number of students  
    if 'Arts Program' in df_url.columns:
        # Count program occurrences
        program_counts = df_url['Arts Program'].value_counts().reset_index()
        program_counts.columns = ['Arts Program', 'Count']

        # Create interactive Plotly bar chart
        st.subheader("📊 Arts Program Distribution")
        fig = px.bar(
            program_counts,
            x='Arts Program',
            y='Count',
            text='Count',
            title='Distribution of Arts Programs',
            color='Arts Program'
        )

        # Improve layout
        fig.update_layout(
            xaxis_title="Arts Program",
            yaxis_title="Number of Students",
            xaxis_tickangle=-45
        )
        fig.update_traces(textposition='outside')

        # Display chart
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠️ The column 'Arts Program' was not found in the dataset.")

# Distribution of Academic Year 
    if 'Bachelor  Academic Year in EU' in df_url.columns and 'Masters Academic Year in EU' in df_url.columns:
        # Combine both columns and remove NaN
        academic_year_combined = pd.concat([
            df_url['Bachelor  Academic Year in EU'],
            df_url['Masters Academic Year in EU']
        ]).dropna()

        # Count occurrences
        academic_year_counts = academic_year_combined.value_counts().reset_index()
        academic_year_counts.columns = ['Academic Year', 'Count']

        # Create interactive donut chart
        st.subheader("📊 Academic Year Distribution (Donut Chart)")
        fig = px.pie(
            academic_year_counts,
            names='Academic Year',
            values='Count',
            hole=0.5,
            title='Distribution of Academic Years (Bachelor & Masters)',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig.update_traces(textinfo='percent+label')

        # Display chart
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠️ One or both columns ('Bachelor  Academic Year in EU', 'Masters Academic Year in EU') were not found in the dataset.")
