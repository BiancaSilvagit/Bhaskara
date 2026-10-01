import tkinter as tk
from tkinter import ttk


class Resultados:
    def __init__(self, pai):
        self.frame = ttk.LabelFrame(pai, text="Resultados", padding=12)
        self.texto = tk.StringVar(value="Informe os coeficientes para calcular.")
        ttk.Label(
            self.frame,
            textvariable=self.texto,
            justify="left",
            anchor="nw",
            wraplength=270,
        ).grid(row=0, column=0, sticky="nsew")
        self.frame.columnconfigure(0, weight=1)

    def atualizar(self, equacao):
        delta = equacao.calcular_delta()
        raizes = equacao.calcular_raizes()
        x_vertice, y_vertice = equacao.calcular_vertice()

        if delta > 0:
            texto_raizes = f"Duas raízes reais: x1 = {raizes[0]:.6g}, x2 = {raizes[1]:.6g}"
        elif delta == 0:
            texto_raizes = f"Uma raiz real (raiz dupla): x = {raizes[0]:.6g}"
        else:
            texto_raizes = f"Raízes complexas: x1 = {raizes[0]}, x2 = {raizes[1]}"

        self.texto.set(
            f"Equação: {equacao.a:g}x² + ({equacao.b:g})x + ({equacao.c:g}) = 0\n"
            f"Delta: {delta:g}\n"
            f"{texto_raizes}\n"
            f"Vértice: ({x_vertice:.6g}, {y_vertice:.6g})"
        )