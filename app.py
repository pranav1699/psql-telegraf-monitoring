import streamlit as st   
from sqlalchemy import create_engine
import pandas as pd
import os

connection_string = user = os.getenv('OUTPUT_DATABASE')
db = create_engine(connection_string)
conn = db.connect()


smtp = "select * from postgresql"

result = conn.execute(smtp) 

postgres = pd.DataFrame(result.fetchall(), columns=result.keys())

st.dataframe(postgres)

