import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

from models.experience_analysis import experience_clustering
from models.engagement_analysis import classify_customers_by_engagment

def assign_experience_score(data):
    
    [df,features,cluster_df,scaler,experience_cluster_centers] = experience_clustering(data)

    #Determine the cluster with the worst experience by calculating the Euclidean distance of each cluster center from the origin
    worst_cluster_idx = np.argmax([np.sqrt(np.sum(center ** 2)) for center in experience_cluster_centers])

    worst_cluster_center = experience_cluster_centers[worst_cluster_idx]

    grouped = df.groupby("MSISDN/Number")
    experience_scores = grouped[features.columns].apply(lambda x: np.sqrt(np.sum((scaler.transform(x) - worst_cluster_center) ** 2, axis=1)).mean())

    # Add the experience scores to the original DataFrame
    df["Experience Score"] = df["MSISDN/Number"].map(experience_scores)

    # Sort the DataFrame by the Experience Score in ascending order
    df = df.sort_values(by="Experience Score")

    # Print the top 10 users with the worst experience scores
    print("Top 10 users with the worst experience scores:")
    print(df.head(10)[["MSISDN/Number", "Experience Score"]])

    return df[["MSISDN/Number","Cluster", "Experience Score"]]

def assign_engagment_score(data):
    
    [df,features,cluster_df,scaler,engagment_cluster_centers] = classify_customers_by_engagment(data)

    #Determine the cluster with the worst engagement by calculating the Euclidean distance of each cluster center from the origin
    worst_cluster_idx = np.argmax([np.sqrt(np.sum(center ** 2)) for center in engagment_cluster_centers])

    worst_cluster_center = engagment_cluster_centers[worst_cluster_idx]

    grouped = df.groupby("tuser")
    engagement_scores = grouped[features.columns].apply(lambda x: np.sqrt(np.sum((scaler.transform(x) - worst_cluster_center) ** 2, axis=1)).mean())

    # Add the experience scores to the original DataFrame
    df["Engagment Score"] = df["tuser"].map(engagement_scores)

    # Sort the DataFrame by the Experience Score in ascending order
    df = df.sort_values(by="Engagment Score")

    # Print the top 10 users with the worst experience scores
    print("Top 10 users with the worst engagment scores:")
    print(df.head(10)[["tuser", "Engagment Score"]])

    return df[["tuser","Cluster", "Engagment Score"]]

def assign_satisfaction_score(df_experience_score,df_engagment_score):
    #join the two dataframes on userId
    merged_df = pd.merge(df_experience_score,df_engagment_score,left_on="MSISDN/Number",right_on="tuser",how="inner")
    merged_df["Satisfaction Score"]=(merged_df["Experience Score"] + merged_df["Engagment Score"])/2
    print(merged_df.columns)
    result_df = merged_df[["MSISDN/Number", "Experience Score", "Engagment Score", "Satisfaction Score"]].sort_values(by="Satisfaction Score", ascending=False)

    return result_df



def statisfaction_clustering(dataframe):
    """
    Perform K-Means clustering on the given dataset. and returns the cluster description and the clustrres
    """
   
    # Extract relevant features for clustering
    features = dataframe[['Experience Score', 'Engagment Score']]

    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(features)

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=2, random_state=42)
    kmeans.fit(X_scaled)
    dataframe['Cluster'] = kmeans.labels_

    # Analyze the clusters
    cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)  # Scale back to original values
    
    cluster_descriptions = []

    for i, center in enumerate(cluster_centers):
        description = {
            "Cluster": i + 1,
            "Experience Score": center[0],
            "Engagment Score": center[1],
        }
        cluster_descriptions.append(description)
    
    # Create DataFrame from cluster descriptions
    cluster_df = pd.DataFrame(cluster_descriptions)
    cluster_df.set_index("Cluster", inplace=True)

    # Print cluster descriptions
    for cluster_desc in cluster_descriptions:
        print("Cluster {}: ".format(cluster_desc["Cluster"]))
        print("Experience: {:.2f}".format(cluster_desc["Experience Score"]))
        print("Engagment: {:.2f}".format(cluster_desc["Engagment Score"]))
        print()
    
    return dataframe,cluster_df#,features,scaler,cluster_centers