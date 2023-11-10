import matplotlib.pyplot as plt
import pandas as pd

def load_gdp_data(file_path="GDP_2015dollars.csv"):
    """
    Load GDP data from a CSV file.

    Args:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: The loaded GDP data.
    """
    ds = pd.read_csv(file_path)
    return ds

# Load GDP data
ds = load_gdp_data()

def plot_line_chart(x, y1, y2, y3, y4, title_text, output_file=None):
    """
    Create a line chart to visualize GDP growth over time for multiple countries.

    Args:
    x (pd.Series): Data for the x-axis (Year).
    y1 (pd.Series): Data for the first line (e.g., China).
    y2 (pd.Series): Data for the second line (e.g., Germany).
    y3 (pd.Series): Data for the third line (e.g., Japan).
    y4 (pd.Series): Data for the fourth line (e.g., United States).
    title_text (str): Title for the line chart.
    output_file (str): Path to save the chart as an image (optional).

    Returns:
    None
    """
    plt.figure(figsize=(10, 5))
    plt.plot(x, y1, label="China")
    plt.plot(x, y2, label="Germany")
    plt.plot(x, y3, label="Japan")
    plt.plot(x, y4, label="United States")
    plt.title(title_text)
    plt.xlabel("Years")
    plt.ylabel("US$")
    plt.legend()
    if output_file:
        plt.savefig(output_file)
    plt.show()

# Extract data
years = ds["Year"]
china = ds["China"]
germany = ds["Germany"]
japan = ds["Japan"]
united_states = ds["United States"]

# Filter data to start from 1990
start_year = 1990
filtered_data = ds[ds["Year"] >= start_year]

# Create and display the line chart
chart_title = 'GDP Growth'
output_image = "GDP_Growth.png"
plot_line_chart(
    filtered_data["Year"],
    filtered_data["China"],
    filtered_data["Germany"],
    filtered_data["Japan"],
    filtered_data["United States"],
    chart_title,
    output_file=output_image
)

def load_world_cup_data(file_path="WorldCups.csv"):
    """
    Load data from a CSV file.

    Args:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: The loaded data from the CSV file.
    """
    ds = pd.read_csv(file_path)
    return ds

# Load World Cup data
data = load_world_cup_data()

def plot_bar_graph(x, y, xlabel, ylabel, title_text):
    """
    Create a bar graph to visualize goals scored in World Cups over the years.

    Args:
    x (pd.Series): Data for the x-axis (Year).
    y (pd.Series): Data for the y-axis (Number of Goals).
    xlabel (str): Label for the x-axis.
    ylabel (str): Label for the y-axis.
    title_text (str): Title for the graph.

    Returns:
    None
    """
    plt.figure(figsize=(15, 10))
    plt.bar(x, y, label="Goals Scored")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title_text)
    plt.legend(loc='best')
    plt.savefig("WorldCup_Goals.png")
    plt.show()

# Extract data for the bar graph
years = data["Year"]
goals_scored = data["GoalsScored"]

# Create and display the bar graph
plot_bar_graph(years, goals_scored, 'Years', 'Number of Goals', 'Goals in World Cups')

def load_population_data(file_path="world_population.csv"):
    """
    Load data from a CSV file.

    Args:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: The loaded data from the CSV file.
    """
    ds = pd.read_csv(file_path)  # Adjust the delimiter if needed
    return ds

# Load world population data
ds = load_population_data()

# Group data by continent and sum the population percentages
grouped_data = ds.groupby('Continent')['World Population Percentage'].sum().reset_index()

def plot_pie_chart(values, labels, title_text):
    """
    Create a pie chart to visualize population distribution by continent.

    Args:
    values (pd.Series): Population percentage values.
    labels (pd.Series): Continent labels.
    title_text (str): Title for the pie chart.

    Returns:
    None
    """
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%')  # Adjust autopct to display percentages
    plt.title(title_text)
    plt.axis('equal')  # Equal aspect ratio ensures a circular chart
    plt.savefig("world_population.png")  # Save the chart as an image
    plt.show()  # Display the chart
# Extract data for the pie chart
continent = grouped_data["Continent"]
population_percentage = grouped_data["World Population Percentage"]

# Create and display the pie chart
plot_pie_chart(population_percentage, continent, 'Population Distribution by Continent')