import streamlit as st    
import joblib
model = joblib.load('Iris Data(1)')  
st.title('Iris Flower Data')  

ip = st.slider('Select Stepal Length',min_value=0.0,max_value=10.0,step=0.1)     
jp = st.slider('Select Stepal Width',min_value=0.0,max_value=10.0,step=0.1)  
kp = st.slider('Select Petal Length',min_value=0.0,max_value=10.0,step=0.1)    
lp = st.slider('Select Petal Width',min_value=0.0,max_value=10.0,step=0.1)    

op = model.predict([ip,jp,kp,lp])      

if st.button('Predict'):   
  st.title(op[0])      

