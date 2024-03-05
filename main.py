import sys
from lexer import LexerClass
from parser import ParserClass


def main(argv):
    if len(argv) == 1:
        print("Usage: python main.py <filenames>")
        sys.exit(1)

    for filename in argv[1:]:
        with open(filename, 'r') as file:
            code = file.read()
            parser = ParserClass()
            parser.test(code)
            print("==========================================================")

if __name__ == "__main__":
    main(sys.argv)
