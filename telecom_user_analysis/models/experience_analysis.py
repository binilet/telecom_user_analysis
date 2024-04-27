import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

from utils.utils import handle_numerical_missing_values,handle_string_missing_values

def get_experience_data(data):
    
    columns = [
        "MSISDN/Number",
        "Handset Type",
        "Avg RTT DL (ms)",
        "Avg RTT UL (ms)",
        "TCP DL Retrans. Vol (Bytes)",
        "TCP UL Retrans. Vol (Bytes)",
        "Avg Bearer TP DL (kbps)",
        "Avg Bearer TP UL (kbps)"
    ]

    raw_df = pd.DataFrame(data, columns=columns)

    raw_df = handle_numerical_missing_values(raw_df)

    raw_df = handle_string_missing_values(raw_df)

    return raw_df


#aggregate per customer the tootal rtt, total tcp retran, total through put
def aggregate_experience_data_per_customer(data):
    df = get_experience_data(data)

    #first sum the values
    df['Total RTT'] = df['Avg RTT DL (ms)'] + df['Avg RTT UL (ms)']
    df['Total TCP Retran'] = df['TCP DL Retrans. Vol (Bytes)'] + df['TCP UL Retrans. Vol (Bytes)']
    df['Total TP'] = df['Avg Bearer TP DL (kbps)'] + df['Avg Bearer TP UL (kbps)']

      # Group by 'MSISDN/Number' and aggregate the data
    aggregated_data = df.groupby('MSISDN/Number').agg({
        'Total RTT': 'sum',
        'Total TCP Retran': 'sum',
        'Total TP': 'sum',
        'Handset Type': 'first'  
    }).reset_index()

    return aggregated_data


def top_ten_experience_metrics(df):
    """
    Computes & lists 10 of the top, bottom and most frequent:
    """

    top_tcp = df['Total TCP Retran'].nlargest(10)
    bottom_tcp =  df['Total TCP Retran'].nsmallest(10)
    frequent_tcp = df['Total TCP Retran'].nsmallest(10).value_counts().head(10)

    top_rtt = df['Total RTT'].nlargest(10)
    bottom_rtt =  df['Total RTT'].nsmallest(10)
    frequent_rtt = df['Total RTT'].nsmallest(10).value_counts().head(10)

    top_tp = df['Total TP'].nlargest(10)
    bottom_tp =  df['Total TP'].nsmallest(10)
    frequent_tp = df['Total TP'].nsmallest(10).value_counts().head(10)


def distribution_tp_per_handset(data):
    """
    The distribution of the average throughput  per handset type
    """
    df = get_experience_data(data)

    #get total tp
    df['Total TP'] = df['Avg Bearer TP DL (kbps)'] + df['Avg Bearer TP UL (kbps)']
    top_tp = df.nlargest(10,'Total TP')
    
    #group by handset type and take the mean of the total throughput
    grouped_data = top_tp.groupby('Handset Type')['Total TP'].mean()
    
    return grouped_data

def distribution_tcp_per_handset(data):
    """
    The distribution of the average tcp transmission  per handset type
    """
    df = get_experience_data(data)
    #get total tp
    df['Total TCP Retran'] = df['TCP DL Retrans. Vol (Bytes)'] + df['TCP UL Retrans. Vol (Bytes)']
    print('tootal added ...')
    mod_df = df[['TCP DL Retrans. Vol (Bytes)','TCP UL Retrans. Vol (Bytes)','Total TCP Retran']]
    print(mod_df)
    top_tp = df.nlargest(10,'Total TCP Retran')
    print(top_tp.head(10))
    #group by handset type and take the mean of the total throughput
    grouped_data = top_tp.groupby('Handset Type')['Total TCP Retran'].mean()
    
    return grouped_data



def experience_clustering(raw_data):
    """
    Perform K-Means clustering on the given dataset. and returns the cluster description and the clustrres
    """
    data = get_experience_data(raw_data)
    

    # Sum pairs of fields
    data['Total RTT'] = data["Avg RTT DL (ms)"] + data["Avg RTT UL (ms)"]
    data['Total TCP Retrans. Vol (Bytes)'] = data["TCP DL Retrans. Vol (Bytes)"] + data["TCP UL Retrans. Vol (Bytes)"]
    data['Total Avg Bearer TP DL (kbps)'] = data["Avg Bearer TP DL (kbps)"] + data["Avg Bearer TP UL (kbps)"]

    # Extract relevant features for clustering
    features = data[['Total RTT', 'Total TCP Retrans. Vol (Bytes)', 'Total Avg Bearer TP DL (kbps)']]

    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(features)

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X_scaled)
    data['Cluster'] = kmeans.labels_

    # Analyze the clusters
    cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)  # Scale back to original values
    
    cluster_descriptions = []

    for i, center in enumerate(cluster_centers):
        description = {
            "Cluster": i + 1,
            "Total RTT": center[0],
            "Total TCP Retrans. Vol (Bytes)": center[1],
            "Total Avg Bearer TP DL (kbps)": center[2]
        }
        cluster_descriptions.append(description)
    
    # Create DataFrame from cluster descriptions
    cluster_df = pd.DataFrame(cluster_descriptions)
    cluster_df.set_index("Cluster", inplace=True)

    # Print cluster descriptions
    for cluster_desc in cluster_descriptions:
        print("Cluster {}: ".format(cluster_desc["Cluster"]))
        print("Total RTT: {:.2f}".format(cluster_desc["Total RTT"]))
        print("Total TCP Retrans. Vol (Bytes): {:.2f}".format(cluster_desc["Total TCP Retrans. Vol (Bytes)"]))
        print("Total Avg Bearer TP DL (kbps): {:.2f}".format(cluster_desc["Total Avg Bearer TP DL (kbps)"]))
        print()
    
    return data,cluster_df,features,scaler,cluster_centers