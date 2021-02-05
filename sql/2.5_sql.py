import sqlite3

connection = sqlite3.connect('lubyTeste.db')
cursor = connection.cursor()

cursor.execute("DELETE FROM tabela_evento WHERE evento='Evento B'")

resultado = cursor.execute("SELECT * FROM tabela_evento").fetchall()
print(resultado)

connection.commit()
connection.close()