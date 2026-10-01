import cmath
import math


def calcular_delta(a, b, c):
    return b**2 - 4 * a * c


def calcular_raizes(a, b, c, delta=None):
    if delta is None:
        delta = calcular_delta(a, b, c)

    raiz_delta = cmath.sqrt(delta)
    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)

    if delta >= 0:
        return x1.real, x2.real
    return x1, x2


def calcular_vertice(a, b, c, delta=None):
    if delta is None:
        delta = calcular_delta(a, b, c)

    x_vertice = -b / (2 * a)
    y_vertice = -delta / (4 * a)
    return x_vertice, y_vertice


def calcular_pontos(a, b, c, quantidade=101):
    if quantidade < 2:
        raise ValueError("A quantidade de pontos deve ser pelo menos 2.")

    delta = calcular_delta(a, b, c)
    x_vertice, _ = calcular_vertice(a, b, c, delta)
    meia_largura = 5.0

    if delta >= 0:
        x1, x2 = calcular_raizes(a, b, c, delta)
        meia_largura = max(meia_largura, abs(x1 - x_vertice), abs(x2 - x_vertice)) * 1.5

    inicio = x_vertice - meia_largura
    passo = (2 * meia_largura) / (quantidade - 1)
    return [
        (x, a * x**2 + b * x + c)
        for x in (inicio + indice * passo for indice in range(quantidade))
    ]


def ponto_esta_no_eixo_x(raiz):
    return math.isclose(raiz.imag, 0.0, abs_tol=1e-12) if isinstance(raiz, complex) else True