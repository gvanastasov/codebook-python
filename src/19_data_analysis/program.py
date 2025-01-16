# Chapter 20: Data Analysis with Pandas

""" 
Introduction: In this chapter, we will explore how to analyze and visualize data using the Pandas library in Python. Pandas is a powerful tool for data manipulation, allowing us to load, process, and analyze structured data such as CSV files. We'll also learn how to visualize data with Matplotlib to uncover trends and insights.

Key Concepts:
1. DataFrames: A core structure in Pandas, DataFrames represent tabular data with rows and columns.
2. Reading CSV Files: Learn how to load CSV files into DataFrames using pandas.read_csv().
3. Basic Visualization: We'll use Pandas with Matplotlib to visualize the data, making it easier to spot patterns and insights.

Notes:
- Pandas is widely used for data analysis and is an essential tool in data science.
- Visualizations are crucial for interpreting data effectively and communicating insights.

"""

import pandas as pd # Importing pandas for data manipulation 
import matplotlib.pyplot as plt # Importing matplotlib for data visualization

def analyze_sales_data(csv_file): 
    """ 
        This function loads a sales dataset, performs basic analysis, 
        and visualizes the data. 
    """
    # Step 1: Read the CSV file into a Pandas DataFrame
    sales_data = pd.read_csv(csv_file)

    # Step 2: Display the first few rows of the data
    print("First 5 rows of the dataset:")
    print(sales_data.head())  # Display the first 5 rows of the dataset

    # Step 3: Data analysis - Basic Summary Statistics
    print("\nSummary Statistics:")
    print(sales_data.describe())  # Get summary statistics (mean, std, min, max, etc.)

    # Step 4: Check for any missing values
    print("\nMissing values:")
    print(sales_data.isnull().sum())  # Check for missing values in each column

    # Step 5: Visualize the total sales over time (assuming 'Date' and 'Sales' columns exist)
    sales_data['Date'] = pd.to_datetime(sales_data['Date'])  # Convert 'Date' column to datetime format
    sales_data.set_index('Date', inplace=True)  # Set 'Date' as the index for the DataFrame

    # Plot total sales over time
    plt.figure(figsize=(10, 6))
    plt.plot(sales_data['Sales'], label='Sales', color='blue')
    plt.title('Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Step 6: Calculate total sales by category (assuming 'Category' and 'Sales' columns)
    sales_by_category = sales_data.groupby('Category')['Sales'].sum()

    # Plot total sales by category
    sales_by_category.plot(kind='bar', figsize=(10, 6), color='skyblue')
    plt.title('Total Sales by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Example: Analyzing sales data from a CSV file
analyze_sales_data('sales_data.csv')