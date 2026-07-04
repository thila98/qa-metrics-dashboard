import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def pass_fail_by_sprint_chart(df: pd.DataFrame):
    """
    Bar chart showing pass vs fail count per sprint.
    Shows quality trend over time.
    """
    fig = px.bar(
        df,
        x='Sprint',
        y='Count',
        color='Status',
        color_discrete_map={'Passed': '#22c55e', 'Failed': '#ef4444'},
        title='Pass vs Fail by Sprint',
        barmode='group'
    )
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=13)
    )
    return fig


def pass_fail_by_feature_chart(df: pd.DataFrame):
    """
    Horizontal bar chart showing pass vs fail per feature area.
    Highlights which features have the most defects.
    """
    fig = px.bar(
        df,
        x='Count',
        y='Feature',
        color='Status',
        color_discrete_map={'Passed': '#22c55e', 'Failed': '#ef4444'},
        title='Pass vs Fail by Feature Area',
        barmode='group',
        orientation='h'
    )
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=13)
    )
    return fig


def category_distribution_chart(df: pd.DataFrame):
    """
    Pie chart showing test coverage by category.
    Shows balance of Functional, Negative, Security etc.
    """
    category_totals = df.groupby('Category')['Count'].sum().reset_index()
    fig = px.pie(
        category_totals,
        names='Category',
        values='Count',
        title='Test Coverage by Category',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig.update_layout(font=dict(size=13))
    return fig


def execution_time_chart(df: pd.DataFrame):
    """
    Bar chart showing average execution time per feature.
    Helps identify slow test areas.
    """
    fig = px.bar(
        df,
        x='Feature',
        y='Avg_Execution_Time',
        title='Average Test Execution Time by Feature (seconds)',
        color='Avg_Execution_Time',
        color_continuous_scale='Blues'
    )
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=13),
        showlegend=False
    )
    return fig
