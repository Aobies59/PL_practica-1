from ply import yacc
from ajson_lexer import LexerClass


class ParserClass:
    def __init__(self, filename):
        self.lexer = LexerClass()
        self.tokens = LexerClass.tokens
        self.parser = yacc.yacc(module=self)
        self.filename = filename

    def print_possible_list(self, element):
        if isinstance(element, list):
            for sub_element in element:
                self.print_possible_list(sub_element)
        else:
            print(element)

    def p_axiom(self, p):
        """axiom : OPEN_DELIMITER element CLOSE_DELIMITER
        | empty"""
        if len(p) == 4:
            p[0] = p[2]
            print(f'FICHERO AJSON "{self.filename}"')
            self.print_possible_list(p[0])
        else:
            p[0] = []
            print(f'FICHERO AJSON VACIO "{self.filename}"')

    def p_element(self, p):
        """element : stringvalue next_element
        | empty"""
        if len(p) == 3:
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1]

    def p_next_element(self, p):
        '''next_element : COMMA element
        | empty'''
        if len(p) == 3:
            p[0] = p[2]
        else:
            p[0] = p[1]

    def p_stringvalue(self, p):
        """stringvalue : string COLON value"""
        # check if value starts with a dot
        if isinstance(p[3], list):
            p[0] = []
            for element in p[3]:
                if element.startswith('.'):
                    p[0] += [f"{p[1]}{element.strip('"') if isinstance(element, str) else element}"]
                else:
                    p[0] += [f"{p[1]}: {element.strip('"') if isinstance(element, str) else element}"]
        else:
            p[0] = [f"{p[1]}: {p[3].strip('"') if isinstance(p[3], str) else p[3]}"]

    def p_string(self, p):
        """string : QUOTED_STRING
        | UNQUOTED_STRING"""
        p[0] = p[1].strip('"')

    def p_value(self, p):
        """value : number
        | QUOTED_STRING
        | BOOLEAN
        | operation
        | NULL
        | nested_element"""
        p[0] = p[1]

    def p_nested_element(self, p):
        'nested_element : OPEN_DELIMITER element CLOSE_DELIMITER'
        # If element is nested, add dot prefix for all sub-elements
        if isinstance(p[2], list):
            p[0] = [f".{sub_element}" for sub_element in p[2]]
        else:
            p[0] = [f".{p[2]}"]

    def p_number(self, p):
        """number : INT
        | FLOAT
        | BINARY
        | OCTAL
        | HEXADECIMAL"""
        p[0] = p[1]  # number can't be string, as it will be used to operate

    def p_operation(self, p):
        """operation : equal_operation
        | greater_operation
        | greater_or_equal_operation
        | less_operation
        | less_or_equal_operation"""
        p[0] = p[1]  # all operations are already strings

    def p_equal_operation(self, p):
        'equal_operation : number EQUAL number'
        p[0] = str(p[1] == p[3])

    def p_greater_operation(self, p):
        'greater_operation : number GREATER number'
        p[0] = str(p[1] > p[3])

    def p_greater_or_equal_operation(self, p):
        'greater_or_equal_operation : number GREATER_OR_EQUAL number'
        p[0] = str(p[1] >= p[3])

    def p_less_operation(self, p):
        'less_operation : number LESS number'
        p[0] = str(p[1] < p[3])

    def p_less_or_equal_operation(self, p):
        'less_or_equal_operation : number LESS_OR_EQUAL number'
        p[0] = str(p[1] <= p[3])

    def p_error(self, p):
        if p:
            print("Syntax error at '%s'" % p.value)
        else:
            print("Syntax error at EOF")

    def p_empty(self, p):
        'empty :'
        p[0] = []

    def test(self, string):
        self.parser.parse(string)
