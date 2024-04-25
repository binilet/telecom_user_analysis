import seaborn as sns
import matplotlib.pyplot as plt

def plot_top_ten_customers_per_engagment_metrics(top_ten_cust):
    figs = []
    (top_ten_per_session_frequency,top_ten_per_duration,top_ten_per_totaldata) = top_ten_cust

    plt.figure(figsize=(10, 6))
    sns.barplot(x="tuser",y="sessionFrequencie",data=top_ten_per_session_frequency)
    plt.xticks(rotation=90)
    plt.xlabel("Users")
    plt.ylabel("Session Frequency")
    plt.title("Engagment Per Session Frequency")
    plt.tight_layout()
    fig_session = plt.gcf()
    figs.append(fig_session)

    plt.figure(figsize=(10, 6))
    sns.barplot(x="tuser",y="duration",data=top_ten_per_duration)
    plt.xticks(rotation=90)
    plt.xlabel("Users")
    plt.ylabel("Session Duration")
    plt.title("Engagment Per Duration")
    plt.tight_layout()
    fig_duration = plt.gcf()
    figs.append(fig_duration)

    plt.figure(figsize=(10, 6))
    sns.barplot(x="tuser",y="totalData",data=top_ten_per_totaldata)
    plt.xticks(rotation=90)
    plt.xlabel("Users")
    plt.ylabel("Total Data")
    plt.title("Engagment Per Total Data")
    plt.tight_layout()
    fig_total_data = plt.gcf()
    figs.append(fig_total_data)
    
    return figs

def plot_kmeans_cluster(df):
    plt.clf()
    plt.xlim(-50,80)
    plt.ylim(-5,100)
    plt.scatter(x=df['sessionFrequencie_T'],y=df['duration_T'],c=df['kmeans_lables'])  
    plt.title('K-Means Clustering Results')
    plt.tight_layout()

    fig = plt.gcf()
    return fig
    
       
        
    