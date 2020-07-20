from flask import Flask, make_response, request, jsonify
from service.comment import get_comments
from service.transcript import get_transcripts

app = Flask(__name__)

@app.route('/score/transcripts', methods=['POST'])
def transcripts():
	response = request.json
	video_id = response["videoID"]
	transcript_list = get_transcripts(video_id)
	return jsonify(results=transcript_list)

@app.route('/score/comments', methods=['POST'])
def comments():
	response = request.json
	video_id = response["videoID"]
	kTop = response["kTopComments"]
	comments_list = get_comments(video_id, kTop)
	return jsonify(results=comments_list)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
