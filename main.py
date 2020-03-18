import sys
from charmap import CharMap

MIN_ARGS_NUM = 2

def main(argv):
    if len(argv) < (MIN_ARGS_NUM + 1):
        print("Please enter the {} arguments, and execute as:\n> python main.py arg1 arg2".format(MIN_ARGS_NUM))
    charmap = CharMap(argv[1])
    print(charmap.create_mapping(argv[2]))

if __name__ == '__main__':
    main(sys.argv)