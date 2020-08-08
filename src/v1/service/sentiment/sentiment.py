

class Sentiment:
	""" Description of Service """

	def __init__(self, video_id: str):
		""" Description of Method """
		self.video_id = video_id

	def get(self):
		""" Description of Method """
		return f'Sentiment get method result for {self.video_id}'
