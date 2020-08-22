from collections import defaultdict
import ast
from .comment_downloader import *
from googleapiclient.discovery import build

API_KEY = "AIzaSyDEyoZhTj3wh0B3r3evEmIxI-4g2Aa9-dE"
service = build('youtube', 'v3', developerKey=API_KEY)

class Comment:
	""" Description of Service """

	def __init__(self, video_id: str):
		""" Description of Method """
		self.video_id = video_id

	def get_list(self, kTopComments=100):
		# Code from https://github.com/shahjaidev/NLP_Radicalization_detection/blob/master/get_and_parse_transcript_and_comments.py
		""" Scrapes the k top comments for a video specified by video_id """

		d_main(self.video_id, 'unparsed_comments.txt', kTopComments)
	    # d_main downloads user comments for the passed video id up to 400 comments and stores them in unparsed_comments.txt
		f = open('unparsed_comments.txt')
		g = [line.strip("\n") for line in f ]
		if g == []:
			return None
		else:
			all_text= []
			for l in g:
				k = ast.literal_eval(l)
				all_text.append(k['text'])
			return(all_text)

	def build_initial_request(self, video_id):
		request = service.commentThreads().list(part="snippet", videoId=video_id)
		return request

	def parse_page(self, result, all_comments):
		for item in result['items']:
			# print(item['snippet']['topLevelComment']['snippet']['authorDisplayName'])
			# print('---')
			comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
			# print(comment_text)
			# print(item['snippet']['topLevelComment']['snippet']['textOriginal'])
			all_comments.append(comment_text)
			# print('====================')

	def parse_result(self, result, all_comments, video_id):
		# 50 comments only to avoid quotaExceeded error
		while result.get('nextPageToken', False) and len(all_comments) <= 50:
			self.parse_page(result, all_comments)
			request = service.commentThreads().list(
				part="snippet",
				videoId=video_id,
				pageToken=result.get('nextPageToken')
			)
			result = request.execute()

	def get_all_comments(self):
		# Build request and fetch comments
		all_comments = list()
		request = self.build_initial_request(self.video_id)
		result = request.execute()
		self.parse_result(result, all_comments, self.video_id)
		return all_comments
