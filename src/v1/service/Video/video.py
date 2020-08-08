

class Video:
  """ Description of Service """
  
  def __init__(self, youtube_api_key: str, video_id: str):
    """ Description of Method """
    self.youtube_api_key = youtube_api_key
    self.video_id = video_id

  def get_details(self):
    """ thumbnails, title, channel name, view, time """

    search_response = self.youtube_api_key.videos().list(
        part='statistics, snippet',
        id=self.video_id
    ).execute()

    title = search_response['items'][0]['snippet']['title']
    thumbnails = search_response['items'][0]['snippet']['thumbnails']
    channelTitle = search_response['items'][0]['snippet']['channelTitle']
    publishedAt = search_response['items'][0]['snippet']['publishedAt'] 
    viewCount = search_response['items'][0]['statistics']['viewCount']
    channelVerified = None

    """
    TODO - 'channelVerified' field is not included in Youtube API
           can use BeautfulSoup to find by element: 
    
    url = "https://www.youtube.com/watch?v=" + video_id
    source = requests.get(url).text
    bs = BeautifulSoup(source, 'lxml')
    # need to figure out how to access the verified badge element
    """

    return {
      'title': title, 
      'thumbnails': thumbnails, 
      'meta': {
        'channelTitle': channelTitle, 
        'publishedAt': publishedAt, 
        'viewCount': viewCount,
        'channelVerified': channelVerified
      }
    }

  def get_description(self):
    """ Description of Method """
      
    search_response = self.youtube_api_key.videos().list(
        part='statistics, snippet',
        id=self.video_id
    ).execute()

    description = search_response['items'][0]['snippet']['description']

    return { 'description': description }


  def get_keywords(self):
    """ Description of Method """

    search_response = self.youtube_api_key.videos().list(
        part='statistics, snippet',
        id=self.video_id
    ).execute()

    keywords = search_response['items'][0]['snippet']['tags']

    return { 'keywords': keywords }
