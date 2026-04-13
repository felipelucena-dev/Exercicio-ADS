import re

def contar_palavras_seguro(caminho_arquivo):
    try:
        # Abrimos com 'utf-8' para o Linux aceitar acentos
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            
            # O 're.findall' busca apenas caracteres de palavras (\w+)
            # Isso ignora pontos e vírgulas, deixando a contagem exata
            palavras = re.findall(r"\w+", conteudo.lower())
            
            return len(palavras)
            
    except FileNotFoundError:
        return "Erro: O arquivo não existe na pasta!"
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}"

# Execução do programa
nome = "texto.txt"
resultado = contar_palavras_seguro(nome)

print("-" * 30)
print(f"Relatório do Arquivo: {nome}")
print(f"Total de palavras: {resultado}")
print("-" * 30)