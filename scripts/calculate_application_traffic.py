import pandas as pd

def calculate_application_traffic(df):
    """
    This function calculates the total traffic contributed by each application (Social Media, Google, YouTube, etc.)
    per user and returns a DataFrame with total traffic and contribution percentages.
    """

    # Ensure relevant application data columns are numeric
    app_columns = [
        'Social Media DL (Bytes)', 'Google DL (Bytes)', 'Youtube DL (Bytes)', 'Netflix DL (Bytes)',
        'Gaming DL (Bytes)', 'Other DL (Bytes)', 'Social Media UL (Bytes)', 'Google UL (Bytes)',
        'Youtube UL (Bytes)', 'Netflix UL (Bytes)', 'Gaming UL (Bytes)', 'Other UL (Bytes)'
    ]
    for col in app_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # Calculate total traffic per application (Download + Upload) for each user
    df['Social Media Traffic'] = df['Social Media DL (Bytes)'] + df['Social Media UL (Bytes)']
    df['Google Traffic'] = df['Google DL (Bytes)'] + df['Google UL (Bytes)']
    df['YouTube Traffic'] = df['Youtube DL (Bytes)'] + df['Youtube UL (Bytes)']
    df['Netflix Traffic'] = df['Netflix DL (Bytes)'] + df['Netflix UL (Bytes)']
    df['Gaming Traffic'] = df['Gaming DL (Bytes)'] + df['Gaming UL (Bytes)']
    df['Other Traffic'] = df['Other DL (Bytes)'] + df['Other UL (Bytes)']

    # Calculate total traffic for each user
    df['Total Traffic'] = df['Total DL (Bytes)'] + df['Total UL (Bytes)']

    # Aggregate data per user
    user_application_traffic = df.groupby('MSISDN/Number').agg(
        total_traffic=('Total Traffic', 'sum'),
        social_media_traffic=('Social Media Traffic', 'sum'),
        google_traffic=('Google Traffic', 'sum'),
        youtube_traffic=('YouTube Traffic', 'sum'),
        netflix_traffic=('Netflix Traffic', 'sum'),
        gaming_traffic=('Gaming Traffic', 'sum'),
        other_traffic=('Other Traffic', 'sum')
    ).reset_index()

    # Calculate percentage contribution of each application to the total traffic
    user_application_traffic['Social Media %'] = (user_application_traffic['social_media_traffic'] / user_application_traffic['total_traffic']) * 100
    user_application_traffic['Google %'] = (user_application_traffic['google_traffic'] / user_application_traffic['total_traffic']) * 100
    user_application_traffic['YouTube %'] = (user_application_traffic['youtube_traffic'] / user_application_traffic['total_traffic']) * 100
    user_application_traffic['Netflix %'] = (user_application_traffic['netflix_traffic'] / user_application_traffic['total_traffic']) * 100
    user_application_traffic['Gaming %'] = (user_application_traffic['gaming_traffic'] / user_application_traffic['total_traffic']) * 100
    user_application_traffic['Other %'] = (user_application_traffic['other_traffic'] / user_application_traffic['total_traffic']) * 100

    return user_application_traffic
