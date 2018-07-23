# Read in file

with open('./test.txt') as file:
    content = file.readlines()

content = [x.strip() for x in content]
print content

file.close()
