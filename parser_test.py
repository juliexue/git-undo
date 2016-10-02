import unittest

from command_parser import CommandParser
from commands.commit import CommitCommand
from commands.unknown import UnknownCommand
from commands.switcher import get_command


class TestParser(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_get_command(self):
        cl = ['commit', '-m', "commit message"]
        command = get_command(cl)
        self.assertTrue(isinstance(command, CommitCommand))

        unknown = ['blah', '-v']
        unknown_command = get_command(unknown)
        self.assertTrue(isinstance(unknown_command, UnknownCommand))

if __name__ == '__main__':
    unittest.main()
