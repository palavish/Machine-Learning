import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('/Users/vishnupalanisamy/Documents/Vishnu/trained_model.sav','rb'))

#creating a function for prediction
def diabetes_prediction(input_data):
    
    #changing the input_data to numpy array
    input_data_as_numpy_array=np.asarray(input_data)

    #Reshape the array to predict single instance 
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

    prediction =loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return "The person is Non Diabetic"
    else:
        return "The person is Diabetic" 

def main():

    #giving a title
    st.title('Diabetic Prediction Web App')

    #getting input data from user
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness= st.text_input('SkinThickness')
    Insulin  = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('Age of the Person')
    
    #Code for Prediction
    diagnosis =''
    # Creating Button for Prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)


if __name__== '__main__':
    main()