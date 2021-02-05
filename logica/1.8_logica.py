def getPessoa(vetor, pessoa):
  vetorRetorno = []

  for item in vetor:
    if pessoa in item:
      vetorRetorno.append(item)

  return vetorRetorno

vetor = ["John Doe", "Jane Doe", "Alice Jones", "Bobby Louis", "Lisa Doe Romero"]
resultado = getPessoa(vetor, "Doe")
print(resultado)