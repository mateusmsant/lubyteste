import sqlite3

connection = sqlite3.connect('lubyTeste.db')
cursor = connection.cursor()

lisaID = cursor.execute("SELECT id FROM tabela_pessoa WHERE nome='Lisa Romero'").fetchall()[0][0]
cursor.execute("INSERT INTO tabela_evento VALUES (?, ?)", ('Evento E', lisaID))

eventos = cursor.execute("SELECT * FROM tabela_evento").fetchall()
print(eventos)

connection.commit()
connection.close()