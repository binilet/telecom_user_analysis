import seaborn as sns
import matplotlib.pyplot as plt

def plot_top_ten_handsets(top_handsets):
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Handset Type",y="Count",data=top_handsets)
    plt.xticks(rotation=90)
    plt.xlabel("Handset Type")
    plt.ylabel("Number Of Users")
    plt.title("Top 10 Handsets Used By Customers")
    plt.tight_layout()
    return plt.gcf()

def plot_top_three_manufactureres(top_manufactureres):
    plt.figure(figsize=(8, 8))
    plt.pie(top_manufactureres['Count'], labels=top_manufactureres['Handset Manufacturer'], autopct='%1.1f%%', startangle=140)
    plt.title('Top Handset Manufacturers')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.tight_layout()
    return plt.gcf()

def plot_top_five_handset_per_top_three_manufactureres(top_handsets_per_manufaturere):
    plt.figure(figsize=(10,6))
    #sns.countplot(data=top_handsets_per_manufaturere,x='Handset Manufacturer',order=top_handsets_per_manufaturere['Handset Manufacturer'].value_counts().index,palette='viridis')
    sns.barplot(data=top_handsets_per_manufaturere, x='Handset Manufacturer', y='count', hue='Handset Type', palette='viridis')
    plt.title('Top 5 Handsets per Top 3 Manufacturers')
    plt.xlabel('Manufacturer')
    plt.ylabel('Count')
    plt.legend(title='Handset Type', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    return plt.gcf()