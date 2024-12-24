def throughput_tcp_per_handset(df):
    
    # Calculate average throughput per handset type
    throughput_per_handset = df.groupby('Handset Type').agg(
        avg_throughput=('Avg Bearer TP DL (kbps)', 'mean')
    ).reset_index()

    # Calculate average TCP retransmission per handset type
    tcp_per_handset = df.groupby('Handset Type').agg(
        avg_tcp_retransmission=('TCP DL Retrans. Vol (Bytes)', 'mean')
    ).reset_index()

    return throughput_per_handset, tcp_per_handset