import streamlit as st
import textstat
import pandas as pd
import plotly.express as px

st.title("📖 Document Readability Tracker")

# --- File uploader ---
uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:
    # Read text file
    text = uploaded_file.read().decode("utf-8")

    # --- Calculate readability scores ---
    flesch = textstat.flesch_reading_ease(text)
    fog = textstat.gunning_fog(text)
    smog = textstat.smog_index(text)

    # --- Function to categorize scores ---
    def categorize(score):
        if score >= 60:
            return "Beginner"
        elif score >= 30:
            return "Intermediate"
        else:
            return "Advanced"

    # --- Categorize each score ---
    scores = {
        "Flesch Reading Ease": flesch,
        "Gunning Fog Index": fog,
        "SMOG Index": smog
    }

    categories = {metric: categorize(value) for metric, value in scores.items()}

    # --- Show scores ---
    st.subheader("📊 Readability Scores")
    for metric, value in scores.items():
        st.write(f"**{metric}:** {value:.2f} → {categories[metric]}")

    # --- Prepare DataFrame for chart ---
    df = pd.DataFrame({
        "Metric": list(scores.keys()),
        "Score": list(scores.values()),
        "Category": list(categories.values())
    })

    # --- Bar chart with different colors for categories ---
    fig = px.bar(
        df,
        x="Metric",
        y="Score",
        color="Category",
        text="Score",
        title="Readability Score Comparison",
        color_discrete_map={
            "Beginner": "green",
            "Intermediate": "orange",
            "Advanced": "red"
        }
    )

    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    st.plotly_chart(fig)
