from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = "AIzaSyC2gP7-BiIDFEEZ9nnRXdnKVAII5mmw2os"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_basic_info(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
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
    