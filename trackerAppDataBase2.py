# this lesson can be found in Using Databases with Python, Week 2, Worked Example: Counting pType in Database

import sqlite3

conn = sqlite3.connect('trackerApp.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
# this makes a new database everytime is one exists called 'Counts' so we can retry the code

cur.execute('''
CREATE TABLE Counts (pType TEXT, count INTEGER)''')
# this creates the new database with specific tables and what var's they use

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'trackerApp.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('pType: '): continue
    pieces = line.split()
    pType = pieces[1]
    # this for loop finds the pTypes in trackerApp.txt
    cur.execute('SELECT count FROM Counts WHERE pType = ? ', (pType,))
    # the '?' eventually turns into pType as a tuple, this is done to avoid SQL injection
    row = cur.fetchone()
    if row is None:
        # if no row then it will insert new row, this is similar to the histogram GET code line
        cur.execute('''INSERT INTO Counts (pType, count)
                VALUES (?, 1)''', (pType,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE pType = ?',
                    (pType,))
conn.commit()
    # this may take time, this will commit every loop but we can set it to commit every 10th time or so

sqlstr = 'SELECT pType, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    # row[0] is pType and row[1] is count

cur.close()

# TO DO
# Create and object for a record
# Create a menu(look into switches or cases) that the user can interact with
#   -display all records AND add a record
