from language.tokens import TokenType
from language.nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos]

    def eat(self, type_=None):
        tok = self.current()
        if type_ and tok.type != type_:
            raise Exception(f"Expected token {type_}, got {tok.type}")
        self.pos += 1
        return tok

    def parse(self):
        statements = []
        while self.current().type != TokenType.EOF:
            if self.current().type == TokenType.KEYWORD:
                if self.current().value == 'let':
                    statements.append(self.parse_var_assign())
                elif self.current().value == 'print':
                    statements.append(self.parse_print())
            else:
                self.eat()
        return statements

    def parse_var_assign(self):
        self.eat(TokenType.KEYWORD)  # let
        name = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.ASSIGN)
        value = self.parse_expression()
        if self.current().type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        return VarAssignNode(name, value)

    def parse_print(self):
        self.eat(TokenType.KEYWORD)  # print
        self.eat(TokenType.LPAREN)
        expr = self.parse_expression()
        self.eat(TokenType.RPAREN)
        if self.current().type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        return PrintNode(expr)

    def parse_expression(self):
        left = self.parse_term()
        while self.current().type in (TokenType.PLUS, TokenType.MINUS):
            op = self.eat().type
            right = self.parse_term()
            left = BinaryOpNode(left, op, right)
        return left

    def parse_term(self):
        left = self.parse_factor()
        while self.current().type in (TokenType.STAR, TokenType.SLASH):
            op = self.eat().type
            right = self.parse_factor()
            left = BinaryOpNode(left, op, right)
        return left

    def parse_factor(self):
        tok = self.current()

        if tok.type == TokenType.NUMBER:
            self.eat()
            return NumberNode(tok.value)

        elif tok.type == TokenType.STRING:
            self.eat()
            return StringNode(tok.value)

        elif tok.type == TokenType.IDENTIFIER:
            self.eat()
            return IdentifierNode(tok.value)

        elif tok.type == TokenType.LPAREN:
            self.eat()
            expr = self.parse_expression()
            self.eat(TokenType.RPAREN)
            return expr

        else:
            raise Exception(f"Unexpected token in expression: {tok}")