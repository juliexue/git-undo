import os

from commands.add import AddCommand
from commands.commit import CommitCommand

class UndoRunner:

    def __init__(self, timeline):
        self.timeline = timeline

    def run(self, command_list):
        '''
            Use command_list for any flag var
        '''
        last_line = self.timeline.get_last_line()
        if not last_line:
            print 'No previous history :('
            return

        print 'The last supported command that ' + \
              'was executed is "{}"'.format(last_line)
        prompt_input = raw_input('Do you want to undo that command? ([y]/N) ')
        if prompt_input == '' or prompt_input.lower() == 'y':

            output = None

            command_list = last_line.split()
            if command_list[0] == 'add':
                AddCommand(command_list).undo_command()
            elif command_list[0] == 'commit':
                CommitCommand(command_list).undo_command()

            self.timeline.pop_last_line()
            print 'Done :)asdfasd'

        # At this point, last_line = the line of the most recent command
        # Do something with it
