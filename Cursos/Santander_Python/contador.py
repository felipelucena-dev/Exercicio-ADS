with open("texto.txt", "r") as arquivo:
    texto = arquivo.read()
    palavras = texto.split()
    print(f"Total de palavras: {len(palavras)}")