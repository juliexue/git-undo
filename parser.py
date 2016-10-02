import argparse

from git_undo_exception import GitUndoException
from commands.commit import CommitCommand
from commands.unknown import UnknownCommand

class Parser:

    class ParserException(GitUndoException):
        pass

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description = ('Wrapper utility around Git to provide undo/redo functions.'),
        )

        self.parser.add_argument('command', nargs = argparse.REMAINDER)
        # TODO: Optional arguments we can pass in. Example: Dry-run

    def parse(self):
        command_list = vars(self.parser.parse_args())
        command_list = command_list['command']
        if len(command_list) == 0:
            raise Parser.ParserException('Command not supplied.')

        command = self.get_command(command_list)
        return command.fix_input_from_shell()

    def get_command(self, command_list):
        switcher = {
            "commit": CommitCommand(command_list),
        }
        return switcher.get(command_list[0], UnknownCommand(command_list))
