import streamlit as st
import pandas as pd
# Define the options for the selectbox
options = [
    "Select State Wise",
    "Andaman & Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar",
    "Chandigarh", "Chhattisgarh", "Dadra & Nagar Haveli and Daman & Diu", "Goa", "Gujarat", 
    "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", 
    "Ladakh", "Lakshadweep", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", 
    "Mizoram", "Nagaland", "NCT OF Delhi", "Odisha", "Puducherry", "Punjab", "Rajasthan", 
    "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

# Create the selectbox
selected_option = st.selectbox('Select State wise', options)

# Function to display information for Andaman & Nicobar Islands
def andaman_nicobar_islands_page():
    st.write("Andaman & Nicobar Islands page content goes here.")

# Add similar functions for other states as needed
def bihar_page():
    st.write("Bihar page content goes here.")
    # Load and process the data for Bihar
    df = pd.read_csv('state-wise/Bihar.csv')
    dat = df[df['won status'] == 'won']
    party_names = dat['Party Name']
    party_counts = party_names.value_counts()
    for party_name, won_count in party_counts.items():
        st.write(f'Party: {party_name}, Wins: {won_count}')

# Use a dictionary to map options to functions
page_functions = {
    "Andaman & Nicobar Islands": andaman_nicobar_islands_page,
    "Bihar": bihar_page,
    # Add more mappings for other states
}

# Check if the selected option has a corresponding page function
if selected_option in page_functions:
    # Call the function to render the appropriate page
    page_functions[selected_option]()
else:
    st.write("Please select a state to view details.")
