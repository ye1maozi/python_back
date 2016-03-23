import sqlite3
conn = sqlite3.connect('a')
curs = conn.cursor()
conn.commit()
print curs