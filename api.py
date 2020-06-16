from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/score', methods=['POST'])
def score():
	response = request.json
	return make_response(response)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)

