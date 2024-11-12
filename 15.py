''' Cálculo de Médias de Alunos

Faça um programa que leia uma sequência de nomes de alunos de uma turma, terminada por "FIM", além de suas duas notas (entre 0 e 10).

Para cada aluno, o programa deve informar:
Média do aluno
Se o aluno está aprovado ou em prova final (Média ≥ 6 = Aprovado).
Ao final, o programa deve mostrar a média geral da turma.
Utilize a função de arredondamento para exibir as médias.
Implemente as funções:
Entrada do nome e das notas.
Cálculo da média do aluno.
Cálculo da média da turma.'''



def entrada_aluno():
    '''Função para entrada de dados do aluno, incluindo nome e notas.
    
        Recebe: string e 2 números
        
        Retorna: tuple: (nome, nota1, nota2) ou (None, None, None) se o nome for FIM '''


    nome = input("Digite o nome do aluno (ou 'FIM' para terminar): ").upper()
    if nome == "FIM":
        return None, None, None  
    
    nota1 = float(input(f"Digite a primeira nota de {nome}: "))
    nota2 = float(input(f"Digite a segunda nota de {nome}: "))
    return nome, nota1, nota2



def media_aluno(nota1, nota2):
    ''' Função para calcular a média do aluno.

        Parâmetros: a primeira e segunda nota (num)
        
        Retorna: float: A média das duas notas
    '''
    media = (nota1 + nota2) / 2
    return media



def media_turma(somas, total_alunos):
    '''Função para calcular a média geral da turma.

        Parâmetros: a soma das notas (num)
        
        Retorna: float: A média das notas da turma
    '''
    media = somas / total_alunos
    return media



def status(media):
    '''Função para determinar o status do aluno com base na sua média.

        Parâmetros: media (float): A média do aluno.
        
        Retorna: (string) aprovado se for maior que ou igual que 6, em recuperação se for menor que 6
    '''
    if media >= 6:
        return "aprovado"
    else:
        return "Em Recuperação"



def principal():
    '''Função principal que gerencia a entrada de dados, cálculos e exibição dos resultados.
    '''
    total_alunos = 0
    soma_notas = 0

    while True:
        nome, nota1, nota2 = entrada_aluno()

        if nome is None:
            break

        media = media_aluno(nota1, nota2)
        soma_notas += media
        total_alunos += 1

        aluno_status = status(media)

        print(f"Média do aluno {nome}: {media:.2f}")
        print(f"Status do aluno {nome}: {aluno_status}")
        print("-" * 20)
    
    if total_alunos > 0:
        media_geral = media_turma(soma_notas, total_alunos)
        print(f"\nMédia geral da turma: {media_geral:.2f}")
        print(f"Total de alunos: {total_alunos}")
    else:
        print("\nNenhum aluno foi registrado.")

principal()