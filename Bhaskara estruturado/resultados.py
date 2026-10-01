def exibir_resultados(a, b, c, delta, raizes, vertice, pontos):
    print("\nResultados da equação:")
    print(f"Equação: {a:g}x² + ({b:g})x + ({c:g}) = 0")
    print(f"Delta: {delta:g}")

    if delta > 0:
        print(f"Duas raízes reais: x1 = {raizes[0]:g}, x2 = {raizes[1]:g}")
    elif delta == 0:
        print(f"Uma raiz real (raiz dupla): x = {raizes[0]:g}")
    else:
        print(f"Duas raízes complexas: x1 = {raizes[0]}, x2 = {raizes[1]}")

    print(f"Vértice: ({vertice[0]:g}, {vertice[1]:g})")
    print("Pontos da parábola (amostra):")

    indices = sorted({0, len(pontos) // 4, len(pontos) // 2, 3 * len(pontos) // 4, len(pontos) - 1})
    for indice in indices:
        x, y = pontos[indice]
        print(f"  ({x:.3f}, {y:.3f})")