def calcular_quadrados(n):
    resultados = []  # <--- ESSA LINHA É O SEGREDO! Ela cria a lista vazia.
    for i in range(n):
        quadrado = i * i
        resultados.append(quadrado)
    return resultados

# Para você ver o resultado no terminal:
print(f"Resultado final: {calcular_quadrados(5)}")