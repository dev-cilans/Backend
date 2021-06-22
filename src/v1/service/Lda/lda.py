import argparse
import gensim
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import numpy as np
import nltk
from youtube_transcript_api import YouTubeTranscriptApi
from model_updated import main as model
from model_updated import get_dictionary_processed_docs, preprocess
import joblib
from pprint import pprint
import warnings
warnings.filterwarnings("ignore")

class LDA:
        
        def __init__(self,video_id: str):
            self.video_id = video_id
        
        def retrieve_transcript(self,video_id):
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
        
        if __name__ == '__main__':
            def lda(self,transcript):
                lda_model = joblib.load(model())
                dictionary, _ = get_dictionary_processed_docs()
                bow_vector = dictionary.doc2bow(preprocess(transcript))

                output = {}
                for index, score in sorted(lda_model[bow_vector], key=lambda tup: -1 * tup[1]):
                    for index, topic in lda_model.show_topics(formatted=False, num_words=10):
                        word_list = [w[0] for w in topic]
                        output[index] = {
                            "score" : score,
                            "words" : word_list
                            }        
                        pprint(output,indent=3)
        
        def get(self):
            video_transcript = self.retrieve_transcript(video_id=self.video_id)
            lda = self.lda(video_transcript)
            return lda
