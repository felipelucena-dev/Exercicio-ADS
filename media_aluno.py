# Entrada de dados (O que o usuário digita)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Processamento (A conta que o computador faz)
media = (nota1 + nota2) / 2

# Saída com Condicional (O coração da lógica de programação)
print(f"Sua média foi: {media}")

if media >= 7 and nota1 > 0:
    print("Situação: APROVADO")
elif media >= 5:
    print("Situação: EXAME")
else:
    print("Situação: REPROVADO")