class GitUndoException(Exception):

	def __init__(self, message):
		self.message = message

	def __str__(self):
		return 'Git Undo Exception: ' + self.message
