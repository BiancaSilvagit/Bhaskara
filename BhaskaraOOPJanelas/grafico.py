import math

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class GraficoParabola:
    def __init__(self, pai):
        self.figura = Figure(figsize=(7, 5), dpi=100, constrained_layout=True)
        self.eixo = self.figura.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figura, master=pai)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
        pai.rowconfigure(0, weight=1)
        pai.columnconfigure(0, weight=1)

    def atualizar(
        self,
        equacao,
        x_min,
        x_max,
        quantidade,
        tema="Claro",
        mostrar_grade=True,
        mostrar_raizes=True,
        mostrar_vertice=True,
    ):
        pontos = equacao.calcular_pontos(x_min, x_max, quantidade)
        valores_x = [ponto[0] for ponto in pontos]
        valores_y = [ponto[1] for ponto in pontos]
        fundo, texto, grade, curva = self._cores_tema(tema)

        self.eixo.clear()
        self.figura.set_facecolor(fundo)
        self.eixo.set_facecolor(fundo)
        self.eixo.plot(
            valores_x,
            valores_y,
            color=curva,
            linewidth=2.2,
            label="Parábola",
        )
        self.eixo.axhline(0, color=texto, linewidth=0.8, alpha=0.7)
        self.eixo.axvline(0, color=texto, linewidth=0.8, alpha=0.7)
        self.eixo.set_xlim(x_min, x_max)
        self.eixo.set_xlabel("x", color=texto)
        self.eixo.set_ylabel("y", color=texto)
        self.eixo.tick_params(colors=texto)
        for borda in self.eixo.spines.values():
            borda.set_color(grade)

        if mostrar_grade:
            self.eixo.grid(True, color=grade, linestyle="--", alpha=0.65)

        if mostrar_raizes:
            raizes_reais = [
                raiz.real if isinstance(raiz, complex) else raiz
                for raiz in equacao.calcular_raizes()
                if not isinstance(raiz, complex)
                or math.isclose(raiz.imag, 0.0, abs_tol=1e-12)
            ]
            raizes_visiveis = [raiz for raiz in raizes_reais if x_min <= raiz <= x_max]
            if raizes_visiveis:
                self.eixo.scatter(
                    raizes_visiveis,
                    [0] * len(raizes_visiveis),
                    color="#22a06b",
                    edgecolor=fundo,
                    linewidth=0.8,
                    zorder=4,
                    label="Raiz(es) real(is)",
                )

        if mostrar_vertice:
            vertice = equacao.calcular_vertice()
            if x_min <= vertice[0] <= x_max:
                self.eixo.scatter(
                    [vertice[0]],
                    [vertice[1]],
                    color="#e07836",
                    edgecolor=fundo,
                    linewidth=0.8,
                    zorder=5,
                    label="Vértice",
                )

        self.eixo.set_title("Gráfico da função quadrática", color=texto, pad=12)
        legenda = self.eixo.legend(facecolor=fundo, edgecolor=grade)
        if legenda is not None:
            for rotulo in legenda.get_texts():
                rotulo.set_color(texto)
        self.canvas.draw_idle()

    @staticmethod
    def _cores_tema(tema):
        if tema == "Escuro":
            return "#17212b", "#e8edf2", "#52606d", "#55b8a6"
        return "#ffffff", "#263442", "#cbd5df", "#176b87"