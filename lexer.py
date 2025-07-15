from language.tokens import TokenType

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {repr(self.value)})'
    
class Lexer:
    def __init__(self, source):
        self.source = source
        self.pos = 0
        self.keywords = {"print", "let"}

    def tokenize(self):
        tokens = []
        while self.pos < len(self.source):
            current = self.source[self.pos]

            if current.isspace():
                if current == "\n":
                    tokens.append(Token(TokenType.NEWLINE, '\n'))
                self.pos += 1
            elif current.isalpha() or current == '_':
                tokens.append(self._identifier())
            elif current.isdigit():
                tokens.append(self._number())
            elif current == '"':
                tokens.append(self._string())
            elif current == '=':
                tokens.append(Token(TokenType.ASSIGN, '='))
                self.pos += 1
            elif current == '+':
                tokens.append(Token(TokenType.PLUS, '+'))
                self.pos += 1
            elif current == '-':
                tokens.append(Token(TokenType.MINUS, '-'))
                self.pos += 1
            elif current == '*':
                tokens.append(Token(TokenType.STAR, '*'))
                self.pos += 1
            elif current == '/':
                tokens.append(Token(TokenType.SLASH, '/'))
                self.pos += 1
            elif current == '(':
                tokens.append(Token(TokenType.LPAREN, '('))
                self.pos += 1
            elif current == ')':
                tokens.append(Token(TokenType.RPAREN, ')'))
                self.pos += 1
            else:
                raise Exception(f"Unexpected character: {current}")
        tokens.append(Token(TokenType.EOF, None))
        return tokens
    
    def _identifier(self):
        start = self.pos
        while self.pos < len(self.source) and (self.source[self.pos].isalnum() or self.source[self.pos] == '_'):
            self.pos += 1
        text = self.source[start:self.pos]
        if text in self.keywords:
            return Token(TokenType.KEYWORD, text)
        return Token(TokenType.IDENTIFIER, text)
    
    def _number(self):
        start = self.pos
        while self.pos < len(self.source) and self.source[self.pos].isdigit():
            self.pos += 1
        return Token(TokenType.NUMBER, int(self.source[start:self.pos]))

    def _string(self):
        self.pos += 1  # skip opening "
        start = self.pos
        while self.pos < len(self.source) and self.source[self.pos] != '"':
            self.pos += 1
        value = self.source[start:self.pos]
        self.pos += 1  # skip closing "
        return Token(TokenType.STRING, value)