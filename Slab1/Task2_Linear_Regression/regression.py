import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("house_data.csv")

# Input (house size) and output (price)
X = data[['Size']]
y = data['Price']

# Create Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Predict price for 1200 sq ft house
predicted_price = model.predict([[1200]])

print("Predicted price for 1200 sq ft house:", predicted_price[0])
