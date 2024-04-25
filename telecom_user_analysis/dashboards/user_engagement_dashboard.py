import streamlit as st
from data.data_loader import load_user_engagment_metrics_data
from models.engagement_analysis import get_top_customers_per_engagment_metrics 
from visualizations.engagement_visualization import plot_top_ten_customers_per_engagment_metrics


def user_engagment_dashboard():
    st.header("User Engagment Analytics")

    #fetch row data from db
    data_engagment = load_user_engagment_metrics_data()
    

    #convert the data to dataframes and do analysis
    df_top_custs_per_engagment = get_top_customers_per_engagment_metrics(data_engagment)

    #streamlit dashboard

    st.subheader("Engagment Per Session Frequency, Session duration and total data Metrics")
    #st.dataframe(df_top_custs_per_engagment)
    figs = plot_top_ten_customers_per_engagment_metrics(df_top_custs_per_engagment)
    for fig in figs:
        st.pyplot(fig=fig)
    