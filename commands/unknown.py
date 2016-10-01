from command import Command

class UnknownCommand(Command):

    def __init__(self, command_list):
        self.command_list = command_list


    def fix_input_from_shell(self):
        return self.command_list
