import os
import pexpect


class GitRunner:

    def __init__(self, timeline):
        self.timeline = timeline

    def run(self, command_list):
        if command_list[0] == 'commit':
            self.timeline.add(command_list)

        self.forward_command(command_list)

    def forward_command(self, command_list):
        command_list.insert(0, 'git')

        if len(command_list) == 2 and command_list[1] == 'commit':
            os.system(' '.join(command_list))
        else:
            output = pexpect.run(' '.join(command_list))
            if output:
                print output
