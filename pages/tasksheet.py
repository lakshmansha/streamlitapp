import os
import streamlit as st
from pymongo import MongoClient
from pandas import DataFrame
import numpy as np

CONNECTION_STRING = str(os.getenv("CONNECTION_STRING"))
DATABASE = str(os.getenv("DATABASE"))

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return MongoClient(CONNECTION_STRING)

client = init_connection()

# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_users_data():
    db = client[DATABASE]
    collection = db["users"]
    items = collection.find()
    items = list(items)  # make hashable for st.cache_data    
    df = DataFrame(items)
    return df

data_load_state = st.text('Loading data...')
items = get_users_data()
data_load_state.text("Done! (using st.cache_data)")

# Print results.
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(items)    
