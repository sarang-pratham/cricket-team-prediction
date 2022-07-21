import streamlit as st
from crick_pred import show_predict_page
from individual_stat import show_individual_stats

page = st.sidebar.selectbox("Menu", ("Team", "Individual"))

if page == "Team":
    show_predict_page()
else:
    show_individual_stats()