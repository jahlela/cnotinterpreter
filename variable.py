
class Variable(object):
    def __init__(self, var_type, value = None):
        self.var_type = var_type
        self.value = value

    def __repr__(self):
        return f'{self.var_type}, {self.value}'
