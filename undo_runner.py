import os

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

            array = last_line.split()
            if array[0] == 'add' and array[1] == '.':
                os.system('git reset HEAD .')
            elif array[0] == 'add':
                os.system('git reset HEAD ' + ' '.join(array[1:]))
            elif array[0] == 'commit' and array[1] == '-m':
                os.system('git reset HEAD~1 --soft')
            elif array[0] == 'commit' and array[1] == '-am':
                os.system('git reset HEAD~1')

            self.timeline.pop_last_line()
            print 'Done :)'

        # At this point, last_line = the line of the most recent command
        # Do something with it
