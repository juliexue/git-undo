from command import Command

class AddCommand(Command):

    def __init__(self, command_list):
        self.command_list = command_list

    def undo_command(self):
        dictionary = {
            '.': 'git reset HEAD .'
        }

        args = self.command_list[1:]
        if args in dictionary:
            os.system(dictionary[args])
        else:
            os.system('git reset HEAD ' + ' '.join(args))
