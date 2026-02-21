import streamlit as st
import requests

# Set page title
st.set_page_config(page_title="Geophysics Calculator")

st.title("🪨 Rock Property Calculator")
st.write("This frontend talks to your FastAPI backend to perform calculations.")

# 1. User Input (The Sliders)
number_to_multiply = st.number_input("Enter a value to multiply by 10:", value=1.0)

# 2. The Action Button
if st.button("Calculate"):
    # We send the request to your local FastAPI server
    # Note: Ensure uvicorn is running on port 8000!
    try:
        response = requests.get(f"http://127.0.0.1:8000/calculate/{number_to_multiply}")
        
        if response.status_code == 200:
            data = response.json()
            result = data["result"]
            
            # 3. Display the result beautifully
            st.success(f"The result is: {result}")
            st.json(data) # Show the raw JSON underneath for debugging
        else:
            st.error("Backend is running but returned an error.")
            
    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to FastAPI. Did you run 'uvicorn app.main:app'?")

st.divider()
st.info("Coming from Physics? This is how you separate the UI from the Math logic.")