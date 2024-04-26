import streamlit as st
from data.data_loader import load_user_experience_metrics_data
from models.experience_analysis import distribution_tp_per_handset
from visualizations.experience_visualization import plot_average_throughput_per_handset


def user_experience_dashboard():
    st.header("User Experience Analytics")

    #fetch row data from db
    data_xperience= load_user_experience_metrics_data()
    

    #convert the data to dataframes and do analysis
    df_avg_tp_per_handset = distribution_tp_per_handset(data_xperience)
   

    st.subheader("Average throughput per handset")
    #st.dataframe(df_top_custs_per_engagment)
    fig = plot_average_throughput_per_handset(df_avg_tp_per_handset)
    st.pyplot(fig=fig)

  

