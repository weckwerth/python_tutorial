#Read the data file
filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:
    data = datafile.read()


#DEBUG
#print(type(data)); tells you data type