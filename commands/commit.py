from command import Command

class CommitCommand(Command):

    def __init__(self, command_list):
        self.command_list = command_list


    def fix_input_from_shell(self):
        for i, argument in enumerate(self.command_list):
            if argument == '-m':
                self.command_list[i+1] = '\"' + self.command_list[i+1] + '\"'
        return self.command_list