# EXERCÍCIO DE MÉDIA (ADS)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print(f"\nMédia: {media}")

# Lógica com o operador OR (OU)
if media >= 7 or nota1 > 0:
    print("Situação: APROVADO")
elif media >= 5:
    print("Situação: EXAME")
else:
    print("Situação: REPROVADO")