# --- MEU PRIMEIRO SCRIPT DE LÓGICA ---

# 1. Definindo as variáveis (a "memória" do programa)
status_louca = "limpa"  # Mude para "limpa" quando terminar a tarefa
aula_revisada = 2

print("--- VERIFICAÇÃO DO DIA ---")

# 2. Criando a lógica de decisão
if status_louca == "limpa":
    print("Sucesso! A louça está ok.")
    print(f"Você já revisou {aula_revisada} aulas. Pode ir para a próxima!")
else:
    print("Atenção: A pia ainda tem trabalho.")
    print("Lave a louça primeiro para manter o foco nos estudos!")

# 3. Exibindo o encerramento
print("---------------------------")
# Minhas Soft Skills para desenvolver em ADS
soft_skills = ["Comunicação", "Resiliência", "Inteligência Emocional"]

print("\n--- MINHA EVOLUÇÃO ---")
for skill in soft_skills:
    print(f"Eu estou desenvolvendo a habilidade: {skill}")
