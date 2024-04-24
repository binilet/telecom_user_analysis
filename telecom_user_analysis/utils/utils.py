#this file will be used for utility functions including handling missing values in data frames

def handle_numerical_missing_values(df):
    """
    For the sake of our analysis, we will use the mean value of the columns for the missing values.
    """
    exclude_column = "MSISDN/Number"
    
    # Select numerical columns excluding the MSISDN/Number we don't need it here; its a customer identifier
    numerical_columns_to_fill = df.select_dtypes(include='float').columns.difference([exclude_column])
    print(f'the numerical fields are: ')
    print(numerical_columns_to_fill)
    # Fill missing values in selected numerical columns with their means
    df[numerical_columns_to_fill].fillna(df[numerical_columns_to_fill].mean(), inplace=True)
    print(df.head(2))
    return df

def handle_string_missing_values(df):
    """
        for string missing values we will use Replace those 
        values with the most frequent category (mode) in the respective column
    """
    modes = df.select_dtypes(include='object').mode().iloc[0] #gets the mode of the non-numerical values and takes the first one
    df.fillna(modes,inplace=True)
    print(df.head(2))
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