import sqlite3

connection = sqlite3.connect('lubyTeste.db')
cursor = connection.cursor()

johnDoeID = cursor.execute("SELECT id FROM tabela_pessoa WHERE nome='John Doe'").fetchall()[0][0]
cursor.execute("UPDATE tabela_evento SET pessoa_id=? WHERE evento='Evento D'", (johnDoeID,))

resultado = cursor.execute("SELECT * FROM tabela_evento").fetchall()
print(resultado)

connection.commit()
connection.close()