import sqlite3

connection = sqlite3.connect('lubyTeste.db')
cursor = connection.cursor()

cursor.execute("""DELETE FROM tabela_pessoa
  WHERE NOT ROWID IN (
  SELECT ROWID FROM tabela_pessoa a
  INNER JOIN tabela_evento b
  ON a.id = b.pessoa_id
);
""")

resultado = cursor.execute("SELECT * FROM tabela_pessoa").fetchall()
print(resultado)

connection.commit()
connection.close()

