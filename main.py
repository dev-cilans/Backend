import sys
from fastapi import FastAPI,Request,Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from service.comment import get_comments
from service.transcript import get_transcripts
from service.basic_info import get_basic_info
from service.description import get_description
from service.keywords import get_keywords
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "https://youtubenlp.com",
    "http://localhost",
    "https://localhost",
    "http://localhost:8080",
    "https://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/score/transcripts/{video_id}')
def transcripts(video_id: str):
	transcript_list = jsonable_encoder(get_transcripts(video_id))
	return JSONResponse(content=transcript_list)

@app.get("/video/{video_id}")
def basic_info(video_id: str):
	basic_info_list = jsonable_encoder(get_basic_info(video_id))
	return JSONResponse(content=basic_info_list)

@app.get("/video/{video_id}/description")
def description(video_id: str):
	description_list = jsonable_encoder(get_description(video_id))
	return JSONResponse(content=description_list)

@app.get("/video/{video_id}/keywords")
def keywords(video_id: str):
	keywords_list = jsonable_encoder(get_keywords(video_id))
	return JSONResponse(content=keywords_list)
