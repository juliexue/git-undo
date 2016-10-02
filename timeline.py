import fileinput


class Timeline:
    PATHS = {
        "undo": '.git/undo.timeline',
        "redo": '.git/redo.timeline',
    }

    # Add the line to end of file
    def add(self, command_list):
        new_line = ' '.join(command_list) + '\n'
        with open(Timeline.PATHS.undo, 'a') as file:  # a = append mode
            file.write(new_line)

    # Return the last line of the file
    # Return None if file is not found or empty
    def get_last_line(self):
        line = None
        try:
            with open(Timeline.PATHS.undo, 'r') as file:
                for line in file:  # get last line
                    pass
        except IOError:  # no such file
            return None

        return line.rstrip() if line else None

    # Pop the last line from
    def pop_last_line(self):
        prev_line = None
        for line in fileinput.input(Timeline.PATHS.undo, inplace=True):
            if prev_line:
                print prev_line.rstrip()
            prev_line = line
