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
    columns = ['tuser','sessionFrequencie','duration','totalData']
    df = pd.DataFrame(data,columns=columns)

    df = handle_numerical_missing_values(df,True)

    return df

def get_top_ten(df,column):
    top_10 = df.nlargest(10,column)
    return top_10[['tuser',column]]

def get_top_customers_per_engagment_metrics(data):
    """
        returns top 10 customers per session frequencies,duration and total data
    """
    df = get_classification_data(data)

    top_ten_per_session_frequency = get_top_ten(df,'sessionFrequencie')
    top_ten_per_duration = get_top_ten(df,'duration')
    top_ten_per_totaldata = get_top_ten(df,'totalData')

    return (top_ten_per_session_frequency,top_ten_per_duration,top_ten_per_totaldata)

def classify_customers_by_engagment(data):
    
    df = get_classification_data(data=data)
    print(df.dtypes)
    # df = original_df.drop(columns=['tuser'])
    # Extract engagement metrics columns
    columns = df[['sessionFrequencie', 'duration', 'totalData']]
    
    # Apply normalization to engagement metrics columns
    scaler = StandardScaler()
    columns_scaled = scaler.fit_transform(columns)


    # Perform k-means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(columns_scaled)
    df['Cluster'] = kmeans.labels_

    cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)  # Scale back to original values
    cluster_descriptions = []

    for i, center in enumerate(cluster_centers):
        description = {
            "Cluster": i + 1,
            "Session Frequency": center[0],
            "Duration": center[1],
            "Total Data": center[2]
        }
        cluster_descriptions.append(description)
    
    # Create DataFrame from cluster descriptions
    cluster_df = pd.DataFrame(cluster_descriptions)
    cluster_df.set_index("Cluster", inplace=True)

    # Print cluster descriptions
    for cluster_desc in cluster_descriptions:
        print("Cluster {}: ".format(cluster_desc["Cluster"]))
        print("Session Frequency: {:.2f}".format(cluster_desc["Session Frequency"]))
        print("Duration: {:.2f}".format(cluster_desc["Duration"]))
        print("Total Data: {:.2f}".format(cluster_desc["Total Data"]))
        print()

    return df,cluster_df
