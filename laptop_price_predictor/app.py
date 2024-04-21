import streamlit as st
import pandas as pd
import numpy as np
import pickle

file = open('./model/pipe.pkl', 'rb')
rf = pickle.load(file)
file.close()

# Load the preprocessed data
data = pd.read_csv("./data/trained_data.csv")

# Create a title for the UI page
st.title("Laptop Price Predictor")

# Create Selection boxes for each feature / attribute
# Laptop brand name
company = st.selectbox('Brand', data['Company'].unique())

# Laptop Type
type_name = st.selectbox('Type', data['TypeName'].unique())

# Laptop RAM
ram = st.selectbox('Ram(in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
ram = int(ram)

# Operating System of a laptop
os = st.selectbox('OS', data['OpSys'].unique())

# Weight of the laptop
weight = st.number_input('Weight of the laptop')
weight = float(weight)

# Touchscreen
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

# IPS
ips = st.selectbox('IPS', ['No', 'Yes'])

# Screen Size
screen_size = st.number_input('Screen Size')

# Laptop screen resolution
resolution = st.selectbox('Screen Resolution', [
                          '1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])

# CPU
cpu = st.selectbox('CPU', data['CPU_name'].unique())

# HDD
hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])
hdd = int(hdd)

# SSD
ssd = st.selectbox('SSD(in GB)', [0, 8, 128, 256, 512, 1024])
ssd = int(ssd)

# GPU
gpu = st.selectbox('GPU(in GB)', data['Gpu brand'].unique())

# Display predicted price on the screen
if st.button('Predict Price'):
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_resolution = int(resolution.split('x')[0])
    Y_resolution = int(resolution.split('x')[1])
    
    ppi = ((X_resolution**2)+(Y_resolution**2))**0.5/(screen_size)

    query = [[company, type_name, ram, os, weight,
                      touchscreen, ips, ppi, cpu, hdd, ssd, gpu]]
    
    # query = query.reshape(1, 12)
    
    prediction = int(np.exp(rf.predict(query)))

    st.title("Predicted price for this laptop could be between " +
             str(prediction-1000)+"₹" + " to " + str(prediction+1000)+"₹")
