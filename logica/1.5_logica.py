def getValorDescontado(valor, desconto):
  valorReal = float(valor.split()[1].replace(",", "."))
  descontoReal = float(desconto.split("%")[0])/100
  
  return f"R$ {valorReal - (valorReal * descontoReal)}".replace(".", ",")

resultado = getValorDescontado("R$ 6817,36", "30%")
print(resultado)