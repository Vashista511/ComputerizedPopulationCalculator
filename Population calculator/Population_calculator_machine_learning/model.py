import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
import pickle
dataset = pd.read_csv('population.csv')
dataset.head()

# Select the particular rows & column
X = dataset.iloc[:, :-1].values        # years
Y = dataset.iloc[:, 1].values          # population

# Data visualisation by ploting graph
# plt.plot(X, Y, label="Bangalore")
# plt.title('population of Bangalore')
# plt.xlabel('years')
# plt.ylabel('population')
# plt.legend()
# plt.show()

polynomial = PolynomialFeatures(degree=3)
X_poly = polynomial.fit_transform(X)
X_train,X_test,Y_train,Y_test= train_test_split(X_poly,Y, test_size=0.10,random_state=42)
regressor=LinearRegression()
regressor.fit(X_train,Y_train)
#y_pred1 = regressor.predict(polynomial.fit_transform([[yr]]))

# y_pred= regressor.predict(X_test)
# y_pred_all = regressor.predict(X_poly)

# plt.scatter(X, Y , label = "Distribution" , color = "navy")
# plt.plot(X, y_pred_all, label = "Polynomial Regression" , color = "orange" , linewidth = 4)
# plt.xlabel('years')
# plt.ylabel('population')
# plt.show()

#make pickle file
pickle.dump(regressor,open("model.pkl","wb"))
pickle.dump(polynomial,open("poly.pkl","wb"))