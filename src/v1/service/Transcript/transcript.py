import sys
import nltk
from youtube_transcript_api import YouTubeTranscriptApi


class Transcript:
	""" Description of Service """

	def __init__(self, video_id: str):
		""" Description of Method """
		self.video_id = video_id

	def get_list(self):
		# Code from https://github.com/shahjaidev/NLP_Radicalization_detection/blob/master/get_and_parse_transcript_and_comments.py
		""" Scrapes the transcript for a video specified by video_id """
		try:
			output = YouTubeTranscriptApi.get_transcript(self.video_id)
			l = []
			for e in output:
				l.append(e['text'])
			return(l)
		except:
	  		# print("An exception occurred")
	  		return(None)
