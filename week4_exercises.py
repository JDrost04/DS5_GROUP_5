import pandas as pd

# EXERCISE 1

# EXERCISE 2
hotel_data = pd.read_excel('hotelBookings.xlsx')
print(hotel_data.head())
print(hotel_data.isnull().any())

def hotel_month_filler(row: int):
    '''
    This function checks if there are months missing and fills them in
    
    Args:
        row: The row that needs to be checked
        
    Returns: 
        The row with the month filled in if it was missing
    '''
    if hotel_data['arrival_date_month'].isnull().iloc[row]==True:
        if hotel_data['arrival_date_week_number'].iloc[row] < 31:
            hotel_data['arrival_date_month'].iloc[row] = 'July'
        elif hotel_data['arrival_date_week_number'].iloc[row] > 31:
            hotel_data['arrival_date_month'].iloc[row] = 'August'
            # the month filled is based on the week number of corresponding months.
        else:
            if hotel_data['arrival_date_day_of_month'].iloc[row] > 7:
                hotel_data['arrival_date_month'].iloc[row] = 'July'
            else: hotel_data['arrival_date_month'].iloc[row] = 'August'
                # there is a week where both months fall so there it used the day.

def hotel_meal_fixer(row: int):
        '''
    This function fixes layout errors in the meal column
    
    Args:
        row: The row that needs to be checked
        
    Returns: 
        The given row in the meal column with a fixed lay out
    '''
    string_fixer = hotel_data['meal'].iloc[row]
    hotel_data['meal'].iloc[row] = string_fixer[-2:]

def hotel_night_stay_fixer(row: int):
        '''
    this function turns the numbers in the nights stay columns into whole numbers
    
    Args:
        row: the row that needs to be checked
        
    Returns: 
        The numbers in the row as whole numbers
    '''
    for column in ['stays_in_weekend_nights','stays_in_week_nights']:
        hotel_data[column].iloc[row] = int(hotel_data[column].iloc[row])
        # chose to round down to have the data be based on full nights.

def hotel_guest_fixer(row: int):
            '''
    This function checks if there are numbers that have more than 1 digit.
    
    Args:
        row: The row that needs to be checked
        
    Returns: 
        The row with only single digit numbers
    '''
    for column in ['adults','children','babies']:
        number_fixer = str(hotel_data[column].iloc[row])
        hotel_data[column].iloc[row] = int(number_fixer[0])
        # chose to only take first number since the data is based on rooms and there is a high likelyhood of there not being 10 adults in 1 room.

def hotel_country_fixer(row:int):
    '''
    This function checks for any incorrect countries and fixes them
    
    Args:
        row: The row that needs to be checked
        
    Returns: 
        The Row with the 3 letter code of the countries.
    '''
    hotel_data['country'].iloc[996] = 'CAN'
    # used to be CN which according to country codes corresponds to canada with 3 letter code CAN.
    hotel_data['country'].iloc[6] = 'UNK'
    hotel_data['country'].iloc[116] = 'UNK'
    hotel_data['country'].iloc[30] = 'UNK'
    # these codes were not correct so the choice was made to have them be UNK for unknown as there is no country with code UNK.
    for row in hotel_data.index:
        if 'ROU' in hotel_data['country'].iloc[row]:
            string_fixer = hotel_data['country'].iloc[row]
            hotel_data['country'].iloc[row] = string_fixer[-3:]

def hotel_market_segment_fixer(row: int):
    '''
    This function turns the numbers in the nights stay columns into whole numbers
    
    Args:
        row: The row that needs to be checked
        
    Returns: 
        The rows with fixed formatting
    '''
    if 'ROU' in hotel_data['market_segment'].iloc[row]:
        hotel_data['market_segment'].iloc[row] = hotel_data['market_segment'].iloc[row].replace(" ", "").capitalize()

def hotel_data_fixer(hotel_data):
    '''
    This function performs the earlier functions for each row in the hotel database
    
    Args:
        hotel_data: the hotel data that needs to be cleaned
    
    Returns:
        The database with the cleaned cells
    '''
    for i in hotel_data.index:
        hotel_month_filler(i)
        hotel_meal_fixer(i)
        hotel_night_stay_fixer(i)
        hotel_market_segment_fixer(i)
        hotel_country_fixer(i)
    return hotel_data

hotel_data_fixer(hotel_data)


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