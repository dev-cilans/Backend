from flask import Flask, make_response, request, jsonify
import sys
import nltk
from youtube_transcript_api import YouTubeTranscriptApi

from collections import defaultdict
import ast
from comment_downloader import *

app = Flask(__name__)

def get_comments(video_id, kTopComments):
	d_main(video_id, "unparsed_comments.txt", kTopComments)
    # d_main downloads user comments for the passed video id upto 400 comments and stores them in unparsed_comments.txt
	f = open("unparsed_comments.txt")
	g = [line.strip("\n") for line in f ]
	if g == []:
		return None
	else:
		all_text= []
		for l in g:
			k = ast.literal_eval(l)
			all_text.append(k["text"])
		return(all_text)

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

@app.route('/score/transcript', methods=['POST'])
def transcript():
	response = request.json
	video_id = response["videoID"]
	transcript_list = get_transcript(video_id)
	return jsonify(results = transcript_list)

@app.route('/score/comments', methods=['POST'])
def comments():
	response = request.json
	video_id = response["videoID"]
	kTop = response["kTopComments"]
	comments_list = get_comments(video_id, kTop)
	return jsonify(results = comments_list)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
