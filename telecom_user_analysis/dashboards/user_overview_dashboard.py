import streamlit as st
from data.data_loader import load_top_ten_handsets_data
from models.overview_analysis import get_top_handsets
from visualizations.overview_visualization import plot_top_ten_handsets

def user_overview_dashboard():
    st.header("User Overview Analysis")

    #fetch row data from db
    data = load_top_ten_handsets_data()
    #convert the data to dataframes
    top_handsets = get_top_handsets(data)

    st.subheader("Top 10 Handsets")
    st.dataframe(top_handsets)

    fig = plot_top_ten_handsets(top_handsets=top_handsets)
    
    st.pyplot(fig)