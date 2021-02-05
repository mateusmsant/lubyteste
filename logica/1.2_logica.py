def getPremio(premioValor, tipo, multi):
  if multi is None:
    tipos = {"basic": 1, "vip": 1.2, "premium": 1.5, "deluxe": 1.8, "special": 2}
    return premioValor * tipos[tipo]    
  else:
    return premioValor * multi


resultado = getPremio(100, "vip", None)
print(resultado)

resultado = getPremio(100, "basic", 3)
print(resultado)