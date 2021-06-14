import gensim
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import numpy as np
import nltk
from youtube_transcript_api import YouTubeTranscriptApi

class LDA:
    if __name__ == '__main__':
        from new_model import main,preprocess,dictionary,lemmatize_stemming
        import joblib
        global lda_model
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
        
        def lda(transcript):
            from new_model import preprocess,dictionary,lemmatize_stemming
            bow_vector = dictionary.doc2bow(preprocess(transcript))
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
        
        def get(self):
            video_transcript = self.retrieve_transcript(self.video_id)
            lda = self.lda(video_transcript)
            return lda
            

