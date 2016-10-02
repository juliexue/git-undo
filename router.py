from git_runner import GitRunner
from undo_runner import UndoRunner
from redo_runner import RedoRunner
from undo_state_runner import UndoStateRunner


class Router:
    def __init__(self, command_list):
        self.command_list = command_list

    def get_runner(self):
        # 0 because it is assumed that 'python main.py' will be aliased to git
        git_command_head = self.command_list[0]
        if git_command_head == 'undo':
            return UndoRunner
        if git_command_head == 'redo':
            return RedoRunner
        if git_command_head == 'undo-state':
            return UndoStateRunner
        return GitRunner
