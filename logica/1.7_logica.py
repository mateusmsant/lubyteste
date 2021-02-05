def getPares(vetor):
  return [x for x in vetor if x % 2 == 0]

vetor = [1, 2, 3, 4, 5]
resultado = getPares(vetor)
print(resultado)