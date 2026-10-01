import math


class Entrada:
    def _ler_coeficiente(self, nome):
        while True:
            try:
                valor = float(input(f"Digite o coeficiente {nome}: "))
            except ValueError:
                print("Valor inválido. Digite um número.")
                continue

            if not math.isfinite(valor):
                print("O valor precisa ser um número finito.")
                continue

            if nome == "a" and valor == 0:
                print("O coeficiente a não pode ser zero.")
                continue

            return valor

    def obter_coeficientes(self):
        return (
            self._ler_coeficiente("a"),
            self._ler_coeficiente("b"),
            self._ler_coeficiente("c"),
        )