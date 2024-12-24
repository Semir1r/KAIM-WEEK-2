def describe_clusters(df, clusters):
    
    df['cluster'] = clusters
    
    # Group by cluster and compute descriptive statistics for each cluster
    cluster_summary = df.groupby('cluster').agg(
        avg_tcp_retransmission=('avg_tcp_retransmission', 'mean'),
        avg_rtt=('avg_rtt', 'mean'),
        avg_throughput=('avg_throughput', 'mean'),
        handset_type=('handset_type', lambda x: x.mode()[0])  # Most frequent handset type
    ).reset_index()
    
    # Display the cluster descriptions
    for idx, row in cluster_summary.iterrows():
        print(f"Cluster {row['cluster']} Description:")
        print(f"  - Average TCP Retransmission: {row['avg_tcp_retransmission']:.2f}")
        print(f"  - Average RTT: {row['avg_rtt']:.2f} ms")
        print(f"  - Average Throughput: {row['avg_throughput']:.2f} kbps")
        print(f"  - Most Common Handset Type: {row['handset_type']}")
        print("\n")
