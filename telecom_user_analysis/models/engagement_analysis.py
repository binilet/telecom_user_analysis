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
    
    # df = original_df.drop(columns=['tuser'])
    # Extract engagement metrics columns
    columns = ["sessionFrequencie", "duration", "totalData"]
    columns_T = ['sessionFrequencie_T','duration_T','totalData_T']

    # Apply normalization to engagement metrics columns
    scaler = StandardScaler()
    df[columns_T] = scaler.fit_transform(df[columns])

    # Perform k-means clustering
    kmeans = KMeans(n_clusters=3)

    kmeans.fit(df[columns_T])
    
    df['kmeans_lables'] = kmeans.labels_

    return df
