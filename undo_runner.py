import os

from commands.switcher import get_command


class UndoRunner:
    STRINGS = {
        'last_command': 'The last supported command that was executed is "{}"',
        'undo_check': 'Do you want to undo that command? ([y]/N) ',
        'no_commands': 'No git commands to undo!',
        'finished': 'Done!',
    }

    def __init__(self, timeline):
        self.timeline = timeline

    def run(self, command_list):
        # use command_list for any flag var
        last_line = self.timeline.get_last_undo()

        if not last_line:
            print UndoRunner.STRINGS['no_commands']
            return

        print UndoRunner.STRINGS['last_command'].format(last_line)
        prompt_input = raw_input(UndoRunner.STRINGS['undo_check'])

        if prompt_input == '' or prompt_input.lower() == 'y':
            command_list = last_line.split()
            command = get_command(command_list)
            command.redo_command()

            self.timeline.pop_last_undo()
            print UndoRunner.STRINGS['finished']
