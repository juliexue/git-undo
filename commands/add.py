import os
from command import Command


class AddCommand(Command):

    def __init__(self, command_list):
        self.command_list = command_list

    def undo_command(self):
        mappings = {
            '.': 'git reset HEAD .'
        }

        args = ' '.join(self.command_list[1:])
        if args in mappings:
            os.system(mapping[args])
        else:
            os.system('git reset HEAD ' + args)
