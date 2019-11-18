import sqlite3
from base64 import b64decode
from webbrowser import open

def getRecordNumber():
    while True:
        recordNumber = input("Choose a record number between 1 and 29: ")
        if recordNumber =='q':
            return 'q'
        try:
            rn = int(recordNumber)
        except:
            continue
        if 1 <= rn <= 29:
            break 
    return recordNumber

conn = sqlite3.connect('week10.db')
c = conn.cursor()

while True:
    rec = getRecordNumber()
    if rec == 'q':
        break
    link = c.execute('SELECT Link FROM Lab10 WHERE id=?',(rec,))

    for row in link:
        url = b64decode(row[0]).decode('utf-8')
        open(url,new=2)
        city = input("Please enter the city: ")
        country = input("Please enter the country: ")
        c.execute('UPDATE Lab10 SET City=? WHERE id=?',(city, rec))
        c.execute('UPDATE Lab10 SET Country=? WHERE id=?',(country, rec))
        addname = input("Do you want to enter a name (y or n): ")
        if addname == 'y':
            name = input("Enter the name: ")
            c.execute('UPDATE Lab10 SET Student=? WHERE id=?',(name, rec))
        
conn.commit()
c.close()
conn.close()