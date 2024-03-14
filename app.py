import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r'C:\\Users\\Admin\\Desktop\\OLYMPIC\\athlete_events.csv')
region_df = pd.read_csv(r'C:\\Users\\Admin\\Desktop\\OLYMPIC\\noc_regions.csv')

df = preprocessor.preprocess(df, region_df)

st.sidebar.title("Olympic Analysis")
user_menu = st.sidebar.radio(
    'select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
)

if user_menu == "Medal Tally":
    st.sidebar.header("Medal Tally")
    year, country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Years", year)
    selected_country = st.sidebar.selectbox("Select Country", country)

    Medal_tally = helper.featch_Medal_tally(df,selected_year,selected_country)
    if selected_year == 'overall' and selected_country == 'overall':
        st.title(" Overall Tally")
    if selected_year != 'overall' and selected_country == 'overall':
        st.title("Medal Tally in " +  str(selected_year) + " Olympics")
    if selected_year == 'overall' and selected_country != 'overall':
        st.title(selected_country +  " Overall performance ")
    if selected_year != 'overall' and selected_country != 'overall':
        st.title(selected_country + " performance in "  + str(selected_year) + " Olympics")
    st.table(Medal_tally)


if user_menu == "Overall Analysis":
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    Nations = df['region'].unique().shape[0]

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

    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(Nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

        Nation_over_time = helper.data_over_time(df,'region')
        fig = px.line(Nation_over_time, x="No. of region", y="count")
        st.title("Participating Nation over time")
        st.plotly_chart(fig)

        events_over_time = helper.data_over_time(df,'region')
        fig = px.line(events_over_time, x="No. of region", y="count")
        st.title("Event over Year")
        st.plotly_chart(fig)

        athletes_over_time = helper.data_over_time(df,'Name')
        fig = px.line(athletes_over_time, x="count", y="No. of Name")
        st.title("Athletes over the Years")
        st.plotly_chart(fig)

        st.title("No. of events over time(Every Sports)")
        fig,ax = plt.subplots(figsize=(20,20))
        x = df.drop_duplicates(['Year', 'Sport', 'Event'])
        sns.heatmap(
            x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
            annot=True)
        st.pyplot(fig)


        st.title('Most Sucessful Athletes')
        sport_list = df['Sport'].unique().tolist()
        sport_list.sort()
        sport_list.insert(0,'Overall')

        selected_sport = st.selectbox('Select a Sport', sport_list)
        x = helper.most_successful(df,'Overall')
        st.table(x)

