import streamlit as st
import pandas as pd


# ==========================================
# PAGE TITLE
# ==========================================

st.title("HR Job Placement Prediction")


# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv(
    "C:/Users/criss/Downloads/HR_Job_Placement_Dataset.csv"
)


# ==========================================
# KPI CALCULATIONS
# ==========================================

# 1. Total Candidates
total_candidates = len(df)


# 2. Placement Rate (%)
placement_rate = (
    (df["status"] == "Placed").mean() * 100
)


# 3. Interview Score
df["interview_score"] = (
    df["technical_score"]
    + df["aptitude_score"]
    + df["communication_score"]
) / 3

average_interview_score = df["interview_score"].mean()


# 4. Average Skills Match (%)
average_skills_match = (
    df["skills_match_percentage"].mean()
)


# 5. High-Risk Candidate Percentage

# Create interview performance category
df["interview_performance"] = pd.cut(
    df["interview_score"],
    bins=[0, 50, 75, 100],
    labels=["Low", "Medium", "High"],
    include_lowest=True
)



# Create skills match category
df["skills_match_level"] = pd.cut(
    df["skills_match_percentage"],
    bins=[0, 50, 75, 100],
    labels=["Low", "Medium", "High"],
    include_lowest=True
)


# High-risk = Low interview + Low skills match
high_risk = (
    (df["interview_performance"] == "Low")
    & (df["skills_match_level"] == "Low")
)

high_risk_percentage = high_risk.mean() * 100


# 6. Job Acceptance Rate (%)
# In this project, Placed is treated as Accepted
job_acceptance_rate = (
    (df["status"] == "Placed").mean() * 100
)


# 7. Offer Dropout Rate
# Current dataset does not contain offer_status
offer_dropout_rate = (
    (df["status"] == "Not Placed").mean() * 100
)


# ==========================================
# KPI CARDS
# ==========================================

# ---------- FIRST ROW ----------

col1, col2, col3, col4 = st.columns(4)


# KPI 1
with col1:
    st.metric(
        "Total Candidates",
        total_candidates
    )


# KPI 2
with col2:
    st.metric(
        "Placement Rate (%)",
        f"{placement_rate:.1f}%"
    )


# KPI 3
with col3:
    st.metric(
        "Job Acceptance Rate (%)",
        f"{job_acceptance_rate:.1f}%"
    )


# KPI 4
with col4:
    st.metric(
        "Average Interview Score",
        f"{average_interview_score:.1f}"
    )


# ---------- SECOND ROW ----------

col5, col6, col7 = st.columns(3)


# KPI 5
with col5:
    st.metric(
        "Average Skills Match %",
        f"{average_skills_match:.1f}%"
    )


# KPI 6
with col6:
    st.metric(
        "Offer Dropout Rate",
        f"{offer_dropout_rate:.1f}%"
    )


# KPI 7
with col7:
    st.metric(
        "High-Risk Candidate Percentage",
        f"{high_risk_percentage:.1f}%"
    )