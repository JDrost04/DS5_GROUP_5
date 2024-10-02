import pandas as pd

# Read the excel file using the pandas library
def read_sales_data(file_path):
    """Reads the sales data from the excel file.

    Args:
        file_path (str): Path to the excel file containing the sales data

    Returns:
        pd.DataFrame: The sales data as a pandas dataframe
    """    
    return pd.read_excel(file_path)

# Perform data analysis on the sales data to calculate the following metrics:
def calculate_sales_metrics(sales_data):
    """Calculates sales per category, month and manager, as well as the percentage of sales per category, month and manager.
    Args:
        sales_data (pd.DataFrame): The sales data as a pandas dataframe

    Returns:
        dict: A dictionary containing the sales metrics
    """    

    # Total sales for each category
    sales_per_category = sales_data.groupby('Category')['Sales'].sum()

    # Percentage that a category contributes to the total sales
    percentage_sales_per_category = (sales_per_category / sales_per_category.sum()) * 100

    # Sales for each month
    sales_per_month = sales_data.groupby('Month')['Sales'].sum()

    # Percentage that the month contributes to the total
    percentage_sales_per_month = (sales_per_month / sales_per_month.sum()) * 100

    # Sales for each sales manager
    sales_per_manager = sales_data.groupby('Sales Manager')['Sales'].sum()

    # Percentage that the sales manager contributes to the total
    percentage_sales_per_manager = (sales_per_manager / sales_per_manager.sum()) * 100

    # Generate a dataframe that displays the metrics calculated. 
    return {
    'Total sales per category': sales_per_category,
    'Sales percentage per category': percentage_sales_per_category,
    'Total sales per month': sales_per_month,
    'Sales percentage per month': percentage_sales_per_month,
    'Total sales per manager': sales_per_manager,
    'Sales percentage per manager': percentage_sales_per_manager
}

# Store the report into an excel file called ‘reportRetail.xlsx’
def generate_sales_report(file_path, output_file):
    """
    Generates a sales report and saves it to an Excel file.

    Args:
        file_path (str): The path to the sales data Excel file.
        output_file (str): The path where the report will be saved.
    """   
    
    sales_data = read_sales_data(file_path)
    sales_metrics = calculate_sales_metrics(sales_data)
    report_df = pd.concat(sales_metrics, axis=1)
    report_df.to_excel(output_file)

generate_sales_report('detailedRetail.xlsx', 'reportRetail.xlsx')
