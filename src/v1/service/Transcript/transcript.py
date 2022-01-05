from youtube_transcript_api import YouTubeTranscriptApi
import spacy


class Transcript:
    """
    Description of Service
    The code is taken from: https://github.com/YouTubeNLP/NLP/tree/master/segmentation
    """

    def __init__(self, video_id):
        """ Return transcript of the video """
        self.video_id = video_id

    def get_transcript(self, video_id):
        """ function to get lines """
        try:
            output = YouTubeTranscriptApi.get_transcript(video_id)
            segments = []
            for e in output:
                line = e["text"]
                line = line.replace("\n", "")
                line = line.replace(">", "")
                line = line.replace("--", "")
                line = line.replace("♪", "")
                segments.append(line)
                transcript = " ".join(segments)
            return transcript
        except:
            print("An exception occurred")
            return None

    def spacy_segmentation(self, document):
        """ function to segment sentences using spacy library """
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(document)
        seg_transcript = []
        for sent in doc.sents:
            seg_transcript.append(sent.text)
        return seg_transcript

    def get_list(self):
        """ main method """
        video_transcript = self.get_transcript(self.video_id)
        if video_transcript != None:
            return self.spacy_segmentation(video_transcript)
        else:
            return 'No Transcript found for this video'
