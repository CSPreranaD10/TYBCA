#importing packages
import numpy as np
from sklearn.linear_model import LinearRegression

#creating objects
x = np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)
y = np.array([7,14,15,18,19,21,26,23])

#creating linear regression object
model = LinearRegression()

#fitting model
model.fit(x,y)

#calculating slope and intercept
b1=model.coef_
b2=model.intercept_

#printing values
print("slope is:",b1)
print("intercept is:",b2)

#calculating accuracy
accuracy=model.score(x,y)

#printing accuracy
print("accuracy of the model is:",accuracy)
#slip 18,7,3
