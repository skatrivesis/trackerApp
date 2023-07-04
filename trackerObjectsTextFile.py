#TODO:
# - please take a look at the output currently, with this logic the full output is not showing from the trackerApp.txt file. Please take a look and try to troubleshoot why. Put your answer below
#    - ANSWER:
# - Take a look at notes and fix things that I have brought up. 
# - **ONLY DO THIS WHEN YOU HAVE DONE EVERYTHING ABOVE. I WANT THIS TO BE LAST ON THE TODO LIST** We need to put null checks in. This is to ensure if a field coming in from the data is empty (null) then we can handle the data without the program bombing out

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'trackerApp.txt'
fh = open(fname)

class Unit:
    num_of_models = 0 #This is no longer accurate, we need to figure out a solution here. We have a qty data point that we need to take into account

    def __init__(self, faction, unitName, qty, notes, complete):
        self.faction = faction
        self.unitName = unitName
        self.qty = qty
        self.notes = notes
        self.complete = complete
    
        Unit.num_of_models += 1 #please see note on line 7
    def __str__(self):
        return '\nFaction: ' + str(self.faction) + '\nUnit: ' + str(self.unitName) + '\nQuantity: ' + str(self.qty) + '\nNotes: ' + str(self.notes) + '\nComplete: ' + str(self.complete)


unitList = []
for line in fh:
    if line.startswith('faction: '): 
        line = line.split()
        faction = line[1] #I want these variables (ie. faction, unitName, qty, etc.) initialized at the top of the program, we are reinitializing these every time we run the loop which is wasted computing power. 
        continue
    elif line.startswith('unit name: '): 
        line = line.split() #we might need to figure out a better use here. line split is good but when we incorperate a database this will need to change and might become irrelevant
        unitName = line[2] #see above note, notice this has the line[2] instead of line[1]. . . I wonder why.... ? ;)
        continue
    elif line.startswith('qty: '): 
        line = line.split()
        qty = line[1]
        continue
    elif line.startswith('notes: '):
        line = line.split()  
        notes = line[1]
        continue
    elif line.startswith('complete: '):
        line = line.split()  
        complete = line[1]

    Units = Unit(faction, unitName, qty, notes, complete)
    print(Units)
    unitList.append(Units)

fh.close()
print('Number of total objects: ', Unit.num_of_models)

for unit in unitList:
    print(unit)
