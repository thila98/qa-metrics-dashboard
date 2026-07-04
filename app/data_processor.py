import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load test results CSV into a pandas DataFrame.
    A DataFrame is like an Excel spreadsheet in Python —
    rows and columns you can filter, group, and calculate.
    """
    df = pd.read_csv(filepath)
    return df


def get_overall_summary(df: pd.DataFrame) -> dict:
    """
    Calculate overall pass/fail summary numbers.
    Returns total tests, passed, failed, and pass rate percentage.
    """
    total = len(df)
    passed = len(df[df['Status'] == 'Passed'])
    failed = len(df[df['Status'] == 'Failed'])
    pass_rate = round((passed / total) * 100, 1) if total > 0 else 0

    return {
        'total': total,
        'passed': passed,
        'failed': failed,
        'pass_rate': pass_rate
    }


def get_pass_fail_by_sprint(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group test results by sprint and count pass/fail.
    Used for the sprint trend chart.
    """
    grouped = df.groupby(['Sprint', 'Status']).size().reset_index(name='Count')
    return grouped


def get_pass_fail_by_feature(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group test results by feature area and count pass/fail.
    Shows which features have the most failures.
    """
    grouped = df.groupby(['Feature', 'Status']).size().reset_index(name='Count')
    return grouped


def get_pass_fail_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group test results by test category (Functional, Negative, Security etc).
    Shows test coverage distribution.
    """
    grouped = df.groupby(['Category', 'Status']).size().reset_index(name='Count')
    return grouped


def get_avg_execution_time_by_feature(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate average test execution time per feature.
    Helps identify slow areas that may need performance attention.
    """
    grouped = df.groupby('Feature')['Execution_Time_Seconds'].mean().reset_index()
    grouped.columns = ['Feature', 'Avg_Execution_Time']
    grouped['Avg_Execution_Time'] = grouped['Avg_Execution_Time'].round(2)
    return grouped


def get_failed_tests(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter and return only the failed test cases.
    Used for the failed tests table at the bottom of the dashboard.
    """
    failed = df[df['Status'] == 'Failed'][['Sprint', 'Feature', 'Category', 'Test_ID', 'Title', 'Priority']]
    return failed.reset_index(drop=True)
