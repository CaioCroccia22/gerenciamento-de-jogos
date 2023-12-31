#Exercicio final do módulo
#Gerenciamento de jogadores e times
# -> Escreva um código em python que realize o gerenciamento de jogadores
#Siga os requisitos:
#1 - A opção de listar os times deve mostrar o indice , o nome e a quantindade de jogadores
#2 - A opção de adicionar um time deve pedir um nome para o time que será cadastrado
#3 - A opção de remover um time deve pedir o indice especifico do time que foi cadastrado
#4 - A opção de adicionar um jogador em um time deve pedir um indice do time que foi cadastrado
#5 - A opção de remover um jogador em um time deve pedir um indice do time que foi cadastrado e utilizar
#esse indice para remover o jogador cadastrado no time
#6 - A opção de listar os jogadores de um time deve ser informado o indice de um time
# e listar os jogadores que foram associados a ele.

teams = {}
team = {}

done = False

def plusTeam():
    name = input("Digite o nome do time:\n")
    players = input("Digite o números de jogadores\n")
    team["name"] = name
    team["players"] = players
    teams["Team"] = team

#Função que lista os times
def listTeam():
    #enumerate - ter acesso ao indice de um determinado valor do dicionario
    for i, team in enumerate(teams.values()):
        print(f"{i+1}, {team['name']} ({len(team['players'])} jogadores)")
    

def listPlayers(team):
    print(f"Jogadores do {team['name']}")
    for i, players in enumerate(team['players']):
        print(f"{i+1}.{players}")


while done == False:
    print("Escolha umas das opções a seguir:\n")
    print("1 - Voce deseja adicionar algum time? \n")
    print("2 - Voce deseja remover algum time? \n")
    print("3 - Voce deseja listar os time? \n")
    print("4 - Voce deseja adicionar jogador do time? \n")
    print("5 - Voce deseja remover jogador do time? \n")
    print("6 - Voce deseja listar os jogadores de um time? \n")
    print("7 - Sair \n")
    choices = input(">")
    if choices == "1":
        team_name = input("Digite o nome do time:\n")
        teams[team_name] = {'name': team_name, 'players': [] }
        print("Time adicionado.")
    elif choices == "2":
        listTeam()
        team_num = int(input("Digite o número do time que deseja remover: \n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            del teams[team_name]
            print("Time já foi removido")
        else:
            print("número inválido")
    elif choices == "3":
        listTeam()
    elif choices == "4":
        listTeam()
        team_num = int(input("Digite o número do time que deseja adicionar o jogador: \n"))
        if team_num <= len(teams):
            #armazena na variavel o time desejado pelo usuario por meio do indice
            team_name = list(teams.keys())[team_num - 1]
            players_name = input("Digite o nome do jogador: \n")
            teams[team_name]['players'].append(players_name)
            print("Jogador adicionado no time")
        else:
            print("Time inválido!!")

    elif choices == "5":
        listTeam()
        team_num = int(input("Digite o número do time que deseja remover o jogador: \n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            listPlayers(teams[team_name])
            player_num = int(input("Informe o número do jogador que deseja remover"))
            if player_num <= len(teams[team_name]['players']):
                del teams[team_name]['players'][player_num - 1]
            else:
                print("número do jogador inválido")
        else:
            print("número do time inválido")

    elif choices == "6":
        team_num = int(input("Digite o número do time que deseja listar os jogadores: \n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            #É passado como parametro na função o dicionário e o subdicionário
            listPlayers(teams[team_name])
        else:
            print("número de time inválido")
    elif choices == "7":
        done = True
    else:
        print("Opção inválida")