import pandas as pd

def calculate_engagement_over_time(df):
    """
    This function calculates user engagement trends over time based on session start and end times.
    The result will show total traffic and session duration per day.
    """
    
    # Convert 'Start' and 'End' columns to datetime format
    df['Start'] = pd.to_datetime(df['Start'], errors='coerce')
    df['End'] = pd.to_datetime(df['End'], errors='coerce')
    
    # Ensure 'Total DL (Bytes)' and 'Total UL (Bytes)' are numeric
    df['Total DL (Bytes)'] = pd.to_numeric(df['Total DL (Bytes)'], errors='coerce').fillna(0)
    df['Total UL (Bytes)'] = pd.to_numeric(df['Total UL (Bytes)'], errors='coerce').fillna(0)
    
    # Extract the date part (without time) for grouping
    df['Start_Date'] = df['Start'].dt.date
    df['End_Date'] = df['End'].dt.date

    # Calculate total traffic per date (Download + Upload)
    df['Total Traffic'] = df['Total DL (Bytes)'] + df['Total UL (Bytes)']

    # Aggregate traffic and session duration by start date
    engagement_over_time = df.groupby('Start_Date').agg(
        total_traffic=('Total Traffic', 'sum'),
        total_session_duration=('Dur. (ms)', 'sum')
    ).reset_index()

    return engagement_over_time
