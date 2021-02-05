def getElementosFaltantes(vetor1, vetor2):
  vetorRetorno = []

  for x in vetor1:
    if x not in vetor2:
      vetorRetorno.append(x)
  for x in vetor2:
    if x not in vetor1:
      vetorRetorno.append(x)

  return vetorRetorno

vetor1 = [1,4,5]
vetor2 = [1,2,3,4,5]

resultado = getElementosFaltantes(vetor1, vetor2)
print(resultado)  