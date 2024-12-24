import seaborn as sns
import matplotlib.pyplot as plt

def plot_distributions(throughput_df, tcp_df):

    # Plot throughput distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(throughput_df['avg_throughput'], bins=30, kde=True)
    plt.title('Distribution of Average Throughput per Handset Type')
    plt.xlabel('Average Throughput (kbps)')
    plt.ylabel('Frequency')
    plt.show()

    # Plot TCP retransmission distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(tcp_df['avg_tcp_retransmission'], bins=30, kde=True)
    plt.title('Distribution of Average TCP Retransmission per Handset Type')
    plt.xlabel('Average TCP Retransmission (Bytes)')
    plt.ylabel('Frequency')
    plt.show()