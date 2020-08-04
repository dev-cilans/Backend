from apiclient.errors import HttpError
from oauth2client.tools import argparser

def get_basic_info(video_id,youtube):
    # Call the videos.list method to retrieve results matching the specified query term.
    search_response = youtube.videos().list(
        part="statistics, snippet",
        id=video_id
    ).execute()

    title = search_response['items'][0]['snippet']['title']
    thumbnails = search_response['items'][0]['snippet']['thumbnails']
    channelTitle = search_response['items'][0]['snippet']['channelTitle']
    publishedAt = search_response['items'][0]['snippet']['publishedAt'] 
    viewCount = search_response['items'][0]['statistics']['viewCount']

    #thumbnails, title, channel name, view, time"
    return { 'title': title, 'thumbnails': thumbnails, 'channelTitle': channelTitle, 
                'publishedAt': publishedAt, 'viewCount': viewCount }
    