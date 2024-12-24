import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

def preprocess_data_for_clustering(df):
    """
    Preprocess the data for k-means clustering: 
    - Normalize numeric experience metrics (TCP retransmission, RTT, throughput)
    - One-hot encode the handset type
    """
    # Select relevant experience metrics
    experience_metrics = df[['avg_tcp_retransmission', 'avg_rtt', 'avg_throughput', 'handset_type']].copy()
    
    # Normalize the numeric columns (TCP, RTT, throughput)
    scaler = StandardScaler()
    experience_metrics.loc[:, ['avg_tcp_retransmission', 'avg_rtt', 'avg_throughput']] = scaler.fit_transform(
        experience_metrics[['avg_tcp_retransmission', 'avg_rtt', 'avg_throughput']]
    )
    
    # One-hot encode the handset type
    encoder = OneHotEncoder()
    handset_encoded = pd.DataFrame(encoder.fit_transform(experience_metrics[['handset_type']]).toarray(), index=experience_metrics.index)
    
    # Merge the encoded handset data with the normalized metrics
    experience_metrics = experience_metrics.drop('handset_type', axis=1)
    experience_metrics = pd.concat([experience_metrics, handset_encoded], axis=1)
    
    # Ensure all column names are strings
    experience_metrics.columns = experience_metrics.columns.astype(str)
    
    return experience_metrics