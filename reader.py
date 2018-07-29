# Read in file

class File(object):
    def __init__(self, filename = ""):
        self.filename = filename
        self.get_file_data()

    def get_file_data(self):
        """
        Returns an array of stripped lines in program
        """
        if self.filename:
            with open(self.filename, 'r') as readable_file:
                self.readable_file = readable_file
                self.content = self.readable_file.readlines()
                self.lines = [x.strip() for x in self.content]
            readable_file.close()
    

class Types(object):
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

class Variable(object):
    def __init__(self, varType, value = None):
        self.varType = varType
        self.value = value

    def __repr__(self):
        return f'{self.varType} {self.value}'
        

class Interpreter(object):
    def __init__(self, filename = ""):
        self.text = File(filename).content
        self.variables = {}
        self.types = Types()

    def parse_variables(self):
        for line in self.text:
            words = line.strip().split(" ")
            varType, name, assignment = words[0:3]
            value = (" ").join(words[3:])
            newVar = Variable(self.types.options[varType], value)
            self.variables[name] = newVar
            print(self.variables)
            

interp = Interpreter('test.txt')
print(interp.parse_variables())
