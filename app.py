import streamlit as st
import pandas as pd
import numpy as np
import joblib
import sklearn

st.header("Zomato classification Project")
st.image("Restaurant.png")  
inputs= joblib.load("input.h5")
Model = joblib.load("rf.h5")
# defining the function which will make the prediction using the data which the user inputs 
def prediction(online_order, book_table, votes, rest_type,cuisines,cost):
    
    if online_order == 'True': 
        online_order = 1
    else:
        online_order = 0
        
    if book_table == 'True': 
        book_table = 1
    else:
        book_table = 0
        
    if cuisines == 'Chines': 
         cuisines = 0
    elif cuisines == 'fastfood':
        cuisines = 1
    elif cuisines == 'Thai':
         cuisines = 2
    elif cuisines == 'Italian':
        cuisines = 3
    elif cuisines == 'Indian':
        cuisines = 4
    elif cuisines == 'Desserts':
        cuisines = 5
    else  :      
        cuisines = 6
        
    if rest_type == 'Takeaway': 
        rest_type = 0
    elif rest_type == 'Desserts':
        rest_type = 1
    elif rest_type == 'Delivery':
        rest_type = 2
    elif rest_type == 'Casual Dining':
        rest_type = 3
    elif rest_type == 'Cafe':
        rest_type = 4
    else:
        rest_type = 5
 
    # Making predictions 
    prediction = Model.predict( 
        [[online_order, book_table, votes, rest_type, cuisines,cost]])
     
    if prediction == 0:
        pred = 'UnderRated'
    else:
        pred = 'OverRated'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:gray;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Zomato Prediction Rate ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    online_order = st.selectbox('online_order',("True","False"))
    book_table = st.selectbox('book_table',("True","False")) 
    votes = st.slider("votes" , min_value=0, max_value=16880, value=25, step=100)
    rest_type = st.selectbox("rest_type",('Takeaway', 'Desserts', 'Delivery','Casual Dining','Cafe','Others'))
    cuisines = st.selectbox("cuisines",('Chines', 'fastfood', 'Thai','Italian','Indian','Desserts','other'))
    cost = st.slider("cost" , min_value=0, max_value=6000, value=100, step=200)
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(online_order, book_table, votes, rest_type, cuisines,cost) 
        st.success('The Zomato Rate is {}'.format(result))     
if __name__=='__main__': 
    main()

