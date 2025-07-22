import streamlit as st
import pandas as pd
import numpy as np
import time

# Text Elements
st.title("StreamLit Summary(Title)")
st.header("StreamLit Summary(Header)")
st.subheader("StreamLit Summary(Sub-Header)")
st.write("StreamLit Summary(Text)")
st.markdown("StreamLit Summary(Markdown)")
st.caption("StreamLit Summary(Caption)")

# Media Elements
# st.image("xyz.jpg")
# st.audio("speech.wav")
# st.video("abc.mkv")

# Input Widgets
st.checkbox('checkbox')
st.button('Click button')
st.radio('Pick your city', ['Pune', 'Mumbai', 'delhi', 'surat'])
st.selectbox('Pick your city', ['Pune', 'Mumbai', 'delhi', 'surat'])
st.multiselect('Pick favourite sports', ['cricket', 'football', 'basketball'])
st.select_slider('Give a Remark', ['Bad', 'Good', 'Excellent'])
st.slider('Your Marks', 0, 100)

import streamlit as st

# Toggle widget
on = st.toggle("Activate feature")
if on:
    st.write("Feature activated!")

# Number input
number = st.number_input("Insert a number")
st.write("The current number is ", number)

# Date and time inputs
d = st.date_input("When's your birthday", value=None)
st.write("Your birthday is:", d)

t = st.time_input("Set an alarm for", value=None)
st.write("Alarm is set for", t)

# Additional input widgets
st.number_input('Enter your marks', 0, 100)
st.text_input('Enter Text')
st.date_input('Exam date')
st.time_input('Exam time')
st.text_area('Description')
st.file_uploader('Upload File')
st.color_picker('Choose a color')

# Status messages
st.success("Success")
st.error("Error")
st.warning("Warning")
st.info("Information")
st.exception(RuntimeError("RuntimeError exception"))

# Sidebar elements
st.sidebar.title("StreamLit Summary(Sidebar Title)")
# st.sidebar.image("xyz.jpg")

# Dataframe display (Note: Corrected 'dataFrame' to 'dataframe')
df = pd.DataFrame(np.random.randn(50, 20), columns=["col %d" % i for i in range(20)])
st.dataframe(df)  # Corrected from st.dataFrame to st.dataframe

# Table display
df = pd.DataFrame(
    np.random.randn(10, 5), columns=["col %d" % i for i in range(5)]
)
st.table(df)

# Columns with metrics
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# Chat input
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

# Progress bar
# progress = st.progress(0)
# Status widget with multiple steps
with st.status("Step 1"):
    st.write("Step 2")
    time.sleep(1)
    st.write("Step 3")
    time.sleep(1)
    st.write("Step 4")
    time.sleep(1)
st.button("Rerun")

# Area chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)

# Bar chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data)

# Line chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)

# Map data (incomplete in original, completed here)
# Chandni Chowk coordinates (center point)
chandni_chowk_lat = 28.6519
chandni_chowk_lon = 77.2315

# Generate 1000 random points around Chandni Chowk
np.random.seed(42)  # For reproducibility
df = pd.DataFrame(
    np.random.randn(1000, 2) * [0.01, 0.01] + [chandni_chowk_lat, chandni_chowk_lon],
    columns=['lat', 'lon']
)

# Display the map
st.title("Chandni Chowk Area Map")
st.map(df, zoom=14)  # Higher zoom level for street-level view

# Show the raw data
st.write("Sample coordinates:")
st.dataframe(df.head())
# df = pd.DataFrame(
#     np.random.randn(1000, 2) / [70, 60] + [47.76, -100.4],
#     columns=['lat', 'lon']
# )
# st.map(df)

# Scatter chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.scatter_chart(chart_data)

# Chat message
with st.chat_message("user"):
    st.write("Hello ji")