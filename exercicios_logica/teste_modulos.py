import math
import datetime
import random

# 1. Usando DATETIME (Data e Hora)
agora = datetime.datetime.now()
data_formatada = agora.strftime("%d/%m/%Y às %H:%M:%S")

# 2. Usando MATH (Matemática)
numero = 81
raiz = math.sqrt(numero)

# 3. Usando RANDOM (Aleatório)
senha_gerada = random.randint(1000, 9999)

print("-" * 30)
print(f"Relatório gerado em: {data_formatada}")
print(f"A raiz quadrada de {numero} é: {raiz}")
print(f"Sua senha aleatória de hoje: {senha_gerada}")
print("-" * 30)
