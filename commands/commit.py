import os
from command import Command
from mapping import Mapping


class CommitCommand(Command):

    def __init__(self, command_list):
        self.command_list = command_list

    def fix_input_from_shell(self):
        for i, argument in enumerate(self.command_list):
            if argument == '-m' and i+1 < len(self.command_list):
                self.command_list[i+1] = '\"' + self.command_list[i+1] + '\"'
        return self.command_list

    def undo_command(self):
        args = self.command_list[1]
        os.system(Mapping.get_commit_undo_mappings().get(args, ''))
