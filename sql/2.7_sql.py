import sqlite3

connection = sqlite3.connect('lubyTeste.db')
cursor = connection.cursor()

cursor.execute("ALTER TABLE tabela_pessoa ADD idade int")

resultado = cursor.execute("SELECT * FROM tabela_pessoa").fetchall()
print(resultado)

connection.commit()
connection.close()