class FOPCParser:
    def __init__(self):
        self.tokens = []

    def tokenize(self, input_string):
        self.tokens = input_string.split()
        return self.tokens

    def parse(self):
        if not self.tokens:
            return False
        return self.expression()

    def expression(self):
        if self.match('('):
            if self.quantifier():
                if self.variable():
                    if self.match(')'):
                        return self.expression()
            elif self.unary_op():
                if self.expression():
                    if self.match(')'):
                        return True
            elif self.binary_op():
                if self.expression() and self.expression():
                    if self.match(')'):
                        return True
        elif self.proposition():
            return True
        return False

    def quantifier(self):
        return self.match('forall') or self.match('exists')

    def unary_op(self):
        return self.match('not')

    def binary_op(self):
        return self.match('and') or self.match('or') or self.match('implies') or self.match('iff')

    def proposition(self):
        return self.match('P') or self.match('Q')  # Assuming propositions are single uppercase letters

    def variable(self):
        return self.match('x') or self.match('y')  # Assuming variables are single lowercase letters

    def match(self, expected):
        if self.tokens and self.tokens[0] == expected:
            self.tokens = self.tokens[1:]
            return True
        return False

# Example usage
parser = FOPCParser()
input_string = "(forall x P(x) and exists y Q(y))"
tokens = parser.tokenize(input_string)
result = parser.parse()

print(f"Input: {input_string}")
print(f"Tokens: {tokens}")
print(f"Parse Result: {result}")
