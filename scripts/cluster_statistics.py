def cluster_statistics(df):
    """
    Compute minimum, maximum, average, and total values for each metric per cluster.
    """
    cluster_stats = df.groupby('cluster').agg(
        min_session_frequency=('session_frequency', 'min'),
        max_session_frequency=('session_frequency', 'max'),
        avg_session_frequency=('session_frequency', 'mean'),
        total_session_frequency=('session_frequency', 'sum'),

        min_session_duration=('total_session_duration', 'min'),
        max_session_duration=('total_session_duration', 'max'),
        avg_session_duration=('total_session_duration', 'mean'),
        total_session_duration=('total_session_duration', 'sum'),

        min_total_traffic=('total_traffic', 'min'),
        max_total_traffic=('total_traffic', 'max'),
        avg_total_traffic=('total_traffic', 'mean'),
        total_total_traffic=('total_traffic', 'sum')
    ).reset_index()

    return cluster_stats