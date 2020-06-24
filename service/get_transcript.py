import sys
import nltk
from youtube_transcript_api import YouTubeTranscriptApi

# Scrapes the transcript for a video specified by video_id
# Code from https://github.com/shahjaidev/NLP_Radicalization_detection/blob/master/get_and_parse_transcript_and_comments.py
def get_transcript(video_id):
	try:
		output = YouTubeTranscriptApi.get_transcript(video_id)
		l = []
		for e in output:
			l.append(e['text'])
		return(l)
	except:
  		# print("An exception occurred")
  		return(None)
