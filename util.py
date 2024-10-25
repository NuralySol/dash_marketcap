# Description: This file contains the utility functions that are used in the main file.
import pandas as pd

def get_data(PATH):
    df = pd.read_csv(PATH)
    df["marketcap"] = df["marketcap"] / 1_000_000_000
    df["marketcap"] = df["marketcap"].replace("[\$,]", "", regex=True).astype(float)
    marketcap = df.groupby("country")[["marketcap"]].sum()
    # reset the index to make the item_name a column again
    marketcap.reset_index(inplace=True)
    marketcap.sort_values(by="marketcap", ascending=False, inplace=True)
    top_five = marketcap.iloc[:5]
    # return the variables to be used in the main file
    return top_five

