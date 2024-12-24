def report_throughput_tcp(throughput_df, tcp_df):
    """
    Print the interpretation of the findings for average throughput and TCP retransmission per handset type.

    :param throughput_df: DataFrame containing average throughput per handset type
    :param tcp_df: DataFrame containing average TCP retransmission per handset type
    """
    # Interpret the throughput findings
    print("Interpretation of Average Throughput per Handset Type:")
    top_throughput_handset = throughput_df.nlargest(1, 'avg_throughput')
    low_throughput_handset = throughput_df.nsmallest(1, 'avg_throughput')
    print(f"Handset Type with the highest average throughput: {top_throughput_handset.iloc[0]['Handset Type']} ({top_throughput_handset.iloc[0]['avg_throughput']} kbps)")
    print(f"Handset Type with the lowest average throughput: {low_throughput_handset.iloc[0]['Handset Type']} ({low_throughput_handset.iloc[0]['avg_throughput']} kbps)\n")

    # Interpret the TCP retransmission findings
    print("Interpretation of Average TCP Retransmission per Handset Type:")
    top_tcp_handset = tcp_df.nlargest(1, 'avg_tcp_retransmission')
    low_tcp_handset = tcp_df.nsmallest(1, 'avg_tcp_retransmission')
    print(f"Handset Type with the highest average TCP retransmission: {top_tcp_handset.iloc[0]['Handset Type']} ({top_tcp_handset.iloc[0]['avg_tcp_retransmission']} Bytes)")
    print(f"Handset Type with the lowest average TCP retransmission: {low_tcp_handset.iloc[0]['Handset Type']} ({low_tcp_handset.iloc[0]['avg_tcp_retransmission']} Bytes)")
