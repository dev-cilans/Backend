from apiclient.errors import HttpError
from oauth2client.tools import argparser


def get_description(video_id,youtube):
    # Call the videos.list method to retrieve results matching the specified query term.
    search_response = youtube.videos().list(
        part="statistics, snippet",
        id=video_id
    ).execute()

    description = search_response['items'][0]['snippet']['description']

    return {"description": description}
