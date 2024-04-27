import streamlit as st
from data.data_loader import load_user_experience_metrics_data,load_user_engagment_metrics_data
from models.satisfaction_analysis import assign_experience_score,assign_engagment_score,assign_satisfaction_score,statisfaction_clustering
from visualizations.satisfaction_visualization import plot_satisfaction_cluster

def user_satisfaction_dashboard():
    st.header("User Satisfaction Analytics")

    #fetch row data from db
    data_xperience= load_user_experience_metrics_data()
    data_engagment = load_user_engagment_metrics_data()
    #assign experience scores
    st.subheader("Experience Score")
    df_experience = assign_experience_score(data_xperience)
    st.dataframe(df_experience.head(10))

    st.subheader("Enagment Score")
    df_satisifaction = assign_engagment_score(data_engagment)
    st.dataframe(df_satisifaction.head(10))

    st.subheader("Satisfaction Score")
    satisifcation_score_df = assign_satisfaction_score(df_experience,df_satisifaction)
    st.dataframe(satisifcation_score_df.head(10))


    st.subheader("Experience and Engagment cluster")
    dataframe,clusterdf = statisfaction_clustering(satisifcation_score_df)
    fig_sat_plot = plot_satisfaction_cluster(dataframe)
    st.dataframe(clusterdf)
    st.subheader("user count per cluster")
    # Count the number of users per cluster
    cluster_user_count_df = dataframe.groupby('Cluster').size().reset_index(name='User Count')
    cluster_user_count_df['Cluster'] += 1  # Adjust cluster labels to start from 1
    st.dataframe(cluster_user_count_df)
    st.pyplot(fig_sat_plot)
    



    

