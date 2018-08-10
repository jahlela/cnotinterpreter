from interpreter import Interpreter

filename = input("Please enter a filename: ")
interp = Interpreter(filename)
print(interp.parsed.variables)
