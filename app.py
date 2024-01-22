import streamlit as st
import pandas as pd
import io
import requests
import zipfile
import json

# imd extract

url = 'https://assets.publishing.service.gov.uk/media/5d8b3abded915d0373d3540f/File_1_-_IMD2019_Index_of_Multiple_Deprivation.xlsx'

res = requests.get(url)
content = io.BytesIO(res.content)

# Read all sheets into a dictionary of DataFrames
dfs = pd.read_excel(content, sheet_name='IMD2019')

df = dfs
df['Unique_ID'] = range(1, len(df) + 1)
df.set_index('Unique_ID', inplace=True)

st.write(df)

# charity commission data

url = 'https://ccewuksprdoneregsadata1.blob.core.windows.net/data/json/publicextract.charity.zip'

# Make a request to get the ZIP file
res = requests.get(url)

# Unzip the content
with zipfile.ZipFile(io.BytesIO(res.content), 'r') as zip_ref:
    # Assuming there's only one JSON file in the ZIP, you can extract it
    file_name = zip_ref.namelist()[0]
    json_content = zip_ref.read(file_name)

# Load JSON content into a Pandas DataFrame named df2
json_data = json.loads(json_content)
df2 = pd.json_normalize(json_data)  # Adjust as needed based on the JSON structure

st.write(df2)



