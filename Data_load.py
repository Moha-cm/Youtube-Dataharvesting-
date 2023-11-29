import pandas as pd

import streamlit as st 


#*********************************** Storing in NoSQL Database - Mongodb*******************************************

def transfrom_nosql(channel_data,play_list,vedio_cont,video_comm):
    from dateutil import parser
    import pymongo
    from pymongo.mongo_client import MongoClient
    from pymongo.server_api import ServerApi 
    from dateutil import parser
    
    # connecting to the Mongodb server 
    
    uri = "mongodb+srv://mohan:mohan@cluster0.rochv2v.mongodb.net/?retryWrites=true&w=majority"
    
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
         
        client = MongoClient("mongodb+srv://mohan:mohan@cluster0.rochv2v.mongodb.net/?retryWrites=true&w=majority")
        db = client.youtube
        records = db.youtube_data
        
        
        
        
        # converting the pandas channel table to dict
        channel_table = pd.DataFrame(channel_data)
        change_dict = {"subscriberCount":int,"videoCount":int,"viewCount":int} # changing the datatype in pandas 
        channel_table = channel_table.astype(change_dict)
        
        # converting the pandas  playlist table to dict
        playlist_t = pd.DataFrame(play_list).to_dict(orient="records")
        
        # converting the pandas vedio tableto dict
        video_t = pd.DataFrame(vedio_cont).to_dict(orient="records")
        records.insert_many(channel_table.to_dict('records'))
        
        # converting the pandas commnet table to dict 
        comments_t = pd.DataFrame(video_comm).to_dict(orient="records")
        
        
        
        for i in channel_table.to_dict(orient="records"):
            channel = i["channel_id"]
            for s in playlist_t:  # playlist table
                if channel == s["channel_id"]:
                    play_id = s["playlist_id"]
                    vedio_ids = []
                    c = 0
                    for j in video_t:  # video_table
                        d = 0
                        if play_id == j["playlist_id"]:
                            video_ID = j['video_id']
                            
                            comments_contents = []
                            for l in comments_t:
                                if video_ID == l["video_id"]:
                                    data = dict(comment_id = l["comment_id"],
                                                comment_author = l["comment_author"],
                                                comment_published = l["comment_published"],
                                                comment_text = l["comment_text"])
                                    comments_contents.append(data)
                                
                            data1 = dict(Video_id=j["video_id"],
                                         video_name=j['video_name'],
                                         published_data=j["published_data"],
                                         view_count = j["view_count"],
                                         Likes_count=j["Likes_count"],
                                         Dislikes_count=j["Dislikes_count"],
                                         favorite_count=j["favorite_count"],
                                         duration=j["duration"],
                                         Description =j["Description"],
                                         comments = comments_contents)
                            vedio_ids.append(data1)
                            c = c+1
                        
                        
                    myquery ={"_id": channel}
                    newvalues = {"$set":{f"play_list_{c} : { play_id}":vedio_ids}}
                    
                    records.update_one(myquery, newvalues)
    
    except Exception as e:
        print(e)
        return  st.warning(" Mongodb Connection Problem!!")
                
    return "Data has been stored to Mongodb"                           
                    
                    
#transfrom_nosql(channel_data,play_list,vedio_cont,video_comm)


# **************************************** Storing in SQL Database****************************************************************

def data_to_sql(channel_data,play_list,vedio_cont,video_comm):
    import pymysql
    import mysql.connector
    from dateutil import parser
    from sqlalchemy import create_engine
    
    try :
         # connecting to the server 
        mydb = mysql.connector.connect(host="localhost", user="root",password="")
        mycursor = mydb.cursor(buffered=True) 
        mycursor = mydb.cursor(buffered=True) 
        mycursor = mydb.cursor()
        # create the database and creating the tables in the database 
        mycursor.execute("CREATE DATABASE youtube")
        mycursor.execute("USE youtube")
        mycursor.execute("CREATE TABLE channel (channel_id VARCHAR(255) PRIMARY KEY, channel_name VARCHAR(255),subscriberCount INT, videoCount INT, channel_description TEXT, channel_status VARCHAR(255),viewCount INT)")
        mycursor.execute("CREATE TABLE playlist (playlist_id VARCHAR(255) PRIMARY KEY,channel_id VARCHAR(255), playlist_name VARCHAR(255), FOREIGN KEY (channel_id) REFERENCES channel (channel_id))")
        mycursor.execute("CREATE TABLE video (video_id VARCHAR(255) PRIMARY KEY, playlist_id VARCHAR(255), video_name VARCHAR(255), Description TEXT, published_data DATETIME, view_count INT, Likes_count INT, Dislikes_count INT, favorite_count INT,Comment_count INT, duration INT, FOREIGN KEY (playlist_id) REFERENCES playlist (playlist_id))")
        mycursor.execute("CREATE TABLE comment (comment_id VARCHAR(255), video_id VARCHAR(255), comment_text TEXT, comment_author VARCHAR(255), comment_published DATETIME, FOREIGN KEY (video_id) REFERENCES video (video_id))")
        # creating the engine to connect with database
        cnx = create_engine('mysql+pymysql://root:@localhost/youtube')
    
        # for channel_table
        channel_table = pd.DataFrame(channel_data)
        change_dict = {"subscriberCount":int,"videoCount":int,"viewCount":int}
        channel_table = channel_table.astype(change_dict)
        channel_table = channel_table[["channel_id","channel_name","subscriberCount","videoCount","channel_Description","channel_status","viewCount"]]
        channel_table.to_sql('channel', con=cnx, if_exists='append', index=False)

        # for playlist table
        play_Table = pd.DataFrame(play_list)
        play_Table.to_sql('playlist', con=cnx, if_exists='append', index=False)

        # for video_table
        video_table = pd.DataFrame(vedio_cont)
        change_dic = {"view_count":int,"Likes_count":int,"Dislikes_count":int,"favorite_count":int,"Comment_count":int,"duration":int}
        video_table=video_table.astype(change_dic)
        published_date = video_table["published_data"].apply(lambda x:parser.parse(x))
        video_table["published_data"] = published_date
    
        video_table =video_table[["video_id","playlist_id","video_name","Description","published_data","view_count","Likes_count","Dislikes_count","favorite_count","Comment_count","duration"]]
        video_Table = video_table.drop_duplicates(subset="video_id")
        video_Table.to_sql('video', con=cnx, if_exists='append', index=False)

        # for comment table
        commnet_table = pd.DataFrame(video_comm)
        commnet_table = commnet_table[["comment_id","video_id","comment_text","comment_author","comment_published"]]
        commnet_table.to_sql('comment', con=cnx, if_exists='append', index=False)
    
        return "Data stored into the SQL Database "
    
    except  Exception as e:
        print(e)
        return st.warning(" Either connection or Uploading problem")
        

#data_to_sql(channel_data,play_list,vedio_cont,video_comm)