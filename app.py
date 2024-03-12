import streamlit as st

import preprocessor

df = preprocessor.preprocess()


st.sidebar.radio(
    'select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
)

st.dataframe(df)
