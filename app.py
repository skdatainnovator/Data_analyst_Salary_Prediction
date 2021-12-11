import streamlit as st
from predict_page import show_predict_page
from explore_page import show_analysis

page_type = st.sidebar.selectbox("Predict or Visualization" , ("Predict","Visualization"))

if page_type=="Predict":
    show_predict_page()
elif page_type == "Visualization":
    show_analysis()