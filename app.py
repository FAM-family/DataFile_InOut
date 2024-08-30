import streamlit as st
import pandas as pd
pd.set_option('display.max_colwidth', None)

# Function to process the CSV file
def process_file(uploaded_file):
    df = pd.read_csv(uploaded_file, encoding='latin-1', delimiter='\t')

    # Rename the column to 'text'
    original_column_name = df.columns[0]  # Assuming the first column is the text column
    df.rename(columns={original_column_name: 'text'}, inplace=True)

    # Add a new column 'text_length' to store the length of each text
    df['text_length'] = df['text'].apply(len)

    return df

# Title of the app
st.title("Data Augmentation")

# Add a title to the sidebar
st.sidebar.title("Input File Uploader")

# File uploader
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type='csv')
#uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Process the uploaded file
    processed_df = process_file(uploaded_file)

    # Display the dimension of the dataframe
    #st.write("Input Data Dimensions:")
    #st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    # Display the processed dataframe
    st.write("Processed Data Extract:")
    st.dataframe(processed_df.head())

    # Display the dimension of the dataframe
    st.write("Processed Data Dimensions:")
    st.write(f"Rows: {processed_df.shape[0]}, Columns: {processed_df.shape[1]}")

    # Create a download button
    csv = processed_df.to_csv(index=False)
    st.download_button(
        label="Download Processed CSV",
        data=csv,
        file_name='processed_file.csv',
        mime='text/csv',
    )
