import streamlit as st  
  
st.title("⚖️ BMI Calculator")  
 
height = st.slider("Enter your height (in cm):", 100, 256, 170)  
weight = st.slider("Enter your weight (in kg):", 40, 200, 70)  

bmi = weight / ((height / 100) ** 2)  
 
st.write(f"Your BMI is: {bmi:.2f}")  
 
st.subheader("BMI Categories")  
st.write("""  
🟡 **Underweight:** BMI less than 18.5  
🟢 **Normal weight:** BMI between 18.5 and 24.9  
🟠 **Overweight:** BMI between 25 and 29.9  
🔴 **Obesity:** BMI 30 or greater  
""")  