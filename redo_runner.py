import os

from commands.switcher import get_command


class RedoRunner:
    STRINGS = {
        'last_command': 'The last command that was undone is "{}"',
        'redo_check': 'Do you want to undo that command? ([y]/N) ',
        'no_commands': 'No git commands to redo!',
    }

    def __init__(self, timeline):
        self.timeline = timeline

    def run(self, command_list):
        last_line = self.timeline.get_last_redo()

        if not last_line:
            print RedoRunner.STRINGS['no_commands']
            return

        print RedoRunner.STRINGS['last_command'].format(last_line)
        prompt_input = raw_input(RedoRunner.STRINGS['redo_check'])

        if prompt_input == '' or prompt_input.lower() == 'y':
            command_list = last_line.split()
            command = get_command(command_list)
            command.redo_command()

            self.timeline.pop_last_undo()
            print RedoRunner.STRINGS['finished']
