import pandas as pd

# EXERCISE 1

# EXERCISE 2
hotel_data = pd.read_excel('hotelBookings.xlsx')
print(hotel_data.head())
print(hotel_data.isnull().any())

'''fouten in data:
200 en 55000 kinderen
' voor bepaalde cellen van meal BB
country in nummers en spatie voor country ROU, canada in 2 letters ipv 3 van CN --> CAN
market segment G ROU ps
cell in rij agent null zonder hoofdletters
komma getal in stays in week

Null niet behorend in:
arrival date month
country


'''

print(hotel_data['arrival_date_month'].isnull())


for i in hotel_data.index:
    if hotel_data['arrival_date_month'].isnull().iloc[i]==True:
        if hotel_data['arrival_date_week_number'].iloc[i] < 31:
            hotel_data['arrival_date_month'].iloc[i] = 'July'
        elif hotel_data['arrival_date_week_number'].iloc[i] > 31:
            hotel_data['arrival_date_month'].iloc[i] = 'August'
        else:
            if hotel_data['arrival_date_day_of_month'].iloc[i] > 7:
                hotel_data['arrival_date_month'].iloc[i] = 'July'
            else: hotel_data['arrival_date_month'].iloc[i] = 'August'
print(hotel_data['arrival_date_month'].isnull().any())


# EXERCISE 3
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


# EXERCISE 4
# 4.1
import langdetect as ld
"""py -m pip install pandas langdetect openpyxl
"""
# Load the Excel file
tweets_df = pd.read_excel('tweets.xlsx')

# Create a new column 'Language' to store the detected language
def detect_language(tweet):
    """Detects language of tweets from excel file.

    Args:
        tweet (str): The text of the tweet for which the language will be detected 
    """    
    try:
        # Ensure that tweet is a string
        if isinstance(tweet, str):
            # Detect the language of the tweet
            return ld.detect(tweet)
        else:
            return 'Unknown'
    except ld.LangDetectException:
        # Handle exception if language detection fails
        return 'Unknown'

# Apply the language detection to the 'Tweet' column
tweets_df['Language'] = tweets_df['Tweet'].apply(detect_language)

# Save the updated DataFrame to a new Excel file
tweets_df.to_excel('tweets_with_language.xlsx', index=False)

print(tweets_df.head(10))


# 4.2