import streamlit as st

st.set_page_config(layout="wide")

title,pp = st.columns((3,2))
base="dark"
primaryColor="purple"

with title:
    st.markdown("Hi! My name is [Aman]")