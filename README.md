# QA Metrics Dashboard

Interactive QA test quality metrics dashboard built with Streamlit and Pandas. Upload your test results CSV and instantly visualise quality trends across sprints, features, and test categories.

## Live Demo

https://thila98-qa-metrics-dashboard-appmain-kphsza.streamlit.app/

## What this does

Takes a CSV of test results as input and generates four interactive charts:

- Pass vs Fail by Sprint - quality trend over time
- Test Coverage by Category - balance of Functional, Negative, Security etc
- Pass vs Fail by Feature Area - which features have the most defects
- Average Execution Time by Feature - performance hotspots

Plus a summary metrics bar showing total tests, passed, failed, and pass rate. And a failed tests table at the bottom for quick defect review.

## Tech stack

- Python 3.10
- Streamlit - interactive web dashboard
- Pandas - data processing and grouping
- Plotly - interactive charts
- pytest - 10 unit tests

## How to run locally

1. Clone the repo
   git clone https://github.com/thila98/qa-metrics-dashboard

2. Create virtual environment
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

4. Run the dashboard
   streamlit run app/main.py

5. Open your browser at http://localhost:8501

## CSV format

Your test results CSV needs these columns:
Sprint, Feature, Category, Test_ID, Title, Status, Priority, Execution_Time_Seconds

Status values: Passed or Failed
See sample_data/test_results.csv for a full example.

## Project structure

- app/main.py - Streamlit dashboard entry point
- app/data_processor.py - data loading and metrics calculation
- app/charts.py - Plotly chart definitions
- sample_data/test_results.csv - realistic sample test data
- tests/test_processor.py - 10 unit tests for data processor

## What I learned

- Building interactive data dashboards with Streamlit
- Processing and grouping tabular data with Pandas
- Creating interactive charts with Plotly
- Applying QA metrics thinking to data visualisation
- Connecting BA and PM skills with QA engineering

## Author

Thilangi Uththara De Silva - Senior QA Engineer
GitHub: https://github.com/thila98
