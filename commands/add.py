import os
from command import Command


class AddCommand(Command):

    mappings = {
        '.': 'git reset HEAD .'
    }

    def __init__(self, command_list):
        self.command_list = command_list

    def undo_command(self):
        args = ' '.join(self.command_list[1:])
        if args in AddCommand.mappings:
            os.system(mapping[args])
        else:
            os.system('git reset HEAD ' + args)
