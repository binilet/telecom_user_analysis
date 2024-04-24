import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

from utils.utils import handle_numerical_missing_values,handle_string_missing_values


def get_top_10_customers_per_engagment(data):
    return data;

def get_classification_data(data):
    """
        returns the dataframe for further analysis
    """
    columns = ["tuser","sessionFrequencie","duration","totalData"]
    df = pd.DataFrame(data,columns=columns)
    return df

def classify_customers_by_engagment(df):
    # Extract engagement metrics columns
    columns = ["sessionFrequencie", "duration", "totalData"]

    # Apply normalization to engagement metrics columns
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])

    # Perform k-means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['cluster_label'] = kmeans.fit_predict(df[columns])

    # Visualize the distribution of cluster labels
    print(df['cluster_label'].value_counts())       
