import gensim
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import numpy as np
import nltk
from youtube_transcript_api import YouTubeTranscriptApi

class LDA:
    """ Description of Service """
    from new_model import lemmatize_stemming,preprocess,dictionary,main
    import joblib
    lda_model = joblib.load(main())
        
    def retrieve_transcript(video_id):
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
    
    def get(self):      
        """ main method """
        
        try:
            
            bow_vector = dictionary.doc2bow(preprocess(retrieve_transcript(self.video_id)))

            output = {}
            for index, score in sorted(lda_model[bow_vector], key=lambda tup: -1 * tup[1]):
                for index, topic in lda_model.show_topics(formatted=False, num_words= 10):
                    word_list = [w[0] for w in topic]
                    output[index] = {
                        "score" : score,
                        "words" : word_list
                        }
                    print('Topic: {}\nScore:{} \nWords: {}\n'.format(index,score, [w[0] for w in topic]))  
            from pprint import pprint
            pprint(output,indent=3)
    
        
        except:    
            return {"Status":500,"error":"Some features of this video are disabled by youtube."}
   
    
