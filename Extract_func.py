



def get_channel_data(youtube,channel_id):
    
    data_requested = []
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics,status",
        id=",".join(channel_id))
    
    response = request.execute()
    
    for i in range(len(response["items"])):
        
        data = dict(_id = response["items"][i]["id"],
                    channel_name = response["items"][i]["snippet"]["title"],
                    channel_id = response["items"][i]["id"],
                    subscriberCount = response["items"][i]["statistics"]["subscriberCount"],
                    videoCount= response["items"][i]["statistics"]["videoCount"],
                    channel_Description =  response["items"][i]["snippet"]["description"],
                    playlist_id = response["items"][i]["contentDetails"]["relatedPlaylists"]["uploads"],
                    channel_status = response["items"][i] ["status"]["privacyStatus"],
                    viewCount = response["items"][i]["statistics"]["viewCount"])
        
        data_requested.append(data)
        
        
                
    return data_requested
        
        
                
    return data_requested



# calling the function
#channel_data = get_channel_data(youtube,channel_id)
#channel_data



def get_playlist_info(youtube,channel_data):
    
    playlist = []
    a1=[]
    
    # looping through each list 
    for i in channel_data:
        # getting the playlist value using the key to get playlist id
        channelid = i["_id"]
        
        request = youtube.playlists().list(
            part="snippet,contentDetails",
            channelId=channelid,
            maxResults=50)   
        response = request.execute()
        
        playlist_ids = []
        for i in response["items"]:
            playlist_data = dict (  channel_id = i["snippet"]["channelId"],
                                  playlist_id =i["id"],
                                  playlist_name = i["snippet"]["title"],
                                )
            playlist_ids.append(playlist_data)
            #print(playlist_data)
            a1.append(playlist_data)
        
        playlist_data = dict(_id =channelid,playlists =playlist_ids)
        playlist.append(playlist_ids ) 
           
     
        
    
    return a1

#play_list = get_playlist_info(youtube,channel_data)



def playlist_video_list(youtube,channel_id):
    play_vedio = []
    
    for channel_ids in channel_id:
        playlist_request = youtube.playlists().list( part="snippet,contentDetails",channelId=channel_ids,maxResults=50)
        playlist_response=playlist_request.execute() 
        play_lists = []
 
        next_page_token = playlist_response.get("nextPageToken")
        Pages = True
        for ids in playlist_response["items"]:
            play_lists.append(ids["id"])
   
        
        while Pages:
            if next_page_token is None:
                Pages = False
            else:
                playlist_request = youtube.playlists().list( part="snippet,contentDetails",channelId=",".join(channel_id),maxResults=50)
                playlist_response=playlist_request.execute()
                for ids in playlist_response["items"]:
                    play_lists.append(ids["id"])
                    
                
                next_page_token = playlist_response.get("nextPageToken")
    
    # looping the playlist ids from the list 
    
        for playlist_IDS in play_lists:
            vedio_id_request = youtube.playlistItems().list(part = "snippet,contentDetails", playlistId= playlist_IDS,maxResults=50)
            vedio_id_response = vedio_id_request.execute()
            vedio_page_token = vedio_id_response.get("nextPageToken")
            vedio_Pages =True
            for i in vedio_id_response["items"]:
                data = dict(vedio_id = i["snippet"]["resourceId"]["videoId"],
                            playlist = i["snippet"]["playlistId"],
                            channel_id = i["snippet"]["channelId"])
                
                play_vedio.append(data)
        
           
            
  
        while vedio_Pages:
            if vedio_page_token is None:
                vedio_Pages = False
            else:
                vedio_id_request = youtube.playlistItems().list(part = "snippet,contentDetails", playlistId= playlist_IDS,maxResults=50)
                vedio_id_response = vedio_id_request.execute()
                for i in vedio_id_response["items"]:
                    data = dict(vedio_id = i["snippet"]["resourceId"]["videoId"],
                                playlist = i["snippet"]["playlistId"],
                                channel_id = i["snippet"]["channelId"])
                    play_vedio.append(data)
                vedio_page_token = vedio_id_response.get("nextPageToken")
        #print(play_lists)
    
    return play_vedio
                    
#out = playlist_vedio_list(youtube,channel_id)


def get_video_contents(youtube,out):
    import isodate
    vedio_contents = []
    a =[]
    for ids in out:
        playlist_id = ids.get("playlist")
        vedio_id = ids.get("vedio_id")
        channel_id =ids.get("channel_id")
        request = youtube.videos().list(part="snippet,statistics,contentDetails",id=vedio_id)
        response = request.execute()
        #print(response["items"])
        for i in range(len(response["items"])):
            channel_id = dict (Channel_id =  response["items"][i]["snippet"]["channelId"])
            c = response["items"][i]["snippet"]["channelId"]
            #print(c)
            L1 = []
            vedio_time = isodate.parse_duration(response["items"][i]["contentDetails"]["duration"])
            vedio_data = dict(Channel_id = response["items"][i]["snippet"]["channelId"],
                              video_id =response["items"][i]["id"],
                              playlist_id =  playlist_id,
                              video_name = response["items"][i]["snippet"]["title"],
                              published_data = response["items"][i]["snippet"]["publishedAt"],
                              view_count =  response["items"][i]["statistics"].get("viewCount",0),
                              Likes_count = response["items"][i]["statistics"].get("likeCount",0),
                              Dislikes_count = response["items"][i]["statistics"].get("dislikeCount",0),
                              favorite_count = response["items"][i]["statistics"].get("favoriteCount",0),
                              Comment_count = response["items"][i]["statistics"].get("commentCount",0),
                              duration =vedio_time.total_seconds(),
                               Description=response["items"][i]["snippet"]["description"])
            vedio_contents.append(vedio_data)
    #print(vedio_contents)
    return vedio_contents


#vedio_cont = vedio_contents(youtube,out)

def get_comments(youtube,out):
    comments = []
    for ids in out:
        vedio_id = ids.get("vedio_id")
        request = youtube.commentThreads().list(part="snippet,replies", videoId=vedio_id,maxResults=100)
        response = request.execute()
        for i in response["items"]:
            data = dict(channel_id = i['snippet']["channelId"],
                        comment_id = i['id'],
                        video_id = i['snippet']["videoId"],
                        comment_author= i['snippet']['topLevelComment']['snippet'].get('authorDisplayName',None),
                        comment_published =i['snippet']['topLevelComment']['snippet'].get("publishedAt",None),
                       comment_text  = i['snippet']['topLevelComment']['snippet'].get('textOriginal',None))
            comments.append(data) 
            #print(data)
    return comments    

#video_comm = get_comments(youtube,out)