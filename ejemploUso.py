from analizadorLexico import Lexer
from analizadorSemantico import SemanticAnalyzer
from analizadorSintactico import Parser
from generadorCodigo import CodeGenerator
from optimizador import Optimizer


input_text = "3 + 5 * (2 - 8)"

# Fase 1: Análisis léxico
lexer = Lexer(input_text)
tokens = lexer.tokenize()
print("Fase 1: Analisis lexico")
print("Tokens:", tokens)

# Fase 2: Análisis sintáctico
parser = Parser(tokens)
ast = parser.parse()
print("Fase 2: Analisis sintactico")
print("AST:", ast)

# Fase 3: Análisis semántico
semantic_analyzer = SemanticAnalyzer(ast)
value = semantic_analyzer.visit(ast)
print("Fase 3: Analisis semantico")
print("Valor:", value)

# Fase 4: Optimización
optimizer = Optimizer(ast)
optimized_ast = optimizer.optimize(ast)
print("Fase 4: Optimizacion")
print("AST optimizado:", optimized_ast)

# Fase 5: Generación de código
code_generator = CodeGenerator(optimized_ast)
result = code_generator.generate(optimized_ast)
print("Fase 5: Generacion de codigo")
print("Resultado:", result)
