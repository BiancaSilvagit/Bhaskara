import matplotlib.pyplot as plt

from calculos import ponto_esta_no_eixo_x


def mostrar_grafico(a, b, c, raizes, vertice, pontos):
    valores_x = [ponto[0] for ponto in pontos]
    valores_y = [ponto[1] for ponto in pontos]

    plt.figure(figsize=(9, 6))
    plt.plot(valores_x, valores_y, label=f"y = {a:g}x² + ({b:g})x + ({c:g})")
    plt.scatter(*vertice, color="darkorange", zorder=3, label="Vértice")

    raizes_reais = [raiz.real if isinstance(raiz, complex) else raiz
                    for raiz in raizes if ponto_esta_no_eixo_x(raiz)]
    if raizes_reais:
        plt.scatter(raizes_reais, [0] * len(raizes_reais), color="seagreen", zorder=3, label="Raiz(es) real(is)")

    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Gráfico da função quadrática")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()