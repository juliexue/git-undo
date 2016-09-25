import sys
import pexpect

def main():
    if sys.argv[1] == 'git':
        args = sys.argv
        args.pop(0) # remove main.py
        args = ' '.join(args)
        output = pexpect.run(args)
    else:
        print 'not git'

if __name__ == '__main__':
    main()
