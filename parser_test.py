import unittest

from parser import Parser
from commands.commit import CommitCommand


class TestParser(unittest.TestCase):
    def setup(self):
        self.parser = Parser()

    def tearDown(self):
       pass 

    def test_get_command(self):
        cl = ['commit', '-m', "commit message"]
        command = self.parser.get_command(cl)
        self.assertTrue(type(command) is CommitCommand)

        unknown = ['blah', '-v']
        unknown_command = self.parser.get_command(cl)
        self.assertTrue(type(unknown_command) is UnknownCommand)

    if __name__ == '__main__':
        unittest.main()
