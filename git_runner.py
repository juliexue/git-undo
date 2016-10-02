import os

from commands.switcher import get_command


class GitRunner:

    def __init__(self, timeline):
        self.timeline = timeline

    def run(self, command_list):
        command = get_command(command_list)
        command.record(self.timeline)

        command_list.insert(0, 'git')
        os.system(' '.join(command_list))
