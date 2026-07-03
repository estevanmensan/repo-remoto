# Neste programa devo criar um sistema de caixa eletronico
# Deve conter um menu com as opções: 1- ver saldo; 2- Depositar; 3- Sacar; 4- Extrato; 5- Sair
# Regras: Saldo começa em R$1000; Não permitir saque maior que o saldo;  
#         Guardar todas as operações em uma lista; Mostrar o extrato no final
# Regra extra: impedir depósitos negativos

#Variável saldo
saldo = 1000
#Variável de Deposito
quantia_dep = 0.0
#Variável de Saque
quantia_saq = 0.0

#Variável de lista para apresentar todas as operações
lista = []
#Arquivo que armazena os resultados
open("Extrato.txt", "r", encoding="utf-8")

#Função que imprime o menu de opções para o usuário
def menu():
    print(" --------------------------------------")
    print("| Bem vindo ao Banco Mensan Ltda       |")
    print("| O que desejas?                       |")
    print(" --------------------------------------")
    print("| 1- Ver Saldo                         |")
    print("| 2- Depositar                         |")
    print("| 3- Sacar                             |")
    print("| 4- Extrato                           |")
    print("| 5- Sair                              |")
    print(" --------------------------------------")


#Função para a opção 1 - Ver Saldo
def ver_saldo():
    print(" --------------------------------------")
    print("| Opção escolhida: Ver Saldo")
    print("| Seu saldo atual é de: ")
    print(f"| R${saldo}")
    print(" --------------------------------------")
    



#Função para a opção 2 - Depositar
def obtem_deposito():
    try:
            qtd_dep = float(input("| R$ "))
    except ValueError:
        print("| Por favor, insira somente números!")
    return qtd_dep

def depositar(i):
    saldo_atualizado = saldo + i
    return saldo_atualizado

#Função para a opção 3 - Sacar
def obtem_saque():
    try:
        qtd_saque = float(input("| R$ "))
    except ValueError:
        print("| Por favor, insira somente números!")
    return qtd_saque

def sacar(saque):    
    novo_saldo = saldo - saque
    return novo_saldo
    

#Função para a opção 4 - Ver Extrato
def ver_extrato(x, y):
    texto= (
        "| \n"
        f"| Quantidade depositada: {x}\n"
        f"| Quantidade sacada: {y}\n"
        f"| Seu saldo atual é de: {saldo}\n"
        "| \n"
        "As funções selecionadas foram: \n"
        f"{lista} \n"
        " --------------------------------------\n"
    )
    print(texto)
    with open("Extrato.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(texto)
    return texto
#def gravar_extrato(x, y):
    

#Função para funcionalidades
while True:
    menu()
    #controle de entrada de dados
    try:
        opcao = int(input("->  ")) #opção do menu (entre 1 e 5)
    except ValueError: 
        print("| Você deve inserir um número inteiro")

    #condicionais para as opções do menu

    #Condicional se 'Ver Saldo' for escolhido
    if opcao == 1:
        ver_saldo()
        lista.append(f"Saldo: {saldo}")
        #print(lista)

    #Condicional se 'Depósito' for escolhido
    elif opcao == 2:
        print(" --------------------------------------") 
        print("| Opção escolhida: Depositar")
        print("| Quanto você deseja depositar? ")
        quantia_dep = obtem_deposito()
        if quantia_dep < 0:
            print("| Só é possível depositar valores acima de 0")
        else:
            depositar(quantia_dep)
            saldo=depositar(quantia_dep)
            lista.append(f"+ {quantia_dep}")
           # print(lista)

        #print(saldo)
        

    #Condicional se 'Saque' for escolhido
    elif opcao == 3:
        print(" --------------------------------------") 
        print("| Opção escolhida: Sacar")
        print("| Opção escolhida: Qual quantia você deseja sacar")
        quantia_saq = obtem_saque()
        if quantia_saq > saldo:
            print("| Valor indisponível para saque!")
        else:
            saldo = sacar(quantia_saq)
            print("| Saque efetuado com sucesso!")
            print(" --------------------------------------") 
            lista.append(f"- {quantia_saq}")
           # print(lista)
    
    #Condicional se 'Extrato' for selecionado
    elif opcao == 4:
        lista.append("Extrato escolhido - Valores apresentados na tela")
        print(" --------------------------------------\n"
              "| Opção escolhida: Extrato\n")
        
        ver_extrato(quantia_dep,  quantia_saq)
       
       # print(lista)
        

    #Condicional se 'Sair' for selecionado
    elif opcao == 5:
        lista.append("Sair escolhido - Usuário se desconectou")
        print(" --------------------------------------")
        print("| Opção escolhida: Sair")
        ver_extrato(quantia_dep, quantia_saq)
        #print(lista)
        print("| Obrigado por escolher nossos serviços!")
        print(" --------------------------------------") 
        break

    #Condicional se for inserido valor diferente dos apresentados no menu
    else:
        print("Por favor, insira um dos valores apresentados no menu!")

