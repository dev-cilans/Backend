import argparse
import os
import json
import pandas as pd
import googleapiclient.discovery
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np
import nltk
from youtube_transcript_api import YouTubeTranscriptApi
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
            
    def retrieve_transcript(video_id):
        output = YouTubeTranscriptApi.get_transcript(video_id)
        segments = []
        for e in output:
            line = e['text']
            line = line.replace('\n', '')
            line = line.replace('>', '')
            line = line.replace('--', '')
            line = line.replace('♪', '')
            segments.append(line)
        return segments

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
    
    def transcript_scrapper(self,video_id):
                transcript=self.retrieve_transcript(video_id=self.video_id)
                df1 = pd.DataFrame()
                df1['Transcript'] =transcript
                df1['Sentiment'] = df1['Transcript'].apply(lambda x : sentiment_scores(x))
                return df1

    def get(self):
        
        df1 = self.transcript_scraper(video_id= self.video_id)
        neutral_trans = df1[df1['Sentiment'] == 'Neutral']['Transcript']
        negative_trans = df1[df1['Sentiment'] == 'Negative']['Transcript']
        positive_trans = df1[df1['Sentiment'] == 'Positive']['Transcript']

        b=len(neutral_trans)+len(negative_trans)+len(positive_trans)
        final_json1 = dict({"positive" : round(len(positive_trans)/b,3), "negative" : round(len(negative_trans)/b,3), "neutral" : round(len(neutral_trans)/b,3) })
        print("{\n\tTranscripts:")
        print(json.dumps(final_json1,indent=4),end="")
        print(",")        
        
        comment_df = self.comment_scraper(video_id= self.video_id,max_comments=self.max_num)
        neutral_comms = comment_df[comment_df['Sentiment'] == 'Neutral']['Comments']
        negative_comms = comment_df[comment_df['Sentiment'] == 'Negative']['Comments']
        positive_comments = comment_df[comment_df['Sentiment'] == 'Positive']['Comments']
        
        a=len(neutral_comms)+len(negative_comms)+len(positive_comments)
        final_json = dict({"positive" : round(len(positive_comments)/a,3), "negative" : round(len(negative_comms)/a,3), "neutral" : round(len(neutral_comms)/a,3) })
	    print("\tComments:")
        print(json.dumps(final_json,indent=4)) #The final json file which contains comments categorized into json/dict with positive,negative and neutral keys
        print("\n}")        
