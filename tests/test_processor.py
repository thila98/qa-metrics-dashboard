import pytest
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.data_processor import (
    get_overall_summary,
    get_pass_fail_by_sprint,
    get_pass_fail_by_feature,
    get_pass_fail_by_category,
    get_failed_tests
)


# Sample test data used across all tests
sample_data = pd.DataFrame({
    'Sprint': ['Sprint 1', 'Sprint 1', 'Sprint 2', 'Sprint 2'],
    'Feature': ['Login', 'Login', 'Dashboard', 'Dashboard'],
    'Category': ['Functional', 'Negative', 'Functional', 'Security'],
    'Test_ID': ['TC_001', 'TC_002', 'TC_003', 'TC_004'],
    'Title': ['Valid login', 'Invalid login', 'Dashboard loads', 'XSS test'],
    'Status': ['Passed', 'Failed', 'Passed', 'Passed'],
    'Priority': ['High', 'High', 'Medium', 'High'],
    'Execution_Time_Seconds': [1.2, 0.8, 2.1, 1.5]
})


def test_summary_total_count():
    """Check that total count matches number of rows"""
    result = get_overall_summary(sample_data)
    assert result['total'] == 4


def test_summary_passed_count():
    """Check that passed count is correct"""
    result = get_overall_summary(sample_data)
    assert result['passed'] == 3


def test_summary_failed_count():
    """Check that failed count is correct"""
    result = get_overall_summary(sample_data)
    assert result['failed'] == 1


def test_summary_pass_rate():
    """Check that pass rate is calculated correctly"""
    result = get_overall_summary(sample_data)
    assert result['pass_rate'] == 75.0


def test_pass_fail_by_sprint_returns_dataframe():
    """Check that sprint grouping returns a DataFrame"""
    result = get_pass_fail_by_sprint(sample_data)
    assert isinstance(result, pd.DataFrame)


def test_pass_fail_by_sprint_has_correct_columns():
    """Check that sprint grouping has Sprint, Status, Count columns"""
    result = get_pass_fail_by_sprint(sample_data)
    assert 'Sprint' in result.columns
    assert 'Status' in result.columns
    assert 'Count' in result.columns


def test_pass_fail_by_feature_returns_dataframe():
    """Check that feature grouping returns a DataFrame"""
    result = get_pass_fail_by_feature(sample_data)
    assert isinstance(result, pd.DataFrame)


def test_pass_fail_by_category_returns_dataframe():
    """Check that category grouping returns a DataFrame"""
    result = get_pass_fail_by_category(sample_data)
    assert isinstance(result, pd.DataFrame)


def test_get_failed_tests_returns_only_failed():
    """Check that only failed tests are returned"""
    result = get_failed_tests(sample_data)
    assert len(result) == 1
    assert result.iloc[0]['Test_ID'] == 'TC_002'


def test_get_failed_tests_empty_when_all_pass():
    """Check that empty DataFrame is returned when no failures"""
    all_pass = sample_data.copy()
    all_pass['Status'] = 'Passed'
    result = get_failed_tests(all_pass)
    assert len(result) == 0
