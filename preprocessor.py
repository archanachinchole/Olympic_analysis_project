import pandas as pd
df = pd.read_csv(r'C:\\Users\\Admin\\Desktop\\OLYMPIC\\athlete_events.csv')
region_df = pd.read_csv(r'C:\\Users\\Admin\\Desktop\\OLYMPIC\\noc_regions.csv')
def preprocess():
    global df,region_df
    # filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    # merge with region_df
    df = df.merge(region_df, on='NOC',how='left')
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    # one ht encoding medal
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df
