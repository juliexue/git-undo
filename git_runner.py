import pexpect


class GitRunner:

    def __init__(self, timeline):
        self.timeline = timeline

    def run(self, command_list):
        if command_list[0] == 'commit':
            self.timeline.add(command_list)

