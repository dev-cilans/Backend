import sys
from fastapi import FastAPI,Request,Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from service.comment import get_comments
from service.transcript import get_transcripts
#from service.basic_info import *
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
	videoID: str
	kTopComments: int

@app.post('/score/transcripts')
def transcripts(item : Item):
	video_id = item.videoID
	transcript_list = jsonable_encoder(get_transcripts(video_id))
	return JSONResponse(content=transcript_list)

@app.post('/score/comments')
def comments(item : Item):
	video_id = item.videoID
	kTop = item.kTopComments
	comments_list = get_comments(video_id, kTop)
	return JSONResponse(content=comments_list)


@app.get("/video/{video_id}")
def basic_info(video_id : str):
	video_id = item.videoID
	basic_info = get_basic_info(video_id)
	return JSONResponse(content=basic_info)

@app.get("/video/{video_id}/description")
def description(video_id: str):
	video_id = item.videoID
	description = get_description(video_id)
	return JSONResponse(content=description)

@app.get("/video/{video_id}/keywords")
def keywords(video_id: str):
	video_id = item.videoID
	keywords = get_keywords(video_id)
	return JSONResponse(content=keywords)
	