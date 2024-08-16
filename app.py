import streamlit as st
from PIL import Image
from streamlit import image

image = Image.open(r'C:\bank.webp')
st.image(image,caption ='Wlecome to Sbi Bank')
st.title('Loan Calculator')
st.header('Sbi Bank of India')
x=st.number_input('Entre your amount')#For taking input
y=st.number_input('Entre your salary')

if y>=50000:
    st.write('Congratulation')
    st.balloons()

else:
    st.write('sorry') #For printing

z=st.radio('Are you a goverment employe:',options=['yes','no'])
st.checkbox('Do you have a credit card')
st.sidebar.header('Schemes from Loan Dept.')
st.sidebar.markdown([1,2,3,4])

    #C:\Users\Administrator\PycharmProjects(location of file)
