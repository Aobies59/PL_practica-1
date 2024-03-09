import ply.lex as lex


class LexerClass:

    def __init__(self):
        self.lexer = lex.lex(module=self)

    reserved = {
    "NULL": "NULL",
    "null": "NULL",
    "TR": "BOOLEAN",
    "tr": "BOOLEAN",
    "FL": "BOOLEAN",
    "fl": "BOOLEAN"
    }

    tokens = [
        'INT',
        'FLOAT',
        'BINARY',
        'OCTAL',
        'HEXADECIMAL',
        'UNQUOTED_STRING',
        'QUOTED_STRING',
        'EQUAL',
        'GREATER',
        'GREATER_OR_EQUAL',
        'LESS',
        'LESS_OR_EQUAL',
        'OPEN_DELIMITER',
        'CLOSE_DELIMITER',
        'COLON',
        'COMMA',
        'BOOLEAN',
        'NULL'
    ]

    def t_reserved(self, t):
        r'(NULL|null|TR|tr|FL|fl)\b'
        t.type = self.reserved.get(t.value)
        return t

    def t_FLOAT(self, t):
        r'-?((\d+|\d*\.\d+)(e|E)(-?\d+)|(\d+\.\d+))'
        t.value = float(t.value)
        return t

    def t_BINARY(self, t):
        r'0b[01]+'
        t.value = int(t.value, 2)
        return t

    def t_OCTAL(self, t):
        r'0[0-7]+'
        t.value = int(t.value, 8)
        return t

    def t_HEXADECIMAL(self, t):
        r'(0x|0X)[0-9a-fA-F]+'
        t.value = int(t.value, 16)
        return t

    def t_INT(self, t):
        r'-?\d+'
        t.value = int(t.value)
        return t

    def t_UNQUOTED_STRING(self, t):
        r'(?!TR|tr|FL|fl|NULL|null\b)([a-zA-Z]|_)\w*'
        return t

    def t_QUOTED_STRING(self, t):
        r'"[^"\n\r]*"'
        return t

    def t_EQUAL(self, t):
        r'=='
        return t

    def t_GREATER(self, t):
        r'>'
        return t

    def t_GREATER_OR_EQUAL(self, t):
        r'>='
        return t

    def t_LESS(self, t):
        r'<'
        return t

    def t_LESS_OR_EQUAL(self, t):
        r'<='
        return t

    def t_OPEN_DELIMITER(self, t):
        r'\{'
        return t

    def t_CLOSE_DELIMITER(self, t):
        r'\}'
        return t

    def t_COLON(self, t):
        r':'
        return t

    def t_COMMA(self, t):
        r','
        return t

    t_ignore = ' \t'

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count('\n')

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def test(self, string):
        self.lexer.input(string)
        for token in self.lexer:
            print(token.type, token.value)
        return self.lexer
