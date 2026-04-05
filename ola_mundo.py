print("Olá, mundo")
# 1. Definimos a variável com o valor desejado
numero = 7

# 2. Usamos o 'if' (se) para verificar o resto da divisão por 2
# O símbolo % calcula o resto. Se o resto for 0, o número é par.
if numero % 2 == 0:
    resultado = "Par"
else:
    # 3. O 'else' (senão) trata todos os outros casos (quando o resto é 1)
    resultado = "Impar"

# 4. Exibimos o resultado final no terminal
print(resultado)
