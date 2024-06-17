#La generación de código transforma el AST optimizado en código ejecutable (en este caso, evaluaremos directamente).

class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast
    
    def generate(self, node):
        if isinstance(node, tuple):
            if node[0] == 'number':
                return int(node[1])
            left = self.generate(node[1])
            right = self.generate(node[2])
            if node[0] == 'plus':
                return left + right
            elif node[0] == 'minus':
                return left - right
            elif node[0] == 'times':
                return left * right
            elif node[0] == 'divide':
                return left / right
        return node
