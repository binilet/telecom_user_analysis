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