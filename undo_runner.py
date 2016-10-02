import os

from commands.add import AddCommand
from commands.commit import CommitCommand


class UndoRunner:
    strings = {
        'last_command': 'The last supported command that was executed is "{}"',
        'undo_check': 'Do you want to undo that command? ([y]/N) ',
        'no_commands': 'No git commands to undo!',
        'finished': 'Done!',
    }

    def __init__(self, timeline):
        self.timeline = timeline

    def run(self, command_list):
        # use command_list for any flag var
        last_line = self.timeline.get_last_line()

        if not last_line:
            print UndoRunner.strings['no_commands']
            return

        print UndoRunner.strings['last_command'].format(last_line)
        prompt_input = raw_input(UndoRunner.strings['undo_check'])
        if prompt_input == '' or prompt_input.lower() == 'y':

            command_list = last_line.split()
            if command_list[0] == 'add':
                AddCommand(command_list).undo_command()
            elif command_list[0] == 'commit':
                CommitCommand(command_list).undo_command()

            self.timeline.pop_last_line()
            print UndoRunner.strings['finished']

        # At this point, last_line = the line of the most recent command
        # Do something with it
