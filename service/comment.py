from collections import defaultdict
import ast
from comment_downloader import *

# Scrapes the k top comments for a video specified by video_id
# Code from https://github.com/shahjaidev/NLP_Radicalization_detection/blob/master/get_and_parse_transcript_and_comments.py
def get_comments(video_id, kTopComments):
	d_main(video_id, "unparsed_comments.txt", kTopComments)
    # d_main downloads user comments for the passed video id up to 400 comments and stores them in unparsed_comments.txt
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
