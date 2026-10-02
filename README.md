# Calculadora de Bhaskara

Este repositório reúne três implementações para resolver equações do segundo grau e visualizar a parábola: uma versão estruturada com funções, uma versão orientada a objetos para terminal e uma versão orientada a objetos com interface gráfica.

## Pré-requisitos

- Python 3.11.
- Matplotlib para gerar os gráficos.
- Tkinter, incluído normalmente na instalação padrão do Python para Windows, para a versão com interface gráfica.

No PowerShell, instale o Matplotlib uma vez para o Python 3.11:

```powershell
py -3.11 -m pip install matplotlib
```

Os comandos abaixo pressupõem que o terminal está na raiz deste repositório. Se o Python 3.11 ainda não estiver instalado, instale-o antes de executar os comandos.

## Como executar

### Bhaskara Estruturado

Implementação modular com funções, sem classes. A entrada e validação, os cálculos, a apresentação dos resultados e o gráfico ficam em módulos separados.

```powershell
py -3.11 ".\Bhaskara estruturado\main.py"
```

### Bhaskara OOP

Implementação orientada a objetos executada no terminal. A classe `EquacaoSegundoGrau` concentra os cálculos; as demais classes cuidam da entrada, dos resultados, do gráfico e da coordenação.

```powershell
py -3.11 .\BhaskaraOOP\main.py
```

### BhaskaraOOPJanelas

Implementação orientada a objetos com janela Tkinter. Permite configurar os coeficientes, o intervalo de x, a quantidade de pontos, o tema, a grade e a exibição de raízes e vértice. O gráfico Matplotlib é exibido dentro da janela.

```powershell
py -3.11 .\BhaskaraOOPJanelas\main.py
```

## Comparação

| Versão | Organização | Interação | Gráfico |
|---|---|---|---|
| Bhaskara Estruturado | Funções distribuídas em módulos | Terminal | Janela do Matplotlib |
| Bhaskara OOP | Classes distribuídas em módulos | Terminal | Janela do Matplotlib |
| BhaskaraOOPJanelas | Classes, com cálculos separados da interface | Interface Tkinter | Matplotlib integrado à janela |

A versão estruturada destaca a separação das tarefas por funções. A versão OOP agrupa dados e operações em classes, mantendo a execução simples no terminal. A versão com janelas reutiliza a abordagem orientada a objetos e acrescenta controles visuais para ajustar e explorar o gráfico.
