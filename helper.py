import numpy as np
def featch_Medal_tally(df, Year, country):
    Medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if Year == 'overall' and country == 'overall':
        temp_df = Medal_df
    if Year == 'overall' and country != 'overall':
        flag = 1
        temp_df = Medal_df[Medal_df['region'] == 'country']
    if Year != 'overall' and country == 'overall':
        temp_df = Medal_df[Medal_df['Year'] == int(Year)]
    if Year != 'overall' and country != 'overall':
        temp_df = Medal_df[(Medal_df['Year'] == Year) & (Medal_df['region'] == country)]

    if flag == 1:
        X = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        X = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                      ascending=False).reset_index()

    X['Total'] = X['Gold'] + X['Silver'] + X['Bronze']

    X['Gold'] = X['Gold'].astype('int')
    X['Silver'] = X['Silver'].astype('int')
    X['Bronze'] = X['Bronze'].astype('int')
    X['Total'] = X['Total'].astype('int')

    return X
def Medal_tally(df):
    Medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    Medal_tally = Medal_tally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                             ascending=False).reset_index()
    Medal_tally['Total'] = Medal_tally['Gold'] + Medal_tally['Silver'] + Medal_tally['Bronze']

    Medal_tally['Gold'] = Medal_tally['Gold'].astype('int')
    Medal_tally['Silver'] = Medal_tally['Silver'].astype('int')
    Medal_tally['Bronze'] = Medal_tally['Bronze'].astype('int')
    Medal_tally['Total'] = Medal_tally['Total'].astype('int')

    return Medal_tally

def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'overall')

    country = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0, 'overall')

    return years, country