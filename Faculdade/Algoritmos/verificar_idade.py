# EXERCÍCIO: VERIFICAÇÃO DE MAIORIDADE
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Resultado: Você é MAIOR de idade.")
    print("Pode tirar a CNH.")
else:
    print("Resultado: Você é MENOR de idade.")
    print("Ainda não pode dirigir.")

# Dica de ADS: Usamos 'int()' porque idade é um número inteiro.