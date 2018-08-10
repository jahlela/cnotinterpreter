from parser import Parser

class Interpreter(object):
    def __init__(self, filename = None):
        self.filename = filename
        self.parsed = self.get_parsed(filename)

    def get_parsed(self, filename):
        if filename:
            return Parser(filename)
