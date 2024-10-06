import pandas as pd

# EXERCISE 1
import pandas as pd
import numpy as np

def read_excel(Filepath, Sheetname):
    '''
    Reads the Excel sheet and does the first cleaning technique: dropping the empty rows
    and adding column names to allow us to work with the data.
    
    Args:
        Filepath (str): The string containing the filepath to the excel file containing our data.
        Sheetname (str): The string containing the name of the excel sheet we want to use.
    
    Returns:
        Dataframe containing the data from the excel file without the unnecessary rows.
    '''
    df = pd.read_excel(Filepath, sheet_name=Sheetname)
    df = df.drop([0,1,2,3]) #Drops the first four rows (these are used for extra information not necessary to our DataFrame)
    df.columns = ['Customer Number', 'Postal Code','Customer Classification','Horeca Menu Webshop','Product Name Webshop','Brand Name','Contents','2018','2019','2020','2021','2022']
    return df

df = read_excel('dataProject4.xlsx','20000-211000')

def resultsplitter(df):
    '''
    Splits the dataframe between a dataframe containing all the individual products ordered by
    a customer and a dataframe containing only the totals. This is done so we can perform calculations
    without counting everything double.
    
    Args: 
        df (DataFrame): The DataFrame containing both individual products and totals ordered by customers.
    
    Returns:
        df1 (DataFrame): The DataFrame containing only individual products ordered by customers.
        
        
        df2 (DataFrame): The DataFrame containing only total amounts ordered by customers.
    '''
    df1 = df.loc[df['Customer Classification'] != 'Result'].copy() #The result rows contain total sales for each customer. This line creates a dataframe without those total sales.
    df2 = df.loc[df['Customer Classification'] == 'Result'].copy() #This line creates a dataframe containing only those rows.
    df2 = df2.drop(columns = ['Horeca Menu Webshop','Product Name Webshop','Brand Name', 'Contents']) #These columns are empty in the results dataframe, so we'll just drop them
    return df1, df2

df1, df2 = resultsplitter(df)
print(df1.head)
print(df2.head)

def unassigned_category_filter(df):
    '''
    This function assigns the type of drink to values that were previously not assigned based on
    the brand that is selling the product.
    
    Args:
        df (DataFrame): The Dataframe containing our data without results rows.
    
    Returns:
        df (DataFrame): The Dataframe where the unassigned product types are given product types.
    '''
    dftemp = df.loc[df['Horeca Menu Webshop'] == 'Not assigned'] #A temporary dataframe containing the unassigned values.
    dfbeer = dftemp.loc[dftemp['Brand Name'] != 'HAVANA'] #Lines 60-62 are used to filter our the brands which are not beer brands.
    dfbeer = dfbeer.loc[dfbeer['Brand Name'] != 'MARTINI']
    dfbeer = dfbeer.loc[dfbeer['Brand Name'] != 'LIPTON']
    dfbeer['Horeca Menu Webshop'] = dfbeer['Horeca Menu Webshop'].replace('Not assigned', 'Bier - Onbekend') #This line assigns the remaining products as unknown beer products.
    dficetea = dftemp.loc[dftemp['Brand Name'] == 'LIPTON'] #Filters the unassigned values to only have the brand Lipton
    dficetea['Horeca Menu Webshop'] = dficetea['Horeca Menu Webshop'].replace('Not assigned','Frisdrank - IJsthee') #Assigns it to be Ice tea
    dfrum = dftemp.loc[dftemp['Brand Name'] == 'HAVANA'] #Filters the unassigned values to only have the brand Havana
    dfrum['Horeca Menu Webshop'] = dfrum['Horeca Menu Webshop'].replace('Not assigned','Gedist. - Rum') #Assigns it to be Rum
    dfmartini = dftemp.loc[dftemp['Brand Name'] == 'MARTINI'] #Filters the unassigned values to only have the brand Martini
    dfmartini['Horeca Menu Webshop'] = dfmartini['Horeca Menu Webshop'].replace('Not assigned', 'Gedist. - Buitenland') #Assigns it to be a foreign distilled drink
    df['Horeca Menu Webshop'].loc[df['Horeca Menu Webshop'] == 'Not assigned'] = dfbeer['Horeca Menu Webshop'] #The lines 70-73 are used to change the unassigned values
    df['Horeca Menu Webshop'].loc[df['Horeca Menu Webshop'] == 'Not assigned'] = dficetea['Horeca Menu Webshop'] #in our original Dataframe to be the same as the values we just changed
    df['Horeca Menu Webshop'].loc[df['Horeca Menu Webshop'] == 'Not assigned'] = dfrum['Horeca Menu Webshop']
    df['Horeca Menu Webshop'].loc[df['Horeca Menu Webshop'] == 'Not assigned'] = dfmartini['Horeca Menu Webshop']
    return df

print(unassigned_category_filter(df1))


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
from textblob import TextBlob
# py -m pip install pandas textblob
# als dit niet werk py -m weghalen
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
# nltk zou als het goed is al gedownload zijn. anders die van textblob pakken en vervangen met nltk.
def analyze_sentiment_english(tweet: str):
    '''
    Checks the sentiment of a string and returns if the string can be percieved as positive or negative

    Args:
        tweet (str): The string that gets checked for polarity
    Returns:
        A rating on the polarity of the string. If it's a positive message, a negative messsage, or a message that is neutral.
    
    '''
    blob = TextBlob(tweet)
    # turns the input string into a textblob so the textblob commands can be used on it
    sentiment = blob.sentiment.polarity
    # checks the blob for words that can be percieved positive or negative and returns a number based on those words
    if sentiment > 0:
        tweet_sentiment = 'positive'
    elif sentiment < 0:
        tweet_sentiment = 'negative'
    else:
        tweet_sentiment = 'neutral'
    
    #print(f'the tweet {tweet} is {tweet_sentiment}')

#analyze_sentiment_english('awesome blob tester')
#analyze_sentiment_english('awful blob tester')
#analyze_sentiment_english('blob tester')

def analyze_sentiment_other(tweet: str):
    '''
    Checks the sentiment of a string and returns if a tweet can be percieved as positive or negative

    Args:
        tweet (str): The string that gets checked for polarity

    Returns: 
        A rating on the polarity of the string. If it's a positive message, a negative messsage, or a message that is neutral.
    
    '''
    analyzer = SentimentIntensityAnalyzer()
    # turns the sentiment intensity analyzer into an object so commands can be used on it
    sentiment = analyzer.polarity_scores(tweet)
    # calculates the polarity scores of the input
    if sentiment['compound'] >= 0.05:
        tweet_sentiment = 'positive'
    elif sentiment['compound'] <= -0.05:
        tweet_sentiment = 'negative'
    else:
        tweet_sentiment = 'neutral'
    #print(f'the tweet {tweet} is {tweet_sentiment}') 

    
#analyze_sentiment_other('awesome nltk tester')
#analyze_sentiment_other('awful blob tester')
#analyze_sentiment_other('nltk tester')

# Function to apply the correct sentiment analysis based on the language of the tweet
def analyze_sentiment(tweet, language):
    """Applies language-specific sentiment analysis to the tweet.

    Args:
        tweet (str): The tweet text to analyze.
        language (str): The language code of the tweet (e.g., 'en' for English).

    Returns:
        str: The sentiment of the tweet: 'positive', 'negative', or 'neutral'.
    """
    if pd.isna(tweet) or not isinstance(tweet, str):  # Check if the tweet is NaN or not a string
        return 'Unknown'  # Return 'Unknown' or handle it as needed

    if language == 'en':  # English tweets
        return analyze_sentiment_english(tweet)
    else:  # Other language tweets
        return analyze_sentiment_other(tweet)

# Apply sentiment analysis to the DataFrame
tweets_df['Sentiment'] = tweets_df.apply(lambda row: analyze_sentiment(row['Tweet'], row['Language']), axis=1)

# Save the updated DataFrame to a new Excel file
tweets_df.to_excel('tweets_with_language_and_sentiment.xlsx', index=False)

# Display the first 10 rows to verify results
print(tweets_df.head(10))