#TODO:
# - please take a look at the output currently, with this logic the full output is not showing from the trackerApp.txt file. Please take a look and try to troubleshoot why. Put your answer below
#    - ANSWER: I think this is because the output is compiled in the form of arrays instead of strings. Daddy will fix this. >> Used the Join fuction for better presentation
# - Take a look at notes and fix things that I have brought up. 
# - input data from user to append text file in full entry form
# - **ONLY DO THIS WHEN YOU HAVE DONE EVERYTHING ABOVE. I WANT THIS TO BE LAST ON THE TODO LIST** We need to put null checks in. This is to ensure if a field coming in from the data is empty (null) then we can handle the data without the program bombing out
# TOM: for above, I put in another entry called Gay Robot Man with blank spaces and the program still works. When this is put in a data base these entries will be italisized and say Null

from readchar import readkey, key

fname = 'trackerApp/trackerapp.txt'
fh = open(fname, "r+")

class Unit:
    num_of_entries = 0 

    def __init__(self, faction, unitName, qty, notes, complete):
        self.faction = faction
        self.unitName = unitName
        self.qty = qty
        self.notes = notes
        self.complete = complete
    
        Unit.num_of_entries += 1 

    def __str__(self):
        return '\nFaction: ' + str(self.faction) + '\nUnit: ' + str(self.unitName) + '\nQuantity: ' + str(self.qty) + '\nNotes: ' + str(self.notes) + '\nComplete: ' + str(self.complete)


num_Of_Units_Lst = []
unit_Entry_List = []
faction = None
unitName = None
qty = None
notes = None
complete = None


# Read file loops
for line in fh:
    if line.startswith('faction: '): 
        line = line.split()
        faction = line[1:] 
        faction = ' '.join(faction)
        continue
    elif line.startswith('unit name: '): 
        line = line.split()
        unitName = line[2:] 
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


# TOM NOTE: Menu and write file loops
while True:
    print("\nWhat would you like to do?\nPress '1' to close program\nPress '2' to add units\nPress '3' to see all units")
    prompt = readkey()
    if prompt == '1':
        break
    if prompt == '2':
        prompt = 0
        while True:
            try: 
                entryNum = int(input('\nhow many entries do you want to put in?: ')) 
                break
            except ValueError:
                print('\nYou entered a non integer value, try again.')
                continue



        while entryNum > 0:
            faction = input('faction: ')
            fh.write('\nfaction: ')
            fh.write(faction)
            unitName = input('unit name: ')
            fh.write('\nunit name: ')
            fh.write(unitName)

            while True:
                try: 
                    qty = int(input('quantity: ')) 
                    num_Of_Units_Lst.append(qty)
                    qtyStr = str(qty)
                    fh.write('\nquantity: ')
                    fh.write(qtyStr)
                    break
                except ValueError:
                    print('\nYou entered a non integer value, try again.')
                    continue

            notes = input('notes: ')
            fh.write('\nnotes: ')
            fh.write(notes)
            complete = input('complete: ')
            fh.write('\ncomplete: ')
            fh.write(complete)
            if entryNum > 1: print('\n>>>New Entry>>>')
            entryNum = entryNum-1

            Units = Unit(faction, unitName, qty, notes, complete)
            num_Of_Units_Lst.append(qty)
            unit_Entry_List.append(Units)
            continue

    if prompt == '3':
        print('>>>ALL ENTRIES>>>')
        for unit in unit_Entry_List:
            print(unit)
         
    num_Of_Units = 0
    [int(str_Units)for str_Units in num_Of_Units_Lst]
    for int_Units in num_Of_Units_Lst: 
         num_Of_Units = num_Of_Units + int(int_Units)

    print('\nNumber of total Models: ', num_Of_Units ) 
    print('Number of total Entries: ', Unit.num_of_entries) 

fh.close()