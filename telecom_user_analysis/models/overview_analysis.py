import pandas as pd

from utils.utils import handle_numerical_missing_values,handle_string_missing_values,get_working_fields,set_working_data_types


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
        this dipersion param analysis will calculate the mean,range,variance and std deviation for each column
    """

    columns = get_working_fields()
    data_types = set_working_data_types()
    
    df = pd.DataFrame(data,columns=columns).astype(data_types)
    print(df.dtypes)

    #handle numerical missing values
    df = handle_numerical_missing_values(df).astype(data_types)

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


def bivariate_analysis(data):
     """
     prepares data for bivarate ploting
     """
     columns = get_working_fields()
     data_types = set_working_data_types()

     df = pd.DataFrame(data,columns=columns).astype(data_types)
     df = handle_numerical_missing_values(df).astype(data_types)


     return df

def variable_transformation_analysis(data):
    df = pd.DataFrame(data=data)
    df = handle_numerical_missing_values(df)
    total_duration_per_user = df.groupby('')[''].sum()

    #segment users into decile classes
    decile_classes = pd.qcut(total_duration_per_user,q=5,labels=False)
    df['decile_class'] = decile_classes

    #compute total data per decile class
    total_data_per_decile_class = df.groupby('decile_class')[['Total UL (Bytes)','Total DL (Bytes)']].sum()
    return total_data_per_decile_class

def correlation_analysis(data):
    df = pd.DataFrame(data=data)
    df = handle_numerical_missing_values(df)

    return df.corr()

     

