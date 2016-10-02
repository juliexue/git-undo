import unittest

from parser import Parser
from commands.commit import CommitCommand
from commands.unknown import UnknownCommand


class TestParser(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_get_command(self):
        cl = ['commit', '-m', "commit message"]
        command = Parser().get_command(cl)
        self.assertTrue(isinstance(command, CommitCommand))

        '''
        unknown = ['blah', '-v']
        unknown_command = Parser().get_command(cl)
        self.assertTrue(isinstance(unknown_command, UnknownCommand))
        '''

if __name__ == '__main__':
    unittest.main()
