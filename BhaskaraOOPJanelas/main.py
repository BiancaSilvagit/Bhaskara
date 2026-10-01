import tkinter as tk
from tkinter import messagebox, ttk

from calculos import EquacaoSegundoGrau
from entrada import Entrada
from grafico import GraficoParabola
from resultados import Resultados


class AplicacaoBhaskara:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Bhaskara | Equação do segundo grau")
        self.janela.geometry("1120x740")
        self.janela.minsize(900, 620)

        self.estilo = ttk.Style(self.janela)
        if "clam" in self.estilo.theme_names():
            self.estilo.theme_use("clam")
        self.estilo.configure("Titulo.TLabel", font=("Segoe UI", 18, "bold"))
        self.estilo.configure("Subtitulo.TLabel", foreground="#667684")

        conteudo = ttk.Frame(self.janela, padding=(20, 16))
        conteudo.grid(row=0, column=0, sticky="nsew")
        self.janela.rowconfigure(0, weight=1)
        self.janela.columnconfigure(0, weight=1)
        conteudo.columnconfigure(0, weight=1)
        conteudo.rowconfigure(1, weight=1)

        cabecalho = ttk.Frame(conteudo)
        cabecalho.grid(row=0, column=0, sticky="ew", pady=(0, 12))
        ttk.Label(
            cabecalho,
            text="Equação do segundo grau",
            style="Titulo.TLabel",
        ).grid(row=0, column=0, sticky="w")
        ttk.Label(
            cabecalho,
            text="Calcule raízes, vértice e visualize a parábola.",
            style="Subtitulo.TLabel",
        ).grid(row=1, column=0, sticky="w", pady=(3, 0))

        area = ttk.Panedwindow(conteudo, orient="horizontal")
        area.grid(row=1, column=0, sticky="nsew")

        painel_lateral = ttk.Frame(area, padding=(0, 0, 14, 0), width=290)
        painel_lateral.grid_propagate(False)
        painel_grafico = ttk.Frame(area, padding=(10, 0, 0, 0))
        area.add(painel_lateral, weight=0)
        area.add(painel_grafico, weight=1)

        self.entrada = Entrada(painel_lateral, self.atualizar)
        self.entrada.frame.pack(fill="x")
        self.resultados = Resultados(painel_lateral)
        self.resultados.frame.pack(fill="x", pady=(14, 0))
        self.grafico = GraficoParabola(painel_grafico)

        self.atualizar()

    def atualizar(self):
        try:
            configuracao = self.entrada.obter_configuracao()
            equacao = EquacaoSegundoGrau(
                configuracao["a"],
                configuracao["b"],
                configuracao["c"],
            )
            self.resultados.atualizar(equacao)
            self.grafico.atualizar(
                equacao,
                configuracao["x_min"],
                configuracao["x_max"],
                configuracao["quantidade"],
                tema=configuracao["tema"],
                mostrar_grade=configuracao["grade"],
                mostrar_raizes=configuracao["raizes"],
                mostrar_vertice=configuracao["vertice"],
            )
        except (ValueError, OverflowError) as erro:
            messagebox.showerror("Entrada inválida", str(erro), parent=self.janela)

    def executar(self):
        self.janela.mainloop()


if __name__ == "__main__":
    AplicacaoBhaskara().executar()