import streamlit as st  
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.linear_model import LinearRegression  
 
st.title("🏘️ House Price Prediction App")  
  
st.header("Input Data")  
feature1 = st.number_input("Enter Feature 1 (e.g., Area in sq ft):", min_value=0, value=1000)  
feature2 = st.number_input("Enter Feature 2 (e.g., Number of Rooms):", min_value=0, value=3)  
 
data = {  
    'Feature1': [800, 1000, 1200, 1500, 1800],  
    'Feature2': [2, 3, 3, 4, 5],  
    'Price': [150000, 200000, 250000, 300000, 350000]  
}  
 
df = pd.DataFrame(data)  
 
X = df[['Feature1', 'Feature2']]  
y = df['Price']  
model = LinearRegression()  
model.fit(X, y)  

input_data = np.array([[feature1, feature2]])  
prediction = model.predict(input_data)  
 
st.subheader("Predicted Price")  
st.write(f"The estimated price is: ${prediction[0]:,.2f}")  

st.subheader("Data Visualization")  
plt.figure(figsize=(10, 6))  
 
plt.scatter(df['Feature1'], df['Price'], color='blue', label='Data Points')  
plt.scatter(feature1, prediction, color='red', label='Prediction Point', s=100)  

x_range = np.linspace(df['Feature1'].min(), df['Feature1'].max(), 100).reshape(-1, 1)  
predicted_prices = model.predict(np.column_stack((x_range, np.zeros(x_range.shape))))  
plt.plot(x_range, predicted_prices, color='green', label='Regression Line')  

plt.title("House Price vs Area")  
plt.xlabel("Area (sq ft)")  
plt.ylabel("Price ($)")  
plt.legend()  
plt.grid()  
st.pyplot(plt)  
 
st.write("Made with ❤️by Hina Sher using Streamlit- thanks for using it!")  