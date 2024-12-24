from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def run_kmeans_on_scores(user_scores, k=2):

    # Extract the engagement and experience scores
    score_data = user_scores[['engagement_score', 'experience_score']]
    
    # Standardize the scores
    scaler = StandardScaler()
    score_data_scaled = scaler.fit_transform(score_data)
    
    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=k, random_state=42)
    user_scores['cluster'] = kmeans.fit_predict(score_data_scaled)
    
    # Return the updated DataFrame with cluster labels
    return user_scores, kmeans.cluster_centers_