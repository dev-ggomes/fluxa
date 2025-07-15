class Node: 
    pass

class NumberNode(Node):
    def __init__(self, value):
        self.value = value

class StringNode(Node): 
    def __init__(self, value):
        self.value = value

class IdentifierNode(Node):
    def __init__(self, value):
        self.value = value

class BinaryOpNode(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class VarAssignNode(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class PrintNode(Node): 
    def __init__(self, expression):
        self.expression = expression