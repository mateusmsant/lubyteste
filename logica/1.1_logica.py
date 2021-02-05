def getFatorial(num):
  total = 0
  i = 0

  while num > 1:
    total = num if i == 0 else num * total
  
    num -= 1
    i += 1

  return total

resultado = getFatorial(5)
print(resultado)
