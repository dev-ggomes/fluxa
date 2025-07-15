from lexer import Lexer
from parser import Parser

code = '''
let nome = "Fluxa"
let idade = 18
print(nome + idade)
'''

# Etapa 1: Lexer
lexer = Lexer(code)
tokens = lexer.tokenize()

# Etapa 2: Parser
parser = Parser(tokens)
ast = parser.parse()

# Etapa 3: Mostrar AST
for node in ast:
    print(node)