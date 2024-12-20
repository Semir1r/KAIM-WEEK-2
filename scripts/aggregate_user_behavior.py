def aggregate_user_behavior(df):
    """
    Aggregate user behavior per user.
    This function will return a DataFrame with aggregated data for each user including:
    - Number of xDR sessions
    - Total session duration
    - Total download (DL) and upload (UL) data
    - Total data volume (in Bytes) for each application
    """

    # Aggregate per user
    aggregated_data = df.groupby('MSISDN/Number').agg(
        number_of_xdr_sessions=('Bearer Id', 'count'),  # Count the number of xDR sessions
        total_session_duration=('Dur. (ms)', 'sum'),  # Total session duration
        total_download_data=('Total DL (Bytes)', 'sum'),  # Total download data
        total_upload_data=('Total UL (Bytes)', 'sum'),  # Total upload data
        
        # Total data volume for each application
        social_media_dl=('Social Media DL (Bytes)', 'sum'),
        google_dl=('Google DL (Bytes)', 'sum'),
        email_dl=('Email DL (Bytes)', 'sum'),
        youtube_dl=('Youtube DL (Bytes)', 'sum'),
        netflix_dl=('Netflix DL (Bytes)', 'sum'),
        gaming_dl=('Gaming DL (Bytes)', 'sum'),
        other_dl=('Other DL (Bytes)', 'sum'),
        social_media_ul=('Social Media UL (Bytes)', 'sum'),
        google_ul=('Google UL (Bytes)', 'sum'),
        email_ul=('Email UL (Bytes)', 'sum'),
        youtube_ul=('Youtube UL (Bytes)', 'sum'),
        netflix_ul=('Netflix UL (Bytes)', 'sum'),
        gaming_ul=('Gaming UL (Bytes)', 'sum'),
        other_ul=('Other UL (Bytes)', 'sum')
    ).reset_index()

    return aggregated_data
