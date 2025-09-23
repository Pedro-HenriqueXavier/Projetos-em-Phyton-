def menu():
    print("\n--- Sistema de Cadastro de Pacientes ---")
    print("1 - Cadastrar paciente")
    print("2 - Mostrar paciente cadastrado")
    print("3 - Atender paciente")
    print("4 - Sair")
    return input("Digite o nome do paciente: ")
    
    
#Variáveis de controle
paciente = None
quantidade = 0

while True:
    opcao = menu ()

    if opcao == "1":
        produto = input("Digite o nome do paciente:  ")
        print(f"Paciente '{paciente}'  cadastrado com sucesso!")

    elif opcao == "2":
        lista = input("Mostrar paciente cadastrado: ")
        lista_de_pacientes = ["Pedro","Maria","Snow"]
        
                
    elif opcao == "3":
        if produto is None:
            print("Nenhum produto cadastrado ainda!")
        else:
            adicionar = int(input("Digite a quantidade a adicionar: "    ))
            if adicionar <= 0:
                print("A quantidade deve ser maior que zero!")
            else:
                quantidade += adicionar
                print(f"Adicionado {adicionar} unidade(s). Estoque      atual: {quantidade}")
                
    elif opcao == "4":
        if produto is None:
            print("Nenhum produto cadastrado ainda!")
        else:
            print(f"Produto: {produto} | Quantidade em estoque:         {quantidade}")
            
    elif opcao == "0":
        print("Saindo do sistema... até mais!")
        break
    
    else:
        print("Opção inválida! Tente novamente.")
