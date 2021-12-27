import streamlit as st

st.title('Iris Flower Data')

ip = st.slider('Select Stepal Length',min_value=0.0,max_value=10.0,step=0.1)   
jp = st.slider('Select Stepal Width',min_value=0.0,max_value=10.0,step=0.1)
kp = st.slider('Select Petal Length',min_value=0.0,max_value=10.0,step=0.1)
lp = st.slider('Select Petal Width',min_value=0.0,max_value=10.0,step=0.1)

from sklearn.datasets import load_iris
iris = load_iris()

from sklearn.tree import DecisionTreeClassifier
model== = DecisionTreeClassifier()
model.fit(iris.data,iris.target)

op = model.predict([[ip,jp,kp,lp]])
op = iris.target_names[op[0]]

st.title(op[0])

