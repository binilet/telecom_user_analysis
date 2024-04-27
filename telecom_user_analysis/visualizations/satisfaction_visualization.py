import seaborn as sns
import matplotlib.pyplot as plt

def plot_satisfaction_cluster(data):
    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Experience Score'], data['Engagment Score'], c=data['Cluster'], cmap='viridis')
    plt.title('Clusters of User Experiences')
    plt.xlabel('Experience Score')
    plt.ylabel('Engagment Score')
    plt.colorbar(label='Cluster')
    plt.tight_layout()
    return plt.gcf()