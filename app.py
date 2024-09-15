import pandas as pd
import streamlit as st

# Load the dataset
file_path = 'industry_recycling_dataset.csv'  # Adjust the path if needed
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    st.error("The dataset file was not found. Please check the file path.")
    st.stop()

# Search function that matches the waste type ignoring case
def search_waste_type(input_text):
    # Case-insensitive search using str.contains
    results = df[df['Waste_Type'].str.contains(input_text, case=False, na=False)]
    
    # Check if results exist
    if results.empty:
        return None
    else:
        return results[['Company_Name', 'Waste_Type', 'Location', 'Monthly_Waste_Generated',  'Year']]

# Streamlit interface
st.title("Industry Recycling Matching System")

# Input for user to search waste type
user_input = st.text_input("Enter the waste type to search for relevant companies:")

# Perform search and display results
if user_input:
    search_results = search_waste_type(user_input)
    
    if search_results is not None:
        st.write(f"Results for waste type similar to '{user_input}':")
        st.dataframe(search_results)
    else:
        st.write(f"No relevant companies found for '{user_input}'.")

