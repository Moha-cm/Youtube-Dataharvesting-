import streamlit as st
import streamlit as st 
from API_connection import *
from Extract_func import *
from Data_load import *
import pymysql
import mysql.connector
from dateutil import parser
from sqlalchemy import create_engine
import isodate


st.set_page_config(page_title="Load Page")
st.title("Load Page")
st.subheader("Data Warehousing 📁 ")

st.markdown("##")

st.write("Press the button to store tha data in the database ")
button2 = st.button("💾 Store data")

if button2:
    channel_data = st.session_state.channel_data
    playlist_ids = st.session_state.playlist_ids
    video_ids = st.session_state.video_ids
    video_data = st.session_state.video_data
    comments  =  st.session_state.comments 
    
    # store to Mongodb
    Non_structured = transfrom_nosql(channel_data,playlist_ids,video_data,comments )
    structured = data_to_sql(channel_data,playlist_ids,video_data,comments)
    
    st.write("Data has been stored in database")
    st.balloons()