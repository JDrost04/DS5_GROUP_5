import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm # py -m pip install statsmodels
from sklearn.metrics import mean_squared_error

#exercise 1
np.random.seed(2)

x = np.random.uniform(0, 10, 200)
y = 2 * x**2 - 5 * x + 3 + np.random.normal(0, 10, 200)

# Plot the dataset
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Dataset')
plt.show()

# Split into Train/Test
trainValues = {
    'x': x[:80],
    'y': y[:80]
}
training_data = pd.DataFrame(trainValues)

testValues = {
    'x': x[80:],
    'y': y[80:]
}
test_data = pd.DataFrame(testValues)

# Fit the regression model
train_x = training_data['x']
train_x_sq = pd.DataFrame(training_data['x']**2)

# Create polynomial features
train_x_poly = pd.concat([train_x, train_x_sq], axis = 1)

# Fit the OLS model
X = sm.add_constant(train_x_poly)
model = sm.OLS(training_data['y'], X)
results = model.fit()

# Obtain the predicted values
predicted_training_y = results.predict(X)
 
# Plot the training set and regression line
plt.scatter(training_data['x'], training_data['y'])
plt.scatter(training_data['x'], predicted_training_y, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Regression Model (Degree 2)')
plt.show()

# Evaluate R_squared and MSE
train_R_squared = results.rsquared
print('Train R^2 = ',train_R_squared)
# R_squared = 0.9378508186540011

# Prepare the test data 
test_x = test_data['x']
test_x_sq = pd.DataFrame(test_data['x']**2)

# Create polynomial features for the test set
test_x_poly = pd.concat([test_x, test_x_sq], axis=1)

# Predict the test set outcomes
X_test = sm.add_constant(test_x_poly)  # Add the constant (intercept term)
predicted_test_y = results.predict(X_test)

# Evaluate the model on the test set 
test_R_squared = 1 - sum((test_data['y'] - predicted_test_y)**2) / sum((test_data['y'] - np.mean(test_data['y']))**2)

print("Test R^2 = ", test_R_squared)

# Plot the test set and the predicted values
plt.scatter(test_data['x'], test_data['y'], label="Actual Test Data")
plt.scatter(test_data['x'], predicted_test_y, color='red', label="Predicted Test Data")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Test Data vs. Predicted Data (Polynomial Regression)')
plt.legend()
plt.show()

#exercise 2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm # py -m pip install statsmodels
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor

# a) read csv file
wine_data = pd.read_csv('winequality-red.csv', sep=';')

# b) Explore data
print(wine_data.head())
print(wine_data.describe())

# c) data handeling
def drop_duplicates(df):
    if df.duplicated().any():
        print('there are duplicates in the data')
        df.drop_duplicates()
        print('duplicates removed')
    
    else: 
        print('no duplicates found') 
        
def find_missing_values(df):
    if df.isnull().values.any():
        print('the data contains missing values')
    else:
        print('no missing values found')

drop_duplicates(wine_data)
find_missing_values(wine_data)

# d) Plot distribution of quality
plt.hist(wine_data['quality'], bins=6)
plt.title('Distribution of Wine Quality Ratings')
plt.show()

# Plot heatmap for relations
correlation_matrix = wine_data.corr()
plt.imshow(correlation_matrix, cmap='RdYlGn')
plt.title('Correlation between Features and Wine Quality')
plt.show()

# e) Define features (X) and target (y)
X = wine_data.drop('quality', axis=1)
y = wine_data['quality']

# Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training set size:", X_train.shape)
print("Test set size:", X_test.shape)

# f) Initialize the linear regression model
lin_reg_model = LinearRegression()

# g) Train the linear regression model
lin_reg_model.fit(X_train, y_train)

# Make predictions
y_pred_train = lin_reg_model.predict(X_train)
y_pred_test = lin_reg_model.predict(X_test)

# h) Evaluate the model performance using R^2 score
train_r2 = r2_score(y_train, y_pred_train)
test_r2 = r2_score(y_test, y_pred_test)

print("Linear Regression Model - Training R^2 Score:", train_r2)
print("Linear Regression Model - Test R^2 Score:", test_r2)

# i) Initialize the Random Forest model
rf_model = RandomForestRegressor(random_state=42)

# Train the Random Forest model
rf_model.fit(X_train, y_train)

# Make predictions
y_pred_train_rf = rf_model.predict(X_train)
y_pred_test_rf = rf_model.predict(X_test)

# Evaluate the model performance using R^2 score
train_r2_rf = r2_score(y_train, y_pred_train_rf)
test_r2_rf = r2_score(y_test, y_pred_test_rf)

print("Random Forest Model - Training R^2 Score:", train_r2_rf)
print("Random Forest Model - Test R^2 Score:", test_r2_rf)

# j) Compare the two models
print(f"Comparison of Models:")
print(f"Linear Regression - Training R^2: {train_r2}, Test R^2: {test_r2}")
print(f"Random Forest - Training R^2: {train_r2_rf}, Test R^2: {test_r2_rf}")

# h) Discussion
"""
Linear Regression is a simple model that assumes linear relationships between the features and the target, 
which might not be true for this dataset. This can lead to underfitting and lower R² scores, especially on non-linear data.

Random Forest is a more complex model that can capture non-linear relationships and interactions between features, 
leading to better performance, but it can be prone to overfitting if the model is not properly tuned.

Some feature transformations such as scaling, normalization, or interaction terms could improve model performance.
"""

#exercise 3.1
data_training = pd.read_excel('training.xlsx')
data_predictions = pd.read_excel('predictions_training.xlsx')
def malaria_prediction_accuracy_checker(data_training,data_predictions):
    '''
    A function calculating the accuracy of predictions made by a program based on placing borders around images
    
    Args:
        data_training(dataframe): dataframe containing the exact borders around the images.
        data_predictions(dataframe): dataframe containing predicted borders where images could be.
        
    Returns:
        mean_IOU: the average of the prediction succes rates for each border. 
    '''
    limit_r = int(max(max(data_training['max_r']),max(data_predictions['max_r']))) # vind de hoogste waarde van de rij coordinaten
    limit_c = int(max(max(data_training['max_c']),max(data_predictions['max_c']))) # vind de hoogste waarde van de kolom coordinaten
    A = np.zeros([limit_r,limit_c]) # maakt een lijst van nullen met een lengte en breedte van de maximale waarde. Wordt gebruikt om de borders te visualiseren
    IOU = [] # maakt een lijst aan waarin de IOU opgeslagen worden
    for t in data_training.index:
        t_min_r,p_min_r = data_training['min_r'].iloc[t],round(data_predictions['min_r'].iloc[t]) # vind de minimale coordinaten op de rij van een border
        t_max_r,p_max_r = data_training['max_r'].iloc[t]+1,round(data_predictions['max_r'].iloc[t]+1) # vind de maximale coordinaten op de rij van een border
        t_min_c,p_min_c = data_training['min_c'].iloc[t],round(data_predictions['min_c'].iloc[t]) # vind de minimale coordinaten op de kolom van een border
        t_max_c,p_max_c = data_training['max_c'].iloc[t]+1,round(data_predictions['max_c'].iloc[t]+1) # vind de maximale coordinaten op de kolom van een border
        A[t_min_r:t_max_r,t_min_c:t_max_c] = 1 # voegt een waarde 1 toe om de binnenkant van een border te visualiseren
        A[p_min_r:p_max_r,p_min_c:p_max_c]+=2 # voegt de waarde 2 aan de binnenkant van een predicted border.
        intersection = np.count_nonzero(A > 2) # berekent hoeveel van de predicted border met de daadwerkelijke border matchet
        union = np.count_nonzero(A > 0) # berekent hoeveel er in de daadwerkelijke en predicted border zit.
        IOU.append(intersection/union) # berekent hoeveel van de predicted border in de daadwerkelijke border zit.
        A[data_training['min_r'].iloc[t]-150:data_training['max_r'].iloc[t]+150,data_training['min_c'].iloc[t]-150:data_training['max_c'].iloc[t]+150] = 0 # reset de lijst van nullen zodat een nieuwe border gevisualiseerd kan worden.
        print(f'Currently at row {t}', end = '\r')
    mean_IOU = np.mean(IOU) # berekent het gemiddelde percentage van hoeveel de predicted borders matchen met de echte borders.
    print(f'The average IOU of the prediction is {mean_IOU:.4f}')
    return mean_IOU


#malaria_prediction_accuracy_checker(data_training,data_predictions) #Om de functie te testen. waarschuwing duurt best wel lang om uit te voeren.

#exercise 3.2