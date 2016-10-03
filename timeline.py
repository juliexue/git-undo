import fileinput


class Timeline:
    PATHS = {
        'undo': '.git/undo.timeline',
        'redo': '.git/redo.timeline',
    }

    # Add the line to end of file
    def add(self, command_list, path):
        new_line = ' '.join(command_list) + '\n'
        with open(path, 'a') as file:  # a = append mode
            file.write(new_line)

    def add_undo(self, command_list):
        self.add(command_list, Timeline.PATHS['undo'])
        with open(Timeline.PATHS['redo'], 'w') as file:  # w = write mode
            file.write('')

    def add_redo(self, command_list):
        self.add(command_list, Timeline.PATHS['redo'])

    # Return the last line of the file
    # Return None if file is not found or empty
    def get_last(self, path):
        line = None
        try:
            with open(path, 'r') as file:
                for line in file:  # get last line
                    pass
        except IOError:  # no such file
            return None

        return line.rstrip() if line else None

    def get_last_undo(self):
        return self.get_last(Timeline.PATHS['undo'])

    def get_last_redo(self):
        return self.get_last(Timeline.PATHS['redo'])

    # Pop the last line from
    def pop_last(self, path):
        prev_line = None
        for line in fileinput.input(path, inplace=True):
            if prev_line:
                print prev_line.rstrip()
            prev_line = line

    def pop_last_undo(self):
        last_line = self.get_last_undo()
        self.add_redo(last_line.split())
        self.pop_last(Timeline.PATHS['undo'])

    def pop_last_redo(self):
        self.pop_last(Timeline.PATHS['redo'])
