from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
import argparse


def get_transcript(video_url):
    '''
    function to get transcripts

    parameters: 
    video_url(string)=this is url of the video for which we want the transcript

    returns:
    result(string)= transcript of the url in required format

    '''

    video_id = video_url.split("=")[1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    result =""
    for i in transcript:
        result += ' ' + i['text']
    return result


def get_summarization(result):
    '''
    function to get summarization of video

    parameters: 
    result(string)=transcript of the url in required format

    returns:
    summarization(string)= summary of the video

    '''
    summarizer = pipeline('summarization', model="t5-3b", tokenizer="t5-3b", framework="tf")
    num_iters = int(len(result)/1000)
    summarized_text = []
    for i in range(0, num_iters + 1):
        start = 0
        start = i * 1000
        end = (i + 1) * 1000
        out = summarizer(result[start:end])
        out = out[0]
        out = out['summary_text']
        summarized_text.append(out)
    return " ".join(summarized_text)

if __name__=="__main__": 
    ap = argparse.ArgumentParser()
    ap.add_argument("id", type = str, help = "Video ID for YouTube video.")
    ap.add_argument("-s", "--file", help = "Summary of the video", action="store_true")
    args = vars(ap.parse_args())
    
    
    if args['id']:
        print("Video Id is:",args['id'])
        video_id = args['id']
        video_url="https://www.youtube.com/watch?v="+args['id']
        video_transcript=get_transcript(video_url)
        if args['file']:
            summ=get_summarization(video_transcript)
            print(summ)
    else:
        print("ERROR: No Id provided")

