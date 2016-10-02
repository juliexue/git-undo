import unittest

from commands.commit import CommitCommand
from commands.unknown import UnknownCommand


class TestParser(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_get_command(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
