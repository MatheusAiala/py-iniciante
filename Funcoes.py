def perguntar():
    resposta = input("O que deseja realizar?"
                     "<I> -Para Inserir um usuário"
                     "<P> - Para Pesquisar um usuário"
                     "<E> - Para Excluir um usuário"
                     "<L> - Para Listar um usuário:").upper()
    return resposta

def inserir(dicionario):
    codigo_lancamento = input("Digite o código do lançamento: ")
    if codigo_lancamento in dicionario:
        print("Código de lançacmento já existe! Tente novamente")
        return
    login = input("Digite o login:").upper()
    nome = input("Digite o nome").upper()
    ultima_data_acesso = input("Digite a última data de acesso (dd/mm/aaaa):").upper()
    ultima_estacao = input("Qual a última estação acessada: ").upper()
    hora_login = input("Digite a hora do login:")
    nivel_usuario = input("Digite o nível de usuário:").upper()

    dicionario[codigo_lancamento] = {
        "Login": login,
        "Nome": nome,
        "Última Data de Acesso": ultima_data_acesso,
        "Última Estação": ultima_estacao,
        "Hora do Login": hora_login,
        "Nível do Usuário": nivel_usuario 
    }
    print("Usuário inserido com sucesso!")
    
def pesquisar(dicionario, chave):
    dados = dicionario.get(chave)
    if dados:
        print("\n--- Dados do Usuário ---")
        

def excluir(dicionario, chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print("Objeto Eliminado")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto.....")
        print("Login:", chave)
        print("Dados:", valor)

from datetime import date

data_atual = date.today()
print(data_atual)