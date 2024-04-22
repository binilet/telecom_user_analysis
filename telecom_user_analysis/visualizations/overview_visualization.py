import seaborn as sns
import matplotlib as plt

def plot_top_ten_handsets(top_handsets):
    plt.figure(figsize=(10,6))
    sns.barplot(x="Handset Type",y="Count",data=top_handsets)
    plt.xticks(rotation=60)
    plt.xlable("Handset Type")
    plt.ylable("Number Of Users")
    plt.title("Top 10 Handsets Used By Customers")
    plt.tight_layout()
    return plt.gcf()