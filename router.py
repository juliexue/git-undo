from git_runner import GitRunner
from undo_runner import UndoRunner


class Router:
    def __init__(self, command_list):
        self.command_list = command_list

    def get_runner(self):
        # 0 because it is assumed that 'python main.py' will be aliased to git
        return UndoRunner if self.command_list[0] == 'undo' else GitRunner
