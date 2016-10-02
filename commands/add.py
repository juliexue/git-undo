import os
from command import Command
from mapping import Mapping


class AddCommand(Command):

    def __init__(self, command_list):
        self.command_list = command_list

    def undo_command(self):
        args = ' '.join(self.command_list[1:])
        mapping = Mapping.get_add_undo_mappings()
        if args in mapping:
            os.system(mapping[args])
        else:
            os.system('git reset HEAD ' + args)
