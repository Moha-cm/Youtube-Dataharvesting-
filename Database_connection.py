import streamlit as st
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine, MetaData  
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi 
    

# get all the tables form the table from SQL

@st.cache_data
def get_all_Tables():
    try:
        cnx = create_engine('mysql+pymysql://root:@localhost/youtube')
        data1 = pd.read_sql('SELECT * FROM channel',  con = cnx).sort_values(by ="videoCount",ascending=False)
        data2 = pd.read_sql('SELECT * FROM playlist',  con = cnx)
        datas3 = pd.read_sql('SELECT * FROM video',  con = cnx)
        datas4 = pd.read_sql('SELECT * FROM comment',  con = cnx)
        df = pd.merge(datas3,datas4,on="video_id",how="inner")
        df = pd.merge(data2,datas3,on="playlist_id",how="inner")
        df= pd.merge(data1,df,on="channel_id",how="inner")
        return df
    except:
        st.warning("Connect to the database")
    
# To Drop the databse in SQL
def clear_SQLdatabase():
    try :
        mydb = mysql.connector.connect(host="localhost",                    
                               user="root",password=""
                              )#database='joins' 
        print(mydb) # object
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("DROP DATABASE youtube")
        st.write("Database deleted")
    except:
        st.write("Database not exit")
    

# To Drop the databse in MongoDB
def clear_mongodv():
    # connecting to the Mongodb server 
    try :
        uri = "mongodb+srv://mohan:mohan@cluster0.rochv2v.mongodb.net/?retryWrites=true&w=majority"
    
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            
            client = MongoClient("mongodb+srv://mohan:mohan@cluster0.rochv2v.mongodb.net/?retryWrites=true&w=majority")
            client.drop_database("youtube")
            st.write("Database deleted")
            

        except Exception as e:
            print(e)
    except:
        st.write("Datase not exit")
        
    
    
    
    
    