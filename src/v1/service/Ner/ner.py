from youtube_transcript_api import YouTubeTranscriptApi
import argparse
import spacy
from nerd import ner
      
class Ner():
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
	# function to apply ner using spacy library
	def spacy_ner(self,document):
	    nlp = spacy.load("en_core_web_sm") 
	    doc = nlp(document)
	    results = [(ent.text, ent.label_) for ent in doc.ents]
	    return results
	# function to apply ner using nerd library
	def nerd_ner(self,document):
	    doc = ner.name(document, language='en_core_web_sm')
	    results = [(ent.text, ent.label_) for ent in doc]
	    return results
	# function to save transcript
	def save_file(self,document_name, transcript):
	    file_name = args['file'] + '-' + document_name +'.txt'
	    f = open(file_name, 'w+')
	    for line in transcript:
	        f.write(line + '\n')
	    f.close()
	# main method
	def get_ner(self):
	    video_transcript = self.get_transcript(self.video_id)	    
	    ner_spacy = self.spacy_ner(video_transcript)
	    ner_nerd = self.nerd_ner(video_transcript)
	    return ner_nerd
