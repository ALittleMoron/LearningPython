import argparse, sys


def echo():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--time', action='store')
    parser.add_argument('-a', '--action', action='store')
    parser.add_argument('-s', '--stop', action='store')
    parser.add_argument('-f', '--finish', action='store')
    print(parser.parse_args())
    if parser.parse_args().time == '1':
        print('yes, it work')
    else:
        print('yes, it work too')
    # etc с другими аргументами

if __name__ == "__main__":
    echo()
