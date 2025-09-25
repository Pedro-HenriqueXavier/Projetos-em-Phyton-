from dataclasses import dataclass
from datetime import datetime
#1.O sistema precisa ter agendamento onde o cliente escolhe o barbeiro
#2.O sistema precisa ter cadastro da agenda do barbeiro
#4.O sistema precisa ter cadastro de cliente 
#6.O sistema precisa ter reagendamento. 
#7.O sistema precisa ter um lembrete via email para o cliente
#8.O sistema precisa ter o faturamento da barbearia no mês

@dataclass
class Pessoa:
    nome:str
    celular:str
    email:str
    
lista_pessoas = ["João", "Pedro"]
@dataclass
class Barbeiro:
    nome:str
    disponibilidade:str
    complemento:str
    horario:str
    corte:str
    
lista_nome_barbeiros = ["Thiago", "Ademar", "Marcos"]
@dataclass
class Agendamento:
    data:str
    hora:str
    barbeiro:str
    
lista_horarios = ["10h", "11h", "14h", "15h30", "16h"]
@dataclass
class Serviços:
    corte:str
    barba:str
    sobrancelha:str
    
lista_serviços = ["corte", "barba", "sobrancelha"]

lista_cortes = ["Social", "Careca", "Americano", "Asa delta"]
lista_barba = ["Barba cheia", "Curta", "Italiana", "Por fazer"]
lista_sombrancelha = ["Risquinho", "nenhuma"]

def agendar():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    barbeiro = input("Escolha seu barbeiro: ")
    data = input("Digite a data desejada: ")
    hora = input("Digite seu horario: ")
    celular = input("Qual seu contato: ")
    cliente_digitado = cliente(nome,email,celular)
    lista.append(cliente_digitado)
    print("Cadastro realizado com sucesso")
    
def menu():
    print("1 - Cadastrar agendamento")
    print("2 - Ver serviços")
    print("3 - Preço do serviço ")
    print("4 - Ver horario disponivel")
    print("5 - Ver clientes cadastrados")
    print("6 - Sair")
    return input("Escolha uma opção: ")
#variaveis de controle


while True:
    opcao = menu()
        
    if opcao == "1":
        nome = input("Nome do cliente: ")
        contato = input("Inserir contato: ")
        email = input("Digite seu email: ")
        cliente = Pessoa(nome,contato,email)
        lista_pessoas.append(cliente)
        data = input("Inserir data: ")
        hora = input("Digite o horário: ")
        barbeiro = input("Escolha seu barbeiro: ")
        servico = input("Tipo de serviço: ")
        agendamento = Agendamento(data,hora,barbeiro)
        lista_serviços.append(agendamento)    
        print(f"agendamento '{agendamento}' agendado com sucesso!")
        
    if opcao == "2":
        corte = input("Corte: ")
        barba = input("Barba: ")
        sobrancelha = input("Sobrancelha: ")
        print("Serviço confirmado!")
        
    if opcao == "3":
        valor_do_corte=40
        print(f"O valor do corte é R$ {valor_do_corte},00")
        valor_da_barba=20
        print(f"O valor da barba é R$ {valor_da_barba},00")
        valor_da_sobrancelha=10
        print(f"O valor da sobrancelha é R$ {valor_da_sobrancelha},00")
        
    if opcao == "4":
        print("Horários disponíveis: ")
        for horario in lista_horarios:
            print(horario)
        escolher = input("Escolha o horário: ")
        if escolher in lista_horarios:
            print(f"Você escolheu o horário {escolher}. Agendamento feito!")
            
    if opcao == "5":
        print("\n--- Ver clientes cadastrados ---")
        if not lista_pessoas:
            print("Ainda não há clientes cadastrados!")
        else:
            for cliente in lista_pessoas:
                print(f" {cliente}")
                
        print("Esses são os clientes cadastrados.")
        
