import streamlit as st
from Database_connection import *
from API_connection import *
from Extract_func import *
from Data_load import *
import pymysql
import mysql.connector
from dateutil import parser
from sqlalchemy import create_engine
import isodate

st.set_page_config(page_title="YouTube Data Harvesting and Warehousing")
st.title("YouTube Data Harvesting ")
st.subheader("⚒️Extract the Data from the source")

youtube = Api_connection()
#st.write(youtube)

channel_id = st.text_input("Enter the channel_id").split(",")

button1 = st.button("Submit")
button2 = st.sidebar.button("clear Database")

#st.write(channel_ids)

if button1 :
    
    channel_ids = validate_id(channel_id)
    channel_data = get_channel_data(youtube,channel_ids)
    playlist_ids = get_playlist_info(youtube,channel_data)
    video_ids = playlist_video_list(youtube,channel_ids)
    video_data = get_video_contents(youtube,video_ids)
    comments = get_comments(youtube,video_ids)
        
    if 'channel_data' not in st.session_state:
        st.session_state.channel_data = channel_data
    if 'playlist_ids' not in st.session_state:
        st.session_state.playlist_ids = playlist_ids
    if 'video_ids' not in st.session_state:
        st.session_state.video_ids = video_ids
    if 'video_data' not in st.session_state:
        st.session_state.video_data =  video_data
    if 'comments' not in st.session_state:
        st.session_state.comments = comments 
    st.success("select a page above for further Process....!")
    st.write(channel_data[0],playlist_ids[0],video_data[0],comments[0])
    st.balloons()
    
    
if button2:
    clear_SQLdatabase()
    clear_mongodv()
    st.write("Database Deleted successfully!!! ")
    
    
    


# UCwr-evhuzGZgDFrq_1pLt_A,UCuf90yPD_Yx53xZyVLtvRmA,UCnXs-Nq1dzMZQOKUHKW3rdw,UCG4kmWK8UyzfenZ60xVBapw,UCW-DzgC7mJGPoVFz8F0W6Sw,UC0DNFLi8yg1UVo67bCLMMJg,UC9cBIteC3u7Ee6bzeOcl_Og,UCQqQpIx3zQPaifBj67ocv1w,UCikIHemqr_ypPpf4wFqjUlg,UCDbobv7_LYSJzUVwmMR-fRA

