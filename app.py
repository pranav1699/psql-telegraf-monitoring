import streamlit as st   
from sqlalchemy import create_engine
import pandas as pd
import os
from streamlit.components.v1 import html
import plotly.express as px
from streamlit_autorefresh import st_autorefresh 

st.set_page_config(layout="wide")

count = st_autorefresh(interval=10000, limit=10000000, key="autorefreshapp")

try:
    connection_string = user = os.getenv('OUTPUT_DATABASE')
    db = create_engine(connection_string)
    conn = db.connect()

    smtp = "select count(distinct(db)) from postgresql"
    cun = conn.execute(smtp) 
    postgres = pd.DataFrame(cun.fetchall(), columns=cun.keys())
    ct=postgres['count']
    st.metric("Total databases",ct)

    smtp = "select * from postgresql"

    result = conn.execute(smtp) 

    postgres = pd.DataFrame(result.fetchall(), columns=result.keys())

    st.dataframe(postgres)

    smtp = '''select time,db,avg(tup_fetched) as tup_fetched from postgresql
    group by "time","db" order by time desc
    '''
    res = conn.execute(smtp) 

    postgres_ = pd.DataFrame(res.fetchall(), columns=res.keys())
    fig = px.line(postgres_,x='time',y='tup_fetched',color='db')
    st.plotly_chart(fig,use_container_width=True,theme="streamlit" )
except:
  st.info("Database being Initialized please wait..")

