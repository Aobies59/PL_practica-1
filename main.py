import sys
from ajson_parser import ParserClass


def main(argv):
    if len(argv) == 1:
        print("Usage: python main.py <filenames>")
        sys.exit(1)

    elif len(argv) == 2:
        with open(argv[1], 'r') as file:
            code = file.read()
            parser = ParserClass(argv[1])
            parser.test(code)
            sys.exit(0)

    print("==========================================================")
    for filename in argv[1:]:
        if filename == "":
            continue  # skip empty filename (in case script is being called with run.sh)
        with open(filename, 'r') as file:
            code = file.read()
            parser = ParserClass(filename)
            parser.test(code)
        print("==========================================================")
    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv)
