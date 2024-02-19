import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO utilisateurs (username,password ) VALUES (?, ?, ?)",('Vendeur', 'V', '2789, Rue des Roses, 13005 Marseille'))
cur.execute("INSERT INTO utilisateurs (username,password ) VALUES (?, ?, ?)",('Admin', 'A', '333, Rue de la Paix, 75002 Paris'))

connection.commit()
connection.close()
