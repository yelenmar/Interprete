#El analizador semántico verifica la semántica de las estructuras sintácticas generadas por el parser.

class SemanticAnalyzer:
    def __init__(self, ast):
        self.ast = ast
    
    def visit(self, node):
        if isinstance(node, tuple):
            if node[0] == 'number':
                return int(node[1])
            elif node[0] in ('plus', 'minus', 'times', 'divide'):
                left = self.visit(node[1])
                right = self.visit(node[2])
                if node[0] == 'plus':
                    return left + right
                elif node[0] == 'minus':
                    return left - right
                elif node[0] == 'times':
                    return left * right
                elif node[0] == 'divide':
                    return left / right
        return node
