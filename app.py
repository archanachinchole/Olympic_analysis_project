import streamlit as st
import pandas as pd
import preprocessor,helper

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