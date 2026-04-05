preco = float(input("Digite o valor da compra: R$ "))

# Início da Escada de Descontos
if preco <= 100:
    desconto = 0
elif preco <= 200:
    desconto = 10
elif preco <= 300:
    desconto = 20
elif preco <= 400:
    desconto = 30
elif preco <= 500:
    desconto = 40
else:
    desconto = 50

# Cálculo do valor com desconto
# (Se o desconto é 10%, você paga 90%, ou seja, 1 - 0.10)
valor_final = preco * (1 - desconto/100)

print(f"Desconto de {desconto}% aplicado.")
print(f"Total a pagar: R$ {valor_final:.2f}")