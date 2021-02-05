def getPrimos(num):
  primos = 0
  for num in range(1, num + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primos += 1

  return primos


resultado = getPrimos(10)
print(resultado)


