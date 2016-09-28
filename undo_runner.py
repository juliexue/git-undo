import pexpect


class UndoRunner:

    def __init__(self, timeline):
        self._timeline = timeline

    def run(self, command_list):
        '''
            Use command_list for any flag var
        '''

        last_line = self._timeline.get_last_line()
        if not last_line:
            print 'No previous history :('
            return

        print 'The last supported command that ' + \
              'was executed is "{}"'.format(last_line)
        is_run = raw_input("Do you want to undo? ([y]/N) ")
        if is_run == '' or is_run.lower() == 'y':
            self._timeline.pop_last_line()
            print 'Done :)'

        # At this point, last_line = the line of the most recent command
        # Do something with it
