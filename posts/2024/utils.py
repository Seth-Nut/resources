import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_histogram(data, column, figsize=(8, 4)):
    """
    Creates and displays a histogram of the distribution of the data for a given column in a DataFrame.

    Parameters:
    data (pandas DataFrame): The DataFrame containing the data.
    column (str): The name of the column for which the histogram will be created.
    figsize (tuple, optional): The size of the histogram figure. Default is (8, 4).

    Returns:
    None
    """

    # Configure the Seaborn style
    sns.set(style='whitegrid')

    # Create a figure with the specified size
    plt.figure(figsize=figsize)

    # Create the histogram using Seaborn
    sns.histplot(data[column].dropna(), bins=20, color='steelblue', edgecolor='black')

    # Add title and axis labels
    plt.title(f'Distribution of column {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

    # Show the grid in the plot
    plt.grid(True)

    # Display the histogram
    plt.show()

def plot_histogram_vo(data, column, vo, figsize=(8, 4)):
    """
    Creates and displays a histogram of the distribution of the data for a given column in a DataFrame,
    divided by a categorical variable (target variable).

    Parameters:
    data (pandas DataFrame): The DataFrame containing the data.
    column (str): The name of the column for which the histogram will be created.
    vo (str): The name of the target variable to divide the data in the histogram.
    figsize (tuple, optional): The size of the histogram figure. Default is (8, 4).

    Returns:
    None
    """

    # Configure the Seaborn style
    sns.set(style='whitegrid')

    # Create a figure with the specified size
    plt.figure(figsize=figsize)

    # Create histograms using Seaborn
    sns.histplot(x=column, hue=vo, data=data, palette='Blues', edgecolor='black')

    # Add title and axis labels
    plt.title(f'Distribution of column {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

    # Display the histogram
    plt.show()

def plot_range_distribution(data, column, bins, figsize=(8, 4)):
    """
    Creates and displays a bar chart that represents the distribution of a column
    divided into specific ranges in a DataFrame.

    Parameters:
    data (pandas DataFrame): The DataFrame containing the data.
    column (str): The name of the column for which the range distribution will be created.
    bins (int or sequence of scalars): The number of bins or bin edges for the division.
    figsize (tuple, optional): The size of the bar chart figure. Default is (8, 4).

    Returns:
    None
    """

    # Configure the Seaborn style
    sns.set(style='whitegrid')

    # Add a new column to the DataFrame with the ranges of the specific column
    data[column + 'Range'] = pd.cut(data[column], bins=bins, right=False)

    # Count the number of elements in each range
    temp_counts = data[column + 'Range'].value_counts().sort_index()

    # Calculate the percentages instead of counting the number of elements
    temp_percentages = (temp_counts / temp_counts.sum()) * 100  # Calculate the relative percentages

    # Create the bar chart
    plt.figure(figsize=figsize)
    sns.barplot(x=temp_percentages.index, y=temp_percentages.values, color='steelblue', edgecolor='black')

    # Add value annotations on the bars (percentages)
    for i, value in enumerate(temp_percentages):
        plt.text(i, value + 0.2, f'{value:.2f}%', ha='center', va='bottom', fontsize=9)

    # Set title and axis labels
    plt.title(f'Range Distribution of column {column}')
    plt.xlabel('Ranges')
    plt.ylabel('Frequency')
    plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
    plt.tight_layout()

    # Display the chart
    plt.show()

    # Remove extra column
    data.drop(column + 'Range', axis=1, inplace=True)

def plot_range_distribution_vo(data, column, bins, vo, figsize=(8, 4)):
    """
    Creates and displays a bar chart that represents the distribution of a column divided into specific ranges in a DataFrame,
    grouped by a target variable and visualizing the relative percentages in each group.

    Parameters:
    data (pandas DataFrame): The DataFrame containing the data.
    column (str): The name of the column for which the range distribution will be created.
    bins (int or sequence of scalars): The number of bins or bin edges for the division.
    vo (str): The name of the target variable to group the data in the bar chart.
    figsize (tuple, optional): The size of the bar chart figure. Default is (8, 4).

    Returns:
    None
    """

    # Configure the Seaborn style
    sns.set(style='whitegrid')

    # Add a new column to the DataFrame with the ranges of the specific column
    data[column + 'Range'] = pd.cut(data[column], bins=bins, right=False)

    # Calculate the count of each group and restructure the data
    counts = data.groupby([vo, column + 'Range']).size().reset_index(name='Count')

    # Calculate the percentages by category
    counts['Percentage'] = counts.groupby(vo)['Count'].transform(lambda x: (x / x.sum()))

    # Bar chart with Seaborn
    plt.figure(figsize=figsize)
    ax = sns.barplot(data=counts, x=column + 'Range', y='Percentage', hue=vo, palette='Blues', edgecolor='black')

    # Rotate the x-axis labels (45 degrees) and add values on each bar (excluding 0%)
    for p in ax.patches:
        if p.get_height() != 0:  # If the value is not 0%
            ax.annotate(f'{p.get_height():.2%}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center',
                        va='center', xytext=(0, 10), textcoords='offset points', fontsize=8)

    # Set title and axis labels
    plt.title(f'Range Distribution of column {column}')
    plt.xlabel('Ranges')
    plt.ylabel('Frequency')
    plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
    plt.tight_layout()

    # Display the chart
    plt.show()

    # Remove extra column
    data.drop(column + 'Range', axis=1, inplace=True)

def plot_barplot(data, column, figsize=(8, 4)):
    """
    Creates and displays a bar chart that represents the distribution of a column in a DataFrame.

    Parameters:
    data (pandas DataFrame): The DataFrame containing the data.
    column (str): The name of the column for which the bar chart will be created.
    figsize (tuple, optional): The size of the bar chart figure. Default is (8, 4).

    Returns:
    None
    """

    # Configure the Seaborn style
    sns.set(style='whitegrid')

    # Calculate the percentages of each category in the specified column
    temp_percentages = (data[column].value_counts(normalize=True) * 100).sort_index()

    # Create the bar chart with percentages
    plt.figure(figsize=figsize)
    temp_percentages.plot(kind='bar', color='steelblue', edgecolor='black')

    # Add value annotations on the bars (percentages)
    for i, value in enumerate(temp_percentages):
        plt.text(i, value + 1, f'{value:.2f}%', ha='center', va='bottom', fontsize=9)

    # Set title and axis labels
    plt.title(f'Distribution of column {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
    plt.ylim(0, 100)  # Set y-axis range from 0 to 100 for percentages
    plt.show()

def plot_barplot_vo(data, column, vo, figsize=(8, 4)):
    """
    Creates and displays a bar chart that represents the distribution of a column divided by a target variable.

    Parameters:
    data (pandas DataFrame): The DataFrame containing the data.
    column (str): The name of the column for which the bar chart will be created.
    vo (str): The name of the target variable to group the data in the bar chart.
    figsize (tuple, optional): The size of the bar chart figure. Default is (8, 4).

    Returns:
    None
    """

    # Configure the Seaborn style
    sns.set(style='whitegrid')

    # Calculate the count of each group and restructure the data
    counts = data.groupby([vo, column]).size().reset_index(name='Count')

    # Calculate the percentages by category
    counts['Percentage'] = counts.groupby(vo)['Count'].transform(lambda x: (x / x.sum()))

    # Bar chart with Seaborn
    plt.figure(figsize=figsize)
    ax = sns.barplot(data=counts, x=column, y='Percentage', hue=vo, palette='Blues', edgecolor='black')

    # Rotate the x-axis labels (45 degrees) and add values on each bar (excluding 0%)
    for p in ax.patches:
        if p.get_height() != 0:  # If the value is not 0%
            ax.annotate(f'{p.get_height():.2%}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center',
                        va='center', xytext=(0, 10), textcoords='offset points', fontsize=8)

    # Set title and axis labels
    plt.title(f'Range Distribution of column {column}')
    plt.xlabel('Ranges')
    plt.ylabel('Frequency')
    plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
    plt.tight_layout()

    # Display the chart
    plt.show()

def calculate_percentage_vo_int(data, column, vo):
    """
    Calculates the relative percentages of each group divided by a target variable (vo) in a DataFrame,
    keeping the column of interest as the index in the pivot table.

    Parameters:
    data (pandas DataFrame): The DataFrame containing the data.
    column (str): The name of the column for which the percentages will be calculated.
    vo (str): The name of the target variable to group the data and calculate the percentages.

    Returns:
    pandas DataFrame: A pivot table with the relative percentages.
    """

    # Calculate the count of each group and restructure the data
    counts = data.groupby([vo, column]).size().reset_index(name='Count')

    # Calculate the percentages by category
    counts['Percentage'] = counts.groupby(vo)['Count'].transform(lambda x: (x / x.sum()))

    # Create a pivot table with the percentages
    pivot_counts = counts.pivot_table(values=['Count', 'Percentage'], index=column, columns=vo)

    return pivot_counts

def calculate_percentage_vo(data, column, bins, vo):
    """
    Calculates the relative percentages of each group divided by a target variable (vo) in a DataFrame,
    within specific ranges defined by column and bins.

    Parameters:
    data (pandas DataFrame): The DataFrame containing the data.
    column (str): The name of the column for which the percentages will be calculated.
    bins (int or sequence of scalars): The number of bins or bin edges for the division.
    vo (str): The name of the target variable to group the data and calculate the percentages.

    Returns:
    pandas DataFrame: A pivot table with the relative percentages.
    """

    # Add a new column to the DataFrame with the ranges of the specific column
    data[column + 'Range'] = pd.cut(data[column], bins=bins, right=False)

    # Calculate the count of each group and restructure the data
    counts = data.groupby([vo, column + 'Range']).size().reset_index(name='Count')

    # Calculate the percentages by category
    counts['Percentage'] = counts.groupby(vo)['Count'].transform(lambda x: (x / x.sum()))

    # Create a pivot table with the percentages
    pivot_counts = counts.pivot_table(values=['Count', 'Percentage'], index=column + 'Range', columns=vo)

    # Remove extra column
    data.drop(column + 'Range', axis=1, inplace=True)

    return pivot_counts



