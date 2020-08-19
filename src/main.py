import sys

from fastapi import FastAPI,Request,Response, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from apiclient.discovery import build

from v1.service import Comment, Transcript, Video, Ner

app = FastAPI()

origins = [
    "https://youtubenlp.com",
    "http://localhost", "https://localhost",
    "http://localhost:80", "https://localhost:80",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DEVELOPER_KEY = "AIzaSyC2gP7-BiIDFEEZ9nnRXdnKVAII5mmw2os"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube_api_key = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

#Handles exceptions for invalid video_id
class VideoException(Exception):
    def __init__(self, video_id: str):
        self.video_id = video_id

@app.exception_handler(VideoException)
async def video_exception_handler(request: Request, exc: VideoException):
    return JSONResponse(
        status_code=400,
        content={
            'status': 400,
            'error': f'{exc.video_id} is an invalid video url'
        }
    )

@app.get("/video/{video_id}")
async def video_details(video_id: str):
    video = Video(youtube_api_key, video_id)
    try:
        details = jsonable_encoder(video.get_details())
    except:
        raise VideoException(video_id=video_id)
    return JSONResponse(content=details)

@app.get("/video/{video_id}/description")
async def video_description(video_id: str):
    video = Video(youtube_api_key, video_id)
    try:
        description = jsonable_encoder(video.get_description())
    except:
        raise VideoException(video_id=video_id)
    return JSONResponse(content=description)

@app.get("/video/{video_id}/keywords")
async def video_keywords(video_id: str):
    video = Video(youtube_api_key, video_id)
    try:
        keywords = jsonable_encoder(video.get_keywords())
    except:
        raise VideoException(video_id=video_id)
    return JSONResponse(content=keywords)

@app.get("/transcripts/{video_id}")
async def transcripts(video_id: str):
    transcript = Transcript(video_id)
    transcripts = jsonable_encoder(transcript.get_list())
    # wrong video_url is handled by get_list
    if transcripts is None:
        raise VideoException(video_id=video_id)
    return JSONResponse(content=transcripts)

@app.get("/sentiments/{video_id}/score")
async def sentiments(video_id: str):
	pass

@app.get("/sentiments/{video_id}")
async def sentiments_details(video_id: str):
	pass

@app.get("/comments​/{video_id}")
async def comments(video_id: str):
    comment = Comment(video_id)
    try:
        # TODO: fix comment service
        comments = jsonable_encoder(comment.get_list())
    except:
        raise VideoException(video_id=video_id)
    return JSONResponse(content=comments)

@app.get("/comments/{video_id}/controversial")
async def controversial(video_id: str):
	pass

@app.get("/emotions/{video_id}/score")
async def emotions(video_id: str):
	pass

@app.get("/ner/{video_id}")
async def ner(video_id: str):
    video_ner = Ner(video_id)
    try:
        Ner = jsonable_encoder(video_ner.get_ner())
    except:
        raise VideoException(video_id=video_id)
    return JSONResponse(content=Ner)

@app.get("/ner/{video_id}/targeted")
async def ner_targeted(video_id: str):
	pass

@app.get("/lda​/{video_id}")
async def lda(video_id: str):
	pass

@app.get("/world-cloud​/{video_id}")
async def worldcloud(video_id: str):
	pass

@app.get("/")
async def root(request: Request):

    """
    Returns an object with live endpoints details.
    
    To quickly look into the current live services from backend.

    Q. We already have /docs, /redoc, README.md and the swagger spec. So why is this required?
    A. /docs, /redoc, README.md and swagger spec contains the 'mock' spec and won't tell the 
       services which are live at the moment.
    """

    prod_generated_endpoint = "{base_url}docs".format(
        base_url=request.url)
    prod_testing_endpoint = "{base_url}redoc".format(
        base_url=request.url)
    dev_endpoint = "https://app.swaggerhub.com/apis-docs/youtubenlp/backend/0.0.1"

    transcripts_endpoint = "{base_url}transcripts/{{video_id}}".format(
        base_url=request.url)
    comments_endpoint = "{base_url}comments/{{video_id}}?q={{k_top_comments}}{{&type, order}}".format(
        base_url=request.url)
    details_endpoint = "{base_url}video/{{video_id}}".format(
        base_url=request.url)
    description_endpoint = "{base_url}video/{{video_id}}{{/description}}".format(
        base_url=request.url)
    keywords_endpoint = "{base_url}video/{{video_id}}{{/keywords}}".format(
        base_url=request.url)

    return {
        "api_specification": {
            "prod": {
                "description": "Returns generated Specification",
                "endpoint": [prod_generated_endpoint, prod_testing_endpoint]
            },
            "dev": {
                "description": "Returns standard API refrence",
                "endpoint": dev_endpoint
            }
        },
        "transcript_service": {
            "description": "Returns list of transcripts from video",
            "endpoint": transcripts_endpoint
        },
        "comment_service": {
            "description": "Returns list of comments from video",
            "endpoint": comments_endpoint
        },
        "video_service": {
            "description": "Returns various video information",
            "details": {
                "description": "Returns various detials related to video",
                "endpoint": details_endpoint
            },
            "description": {
                "description": "Returns the description text of the video",
                "endpoint": description_endpoint
            },
            "keywords": {
                "description": "Returns a list of keywords related to video",
                "endpoint": keywords_endpoint
            }
        }
    }

