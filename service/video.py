



def get_details(video_id, youtube):
    search_response = youtube.videos().list(
        part="statistics, snippet",
        id=video_id
    ).execute()

    title = search_response['items'][0]['snippet']['title']
    thumbnails = search_response['items'][0]['snippet']['thumbnails']
    channelTitle = search_response['items'][0]['snippet']['channelTitle']
    publishedAt = search_response['items'][0]['snippet']['publishedAt'] 
    viewCount = search_response['items'][0]['statistics']['viewCount']

    """
    TODO - 'channelVerified' field is not included in Youtube API
           can use BeautfulSoup to find by element: 
    
    url = "https://www.youtube.com/watch?v=" + video_id
    source = requests.get(url).text
    bs = BeautifulSoup(source, 'lxml')
    # need to figure out how to access the verified badge element
    """

    #thumbnails, title, channel name, view, time"
    return { 'title': title, 
             'thumbnails': thumbnails, 
             'meta': {
                 'channelTitle': channelTitle, 
                 'publishedAt': publishedAt, 
                 'viewCount': viewCount 
              }
             }

def get_description(video_id, youtube):
    
    search_response = youtube.videos().list(
        part="statistics, snippet",
        id=video_id
    ).execute()

    description = search_response['items'][0]['snippet']['description']

    return {"description": description}


def get_keywords(video_id, youtube):

    search_response = youtube.videos().list(
        part="statistics, snippet",
        id=video_id
    ).execute()

    keywords = search_response['items'][0]['snippet']['tags']

    return {"keywords": keywords}

