import sqlite3

connection = sqlite3.connect('lubyTeste.db')
cursor = connection.cursor()

resultado = cursor.execute("SELECT * FROM tabela_pessoa as tp JOIN tabela_evento as te ON tp.id = te.pessoa_id").fetchall()

for pessoaEvento in resultado:
  print(f"{pessoaEvento[1]} participará do evento {pessoaEvento[3]}")
  
connection.commit()
connection.close()