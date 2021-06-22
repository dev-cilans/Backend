import argparse
import os
import json
import pandas as pd
import googleapiclient.discovery
import numpy as np
import nltk
from pprint import pprint
from youtube_transcript_api import YouTubeTranscriptApi
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()


class Sentiment:
    """ Description of Service """

    def __init__(self, video_id: str, max_num, youtube_obj):
        self.video_id = video_id
        self.max_num = max_num
        self.youtube = youtube_obj
    # Function to classify a sentence into one of the 3 sentiments : Positive, Negative or Neutral

    def sentiment_scores(self, sentence):
        snt = analyser.polarity_scores(sentence)
        if snt['compound'] >= 0.05:
            return 'Positive'
        elif snt['compound'] <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'
    # Function takes in JSON response from Youtube V3 api and extracts comment text,likes and replies

    def json_parser(self, json_response):
        comments = []
        likes = []
        replies = []
        for item in json_response.get('items'):
            comments.append(item.get('snippet').get(
                'topLevelComment').get('snippet')['textOriginal'])
            likes.append(item.get('snippet').get(
                'topLevelComment').get('snippet')['likeCount'])
            replies.append(item.get('snippet')['totalReplyCount'])
        assert len(comments) == len(likes) == len(
            replies), 'Length not matching'
        df = pd.DataFrame()
        df['Comments'] = comments
        df['Likes'] = likes
        df['Replies'] = replies
        return df
    # Function to scrape comments, their number likes and number replies using YouTube V3 API - NEEDS DEVELOPER_KEY

    def comment_scraper(self, video_id, max_comments):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = os.environ["API_KEY"]
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=DEVELOPER_KEY)

        request = self.youtube.commentThreads().list(
            part="snippet,replies",
            maxResults=max_comments,
            order="relevance",
            videoId=video_id)
        response = request.execute()
        comment_df = self.json_parser(response)
        comment_df['Sentiment'] = comment_df['Comments'].apply(
            lambda x: self.sentiment_scores(x))
        return comment_df

    def get(self):
        comment_df = self.comment_scraper(
            video_id=self.video_id, max_comments=self.max_num)
        neutral_comms = comment_df[comment_df['Sentiment']
                                   == 'Neutral']['Comments']
        negative_comms = comment_df[comment_df['Sentiment']
                                    == 'Negative']['Comments']
        positive_comments = comment_df[comment_df['Sentiment']
                                       == 'Positive']['Comments']
        final_json = dict({"positive": positive_comments.tolist(
        ), "negative": negative_comms.tolist(), "neutral": neutral_comms.tolist()})
        return final_json

    def retrieve_transcript(self, video_id):
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

    def retrieve_transcript(self, video_id):
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

    def transcript_scrapper(self, video_id):
        transcript = self.retrieve_transcript(video_id=self.video_id)
        transcript_df = pd.DataFrame()
        transcript_df['Transcript'] = transcript
        transcript_df['Sentiment'] = transcript_df['Transcript'].apply(
            lambda x: self.sentiment_scores(x))
        return transcript_df

    def get_aggregate_analysis(self):

        transcript_df = self.transcript_scrapper(video_id=self.video_id)
        neutral_trans = transcript_df[transcript_df['Sentiment']
                                      == 'Neutral']['Transcript']
        negative_trans = transcript_df[transcript_df['Sentiment']
                                       == 'Negative']['Transcript']
        positive_trans = transcript_df[transcript_df['Sentiment']
                                       == 'Positive']['Transcript']

        trans_len = len(neutral_trans)+len(negative_trans)+len(positive_trans)
        final_json_trans = dict({"positive": round(len(positive_trans)/trans_len, 3), "negative": round(
            len(negative_trans)/trans_len, 3), "neutral": round(len(neutral_trans)/trans_len, 3)})

        comment_df = self.comment_scraper(
            video_id=self.video_id, max_comments=self.max_num)
        neutral_comms = comment_df[comment_df['Sentiment']
                                   == 'Neutral']['Comments']
        negative_comms = comment_df[comment_df['Sentiment']
                                    == 'Negative']['Comments']
        positive_comments = comment_df[comment_df['Sentiment']
                                       == 'Positive']['Comments']

        comms_len = len(neutral_comms)+len(negative_comms) + \
            len(positive_comments)
        final_json_comms = dict({"positive": round(len(positive_comments)/comms_len, 3), "negative": round(
            len(negative_comms)/comms_len, 3), "neutral": round(len(neutral_comms)/comms_len, 3)})
        output = {
            "Transcript": {},
            "Comments": {}
        }
        output["Transcript"] = final_json_trans
        output["Comments"] = final_json_comms
        return output
