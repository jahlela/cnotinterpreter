# Read in file

class File(object):
    def __init__(self, filename = ""):
        self.filename = filename
        self.get_file_data()

    def get_file_data(self):
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
        self.compounds = {}
#        self.options = {**self.primitives, **self.compounds}

    def detect_type(elem):
        elem_type = type(elem)
        if elem_type in self.primitives:
            return self.options[elem_type]
        else:
            raise('Type {} not found'.format(elem_type))



class Interpreter(object):
    def __init__(self, filename = ""):
        self.f = File(filename)
        self.variables = {}
        

    def parse_variables(self):
        t = Types()
        for line in self.f.lines:
            print line[0]
            if line[0] in t.primitives:
                print t.primitives[line[0]]
            

interp = Interpreter('test.txt')
print interp.parse_variables()
