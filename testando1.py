from listaencadeada import LinkedList
from no import Node
from classevoo import VOO
lista = LinkedList()

menuPrincipal = 0
menuCadastrar = 0


while True:
    menuPrincipal = (input("1. Cadastrar Viajem \n2. Exibir Conexões\n3. Sair do Programa\n\nDigite uma opção: "))
    print("\n------------------------")


    if(menuPrincipal == "1"):
        while True:
            menuCadastrar = (input("1. Cadastrar Viajem\n2. Consultar Viajem Cadastrada\n3. Retornar ao Menu Inicial\nDigite uma opção: "))
            print("\n")

            if (menuCadastrar == "1"):

                    while True:
                        origem = Node(input('Digite a Origem: '))
                        destino = Node(input('Digite um Destino: '))
                        conexao1 = Node(input('Digite a Primeira conexão: '))
                        conexao2 = Node(input('Digite a Segunda conexão: '))
                        conexao3 = Node(input('Digite a Terceira conexão: '))
                        print('Viajem Cadastrada com Sucesso!!! ')
                        break

                    lista.inicio = origem
                    origem.proximo = conexao1
                    conexao1.proximo = conexao2
                    conexao2.proximo = conexao3
                    conexao3.proximo = destino
                    print(lista)

                    lista.append(origem)
                    lista.append(conexao1)
                    lista.append(conexao2)
                    lista.append(conexao3)
                    lista.append(destino)
                                    


            elif (menuCadastrar == "3"):
                menuCadastrar = 0
                break    

    elif(menuPrincipal == "2"):
        while True:
            print('Viajem Cadastrada')
            print(lista)
            break




    elif(menuPrincipal == "2"):
        while True:


            VOO3679 = VOO('LATAM AIRLINES GROUP\n', 'Sab 15 dez 2018\n', 'SLZ\n', '17:15\n', 'São Luís\n', 'Marechal Cunha Machado\n', 'Sab 15 dez 2018\n', 'FOR\n', '18:30\n', 'Fortaleza\n', 'Pinto Martins\n', '01:15 hs\n', 'Econômica\n', '..')
            VOO3207 = VOO('LATAM AIRLINES GROUP\n', 'Sab 15 dez 2018\n', 'FOR\n', '19:45\n', 'Fortaleza\n', 'Pinto Martins\n', 'Dom 16 dez 2018\n', 'GRU\n', '00:25\n', 'São Paulo\n', 'Internacional de Guarulhos\n', '03:40 hs\n', 'Econômica\n', '..')
            VOO8194 = VOO('TAM\n', 'Dom 16 dez 2018\n', 'GRU\n', '10:45\n', 'São Paulo\n', 'Internacional de Guarulhos\n', 'Dom 16 dez 2018\n', 'MIA\n', '16:05\n', 'Miami\n', 'Internacional Miami\n', '08:20 hs\n', 'Econômica\n', '..')
            VOO2656 = VOO('AMERICAN AIRLINES\n', 'Dom 16 dez 2018\n', 'MIA\n', '19:40\n', 'Miami\n', 'Internacional Miami\n', 'Dom 16 dez 2018\n', 'BOS\n', '22:50\n', 'Boston\n', 'Internacional Logan\n', '03:10 hs\n', 'Econômica\n', 'Bagagem: 2 malas por adulto')
           
                      
            voo = input('Digite o Número do VOO!\nExemplo: VOO3679\nNº: ')
            if voo == 'VOO3679':
                print(VOO3679)

            elif voo == 'VOO3207':
                print(VOO3207)

            elif voo == 'VOO8194':
                print(VOO8194)

            elif voo == 'VOO2656':
                print(VOO2656)
            break
     

    elif(menuPrincipal == "3"):
        print("Obrigado e boa viagem!!! ")
        break   


