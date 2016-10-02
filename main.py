import sys

from parser import Parser
from router import Router
from timeline import Timeline


def main():
    parser = Parser()
    try:
        command_list = parser.parse()
    except Parser.ParserException as e:
        sys.exit(e)

    router = Router(command_list)
    runner_class = router.get_runner()
    timeline = Timeline()
    runner_class(timeline).run(command_list)

if __name__ == '__main__':
    main()
