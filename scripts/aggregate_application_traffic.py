def aggregate_application_traffic(df):
    """
    Aggregate total traffic per application for each customer and report the top 10 most engaged users per application.
    """
    # Calculate total traffic for each application
    df['social_media_traffic'] = df['Social Media DL (Bytes)'] + df['Social Media UL (Bytes)']
    df['google_traffic'] = df['Google DL (Bytes)'] + df['Google UL (Bytes)']
    df['youtube_traffic'] = df['Youtube DL (Bytes)'] + df['Youtube UL (Bytes)']
    df['netflix_traffic'] = df['Netflix DL (Bytes)'] + df['Netflix UL (Bytes)']
    df['gaming_traffic'] = df['Gaming DL (Bytes)'] + df['Gaming UL (Bytes)']
    df['Other Traffic'] = df['Other DL (Bytes)'] + df['Other UL (Bytes)']

    # Aggregate traffic per user
    app_traffic = df.groupby('MSISDN/Number').agg(
        total_social_media=('social_media_traffic', 'sum'),
        total_google=('google_traffic', 'sum'),
        total_youtube=('youtube_traffic', 'sum'),
        total_netflix=('netflix_traffic', 'sum'),
        total_gaming=('gaming_traffic', 'sum'),
        total_other=('Other Traffic', 'sum')
    ).reset_index()

    return app_traffic