
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'trackerApp/trackerApp.txt'
fh = open(fname)

class Unit:
    num_of_plastics = 0

    def __init__(self, type, status, complete):
        self.type = type
        self.status = status
        self.complete = complete
    
        Unit.num_of_plastics += 1
    def __str__(self):
        return '\nType: ' + str(self.type) + '\nStatus: ' + str(self.status) + '\nComplete: ' + str(self.complete)


modelList = []
for line in fh:
    if line.startswith('type: '): 
        line = line.split()
        type = line[1]
        continue
    elif line.startswith('status: '): 
        line = line.split()
        status = line[1]
        continue
    elif line.startswith('complete: '): 
        line = line.split()
        complete = line[1]

    Models = Unit(type,status,complete)
    print(Models)
    modelList.append(Models)

fh.close()
print('Number of total objects: ', Unit.num_of_plastics)

for model in modelList:
    print(model)
