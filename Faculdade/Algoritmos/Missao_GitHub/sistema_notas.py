# Sistema de Notas - Missão ADS
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

print(f"Sua média foi: {media:.1f}")

if media >= 7:
    print("Status: APROVADO 🚀")
elif media >= 5:
    print("Status: RECUPERAÇÃO ⚠️")
else:
    print("Status: REPROVADO ❌")
    