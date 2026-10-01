import cmath
import math


class EquacaoSegundoGrau:
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
        delta = self.calcular_delta()
        x_vertice = -self.b / (2 * self.a)
        y_vertice = -delta / (4 * self.a)
        return x_vertice, y_vertice

    def calcular_pontos(self, quantidade=101):
        if quantidade < 2:
            raise ValueError("A quantidade de pontos deve ser pelo menos 2.")

        delta = self.calcular_delta()
        x_vertice, _ = self.calcular_vertice()
        meia_largura = 5.0

        if delta >= 0:
            x1, x2 = self.calcular_raizes()
            meia_largura = max(
                meia_largura,
                abs(x1 - x_vertice),
                abs(x2 - x_vertice),
            ) * 1.5

        inicio = x_vertice - meia_largura
        passo = 2 * meia_largura / (quantidade - 1)
        return [
            (x, self.a * x**2 + self.b * x + self.c)
            for x in (inicio + indice * passo for indice in range(quantidade))
        ]