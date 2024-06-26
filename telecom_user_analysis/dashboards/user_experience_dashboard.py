import streamlit as st
from data.data_loader import load_user_experience_metrics_data
from models.experience_analysis import distribution_tp_per_handset,distribution_tcp_per_handset,experience_clustering
from visualizations.experience_visualization import plot_average_throughput_per_handset,plot_average_tcp_per_handset,plot_experience_cluster


def user_experience_dashboard():
    st.header("User Experience Analytics")

    #fetch row data from db
    data_xperience= load_user_experience_metrics_data()
    

    #convert the data to dataframes and do analysis
    df_avg_tp_per_handset = distribution_tp_per_handset(data_xperience)
    df_avg_tcp_per_handset = distribution_tcp_per_handset(data_xperience)
    df_experience_cluster,df_description,features,scaler,cluster_centers = experience_clustering(data_xperience)

    st.subheader("Average throughput per handset")
    st.dataframe(df_avg_tp_per_handset)
    fig = plot_average_throughput_per_handset(df_avg_tp_per_handset)
    st.pyplot(fig=fig)

    st.subheader("Average tcp per handset")
    st.dataframe(df_avg_tcp_per_handset)
    fig = plot_average_tcp_per_handset(df_avg_tcp_per_handset)
    st.pyplot(fig=fig)

    st.subheader("Experience Cluster")
    st.dataframe(df_description)
    st.subheader("user count per cluster")
    cluster_user_count_df = df_experience_cluster.groupby('Cluster').size().reset_index(name='User Count')
    cluster_user_count_df['Cluster'] += 1  # Adjust cluster labels to start from 1
    st.dataframe(cluster_user_count_df)
    fig = plot_experience_cluster(df_experience_cluster)
    st.pyplot(fig=fig)



  

