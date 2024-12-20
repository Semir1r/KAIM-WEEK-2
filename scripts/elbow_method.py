def elbow_method(df):
    """
    Apply the elbow method to determine the optimal value of k for K-Means clustering.
    """
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import MinMaxScaler
    import matplotlib.pyplot as plt

    # Normalize the data
    metrics_to_normalize = df[['session_frequency', 'total_session_duration', 'total_traffic']]
    scaler = MinMaxScaler()
    normalized_metrics = scaler.fit_transform(metrics_to_normalize)

    # Run K-Means for different values of k
    inertia = []
    k_range = range(1, 11)
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=0)
        kmeans.fit(normalized_metrics)
        inertia.append(kmeans.inertia_)

    # Plot the inertia values for the elbow method
    plt.figure(figsize=(10, 6))
    plt.plot(k_range, inertia, 'bo-')
    plt.title('Elbow Method for Optimal K')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Inertia')
    plt.show()