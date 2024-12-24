def experience_analytics(df):
    """
    Perform user experience analysis based on network parameters.

    :param df: DataFrame containing telecommunication data
    :return: Aggregated DataFrame with average TCP retransmission, RTT, throughput, and handset type per customer.
    """

    # Treat missing values: Replace missing with mean (for numeric columns) and mode (for categorical columns)
    df['TCP DL Retrans. Vol (Bytes)'].fillna(df['TCP DL Retrans. Vol (Bytes)'].mean(), inplace=True)
    df['TCP UL Retrans. Vol (Bytes)'].fillna(df['TCP UL Retrans. Vol (Bytes)'].mean(), inplace=True)
    df['Avg RTT DL (ms)'].fillna(df['Avg RTT DL (ms)'].mean(), inplace=True)
    df['Avg RTT UL (ms)'].fillna(df['Avg RTT UL (ms)'].mean(), inplace=True)
    df['Handset Type'].fillna(df['Handset Type'].mode()[0], inplace=True)
    df['Avg Bearer TP DL (kbps)'].fillna(df['Avg Bearer TP DL (kbps)'].mean(), inplace=True)
    df['Avg Bearer TP UL (kbps)'].fillna(df['Avg Bearer TP UL (kbps)'].mean(), inplace=True)

    # Aggregate metrics per customer
    experience_df = df.groupby('MSISDN/Number').agg(
        avg_tcp_retransmission=('TCP DL Retrans. Vol (Bytes)', 'mean'),
        avg_rtt=('Avg RTT DL (ms)', 'mean'),
        avg_throughput=('Avg Bearer TP DL (kbps)', 'mean'),
        handset_type=('Handset Type', lambda x: x.mode()[0])  # Mode is used to get the most common handset per customer
    ).reset_index()

    return experience_df
