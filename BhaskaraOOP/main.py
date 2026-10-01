from calculos import EquacaoSegundoGrau
from entrada import Entrada
from grafico import GraficoParabola
from resultados import Resultados


class AplicacaoBhaskara:
    def __init__(self):
        self.entrada = Entrada()
        self.resultados = Resultados()
        self.grafico = GraficoParabola()

    def executar(self):
        coeficientes = self.entrada.obter_coeficientes()
        equacao = EquacaoSegundoGrau(*coeficientes)
        self.resultados.exibir(equacao)
        self.grafico.mostrar(equacao)


if __name__ == "__main__":
    AplicacaoBhaskara().executar()