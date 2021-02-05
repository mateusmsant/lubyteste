def getDiasDiferenca(data1, data2):
  dia1 = data1[:2]
  dia2 = data2[:2]

  diferenca = int(dia1) - int(dia2)

  if diferenca > 0:
    return diferenca
  elif diferenca < 0:
    return - (diferenca)
  else:
    return "Os dias são iguais"

resultado = getDiasDiferenca("10122020", "25122020")
print(resultado)
