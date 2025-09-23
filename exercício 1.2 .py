#Exercicio 1.2
#Bilheteria de evento com apenas 1 evento
#1. Cadastrar nome do evento.
#2. Vender ingressos (Verificar se há ingressos suficientes).
#3. Repor ingressos (Quantidade >0).
#4. Ver ingressos disponíveis.



def menu():
    print("\n--- Evento ufc 253---")
    print("1 - Nome do evento")
    print("2 - Vender ingressos")
    print("3 - Repor ingressos")
    print("4 - Ingressos disponiveis")
    print("0 - Sair")
    return input("escolha um ingresso")
    
    
    #Variáveis de controle
produto = None
quantidade = 0

while True:
    opcao = menu ()

    if opcao == "1":
        produto = input("Digite o nome do produto:  ")
        quantidade = 0
        print(f"Ingresso '{ingresso}' ingrersso com sucesso!")

    elif opcao == "2":
        if produto is None:
            print("Nenhum ingresso cadastrado ainda!")
        else:
            retirar = int(input("Digite a quantidade a retirar: "))
            if retirar <= 0:
                print("A quantidade deve ser maior que zero!")
            elif retirar > quantidade:
                print("Ingresso insuficiente no estoque!")
            else:
                quantidade -= retirar
                print(f"Retirado {retirar} unidades(s). Estoque atual: {quantidade}")
                
    elif opcao == "3":
        if produto is None:
            print("Nenhum ingresso cadastrado ainda!")
        else:
            adicionar = int(input("Digite a quantidade a adicionar: "    ))
            if adicionar <= 0:
                print("A quantidade deve ser maior que zero!")
            else:
                quantidade += adicionar
                print(f"Adicionado {adicionar} unidade(s). Estoque      atual: {quantidade}")
                
    elif opcao == "4":
        if produto is None:
            print("Nenhum produto ingresso ainda!")
        else:
            print(f"Ingresso: {ingresso} | Quantidade em estoque:         {quantidade}")
            
    elif opcao == "0":
        print("Saindo do sistema... até mais!")
        break
    
    else:
        print("Opção inválida! Tente novamente.")

