import pandas as pd
import numpy as np
from scipy import stats

def clean_data(df):
    """Clean the dataset by replacing missing values and undefined values."""
    
    # Step 1: Replace 'undefined' with 'Unknown' for categorical columns
    categorical_columns = ['Handset Manufacturer', 'Handset Type', 'Last Location Name']
    for column in categorical_columns:
        if column in df.columns:
            df[column] = df[column].replace('undefined', 'Unknown')
    
    # Step 2: Handle missing values in numeric columns
    for column in df.select_dtypes(include=[np.number]).columns:
        
        # Replace missing values (NaN) with the median
        median = df[column].median()
        df[column].fillna(median, inplace=True)
        
        # Calculate Z-scores to detect outliers
        z_scores = stats.zscore(df[column])
        
        # Define the threshold for outliers (e.g., Z-score > 3 or Z-score < -3)
        threshold = 3
        
        # Replace outliers with the median
        df[column] = np.where(np.abs(z_scores) > threshold, median, df[column])
    
    # Step 3: Handle missing and invalid 'Start' and 'End' dates
    # Convert 'Start' and 'End' columns to datetime format
    df['Start'] = pd.to_datetime(df['Start'], errors='coerce')  # Convert invalid dates to NaT
    df['End'] = pd.to_datetime(df['End'], errors='coerce')      # Convert invalid dates to NaT
    
    # Fill missing dates with a placeholder or median date
    # Option 1: Fill missing dates with a specific placeholder (e.g., 'Unknown')
    df['Start'].fillna(pd.Timestamp('1970-01-01 00:00:00'), inplace=True)  # Example placeholder
    df['End'].fillna(pd.Timestamp('1970-01-01 00:00:00'), inplace=True)    # Example placeholder
    
    # Option 2: Alternatively, you can drop rows with missing 'Start' or 'End' dates
    # df.dropna(subset=['Start', 'End'], inplace=True)
    
    # Step 4: Replace any remaining null values in categorical columns with 'Unknown'
    for column in categorical_columns:
        if column in df.columns:
            df[column].fillna('Unknown', inplace=True)
    
    return df