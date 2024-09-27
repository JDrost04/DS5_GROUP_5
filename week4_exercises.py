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

# EXERCISE 4
# 4.1
# 4.2