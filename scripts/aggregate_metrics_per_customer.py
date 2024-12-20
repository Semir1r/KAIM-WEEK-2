def aggregate_metrics_per_customer(df):
    """
    This function aggregates session frequency, total session duration, and total traffic per customer (MSISDN).
    """
    # Aggregate metrics
    customer_metrics = df.groupby('MSISDN/Number').agg(
        session_frequency=('Bearer Id', 'count'),  # Count number of sessions
        total_session_duration=('Dur. (ms)', 'sum'),  # Total session duration
        total_download=('Total DL (Bytes)', 'sum'),  # Total download data
        total_upload=('Total UL (Bytes)', 'sum')  # Total upload data
    ).reset_index()

    # Calculate total traffic as download + upload
    customer_metrics['total_traffic'] = customer_metrics['total_download'] + customer_metrics['total_upload']

    return customer_metrics