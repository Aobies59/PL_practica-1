import sys
from ajson_lexer import LexerClass
from ajson_parser import ParserClass


def main(argv):
    if len(argv) < 3:
        print("Usage: python main.py <0 - lexer | 1 - parser> <filename(s)>")
        sys.exit(1)

    elif (argv[1] != "0" and argv[1] != "1"):
        print("Usage: python main.py <0 - lexer | 1 - parser> <filename(s)>")
        sys.exit(1)

    elif len(argv) == 3:
        with open(argv[2], 'r') as file:
            code = file.read()
            if argv[1] == "0":
                lexer = LexerClass()
                lexer.test(code)
            else:
                parser = ParserClass(argv[1])
                parser.test(code)
            sys.exit(0)

    print("==========================================================")
    for filename in argv[2:]:
        if filename == "":
            continue  # skip empty filename (in case script is being called with run.sh)
        with open(filename, 'r') as file:
            code = file.read()
            if argv[1] == "0":
                print(f'Lexer output for file "{filename}":')
                lexer = LexerClass()
                lexer.test(code)
            else:
                parser = ParserClass(filename)
                parser.test(code)
        print("==========================================================")
    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv)
