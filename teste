from dataclasses import dataclass
from datetime import datetime

@dataclass
class Publicacao:
    conteudo: str
    descricao: str
    autor: str
    data_hora: datetime
    curtidas: int = 0
    
lista_publicacoes = []

def criar_publicacao():
    print("\n=== CRIAR PUBLICAÇÃO ===")
    conteudo = input("Digite o conteúdo da publicação: ")
    descricao = input("Digite a descrição: ")
    autor = input("Digite o nome do autor: ")
    data_hora = datetime.now()
    
    nova_publicacao = Publicacao(conteudo, descricao, autor, data_hora)
    lista_publicacoes.appennd(nova_publicacao)
    print("Publicação criada com sucesso!")
    
def curtir_publicacao():
    print("\n=== CURTIR PUBLICAÇÃO ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return
    
    visualizar_feed()
    try:
        indice = int(input("Digite o número da publicação para curtir: ")) - 1
        if 0 <= indice < len(lista_publicacoes):
            lista_publicacoes[indice].curtidas += 1
            print("Publicação curtida!")
        else:
            print("Publicação não encontrada.")
        except ValuError:
            print("Número inválido.")
            
        def visualizar_feed():    
            print("\n=== FEED ===")
            if not lista_publicacoes:
                print("Nenhuma publicação disponível.")
                return
            
            for i, pub in enumerate(lista_publicacoes, 1):
                print(f"{i}. {pub.autor} - {pub.curtidas} curtidas")
                print(f"  {pub. conteudo[:50]}...")
                {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
