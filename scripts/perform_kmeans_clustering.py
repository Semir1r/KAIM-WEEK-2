from sklearn.cluster import KMeans

def perform_kmeans_clustering(df, k=3):
    """
    Perform K-Means clustering on the preprocessed data.
    
    :param df: Preprocessed DataFrame containing normalized experience metrics and one-hot encoded handset type
    :param k: Number of clusters for K-Means (default is 3)
    :return: Cluster labels for each user
    """
    kmeans = KMeans(n_clusters=k, random_state=42)
    clusters = kmeans.fit_predict(df)
    
    return clusters