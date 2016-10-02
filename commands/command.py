class Command:

    def __init__(self, command_list):
        self.command_list = command_list

    def fix_input_from_shell(self):
        return self.command_list

    def undo_command(self):
        pass

    def redo_command(self):
        pass

    def record(self, timeline):
        pass
