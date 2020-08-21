import sys
from youtube_transcript_api import YouTubeTranscriptApi
import spacy
class Transcript:
	def __init__(self,video_id):
		""" Return transscript of the video """
		self.video_id = video_id
	# function to get lines
	def get_transcript(self,video_id):
		    try:
		        output = YouTubeTranscriptApi.get_transcript(video_id)
		        segments = []
		        for e in output:
		            line = e['text']
		            line = line.replace('\n', '')
		            line = line.replace('>', '')
		            line = line.replace('--', '')
		            line = line.replace('♪', '')
		            segments.append(line)
		        transcript = " ".join(segments)
		        return transcript
		    except:
		          print("An exception occurred")
		          return(None)
	# function to segment sentences using spacy library
	def spacy_segmentation(self,document):
	    nlp = spacy.load('en_core_web_lg')
	    doc = nlp(document)
	    seg_transcript = []
	    for sent in doc.sents:
	        seg_transcript.append(sent.text)
	    return seg_transcript
	def get_list(self):
	    video_transcript = self.get_transcript(self.video_id)
	    return self.spacy_segmentation(video_transcript)
