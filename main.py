import sys

from command_parser import CommandParser
from router import Router
from timeline import Timeline


def main():
    parser = CommandParser()
    try:
        command_list = parser.parse()
    except CommandParser.ParserException as e:
        sys.exit(e)

    router = Router(command_list)
    runner_class = router.get_runner()
    timeline = Timeline()
    runner_class(timeline).run(command_list)

if __name__ == '__main__':
    main()
