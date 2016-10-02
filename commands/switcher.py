from commands.commit import CommitCommand
from commands.unknown import UnknownCommand
from commands.add import AddCommand

def get_command(command_list):
    switcher = {
        "commit": CommitCommand(command_list),
        "add": AddCommand(command_list),
    }
    return switcher.get(command_list[0], UnknownCommand(command_list))
