import streamlit as st
import pandas as pd

# Function to process the CSV file
def process_file(uploaded_file):
    df = pd.read_csv(uploaded_file)

    # Rename the column to 'text'
    original_column_name = df.columns[0]  # Assuming the first column is the text column
    df.rename(columns={original_column_name: 'text'}, inplace=True)

    # Add a new column 'text_length' to store the length of each text
    df['text_length'] = df['text'].apply(len)

    return df

# Title of the app
st.title("CSV Text Processor")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Process the uploaded file
    processed_df = process_file(uploaded_file)

    # Display the processed dataframe
    st.write("Processed Data:")
    st.dataframe(processed_df)

    # Create a download button
    csv = processed_df.to_csv(index=False)
    st.download_button(
        label="Download Processed CSV",
        data=csv,
        file_name='processed_file.csv',
        mime='text/csv',
    )
