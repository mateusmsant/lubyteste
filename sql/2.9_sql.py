import sqlite3

connection = sqlite3.connect('lubyTeste.db')
cursor = connection.cursor()

cursor.execute("""CREATE UNIQUE INDEX hiLuby ON tabela_telefone (telefone)""")

connection.commit()
connection.close()