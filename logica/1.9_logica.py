def stringToArray(string):
  vetorRetorno = []
  miniVetor = []

  for num in string:
    if num != "," and num != " ":
      miniVetor.append(num)
      if len(miniVetor) == 2:
        vetorRetorno.append(miniVetor)
        miniVetor = []
  
  return vetorRetorno

resultado = stringToArray("1, 2, 3, 4, 5, 6")
print(resultado)