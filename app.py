import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

from plotly.figure_factory import create_distplot


df = pd.read_csv(r'C:\\Users\\Admin\\Desktop\\OLYMPIC\\athlete_events.csv')
region_df = pd.read_csv(r'C:\\Users\\Admin\\Desktop\\OLYMPIC\\noc_regions.csv')

df = preprocessor.preprocess(df,region_df)

st.sidebar.title("Olympics Analysis")
st.sidebar.image('data:image/png;base64,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')
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Medal Tally in " + str(selected_year) + " Olympics")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " overall performance")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
    st.table(medal_tally)

if user_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title("Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    nations_over_time = helper.data_over_time(df,'region')
    fig = px.line(nations_over_time, x="region", y="count")
    st.title("Participating Nations over the years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x="Event", y="count")
    st.title("Events over the years")
    st.plotly_chart(fig)

    athlete_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athlete_over_time, x="Name", y="count")
    st.title("Athletes over the years")
    st.plotly_chart(fig)

    st.title("No. of Events over time(Every Sport)")
    fig,ax = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
                annot=True)
    st.pyplot(fig)

    st.title("Most successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sport = st.selectbox('Select a Sport',sport_list)
    x = helper.most_successful(df,selected_sport)
    st.table(x)

if user_menu == 'Country-wise Analysis':

    st.sidebar.title('Country-wise Analysis')

    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_country = st.sidebar.selectbox('Select a Country',country_list)

    country_df = helper.yearwise_medal_tally(df,selected_country)
    fig = px.line(country_df, x="Year", y="Medal")
    st.title(selected_country + " Medal Tally over the years")
    st.plotly_chart(fig)

    st.title(selected_country + " excels in the following sports")
    pt = helper.country_event_heatmap(df,selected_country)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(pt,annot=True)
    st.pyplot(fig)

    st.title("Top 10 athletes of " + selected_country)
    top10_df = helper.most_successful_countrywise(df,selected_country)
    st.table(top10_df)

if user_menu == 'Athlete wise Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
                             show_hist=False, show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=600)
    fig.update_layout(title="Distribution of Age")
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title('Height Vs Weight')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df = helper.weight_v_height(df,selected_sport)
    fig,ax = plt.subplots()
    ax = sns.scatterplot(x=temp_df['Weight'], y=temp_df['Height'],hue=temp_df['Medal'],style=temp_df['Sex'],s=60)
    st.pyplot(fig)

    st.title("Men Vs Women Participation Over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)



