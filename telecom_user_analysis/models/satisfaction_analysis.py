import numpy as np
import pandas as pd

from models.experience_analysis import experience_clustering

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