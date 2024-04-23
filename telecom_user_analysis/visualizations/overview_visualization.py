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
    # plt.figure(figsize=(8,8))
    # sns.set(style='whitegrid')
    # sns.set_palette("pastel")
    # sns.pieplot(data=top_manufactureres, x='Count', labels='Handset Manufacturer', autopct='%1.1f%%')
    # plt.title('Top Handset Manufacturers')
    # plt.show()

    plt.figure(figsize=(8, 8))
    plt.pie(top_manufactureres['Count'], labels=top_manufactureres['Handset Manufacturer'], autopct='%1.1f%%', startangle=140)
    plt.title('Top Handset Manufacturers')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.tight_layout()
    return plt.gcf()