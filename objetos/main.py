from tkinter import ttk
import tkinter as tk
from controller import Controller
import sqlite3

class Interface(Controller):
  def __init__(self):
    root = tk.Tk()

    self.tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings')
    self.tree.column("#1", anchor=tk.CENTER)
    self.tree.heading("#1", text="Código")
    self.tree.column("#2", anchor=tk.CENTER)
    self.tree.heading("#2", text="Preço")
    self.tree.column("#3", anchor=tk.CENTER)
    self.tree.heading("#3", text="Valor")
    self.tree.column("#4", anchor=tk.CENTER)
    self.tree.heading("#4", text="Estoque")
    self.tree.pack()

    self.comprarBebidaButton = tk.Button(text="Adicionar bebida", command=self.comprarBebida)
    self.pagamentoButton = tk.Button(text="Pagar", command=self.acabarCompra)
    self.codigoLabel = tk.Label(text="Código")
    self.labelQuantidade = tk.Label(text="Quantidade")
    self.labelPagamento = tk.Label(text="Pagamento")
    self.msgLabel = tk.Label(text="")
    self.totalCompraSessao = tk.Label()
    self.totalVendido = tk.Label()
    self.codigoEntry = tk.Entry(root)
    self.codigoLabel.pack()
    self.codigoEntry.pack()
    self.labelQuantidade.pack()
    self.quantidadeBebidaEntry = tk.Entry(root)
    self.quantidadeBebidaEntry.pack()
    self.comprarBebidaButton.pack(pady=10)
    self.codigoEntry.pack()
    self.labelPagamento.pack()
    self.pagamentoEntry = tk.Entry(root)
    self.pagamentoEntry.pack()
    self.pagamentoButton.pack(pady=10)
    self.msgLabel.pack()
    self.totalCompraSessao.pack(pady=35)

    self.total = 0
    self.quantidadeInput = 0
    self.vendasAnterior = 0
    self.dictQuantidades = {}
    self.showData()   

    root.geometry("840x720")
    root.mainloop()

Interface()
