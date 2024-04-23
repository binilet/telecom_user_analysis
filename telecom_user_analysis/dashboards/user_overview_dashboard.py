import streamlit as st
from data.data_loader import load_top_ten_handsets_data,load_top_three_handset_manufactureres
from models.overview_analysis import get_top_handsets,get_top_manufacturers
from visualizations.overview_visualization import plot_top_ten_handsets,plot_top_three_manufactureres

def user_overview_dashboard():
    st.header("User Overview Analytics")

    #fetch row data from db
    data_handsets = load_top_ten_handsets_data()
    data_manufacturers = load_top_three_handset_manufactureres()

    #convert the data to dataframes
    top_handsets = get_top_handsets(data_handsets)
    top_manufactureres = get_top_manufacturers(data_manufacturers)

    # Dashboard for top 10 handsets
    st.subheader("Top 10 Handsets")
    #st.dataframe(top_handsets)
    fig_handsets = plot_top_ten_handsets(top_handsets=top_handsets)
    st.pyplot(fig_handsets)

    # Dashboard for top 3 manufacturers
    st.subheader("Top 3 Manufacturers")
    #st.dataframe(top_manufactureres)
    fig_manufacturers = plot_top_three_manufactureres(top_manufactureres=top_manufactureres)
    st.pyplot(fig_manufacturers)
    