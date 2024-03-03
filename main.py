import sys
from lexer import LexerClass



def main(argv):
    if len(argv) != 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)

    filename = argv[1]
    with open(filename, 'r') as file:
        code = file.read()
        lexer = LexerClass()
        lexer.test(code)


if __name__ == "__main__":
    main(sys.argv)
