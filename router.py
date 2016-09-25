from git_runner import GitRunner
from undo_runner import UndoRunner

class Router:
	def __init__(self, command):
		self.command = command

	def get_runner(self):
		return UndoRunner if self.command[1] == 'undo' else GitRunner
