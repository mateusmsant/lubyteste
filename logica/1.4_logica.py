def getVogais(string):
  vogais = 0
  for x in string:
    if x in 'aeiou':
      vogais += 1

  return vogais

resultado = getVogais("Luby Software")
print(resultado)