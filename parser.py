
from variable import Variable
from file_object import FileObject
from var_types import VarTypes


class Parser(object):
    def __init__(self, filename = ""):
        self.text = FileObject(filename).content
        self.variables = {}
        self.types = VarTypes()

    def parse_variables(self):
        for line in self.text:
            words = line.strip().split(" ")
            var_type, name, assignment = words[0:3]
            value = (" ").join(words[3:])
            new_var = Variable(self.types.options[var_type], value)
            self.variables[name] = new_var
