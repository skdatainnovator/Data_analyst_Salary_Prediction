from PIL import Image
import streamlit as st

def show_analysis():
    image4 = Image.open('industry.png')
    image1 = Image.open('graph1.png')
    image2 = Image.open('language.png')
    image3 = Image.open('state.png')

    st.image(image4,caption="Percentage of Data Analyst Job in Diffferent Industry")

    st.image(image1,caption = 'Salary Variation With relation to Experience')
    st.image(image2,caption = 'Top Paid language for Data Analyst ')
    st.image(image3, caption = "No of Data Analyst Jobs in Different States in USA")