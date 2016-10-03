import os


class UndoStateRunner:
    STRINGS = {
        'undo_reflog_command': 'git reset --hard $(git rev-parse --abbrev-ref HEAD)@{${1-1}};'
    }

    def __init__(self, timeline):
        self.timeline = timeline

    def run(self, command_list):
        os.system(UndoStateRunner.STRINGS['undo_reflog_command'])
