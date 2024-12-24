import matplotlib.pyplot as plt

def calculate_satisfaction_score(user_data):
    
    # Calculate the satisfaction score as the average of engagement and experience scores
    user_data['satisfaction_score'] = (user_data['engagement_score'] + user_data['experience_score']) / 2
    
    # Sort the users by satisfaction score in descending order
    top_10_satisfied_customers = user_data[['MSISDN/Number', 'satisfaction_score']].sort_values(
        by='satisfaction_score', ascending=False).head(10)
        
    # return top_10_satisfied_customers

    customer_ids = top_10_satisfied_customers['MSISDN/Number']
    satisfaction_scores = top_10_satisfied_customers['satisfaction_score']

    # Create a horizontal bar chart
    plt.figure(figsize=(10, 6))
    plt.barh(customer_ids, satisfaction_scores, color='skyblue')
    plt.xlabel('Satisfaction Score')
    plt.ylabel('Customer ID')
    plt.title('Top 10 Satisfied Customers')

    # Show the plot
    plt.show()