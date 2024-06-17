#El optimizador intenta mejorar el rendimiento del código (en este caso, simplificaremos).

class Optimizer:
    def __init__(self, ast):
        self.ast = ast
    
    def optimize(self, node):
        if isinstance(node, tuple):
            if node[0] == 'number':
                return node
            left = self.optimize(node[1])
            right = self.optimize(node[2])
            if left[0] == 'number' and right[0] == 'number':
                if node[0] == 'plus':
                    return ('number', str(int(left[1]) + int(right[1])))
                elif node[0] == 'minus':
                    return ('number', str(int(left[1]) - int(right[1])))
                elif node[0] == 'times':
                    return ('number', str(int(left[1]) * int(right[1])))
                elif node[0] == 'divide':
                    return ('number', str(int(left[1]) / int(right[1])))
            return (node[0], left, right)
        return node
