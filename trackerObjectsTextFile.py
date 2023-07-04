
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'trackerApp.txt'
fh = open(fname)

class Plastic:
    num_of_plastics = 0

    def __init__(self, type, status, complete):
        self.type = type
        self.status = status
        self.complete = complete
    
        Plastic.num_of_plastics += 1
    def __str__(self):
        return '\nType: ' + str(self.type) + '\nStatus: ' + str(self.status) + '\nComplete: ' + str(self.complete)


modellist = []
for line in fh:
    if line.startswith('pType: '): 
        line = line.split()
        pType = line[1]
        continue
    elif line.startswith('pStatus: '): 
        line = line.split()
        pStatus = line[1]
        continue
    elif line.startswith('pComplete: '): 
        line = line.split()
        pComplete = line[1]

    Models = Plastic(pType,pStatus,pComplete)
    print(Models)
    modellist.append(Models)

fh.close()
print('Number of total objects: ', Plastic.num_of_plastics)
