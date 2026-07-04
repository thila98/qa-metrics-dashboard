import streamlit as st
import pandas as pd
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.data_processor import (
    load_data,
    get_overall_summary,
    get_pass_fail_by_sprint,
    get_pass_fail_by_feature,
    get_pass_fail_by_category,
    get_avg_execution_time_by_feature,
    get_failed_tests
)
from app.charts import (
    pass_fail_by_sprint_chart,
    pass_fail_by_feature_chart,
    category_distribution_chart,
    execution_time_chart
)

st.set_page_config(
    page_title="QA Metrics Dashboard",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 QA Metrics Dashboard")
st.markdown("Interactive test quality metrics — upload your test results CSV to get started.")
st.divider()

st.sidebar.header("Data Source")
use_sample = st.sidebar.checkbox("Use sample data", value=True)

if use_sample:
    filepath = os.path.join(os.path.dirname(__file__), "..", "sample_data", "test_results.csv")
    df = load_data(filepath)
    st.sidebar.success("Using sample test data")
else:
    uploaded_file = st.sidebar.file_uploader("Upload your test results CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.sidebar.success("File uploaded successfully")
    else:
        st.info("Please upload a CSV file or use the sample data option in the sidebar.")
        st.stop()

st.sidebar.header("Filters")
sprints = ["All"] + sorted(df["Sprint"].unique().tolist())
selected_sprint = st.sidebar.selectbox("Sprint", sprints)

if selected_sprint != "All":
    df = df[df["Sprint"] == selected_sprint]

summary = get_overall_summary(df)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Tests", summary["total"])
col2.metric("Passed", summary["passed"])
col3.metric("Failed", summary["failed"])
col4.metric("Pass Rate", f"{summary[chr(39)+'pass_rate'+chr(39)]}%")

st.divider()

col_left, col_right = st.columns(2)

with col_left:
    sprint_data = get_pass_fail_by_sprint(df)
    st.plotly_chart(pass_fail_by_sprint_chart(sprint_data), use_container_width=True)

with col_right:
    category_data = get_pass_fail_by_category(df)
    st.plotly_chart(category_distribution_chart(category_data), use_container_width=True)

col_left2, col_right2 = st.columns(2)

with col_left2:
    feature_data = get_pass_fail_by_feature(df)
    st.plotly_chart(pass_fail_by_feature_chart(feature_data), use_container_width=True)

with col_right2:
    exec_data = get_avg_execution_time_by_feature(df)
    st.plotly_chart(execution_time_chart(exec_data), use_container_width=True)

st.divider()

st.subheader("Failed Tests")
failed_df = get_failed_tests(df)

if len(failed_df) == 0:
else:
    st.dataframe(failed_df, use_container_width=True)

st.divider()
st.caption("QA Metrics Dashboard — Built by Thilangi Uththara De Silva")
