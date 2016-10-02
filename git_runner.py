import os

class GitRunner:

    def __init__(self, timeline):
        self.timeline = timeline

    def run(self, command_list):
        if command_list[0] == 'commit' or command_list[0] == 'add':
            self.timeline.add(command_list)

        command_list.insert(0, 'git')
        os.system(' '.join(command_list))
