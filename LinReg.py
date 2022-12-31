import pandas as pd 
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score 
from sklearn.linear_model import LinearRegression 

# read the data 
data = pd.read_csv('student_scores.csv') 

# separate the features and target 
features = data.iloc[:, :-1].values 
target = data.iloc[:, 1].values 

# create the model 
model = LinearRegression() 

# fit the model 
model.fit(features, target) 

# predict the target 
predictions = model.predict(features) 

# calculate the mean absolute error 
mae = mean_absolute_error(target, predictions) 

# calculate the mean squared error 
mse = mean_squared_error(target, predictions) 

# calculate the root mean squared error 
rmse = mse ** 0.5 

print("Mean Absolute Error:", mae) 
print("Mean Squared Error:", mse) 
print("Root Mean Squared Error:", rmse)
#slip 1