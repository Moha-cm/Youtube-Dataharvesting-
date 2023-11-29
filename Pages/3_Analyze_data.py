from Database_connection import * 
import streamlit as st 
import plotly.subplots as sp
import plotly.express as px 
import pandas as pd 
import streamlit as st
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine, MetaData  

# ======================================== Setting the Page configuration ==================================================================
st.set_page_config(layout="wide",page_icon="")
st.title("📉 Youtube Data Analysis")

#Passing the query to get the data 
results  = get_all_Tables()
if results is None:
    pass
else:
    df = pd.DataFrame(results,columns=["channel_name","playlist_name","viewCount","videoCount","video_name","view_count","Likes_count","Comment_count","duration","published_data"])
    df["published_data"]=pd.DatetimeIndex(df["published_data"]).year
    
    #  side bar  to Channels
    st.sidebar.header("Filters Channels")
    Channels = st.sidebar.multiselect(
        label= "Filter Channels",
        options= df["channel_name"].unique(),
        default=df["channel_name"].unique()
        )

    # Side bar to playlists
    st.sidebar.header("Filters Playlist")
    Playlists = st.sidebar.multiselect(
        label= "Filter channels",
        options= df["playlist_name"].unique(),
        default= df["playlist_name"].unique()
        )


    # side bar to Year
    st.sidebar.header("Filters Year")
    Year = st.sidebar.multiselect(
        label= "Filter Year",
        options= df["published_data"].unique(),
        default= df["published_data"].unique()
        )
   
   
    # process query 
    df_selection = df.query(
        "channel_name==@Channels & published_data==@Year & playlist_name==@Playlists")
    #st.dataframe(df_selection)
    
    def Home():
        
        if df_selection is not None:
            channels =pd.DataFrame(df_selection["channel_name"].unique())
            channel_count = channels.count()
            playlist_count =pd.DataFrame(df_selection["playlist_name"].unique())
            playlist_count = playlist_count.count()
        
            Channel_vedio_count =pd.DataFrame(df_selection["videoCount"].unique())
            Channel_vedio_count = Channel_vedio_count.sum()
        
        
            col1,col2,col3 = st.columns(3)
            with col1:
                st.info("Channel Count")
                st.metric(value=channel_count,label="Count")
            with col2:
                st.info("playlist_count")
                st.metric(value=playlist_count,label="Count")
            with col3:
                st.info("Total vedio count ")
                st.metric(value=Channel_vedio_count,label="sum")
                
            with st.expander("Tabular"):
                showData = st.multiselect("Filter: ",df_selection.columns,default=["channel_name","playlist_name","viewCount","videoCount","video_name","view_count","Likes_count","Comment_count","duration","published_data"] )
                st.write(df_selection[showData])
        else:
            st.warning("Select the channels and playlists and year ")
    Home()

    left_column, right_column = st.columns(2)

    def graphs():
        if df_selection is not None:
            unique_channel_names = df_selection['channel_name'].unique()
            unique_video_counts = df_selection['videoCount'].unique()
        # Create a new DataFrame
            unique_values_df = pd.DataFrame({'channel_name': unique_channel_names, 'videoCount': unique_video_counts})
        
        # Pie Chart channel  and vediocount
            fig1 = px.pie(unique_values_df,names = "channel_name",values = "videoCount",hole=0.2, title  = "<b> Vedios in Each Channel <b>")
            fig1.update_layout(legend_title ="channel_name",legend_y = 0.9 )
            fig1.update_traces(textposition = "outside",textinfo =None)
            left_column.plotly_chart(fig1,use_container_width=True,height = 400)
        
        
            # bar plot for channel and vediocount 
            fig = px.bar(unique_values_df,x = "channel_name",y = "videoCount",
                    title  = "<b>Vedios in Each Channel<b>",
                    color_discrete_sequence = ["#0083B8"]*len(df_selection),
                    color = "videoCount",
                    template = "plotly_white")
            fig.update_layout( plot_bgcolor = "rgba(0,0,0,0)",
                    xaxis=(dict(showgrid=False))) 
            fig.update_traces(textposition = "outside")
            right_column.plotly_chart(fig,use_container_width=True,height =400)

        #  Pie plot for channel vs comment count

            div1,div2 = st.columns(2) 
            # pie chart
            fig = px.pie(df_selection, names='channel_name', values='Comment_count',
                    title="Total Comments in each channels")    
            div2.plotly_chart(fig,use_container_width=True,height = 400)
            
        # bar plot for channel and playlist count  
            channel_playlist_counts = df.groupby('channel_name')['playlist_name'].nunique().reset_index()
            channel_playlist_counts.columns = ['channel_name', 'playlist_count']   
            fig = px.bar(channel_playlist_counts,x = "channel_name",y = "playlist_count",
                    title  = "<b>Playlist in each Channel<b>",
                    color_discrete_sequence = ["#0083B8"]*len(df_selection),
                    color = "playlist_count",
                    template = "plotly_white")
            
            fig.update_layout( plot_bgcolor = "rgba(0,0,0,0)",
                    xaxis=(dict(showgrid=False))) 
            fig.update_traces(textposition = "outside")
            div1.plotly_chart(fig,use_container_width=True,height = 400)

        
        # Bar plot for channel vs vedio count
            
            fig = px.bar(df_selection,x ="channel_name",y = "viewCount",log_y=True, title  = "<b> Viewers count  in each Channel<b>",
                    color_discrete_sequence = ["#0083B8"]*len(df_selection),
                    color = "viewCount",
                    template = "plotly_white")
            
            fig.update_layout( plot_bgcolor = "rgba(0,0,0,0)",
                    xaxis=(dict(showgrid=False)))
            st.plotly_chart(fig,use_container_width=True,height = 400)
        
        # Bar plot for channels  vs likecount 
            df1 = df_selection[["channel_name","playlist_name","video_name","Likes_count"]]
            a = df1.groupby("channel_name")
            channel_likes = a["Likes_count"].sum()
            unique_values_df = pd.DataFrame({'channel_name':channel_likes.keys(), 'LikesCount': channel_likes.values})
            
            fig = px.bar( unique_values_df,x ="channel_name",y = "LikesCount", title  = "<b>Total Likes in the each Channel <b>",
                    color_discrete_sequence = ["#0083B8"]*len( unique_values_df),
                    color = "LikesCount",
                    template = "plotly_white")
            
            fig.update_layout( plot_bgcolor = "rgba(0,0,0,0)",
                    xaxis=(dict(showgrid=False)))
            st.plotly_chart(fig,use_container_width=True,height = 400)
            

            df1 = df_selection[["channel_name","playlist_name","video_name","Likes_count"]]
            a =df1.groupby("playlist_name")
            playlist_likes = a["Likes_count"].sum()
            unique_values_df1 = pd.DataFrame({'playlist_name':playlist_likes.keys(), 'LikesCount': playlist_likes.values})
        
            # Bar plot for the likes for playlists
            fig = px.bar( unique_values_df1,x ="playlist_name",y = "LikesCount", title  = "<b>Total Likes in the each  Playlist<b>",
                    color_discrete_sequence = ["#0083B8"]*len( unique_values_df1),
                    color = "LikesCount",
                    template = "plotly_white")
        
            fig.update_layout( plot_bgcolor = "rgba(0,0,0,0)",
                    xaxis=(dict(showgrid=False)))
            st.plotly_chart(fig,use_container_width=True,height = 400)
            
        
        
            fig = px.scatter(unique_values_df1,x = "playlist_name", y ="LikesCount",size="LikesCount",color = "playlist_name",title="Total Likes of each  playlist",
                            orientation="h")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        
        # bar plot for the average time for the vedios in the channel
            a = df_selection.groupby("channel_name")
            duration_df = a["duration"].mean()
            unique_values_df1 = pd.DataFrame({'channel_name':duration_df.keys(), 'Average_Duration': duration_df.values})
            
            fig = px.bar(unique_values_df1,x = "channel_name",y ="Average_Duration",color="Average_Duration",title="Average Time Duration of all vedios  in Sec ")
            
            st.plotly_chart(fig,use_container_width=True,height = 400)
        
    graphs()
    