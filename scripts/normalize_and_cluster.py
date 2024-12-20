from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

def normalize_and_cluster(df):
    """
    Normalize engagement metrics and run K-Means clustering with k=3.
    """
    # Select metrics for normalization
    metrics_to_normalize = df[['session_frequency', 'total_session_duration', 'total_traffic']]

    # Normalize the data using Min-Max scaling
    scaler = MinMaxScaler()
    normalized_metrics = scaler.fit_transform(metrics_to_normalize)

    # Run K-Means with k=3
    kmeans = KMeans(n_clusters=3, random_state=0)
    df['cluster'] = kmeans.fit_predict(normalized_metrics)

    return df, kmeans