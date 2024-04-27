import streamlit as st
from data.data_loader import load_user_experience_metrics_data
from models.satisfaction_analysis import assign_experience_score

def user_satisfaction_dashboard():
    st.header("User Satisfaction Analytics")

    #fetch row data from db
    data_xperience= load_user_experience_metrics_data()

    #assign experience scores
    st.subheader("Experience Satisfaction Score")
    df = assign_experience_score(data_xperience)
    st.dataframe(df.head(10))
    

