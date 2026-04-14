# Exercício de Fixação - Aula 3 ADS
def verificar_aprovacao():
    print("--- Sistema de Notas da Faculdade ---")
    
    try:
        # 1. Abstração: Só importam os valores numéricos
        nota1 = float(input("Digite a nota da primeira prova: "))
        nota2 = float(input("Digite a nota da segunda prova: "))
        
        # 2. Processamento (Algoritmo)
        media = (nota1 + nota2) / 2
        
        # 3. Tomada de Decisão (Padrões)
        if media >= 6:
            status = "APROVADO"
        else:
            status = "EM EXAME"
            
        print(f"\nMédia final: {media:.1f}")
        print(f"Status do aluno: {status}")
        
    except ValueError:
        print("Erro: Por favor, use números e utilize o ponto (.) para decimais.")

verificar_aprovacao()
