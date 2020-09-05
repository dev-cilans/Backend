from youtube_transcript_api import YouTubeTranscriptApi
from nerd import ner


class Ner:
    """
    Description of Service
    The code is taken from: https://github.com/YouTubeNLP/NLP/tree/master/ner
    """

    def __init__(self, video_id):
        self.video_id = video_id

    def get_transcript(self, video_id):
        """ function to get transcripts """
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

    def nerd_ner(self, document):
        """ function to apply ner using nerd library """
        doc = ner.name(document, language="en_core_web_sm")
        results = [(ent.text, ent.label_) for ent in doc]
        return results

    def get_ner(self):
        """ main method """
        video_transcript = self.get_transcript(self.video_id)
        ner_nerd = self.nerd_ner(video_transcript)
        ners = {"video_id": self.video_id, "entity": []}
        ners_list = ner_nerd
        label_list = []
        j = 1
        for (_, label) in ners_list:
            Available = False
            for i in range(len(label_list)):
                if label == label_list[i]:
                    Available = True
                    break
            if not Available:
                label_list.append(label)
                ners["entity"].append({"label" + str(j): label, "text": []})
                j = j + 1
        for (text, label) in ners_list:
            label_num = 0
            for k in range(len(label_list)):
                if label_list[k] == label:
                    label_num = k + 1
                    break
            text_Available = False
            for a in range(len(ners["entity"][label_num - 1]["text"])):
                if text == ners["entity"][label_num - 1]["text"][a]:
                    text_Available = True
                    break
            if not text_Available:
                ners["entity"][label_num - 1]["text"].append(text)
        return ners
