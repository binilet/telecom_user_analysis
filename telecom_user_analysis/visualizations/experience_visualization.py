import seaborn as sns
import matplotlib.pyplot as plt

def plot_average_throughput_per_handset(tp_df):

    # Plot a histogram to visualize the distribution
    plt.figure(figsize=(10, 6))
    tp_df.plot(kind='bar', color='skyblue')
    plt.title('Distribution of Average Throughput per Handset Type')
    plt.xlabel('Handset Type')
    plt.ylabel('Average Throughput (kbps)')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    return plt.gcf()


def plot_average_tcp_per_handset(tp_df):

    plt.clf()
    plt.figure(figsize=(10, 6))
    tp_df.plot(kind='bar', color='skyblue')
    plt.title('Distribution of Average TCP Transmission per Handset Type')
    plt.xlabel('Handset Type')
    plt.ylabel('Average Total TCP (kbps)')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    return plt.gcf()

def plot_experience_cluster(data):
    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Total RTT'], data['Total Avg Bearer TP DL (kbps)'], c=data['Cluster'], cmap='viridis')
    plt.title('Clusters of User Experiences')
    plt.xlabel('Total RTT')
    plt.ylabel('Total Avg Bearer TP DL (kbps)')
    plt.colorbar(label='Cluster')
    plt.tight_layout()
    return plt.gcf()

    