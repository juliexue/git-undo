from git_runner import GitRunner
from undo_runner import UndoRunner
from redo_runner import RedoRunner


class Router:
    def __init__(self, command_list):
        self.command_list = command_list

    def get_runner(self):
        # 0 because it is assumed that 'python main.py' will be aliased to git
        if self.command_list[0] == 'undo':
            return UndoRunner
        if self.command_list[0] == 'redo':
            return RedoRunner
        return GitRunner
