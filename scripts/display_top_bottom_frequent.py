def top_bottom_frequent_values(df, column, n=10):
    """
    This function computes and returns the top, bottom, and most frequent values for a specified column.

    :param df: DataFrame containing the data
    :param column: The column name for which to compute the top, bottom, and frequent values
    :param n: The number of values to return (default is 10)
    :return: A dictionary containing top, bottom, and most frequent values
    """
    top_values = df[column].nlargest(n)
    bottom_values = df[column].nsmallest(n)
    most_frequent_values = df[column].value_counts().head(n)
    
    return {
        'top_values': top_values,
        'bottom_values': bottom_values,
        'most_frequent_values': most_frequent_values
    }

def display_top_bottom_frequent(df):
    """
    This function computes and displays the top, bottom, and most frequent values for TCP, RTT, and Throughput.
    
    :param df: DataFrame containing telecommunication data
    """

    # Top, bottom, and most frequent TCP values
    tcp_values = top_bottom_frequent_values(df, 'TCP DL Retrans. Vol (Bytes)')
    print("TCP Retransmission Values:")
    print(f"Top 10:\n{tcp_values['top_values']}")
    print(f"Bottom 10:\n{tcp_values['bottom_values']}")
    print(f"Most Frequent:\n{tcp_values['most_frequent_values']}\n")

    # Top, bottom, and most frequent RTT values
    rtt_values = top_bottom_frequent_values(df, 'Avg RTT DL (ms)')
    print("RTT Values:")
    print(f"Top 10:\n{rtt_values['top_values']}")
    print(f"Bottom 10:\n{rtt_values['bottom_values']}")
    print(f"Most Frequent:\n{rtt_values['most_frequent_values']}\n")

    # Top, bottom, and most frequent Throughput values
    throughput_values = top_bottom_frequent_values(df, 'Avg Bearer TP DL (kbps)')
    print("Throughput Values:")
    print(f"Top 10:\n{throughput_values['top_values']}")
    print(f"Bottom 10:\n{throughput_values['bottom_values']}")
    print(f"Most Frequent:\n{throughput_values['most_frequent_values']}\n")