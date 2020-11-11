
#Create column dictionary; column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'rh':5, 'windspeed':7}

# Data types for each column (only if non-string)
types = {'tempout': float, 'rh': int, 'windspeed':float}

#Initialize my data variable; this is how you create a list
data = {}
for column in columns:
    data[column] = []

#Read and parse the data file
filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:

   # Read the first three lines (header)
   for _ in range(3):
       headerline = datafile.readline()
#       print(headerline) 

   #Read and parse the rest of the file into data dictionary
   for line in datafile:
       split_line = line.split()
       for column in columns:
           i = columns[column]
           t = types.get(column, str)
           value = t(split_line[i])
           data[column].append(value)

#Compute wind chill temperature
def compute_windchill(t, v):
    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275

    v16 = v**0.16

    wci = a + (b*t) - (c * v16) + (d * t * v16)
    return wci


# Running the function to compute wci
windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(compute_windchill(temp, windspeed))
#DEBUG
print(windchill)
#for i, j in zip([1, 2], [3, 4, 5]):
#    print(i, j)
rh=data['rh']
#print(data['rh'][0:10])
#print(data['date'])
