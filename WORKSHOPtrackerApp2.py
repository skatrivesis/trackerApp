import sqlite3

conn = sqlite3.connect('trackerApp.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Models;

CREATE TABLE Models (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE, 
    pType TEXT, 
    pStatus TEXT, 
    pComplete TEXT
    )
    ''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'trackerApp.txt'
fh = open(fname)

pType = 0
pStatus = 0
pComplete = 0
for line in fh:
    if line.startswith('pType: '): 
        print(line)
        piecesT = line.split()
        pType = piecesT[1]
        continue
    elif line.startswith('pStatus: '): 
        piecesS = line.split()
        pStatus = piecesS[1]
        print(line)
        continue
    # SOMETHING IS WRONG WITH THE BELOW ELIF, ONCE ITS UNCOMMENTED THE DATABASE DOESNT SHOW ANYTHING AT ALL
    # elif line.startswith('pComplete: '): 
    #     piecesC = line.split()
    #     pComplete = piecesC[1]
    #     print(line)
    #     continue
    

    # row = cur.fetchone()
    # if row is None: 
    cur.execute('''INSERT OR REPLACE INTO Models (pType, pStatus) 
    VALUES ( ?, ?)''', ( pType, pStatus) )
    # else:
    #     cur.execute('UPDATE Models SET count = count + 1 WHERE pType = ?',
    #                  (pType,))

 # NEW CODE: ------------------------------------------------------

    # cur.execute('''INSERT OR REPLACE INTO Track
    #     (title, album_id, genre_id, len, rating, count) 
    #     VALUES ( ?, ?, ?, ?, ?, ? )''', 
    #     ( name, album_id, genre_id, length, rating, count ) )

    # cur.execute('''INSERT OR IGNORE INTO Genre (name) 
    #     VALUES ( ? )''', ( genre, ) )
    # cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    # genre_id = cur.fetchone()[0]

    # cur.execute('''INSERT OR IGNORE INTO User (name)
    #     VALUES ( ? )''', ( name, ) )
    # cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    # user_id = cur.fetchone()[0]  

    # cur.execute('''INSERT OR REPLACE INTO Track
    #     (title, album_id, genre_id, len, rating, count) 
    #     VALUES ( ?, ?, ?, ?, ?, ? )''', 
    #     ( name, album_id, genre_id, length, rating, count ) )
 # -----------------------------------------------------------------

conn.commit()

# sqlstr = 'SELECT pType, count FROM Models ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])
    

cur.close()

# TO DO
# Create and object for a record
# Create a menu(look into switches or cases) that the user can interact with
#   -display all records AND add a record