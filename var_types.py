
class VarTypes(object):
    def __init__(self):
        self.primitives = {
            'bool': 'BOOL',
            'int': 'INT',
            'str': 'STRING',
            'float': 'FLOAT',
            'long': 'LONG'
        }
        self.compounds = {
            'list': 'LIST',
            'dictionary': 'DICTIONARY',
            'set': 'SET'
        }
        self.options = {**self.primitives, **self.compounds}
        print(self.options)

    def detect_type(elem):
        elem_type = type(elem)
        if elem_type in self.primitives:
            return self.options[elem_type]
        else:
            raise('Type {} not found'.format(elem_type))
