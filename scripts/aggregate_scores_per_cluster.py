def aggregate_scores_per_cluster(user_scores):

    # Group by the 'cluster' column and compute the average satisfaction and experience scores
    cluster_aggregates = user_scores.groupby('cluster').agg(
        avg_satisfaction_score=('satisfaction_score', 'mean'),
        avg_experience_score=('experience_score', 'mean')
    ).reset_index()
    
    return cluster_aggregates