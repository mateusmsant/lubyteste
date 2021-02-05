# pylint: disable=E1101
# pylint: disable=E0203
from tkinter import ttk
import tkinter as tk
import sqlite3

class Controller(): 
  def compraAprovada(self, key, value):
    connection = sqlite3.connect('vendingDb.db')
    cursor = connection.cursor()

    self.retirarEstoque = self.emEstoque - value

    query = f"UPDATE bebidas SET quantidade=? WHERE codigo=?"
    cursor.execute(query, (self.retirarEstoque, key,)) 

    self.vendasAnterior += self.total
    self.totalCompraSessao["text"] = f"Compra encerrada. Total de compras da sessão: {self.vendasAnterior}" + "\n"

    connection.commit()
    connection.close()

  def acabarCompra(self):
    pagamentoInput = self.pagamentoEntry.get()
    troco = float(pagamentoInput) - self.total

    connection = sqlite3.connect('vendingDb.db')
    cursor = connection.cursor()

    for key, value in self.dictQuantidades.items():
      self.emEstoque = cursor.execute(f"SELECT quantidade FROM bebidas WHERE codigo=?", (key,)).fetchall()[0][0]


      if troco > 0:
        self.msgLabel["text"] = f"Seu troco é de {troco}"
        self.compraAprovada(key, value)
      elif troco == 0:
        self.msgLabel["text"] = "Não há troco"
        self.compraAprovada(key, value)
      else:
        self.msgLabel["text"] = f"O valor inserido é menos que o valor total da compra ({self.total}) - compra encerrada"
        
    self.dictQuantidades = {}
    self.total = 0 

    self.showData()

    connection.commit()
    connection.close()

  def comprarBebida(self):
    self.codigoInput = self.codigoEntry.get()
    self.quantidadeInput = self.quantidadeBebidaEntry.get()

    if self.codigoInput == "" or self.quantidadeInput == "":
      self.msgLabel["text"] = "Há campos em brancos"

    elif self.codigoInput.isnumeric() and self.quantidadeInput.isnumeric():
      self.codigoInput = int(self.codigoInput)
      self.quantidadeInput = int(self.quantidadeInput)
      
      if (self.codigoInput > 0 and self.codigoInput < 11) and self.quantidadeInput > 0:
        connection = sqlite3.connect("vendingDb.db")
        cursor = connection.cursor()        

        self.emEstoque = cursor.execute("SELECT quantidade FROM bebidas WHERE codigo=?", (self.codigoInput, )).fetchall()[0][0]
        precoBebida = cursor.execute("SELECT valor FROM bebidas WHERE codigo=?", (self.codigoInput, )).fetchall()[0][0]

        if self.emEstoque - self.quantidadeInput >= 0:
          self.total += self.quantidadeInput * precoBebida
          self.msgLabel["text"] = f"Total da compra: {self.total}"
          self.dictQuantidades[self.codigoInput] = self.dictQuantidades.get(self.codigoInput, 0) + self.quantidadeInput
          self.nome = cursor.execute("SELECT nome FROM bebidas WHERE codigo=?", (self.codigoInput, )).fetchall()[0][0]
          self.totalCompraSessao["text"] += f"Bebida: {self.nome} | Quantidade: {self.quantidadeInput}\n"
          
          connection.commit()
          connection.close()

        else:
          self.msgLabel["text"] = "Não há estoque"

      else:
        self.msgLabel["text"] = "Valores inválidos"

  def showData(self):
    for i in self.tree.get_children():
      self.tree.delete(i)
    
    connection = sqlite3.connect("vendingDb.db")
    cursor = connection.cursor()

    rows = cursor.execute("SELECT * FROM bebidas").fetchall()

    for row in rows:
      self.tree.insert("", tk.END, values=row)        
      
    connection.commit()
    connection.close()