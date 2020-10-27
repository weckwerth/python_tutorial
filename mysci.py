print("Hello, world!")

#Read the data file and look at first 4 lines
#filename = "data/wxobs20170821.txt"
#datafile = open(filename, 'r')
#print(datafile.readline())
#print(datafile.readline())
#print(datafile.readline())
#print(datafile.readline())
#datafile.close()

#Read entire data file
filename = "data/wxobs20170821.txt"
datafile = open(filename, 'r')
data = datafile.read()
datafile.close()

#DEBUG
#print all the data
print(data)
#print the word data
print('data')


filename = "data/wxobs20170821.txt"
with open(filename, 'r') as datafile:
    data = datafile.read()

#DEBUG
print(data)
print(type(data))

#DEBUG
#print(type(data)); tells you data type
