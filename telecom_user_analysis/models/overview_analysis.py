import pandas as pd

from utils.utils import handle_numerical_missing_values,handle_string_missing_values


#may be i should do data cleaning and transformation after loading to a dataframe

def get_top_handsets(data):
    columns = ["Handset Type","Count"]
    df = pd.DataFrame(data,columns=columns)
    return df

def get_top_manufacturers(data):
    columns = ["Handset Manufacturer","Count"]
    df = pd.DataFrame(data,columns=columns)
    return df

def get_top_five_handset_per_top_three_manufactureres(data):
    columns = ["Handset Manufacturer", "Handset Type"]
    df = pd.DataFrame(data, columns=columns)

    # Count the occurrences of each handset type within each manufacturer group
    handset_counts = df.groupby('Handset Manufacturer')['Handset Type'].value_counts().reset_index(name='count')

    # Get the top five handsets for each manufacturer
    top_handsets_per_manufacturer = df.groupby('Handset Manufacturer').head(5)

    # Merge the counts back to the DataFrame
    top_handsets_per_manufacturer = pd.merge(top_handsets_per_manufacturer, handset_counts, on=['Handset Manufacturer', 'Handset Type'], how='left')

    return top_handsets_per_manufacturer

def calculate_univariate_dispersion(data):
    """
        this dipersion param analysis will calculate the range,variance and std deviation for each column
    """
    columns = ["Handset Manufacturer","Handset Type","MSISDN/Number","Dur. (ms)","Social Media DL (Bytes)",
                "Social Media UL (Bytes)","Google DL (Bytes)","Google UL (Bytes)",
                "Email DL (Bytes)","Email UL (Bytes)","Youtube DL (Bytes)","Youtube UL (Bytes)",
                "Netflix DL (Bytes)","Netflix UL (Bytes)","Gaming DL (Bytes)",
                "Gaming UL (Bytes)","Total UL (Bytes)","Total DL (Bytes)"]
    
    data_types = {
    "Handset Manufacturer": str,
    "Handset Type": str,
    "MSISDN/Number": str,
    "Dur. (ms)": float,
    "Social Media DL (Bytes)": float,
    "Social Media UL (Bytes)": float,
    "Google DL (Bytes)": float,
    "Google UL (Bytes)": float,
    "Email DL (Bytes)": float,
    "Email UL (Bytes)": float,
    "Youtube DL (Bytes)": float,
    "Youtube UL (Bytes)": float,
    "Netflix DL (Bytes)": float,
    "Netflix UL (Bytes)": float,
    "Gaming DL (Bytes)": float,
    "Gaming UL (Bytes)": float,
    "Total UL (Bytes)": float,
    "Total DL (Bytes)": float
}
    
    df = pd.DataFrame(data,columns=columns).astype(data_types)
    print(df.dtypes)

    #handle numerical missing values
    df = handle_numerical_missing_values(df).astype(data_types)

    print('after numerical missing')
    print(df.dtypes)

    print(df.head(3))

    print('start analysis ...')
    dispersion_vals = {}
    for column in df.columns:
        

        if df[column].dtype == float:
            mean = df[column].mean()
            range_val = df[column].max() - df[column].min()
            variance = df[column].var()
            std_deviation = df[column].std()
            dispersion_vals[column] = {
                'Mean': mean,
                'Range' : range_val,
                "Variance" : variance,
                "Standard Deviation" : std_deviation
            }
        
    return (df,dispersion_vals)