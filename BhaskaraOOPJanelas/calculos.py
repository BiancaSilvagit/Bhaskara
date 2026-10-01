import cmath
import math


class EquacaoSegundoGrau:
    """Representa uma equação quadrática e realiza seus cálculos."""

    def __init__(self, a, b, c):
        if not all(math.isfinite(valor) for valor in (a, b, c)):
            raise ValueError("Os coeficientes precisam ser números finitos.")
        if a == 0:
            raise ValueError("O coeficiente a não pode ser zero.")

        self.a = a
        self.b = b
        self.c = c

    def calcular_delta(self):
        return self.b**2 - 4 * self.a * self.c

    def calcular_raizes(self):
        delta = self.calcular_delta()
        raiz_delta = cmath.sqrt(delta)
        x1 = (-self.b + raiz_delta) / (2 * self.a)
        x2 = (-self.b - raiz_delta) / (2 * self.a)

        if delta >= 0:
            return x1.real, x2.real
        return x1, x2

    def calcular_vertice(self):
        x_vertice = -self.b / (2 * self.a)
        y_vertice = -self.calcular_delta() / (4 * self.a)
        return x_vertice, y_vertice

    def calcular_pontos(self, x_min, x_max, quantidade):
        if not math.isfinite(x_min) or not math.isfinite(x_max):
            raise ValueError("Os limites do eixo x precisam ser números finitos.")
        if x_min >= x_max:
            raise ValueError("O início do intervalo de x deve ser menor que o fim.")
        if quantidade < 2:
            raise ValueError("A quantidade de pontos deve ser pelo menos 2.")

        passo = (x_max - x_min) / (quantidade - 1)
        return [
            (x, self.a * x**2 + self.b * x + self.c)
            for x in (x_min + indice * passo for indice in range(quantidade))
        ]