import streamlit as st

from dashboards.user_overview_dashboard import user_overview_dashboard
from dashboards.user_engagement_dashboard import user_engagment_dashboard
# from dashboards.user_experience_dashboard import user_experience_dashboard
# from dashboards.user_satisfaction_dashboard import user_satisfaction_dashboard

def main():
    st.title("Telecomunication User Analysis")

    pages = {
        "User Overview Analysis" : user_overview_dashboard,
        "User Engagement": user_engagment_dashboard,
        # "User Experience": user_experience_dashboard,
        # "User Satisfaction": user_satisfaction_dashboard
    }

    selected_page = st.sidebar.selectbox("Select Dashboard",list(pages.keys()))
    pages[selected_page]()

if __name__ == "__main__":
    main()