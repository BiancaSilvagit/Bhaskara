import math

import matplotlib.pyplot as plt


class GraficoParabola:
    def mostrar(self, equacao):
        pontos = equacao.calcular_pontos()
        valores_x = [ponto[0] for ponto in pontos]
        valores_y = [ponto[1] for ponto in pontos]
        raizes = equacao.calcular_raizes()
        vertice = equacao.calcular_vertice()

        plt.figure(figsize=(9, 6))
        plt.plot(
            valores_x,
            valores_y,
            label=f"y = {equacao.a:g}x² + ({equacao.b:g})x + ({equacao.c:g})",
        )
        plt.scatter(*vertice, color="darkorange", zorder=3, label="Vértice")

        raizes_reais = [
            raiz.real if isinstance(raiz, complex) else raiz
            for raiz in raizes
            if not isinstance(raiz, complex) or math.isclose(raiz.imag, 0.0, abs_tol=1e-12)
        ]
        if raizes_reais:
            plt.scatter(
                raizes_reais,
                [0] * len(raizes_reais),
                color="seagreen",
                zorder=3,
                label="Raiz(es) real(is)",
            )

        plt.axhline(0, color="black", linewidth=0.8)
        plt.axvline(0, color="black", linewidth=0.8)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Gráfico da função quadrática")
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.legend()
        plt.tight_layout()
        plt.show()