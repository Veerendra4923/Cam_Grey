import streamlit as st
from PIL import Image
#asks to start the camera with being camera automatic after opening the web site
uploaded_image = st.file_uploader("Upload Image")
with st.expander("Start start camera"):
    #takes the input and stores in camera'''
    camera=st.camera_input("Cam")
#In one case the photo is not taken then we will get errors for avoiding that we use this if statement'''
if camera:
    image=Image.open(camera)
    grey=image.convert("L")
    st.image(grey)
elif uploaded_image:
    image1=Image.open(uploaded_image)
    grey=image1.convert("L")
    st.image(grey)