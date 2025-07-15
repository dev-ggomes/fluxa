from lexer import Lexer

code = '''
let nome = "fluxa"
let x = 10
print(nome + x)
'''

lexer = Lexer(code)
tokens = lexer.tokenize()

for token in tokens:
    print(token)