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

    raw_df = pd.DataFrame(data,columns=columns)
    handle_numerical_missing_values(raw_df)
    handle_string_missing_values(raw_df)
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
    print(top_tp)
    #group by handset type and take the mean of the total throughput
    grouped_data = top_tp.groupby('Handset Type')['Total TP'].mean()
    print(grouped_data.head(5))
    return grouped_data


