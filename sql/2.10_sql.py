import sqlite3

connection = sqlite3.connect('lubyTeste.db')
cursor = connection.cursor()

cursor.execute("""DROP TABLE tabela_telefone""")

connection.commit()
connection.close()