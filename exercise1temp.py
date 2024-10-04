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