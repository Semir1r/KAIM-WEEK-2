import numpy as np

def assign_scores(user_data, engagement_centroids, experience_centroids):
    """
    Assign engagement and experience scores to users based on Euclidean distance from the least engaged
    and worst experience clusters.
    
    Parameters:
    - user_data: DataFrame containing the user metrics (e.g., engagement, experience metrics).
    - engagement_centroids: Centroids of engagement clusters.
    - experience_centroids: Centroids of experience clusters.
    
    Returns:
    - DataFrame with engagement and experience scores.
    """
    
    # Identify the index of the least engaged and worst experience clusters
    least_engaged_cluster = np.argmin(np.sum(engagement_centroids, axis=1))
    worst_experience_cluster = np.argmax(np.sum(experience_centroids, axis=1))
    
    # Initialize lists to store engagement and experience scores
    engagement_scores = []
    experience_scores = []
    
    # Iterate over each user and calculate the Euclidean distances
    for i, row in user_data.iterrows():
        # Extract the user's engagement and experience data
        user_engagement_data = row[['session_frequency', 'total_session_duration', 'total_traffic']]
        user_experience_data = row[['avg_tcp_retransmission', 'avg_rtt', 'avg_throughput']]
        
        # Calculate the engagement score (distance from least engaged cluster)
        engagement_score = np.linalg.norm(user_engagement_data.values - engagement_centroids[least_engaged_cluster])
        engagement_scores.append(engagement_score)
        
        # Calculate the experience score (distance from worst experience cluster)
        experience_score = np.linalg.norm(user_experience_data.values - experience_centroids[worst_experience_cluster])
        experience_scores.append(experience_score)
    
    # Assign the scores to the user data
    user_data['engagement_score'] = engagement_scores
    user_data['experience_score'] = experience_scores
    
    return user_data
