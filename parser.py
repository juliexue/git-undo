from argparse import ArgumentParser
from git_undo_exception import GitUndoException

class Parser:

	class ParserException(GitUndoException):
		pass

	def __init__(self):
		self.parser = ArgumentParser(
		    description=(
		    	'Wrapper utility around Git to provide undo/redo functions.'
		    ),
		)
		self.parser.add_argument('command', nargs='*')
		''' TODO: Optional arguments we can pass in:
			Example: Dry-run
		'''

	def parse(self, data):
		_dict = vars(self.parser.parse_args(data))
		command_list = _dict['command']
		if len(command_list) == 0:
			raise Parser.ParserException('Command not supplied.')
		else:
			return command_list
