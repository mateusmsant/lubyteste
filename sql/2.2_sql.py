import sqlite3

connection = sqlite3.connect('lubyTeste.db')
cursor = connection.cursor()

sobrenomesDoe = cursor.execute("SELECT * FROM tabela_pessoa WHERE nome LIKE '%Doe'").fetchall()
print(sobrenomesDoe)

connection.commit()
connection.close()