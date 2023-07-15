#TODO:
# - please take a look at the output currently, with this logic the full output is not showing from the trackerApp.txt file. Please take a look and try to troubleshoot why. Put your answer below
#    - ANSWER: I think this is because the output is compiled in the form of arrays instead of strings. Daddy will fix this. >> Used the Join fuction for better presentation
# - Take a look at notes and fix things that I have brought up. 
# - input data from user to append text file in full entry form
# - **ONLY DO THIS WHEN YOU HAVE DONE EVERYTHING ABOVE. I WANT THIS TO BE LAST ON THE TODO LIST** We need to put null checks in. This is to ensure if a field coming in from the data is empty (null) then we can handle the data without the program bombing out
# TOM: for above, I put in another entry called Gay Robot Man with blank spaces and the program still works. When this is put in a data base these entries will be italisized and say Null
fname = 'trackerApp/trackerapp.txt'
fh = open(fname)

class Unit:
    num_of_entries = 0 # COMPLETE This is no longer accurate, we need to figure out a solution here. We have a qty data point that we need to take into account

    def __init__(self, faction, unitName, qty, notes, complete):
        self.faction = faction
        self.unitName = unitName
        self.qty = qty
        self.notes = notes
        self.complete = complete
    
        Unit.num_of_entries += 1 # COMPLETE please see note on line 12

    def __str__(self):
        return '\nFaction: ' + str(self.faction) + '\nUnit: ' + str(self.unitName) + '\nQuantity: ' + str(self.qty) + '\nNotes: ' + str(self.notes) + '\nComplete: ' + str(self.complete)

num_Of_Units = 0
num_Of_Units_Lst = [] # COMPLETE Need to turn list into integers to count
unit_Entry_List = []



for line in fh:
    if line.startswith('faction: '): 
        line = line.split()
        faction = line[1:] # TOM: NOT SUREWHAT YOU MEAN BY THIS, I want these variables (ie. faction, unitName, qty, etc.) initialized at the top of the program, we are reinitializing these every time we run the loop which is wasted computing power. 
        faction = ' '.join(faction)
        continue
    elif line.startswith('unit name: '): 
        line = line.split() # TOM: COMPLETE WTIH JOIN FUNCTION, we might need to figure out a better use here. line split is good but when we incorperate a database this will need to change and might become irrelevant
        unitName = line[2:] # TOM: THIS IS BECAUSE YOUR GAY, see above note, notice this has the line[2] instead of line[1]. . . I wonder why.... ? ;)
        unitName = ' '.join(unitName)
        continue
    elif line.startswith('qty: '): 
        line = line.split()
        qty = line[1]
        num_Of_Units_Lst.append(qty)
        continue
    elif line.startswith('notes: '):
        line = line.split()  
        notes = line[1:]
        notes = ' '.join(notes)
        continue
    elif line.startswith('complete: '):
        line = line.split()  
        complete = line[1:]
        complete = ' '.join(complete)

    Units = Unit(faction, unitName, qty, notes, complete)
    unit_Entry_List.append(Units)

fh.close()

# TOM NOTE: This is the menu prompt, we currently have three options and the program only stops when you done in the main prompt

while True:
    prompt = input('\nWhat would you like to do? See units or add units or done? >>> ').lower()
    if prompt == 'done':
        break
    if prompt == 'add units':

        entryNum = int(input('\nhow many entries do you want to put in?: ')) 

        while entryNum > 0:
            faction = input('faction: ')
            unitName = input('unit name: ')
            qty = int(input('quantity: '))
            notes = input('notes: ')
            complete = input('complete: ')
            if entryNum > 1: print('\n>>>New Entry>>>')
            entryNum = entryNum-1

            Units = Unit(faction, unitName, qty, notes, complete)
            num_Of_Units_Lst.append(qty)
            unit_Entry_List.append(Units)
            continue

    if prompt == 'see units':
        print('>>>ALL ENTRIES>>>')
        for unit in unit_Entry_List:
            print(unit)
 
        [int(str_Units)for str_Units in num_Of_Units_Lst]
        for int_Units in num_Of_Units_Lst:
            num_Of_Units = num_Of_Units + int(int_Units)    

        print('\nNumber of total Models: ', num_Of_Units ) # COMPLETE needs to count units
        print('Number of total Entries: ', Unit.num_of_entries) # COMPLETE change var name to reflect entries instead of models