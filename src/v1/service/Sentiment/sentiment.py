import argparse
import os
import json
import pandas as pd
import googleapiclient.discovery
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
class Sentiment:
    """ Description of Service """

    def __init__(self, video_id: str,max_num,youtube_obj):
        self.video_id = video_id
        self.max_num = max_num
        self.youtube=youtube_obj
    #Function to classify a sentence into one of the 3 sentiments : Positive, Negative or Neutral
    def sentiment_scores(self,sentence):
            snt = analyser.polarity_scores(sentence)
            if snt['compound'] >= 0.05:
                return 'Positive'
            elif snt['compound'] <= -0.05:
                return 'Negative'
            else:
                return 'Neutral'
    #Function takes in JSON response from Youtube V3 api and extracts comment text,likes and replies 
    def json_parser(self,json_response):
                comments = []
                likes = []
                replies = []
                for item in json_response.get('items'):
                    comments.append(item.get('snippet').get('topLevelComment').get('snippet')['textOriginal'])
                    likes.append(item.get('snippet').get('topLevelComment').get('snippet')['likeCount'])    
                    replies.append(item.get('snippet')['totalReplyCount'])
                assert len(comments) == len(likes) == len(replies),'Length not matching'
                df = pd.DataFrame()
                df['Comments'] = comments
                df['Likes'] = likes
                df['Replies'] = replies
                return df
    #Function to scrape comments, their number likes and number replies using YouTube V3 API - NEEDS DEVELOPER_KEY
    def comment_scraper(self,video_id,max_comments):
                # Disable OAuthlib's HTTPS verification when running locally.
                # *DO NOT* leave this option enabled in production.
                os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
                request = self.youtube.commentThreads().list(
                        part="snippet,replies",
                        maxResults=max_comments,
                        order="relevance",
                        videoId=video_id)
                response = request.execute()
                comment_df = self.json_parser(response)
                comment_df['Sentiment'] = comment_df['Comments'].apply(lambda x : self.sentiment_scores(x))
                return comment_df
    def get(self):
        comment_df = self.comment_scraper(video_id= self.video_id,max_comments=self.max_num)
        neutral_comms = comment_df[comment_df['Sentiment'] == 'Neutral']['Comments']
        negative_comms = comment_df[comment_df['Sentiment'] == 'Negative']['Comments']
        positive_comments = comment_df[comment_df['Sentiment'] == 'Positive']['Comments']
        final_json = dict({"positive" : positive_comments.tolist(), "negative" : negative_comms.tolist(), "neutral" : neutral_comms.tolist() })
        return final_json
