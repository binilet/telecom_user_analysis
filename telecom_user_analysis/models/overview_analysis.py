import pandas as pd


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