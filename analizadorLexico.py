#El analizador léxico (o lexer) convierte una secuencia de caracteres en una secuencia de tokens.

import re

class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.tokens = []
        self.current_position = 0
        self.token_exprs = [
            (r'[ \n\t]+', None),  # whitespace
            (r'\d+', 'NUMBER'),
            (r'\+', 'PLUS'),
            (r'\-', 'MINUS'),
            (r'\*', 'TIMES'),
            (r'\/', 'DIVIDE'),
            (r'\(', 'LPAREN'),
            (r'\)', 'RPAREN')
        ]
    
    def tokenize(self):
        while self.current_position < len(self.input_text):
            match = None
            for token_expr in self.token_exprs:
                pattern, tag = token_expr
                regex = re.compile(pattern)
                match = regex.match(self.input_text, self.current_position)
                if match:
                    text = match.group(0)
                    if tag:
                        token = (tag, text)
                        self.tokens.append(token)
                    break
            if not match:
                raise SyntaxError(f'Unexpected character: {self.input_text[self.current_position]}')
            else:
                self.current_position = match.end(0)
        return self.tokens
