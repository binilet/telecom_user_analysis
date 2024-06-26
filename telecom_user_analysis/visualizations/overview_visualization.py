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

def plot_univariance_dispersion(df):
    numerical_columns = [column for column, dtype in df.dtypes.items() if dtype == 'float']

    # Create box plots for each numerical column
    figs = []
    for column in numerical_columns:
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=df[column].dropna())
        plt.title(f'Box plot of {column}')
        plt.xlabel('Values')
        plt.ylabel(column)
        fig = plt.gcf()  # Get the current figure
        figs.append(fig)
        plt.close()
    
    return figs

def plot_bivariate_analysis(df):
    #get all application columns
    applications = [column for column, dtype in df.dtypes.items() if dtype == 'float64' and column != 'MSISDN/Number' and column != 'Dur. (ms)']

    aggregated_data = df[applications].sum()
    print('aggregated data')
    print(aggregated_data)

    x = applications
    y = aggregated_data[applications]

    print('printing x and y')
    print(len(x))
    print(x)
    print(y)
    
    plt.scatter(x,y, label=applications)

    plt.xlabel('Application Data Usage')
    plt.ylabel('Total Data Usage (UL + DL)')
    plt.title('Relationship between Applications and Total Data Usage')
    plt.xticks(rotation=45)  # Rotate x-axis labels if needed
    plt.tight_layout()
    return plt.gcf()

def plot_correlation(corr_df):
    plt.clf()
    # Create a heatmap to visualize the correlations
    plt.imshow(corr_df, cmap="bwr") # Adjust 'coolwarm' for different colormaps

    # Add labels for the axes
    plt.xticks(range(len(corr_df.columns)), corr_df.columns, rotation=45)  # Rotate x-axis labels for readability
    plt.yticks(range(len(corr_df.columns)), corr_df.columns)

    # Add colorbar to interpret color intensity as correlation strength
    plt.colorbar()

    # Set title for the plot
    plt.title("Correlation Matrix (Excluding First 3 Columns)")

    plt.tight_layout()
    return plt.gcf()