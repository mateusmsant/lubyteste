import sqlite3

connection = sqlite3.connect('lubyTeste.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE tabela_telefone (
  id INTEGER NOT NULL PRIMARY KEY,
  telefone VARCHAR(200),
  pessoa_id int,
  FOREIGN KEY(pessoa_id) REFERENCES tabela_pessoa(id)
)""")

connection.commit()
connection.close()