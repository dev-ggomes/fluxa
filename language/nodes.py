class Node: 
    pass

class NumberNode(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'NumberNode({self.value})'
    
class StringNode(Node): 
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'StringNode({self.value})'

class IdentifierNode(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'IdentifierNode({self.name})'

class BinaryOpNode(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f'BinaryOpNode({self.left}, {self.op}, {self.right})'

class VarAssignNode(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f'VarAssignNode({self.name}, {self.value})'

class PrintNode(Node): 
    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return f'PrintNode({self.expression})'