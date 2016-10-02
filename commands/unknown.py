from command import Command


class UnknownCommand(Command):

    def __init__(self, command_list):
        self.command_list = command_list
