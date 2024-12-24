def experience_analytics(df):

    # Treat missing values: Replace missing with mean (for numeric columns) and mode (for categorical columns)
    df['TCP DL Retrans. Vol (Bytes)'] = df['TCP DL Retrans. Vol (Bytes)'].fillna(df['TCP DL Retrans. Vol (Bytes)'].mean())
    df['TCP UL Retrans. Vol (Bytes)'] = df['TCP UL Retrans. Vol (Bytes)'].fillna(df['TCP UL Retrans. Vol (Bytes)'].mean())
    df['Avg RTT DL (ms)'] = df['Avg RTT DL (ms)'].fillna(df['Avg RTT DL (ms)'].mean())
    df['Avg RTT UL (ms)'] = df['Avg RTT UL (ms)'].fillna(df['Avg RTT UL (ms)'].mean())
    df['Handset Type'] = df['Handset Type'].fillna(df['Handset Type'].mode()[0])
    df['Avg Bearer TP DL (kbps)'] = df['Avg Bearer TP DL (kbps)'].fillna(df['Avg Bearer TP DL (kbps)'].mean())
    df['Avg Bearer TP UL (kbps)'] = df['Avg Bearer TP UL (kbps)'].fillna(df['Avg Bearer TP UL (kbps)'].mean())

    # Aggregate metrics per customer
    experience_df = df.groupby('MSISDN/Number').agg(
        avg_tcp_retransmission=('TCP DL Retrans. Vol (Bytes)', 'mean'),
        avg_rtt=('Avg RTT DL (ms)', 'mean'),
        avg_throughput=('Avg Bearer TP DL (kbps)', 'mean'),
        handset_type=('Handset Type', lambda x: x.mode()[0])  # Mode is used to get the most common handset per customer
    ).reset_index()

    return experience_df
