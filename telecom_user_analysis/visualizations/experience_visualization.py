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

    