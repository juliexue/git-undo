import pexpect


class GitRunner:

    def __init__(self, timeline):
        self._timeline = timeline

    def run(self, command_list):
        if command_list[0] == 'commit':
            self._timeline.add(command_list)

