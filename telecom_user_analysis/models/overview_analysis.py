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