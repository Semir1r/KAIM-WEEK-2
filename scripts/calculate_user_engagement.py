import pandas as pd

def calculate_user_engagement(df):
    """
    This function calculates user engagement metrics such as:
    - Session frequency (number of xDR sessions)
    - Total session duration
    - Total traffic (download + upload data)
    """
    
    # Ensure 'Total DL (Bytes)' and 'Total UL (Bytes)' are numeric, and handle non-numeric values
    df['Total DL (Bytes)'] = pd.to_numeric(df['Total DL (Bytes)'], errors='coerce')
    df['Total UL (Bytes)'] = pd.to_numeric(df['Total UL (Bytes)'], errors='coerce')
    
    # Fill NaN values with 0
    df['Total DL (Bytes)'].fillna(0, inplace=True)
    df['Total UL (Bytes)'].fillna(0, inplace=True)

    # Aggregate user engagement metrics (calculate total DL and UL separately)
    user_engagement = df.groupby('MSISDN/Number').agg(
        session_frequency=('Bearer Id', 'count'),  # Count the number of sessions
        total_session_duration=('Dur. (ms)', 'sum'),  # Sum of session duration
        total_download_data=('Total DL (Bytes)', 'sum'),  # Sum of download data
        total_upload_data=('Total UL (Bytes)', 'sum')  # Sum of upload data
    ).reset_index()

    # Calculate total traffic by adding download and upload traffic
    user_engagement['total_traffic'] = user_engagement['total_download_data'] + user_engagement['total_upload_data']

    return user_engagement