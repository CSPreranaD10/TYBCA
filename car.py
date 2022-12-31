# import the relevant libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Read the data into a pandas DataFrame
df = pd.read_csv('cardata.csv')

# Define the independent and dependent variables
X = df[['Weight', 'Volume']]
y = df['CO2']

# Create the linear regression model
model = LinearRegression()

# Train the model using the training sets
model.fit(X,y)

# Print the coefficients
print('Weight coefficient: ', model.coef_[0])
print('Volume coefficient: ', model.coef_[1])

# Predict the CO2 values
y_pred = model.predict(X)

# Print the prediction results
print('Predicted CO2 values:', y_pred)

#slip 19,12