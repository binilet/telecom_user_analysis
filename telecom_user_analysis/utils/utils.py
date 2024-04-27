#this file will be used for utility functions including handling missing values in data frames

def handle_numerical_missing_values(df,engagment=False):
    """
    For the sake of our analysis, we will use the mean value of the columns for the missing values.
    """
    exclude_column = "MSISDN/Number"
    if(engagment):
        exclude_column = "tuser"
    

    # Select numerical columns excluding the MSISDN/Number
    numerical_columns = df.select_dtypes(include=['float64']).columns.drop(exclude_column)

    # Fill missing values in selected numerical columns with their means
    df[numerical_columns] = df[numerical_columns].fillna(df[numerical_columns].mean())

    # Check if there are any remaining NaN values in the DataFrame
    if df[numerical_columns].isnull().values.any():
        print("******There are still NaN values present in the DataFrame.******")
    else:
        print("All NaN values have been filled successfully.")

    return df

def handle_string_missing_values(df):
    """
    For string missing values, we will replace those values with the most frequent category (mode) in the respective column.
    """
    string_columns = df.select_dtypes(include=['object'])
    
    for column in string_columns:
        mode = df[column].mode()[0]
        df[column] = df[column].fillna(mode)
    
    return df


def get_working_fields():
    return ["Handset Manufacturer","Handset Type","MSISDN/Number","Dur. (ms)","Social Media DL (Bytes)",
                "Social Media UL (Bytes)","Google DL (Bytes)","Google UL (Bytes)",
                "Email DL (Bytes)","Email UL (Bytes)","Youtube DL (Bytes)","Youtube UL (Bytes)",
                "Netflix DL (Bytes)","Netflix UL (Bytes)","Gaming DL (Bytes)",
                "Gaming UL (Bytes)","Total UL (Bytes)","Total DL (Bytes)"]

def set_working_data_types():
    return {
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