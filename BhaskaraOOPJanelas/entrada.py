import math
import tkinter as tk
from tkinter import ttk


class Entrada:
    def __init__(self, pai, ao_calcular):
        self.frame = ttk.LabelFrame(pai, text="Parâmetros", padding=14)
        self.ao_calcular = ao_calcular
        self.campos = {}

        valores_iniciais = {
            "a": "1",
            "b": "-3",
            "c": "2",
            "x_min": "-10",
            "x_max": "10",
        }
        rotulos = {
            "a": "Coeficiente a",
            "b": "Coeficiente b",
            "c": "Coeficiente c",
            "x_min": "Início do eixo x",
            "x_max": "Fim do eixo x",
        }

        for linha, chave in enumerate(valores_iniciais):
            ttk.Label(self.frame, text=rotulos[chave]).grid(
                row=linha * 2,
                column=0,
                sticky="w",
                pady=(4, 2),
            )
            campo = ttk.Entry(self.frame, width=24)
            campo.insert(0, valores_iniciais[chave])
            campo.grid(row=linha * 2 + 1, column=0, sticky="ew", pady=(0, 5))
            self.campos[chave] = campo

        ttk.Label(self.frame, text="Quantidade de pontos").grid(
            row=10, column=0, sticky="w", pady=(4, 2)
        )
        self.quantidade = tk.StringVar(value="400")
        ttk.Spinbox(
            self.frame,
            from_=2,
            to=10000,
            increment=50,
            textvariable=self.quantidade,
            width=22,
        ).grid(row=11, column=0, sticky="ew", pady=(0, 5))

        ttk.Label(self.frame, text="Tema do gráfico").grid(
            row=12, column=0, sticky="w", pady=(4, 2)
        )
        self.tema = tk.StringVar(value="Claro")
        ttk.Combobox(
            self.frame,
            textvariable=self.tema,
            values=("Claro", "Escuro"),
            state="readonly",
        ).grid(row=13, column=0, sticky="ew", pady=(0, 7))

        self.mostrar_grade = tk.BooleanVar(value=True)
        self.mostrar_raizes = tk.BooleanVar(value=True)
        self.mostrar_vertice = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            self.frame, text="Mostrar grade", variable=self.mostrar_grade
        ).grid(row=14, column=0, sticky="w", pady=2)
        ttk.Checkbutton(
            self.frame, text="Marcar raízes reais", variable=self.mostrar_raizes
        ).grid(row=15, column=0, sticky="w", pady=2)
        ttk.Checkbutton(
            self.frame, text="Marcar vértice", variable=self.mostrar_vertice
        ).grid(row=16, column=0, sticky="w", pady=2)

        ttk.Button(
            self.frame,
            text="Atualizar gráfico",
            command=self.ao_calcular,
        ).grid(row=17, column=0, sticky="ew", pady=(12, 2))
        self.frame.columnconfigure(0, weight=1)

    def obter_configuracao(self):
        try:
            coeficientes = {
                chave: float(campo.get())
                for chave, campo in self.campos.items()
            }
        except ValueError as erro:
            raise ValueError("Preencha os coeficientes e limites com números válidos.") from erro

        if not all(math.isfinite(valor) for valor in coeficientes.values()):
            raise ValueError("Os coeficientes e limites precisam ser números finitos.")

        try:
            quantidade = int(self.quantidade.get())
        except ValueError as erro:
            raise ValueError("A quantidade de pontos deve ser um número inteiro.") from erro

        if not 2 <= quantidade <= 10000:
            raise ValueError("A quantidade de pontos deve ficar entre 2 e 10000.")

        return {
            **coeficientes,
            "quantidade": quantidade,
            "tema": self.tema.get(),
            "grade": self.mostrar_grade.get(),
            "raizes": self.mostrar_raizes.get(),
            "vertice": self.mostrar_vertice.get(),
        }