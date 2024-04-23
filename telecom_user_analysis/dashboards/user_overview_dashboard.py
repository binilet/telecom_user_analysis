import streamlit as st
from data.data_loader import load_top_ten_handsets_data,load_top_three_handset_manufactureres,load_top_five_handset_per_top_three_manufactureres
from models.overview_analysis import get_top_handsets,get_top_manufacturers,get_top_five_handset_per_top_three_manufactureres
from visualizations.overview_visualization import plot_top_ten_handsets,plot_top_three_manufactureres,plot_top_five_handset_per_top_three_manufactureres

def user_overview_dashboard():
    st.header("User Overview Analytics")

    #fetch row data from db
    data_handsets = load_top_ten_handsets_data()
    data_manufacturers = load_top_three_handset_manufactureres()
    data_top_five_handsets = load_top_five_handset_per_top_three_manufactureres()

    #convert the data to dataframes
    df_top_handsets = get_top_handsets(data_handsets)
    df_top_manufactureres = get_top_manufacturers(data_manufacturers)
    df_top_five_handsets = get_top_five_handset_per_top_three_manufactureres(data_top_five_handsets)


    # Dashboard for top 10 handsets
    st.subheader("Top 10 Handsets")
    st.dataframe(df_top_handsets)
    fig_handsets = plot_top_ten_handsets(top_handsets=df_top_handsets)
    st.pyplot(fig_handsets)

    # Dashboard for top 3 manufacturers
    st.subheader("Top 3 Manufacturers")
    st.dataframe(df_top_manufactureres)
    fig_manufacturers = plot_top_three_manufactureres(top_manufactureres=df_top_manufactureres)
    st.pyplot(fig_manufacturers)

    # Dashboard for top 5 handsets per top 3 manufactureres
    st.subheader("Top 5 Handsets Per Top 3 Manufacturers")
    st.dataframe(df_top_five_handsets)
    fig_top_fives = plot_top_five_handset_per_top_three_manufactureres(top_handsets_per_manufaturere=df_top_five_handsets)
    st.pyplot(fig_top_fives)
    