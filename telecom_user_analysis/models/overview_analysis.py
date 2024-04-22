import pandas as pd

def get_top_handsets(data):
    columns = ["Handset Type","Count"]
    df = pd.DataFrame(data,columns=columns)
    return df