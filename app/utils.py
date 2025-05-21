import pandas as pd

def get_top_regions(df, n=5):
    return df.groupby('Region')[['GHI']].mean().nlargest(n, 'GHI').reset_index()