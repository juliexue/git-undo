import sys
from parser import Parser
from router import Router

def main():
    parser = Parser()
    try:
        command_list = parser.parse(sys.argv[1:])
    except Parser.ParserException as e:
        sys.exit(e)

    router = Router(command_list)
    runner = router.get_runner()

if __name__ == '__main__':
    main()
