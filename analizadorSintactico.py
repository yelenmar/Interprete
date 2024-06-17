#El analizador sintáctico (o parser) convierte la secuencia de tokens en una estructura de datos sintáctica, como un árbol de sintaxis abstracta (AST).

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        self.current_token = self.tokens[self.current_token_index]
    
    def eat(self, token_type):
        if self.current_token[0] == token_type:
            self.current_token_index += 1
            if self.current_token_index < len(self.tokens):
                self.current_token = self.tokens[self.current_token_index]
        else:
            raise SyntaxError(f'Unexpected token: {self.current_token}')
    
    def factor(self):
        token = self.current_token
        if token[0] == 'NUMBER':
            self.eat('NUMBER')
            return ('number', token[1])
        elif token[0] == 'LPAREN':
            self.eat('LPAREN')
            expr = self.expr()
            self.eat('RPAREN')
            return expr
    
    def term(self):
        node = self.factor()
        while self.current_token[0] in ('TIMES', 'DIVIDE'):
            token = self.current_token
            if token[0] == 'TIMES':
                self.eat('TIMES')
            elif token[0] == 'DIVIDE':
                self.eat('DIVIDE')
            node = (token[0].lower(), node, self.factor())
        return node
    
    def expr(self):
        node = self.term()
        while self.current_token[0] in ('PLUS', 'MINUS'):
            token = self.current_token
            if token[0] == 'PLUS':
                self.eat('PLUS')
            elif token[0] == 'MINUS':
                self.eat('MINUS')
            node = (token[0].lower(), node, self.term())
        return node
    
    def parse(self):
        return self.expr()
