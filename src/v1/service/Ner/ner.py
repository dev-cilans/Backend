# https://github.com/YouTubeNLP/NLP/tree/master/ner
from youtube_transcript_api import YouTubeTranscriptApi
import argparse
import spacy
from nerd import ner
      
class Ner:
	def __init__(self,video_id):
		self.video_id = video_id
	# function to get transcripts
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
	# function to apply ner using nerd library
	def nerd_ner(self,document):
	    doc = ner.name(document, language='en_core_web_sm')
	    results = [(ent.text, ent.label_) for ent in doc]
	    return results
	# main method
	def get_ner(self):
	    video_transcript = self.get_transcript(self.video_id)
	    ner_nerd = self.nerd_ner(video_transcript)
	    return ner_nerd
