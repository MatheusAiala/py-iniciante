from datetime import date, datetime

# nome=input("Digite um funcionário: ")
# empresa=input("Digite a instituição: ")
# qtde_funcionarios=int(input("Digite a qtde de funcionários: "))
# mediaMensalidade=float(input("Digite a média da mensalidade: "))
# print(nome + "trabalha na empresa" + empresa)
# print("A média da mensalidade é de " + str(mediaMensalidade))
# print("---------------Verifique os tipos ee dados abaixo----------------")
# print("O tipo de dado da variavel [nome] é: ",type(nome))
# print("O tipo de dado da variavel [empresa] é:",type(empresa))
# print("O tipo de dado da variavel [qtde_funcionarios] é: ",type(qtde_funcionarios))
# print("O tipo de dado da variavel [mediaMensalidade] é: ",type(mediaMensalidade))

# # -----------------IF ELSE----------------------------------------------

# nome=input("Digite o nome:")
# idade=int(input("Digite a idade:"))
# doenca_infectocontagiosa= input("Suspeita de doença infectocontagiosa?").upper()
# if idade >=65:
#     print("O paciente " + nome + " POSSUI atendimento prioritário!")
# elif doenca_infectocontagiosa=="SIM":
#     print("O paciente " + nome + " Deve ser direcionado para sala espera reserva.")    
# else:
#     print("O paciente " + nome + " NÃO possui atendimento prioritário e pode aguarda na sala comum!")  

# # ----------------------------------WHILE-------------------------------------

# numero=int(input("Digite um numero: "))
# while numero<100:
#     print("\t" + str(numero))
#     numero=numero+1
# print("Laços encerrado...")    

# # -----------------------------------FOR-----------------------------------------

# tabua=int(input("Digite um numero para exibir a tabuada: "))
# print("Tabuada do número", tabua)
# for valor in range(1, 11, 1):
#     print (str(tabua) + " x " + str(valor) + " = " + str(tabua*valor))

# # ------------------------------------LISTA-----------------------------------------

# invertario=[]
# resposta="S"
# while resposta=="S":
#     invertario.append(input("Equipamento: "))
#     invertario.append(float(input("Valor: ")))
#     invertario.append(int(input("Numero Serial: ")))
#     invertario.append(input("Departamento: "))
#     resposta=input("Digite \"s\" para continuar: ").upper()

# for elemento in invertario:
#     print (elemento)    

# # ------------------------------------LISTA COMPOSTA------------------------------------

# equipamentos = []
# valores = []
# seriais = []
# departamentos = []
# resposta="S"
# while resposta=="S":
#     equipamentos.append(input("Equipamento: "))
#     valores.append(float(input("Valor: ")))
#     seriais.append(int(input("Numero Serial: ")))
#     departamentos.append(input("Departamento: "))
#     resposta=input("Digite \"s\" para continuar: ").upper()

# for indice in range(0, len(equipamentos)):
#     print ("\nEquipamento..: ", (indice+1))
#     print ("Nome...........: ", equipamentos[indice])
#     print ("Valor...........: ", valores[indice])
#     print ("Serial...........: ", seriais[indice])
#     print ("Departamento.: ", departamentos[indice])    

# # ------------------------------------LISTA COMPOSTA------------------------------------

# equipamentos = []
# valores = []
# seriais = []
# departamentos = []
# resposta="S"
# while resposta=="S":
#     equipamentos.append(input("Equipamento: "))
#     valores.append(float(input("Valor: ")))
#     seriais.append(int(input("Numero Serial: ")))
#     departamentos.append(input("Departamento: "))
#     resposta=input("Digite \"s\" para continuar: ").upper()

# busca=input("\nDigite o nome do equipamento que seja buscar: ")
# for indice in range(0, len(equipamentos)):
#     if busca==equipamentos[indice]:
#         print("Valor..: ", valores[indice])
#         print("Serial.:", seriais[indice])

# # ------------------------------------LISTA COMPOSTA2------------------------------------

# inventario = []
# resposta = "S"

# while resposta == "S":
#     equipamento = input("Equipamento: ")
#     valor = float(input("Valor: "))
#     serial = int(input("Numero Serial: "))
#     departamento = input("Departamento: ")
#     inventario.append([equipamento, valor, serial, departamento])
#     resposta = input("Digite \"s\" para continuar: ").upper()

# for elemento in inventario:
#     print("\nNome..........: ", elemento[0])
#     print("Valor.........: ", elemento[1])
#     print("Serial........: ", elemento[2])
#     print("Departamento..: ", elemento[3])

# busca = input("\nDigite o nome do equipamento que deseja buscar: ")
# for elemento in inventario:
#     if busca == elemento[0]:
#         print("Valor..: ", elemento[1])
#         print("Serial..: ", elemento[2])

# depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")
# for elemento in inventario:
#     if depreciacao == elemento[0]:
#         print("Valor antigo: ", elemento[1])
#         elemento[1] = elemento[1] * 0.9
#         print("Novo valor: ", elemento[1])

# serial = int(input("\nDigite o serial do equipamento que será excluído: ")) 
# for elemento in inventario:
#     if elemento[2] == serial:
#         inventario.remove(elemento)

# for elemento in inventario:
#     print("\nNome..........: ", elemento[0])
#     print("Valor.........: ", elemento[1])
#     print("Serial........: ", elemento[2])
#     print("Departamento..: ", elemento[3])

# valores = [elemento[1] for elemento in inventario]
# if len(valores) > 0:
#     print("\nO equipamento mais caro custa: ", max(valores))
#     print("O equipamento mais barato custa: ", min(valores))
#     print("O total de equipamentos é de: ", sum(valores))

# # ---------------------------------------------------------------------------------------

# def preencherInventario(lista):
#   resp="S"
#   while resp == "S":
#     equipamento=[input("Equipamento: "),
#               float(input("Valor: ")),
#               int(input("Número Serial: ")),
#               input("Departamento: ")]
#     lista.append(equipamento)
#     resp = input("Digite \"S\" para continuar: ").upper()

# def exibirInventario(lista):
#   for elemento in lista:
#     print("Nome.........: ", elemento[0])
#     print("Valor........: ", elemento[1])
#     print("Serial.......: ", elemento[2])
#     print("Departamento.: ", elemento[3])

# def localizarPorNome(lista):
#   busca=input("Digite o nome do equipamento que deseja buscar:")
#   for elemento in lista:
#     if busca==elemento[0]:
#      print("Valor.: ", elemento[1])
#      print("Serial.:", elemento[2])

# # ---------------------------------------------------------------------------------------------    

# usuarios={}
# usuarios={
#     "Chaves":["Chaves Silva","17/06/1975","Recep_01"],
#     "Quico":["Enrico Flores","03/06/1976","Raiox_02"],
#     "Quico":["Enrico Flores","03/06/1976","Raiox_3"]
# }  


# usuarios["Florinda"]=["Florinda Flores", "26/11/2017", "Recep_01"]
# usuarios["Florinda"]=["Florinda Flores", "26/11/2016", "Recep_01"]

# print(usuarios)
# print("################===========#############")
# print("Dados: ",usuarios.get("Chaves"))

# --------------------------------------------PARTE 1-----------------------------------------------

# usuarios[input("Digite o login: ").upper()]=[input("Digite o nome: ").upper(),
#                  input("Digite a última data de acesso: "),
#                  input("Qual a última estação acessada: ").upper()]

usuarios={}
opcao=input("O que deseja realizar?", "<I> para inserir","<P> para perquisar","<E> para excluir", "<L> para listar um usuario").upper()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
   if opcao=="I":
    chave=input("Digite o login").upper()
    usuarios["Chaves"] = [input("Digite o nome: ").upper(),
                          input("Digite a pultima data de acesso: "),
                          input("Qual a última estação acessada: ").upper()]  
opcao=input("O que deseja realizar?", "<I> para inserir","<P> para perquisar","<E> para excluir", "<L> para listar um usuario").upper()

from Funcoes import *
usuarios={}

opcao=perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":

    if opcao=="I":
       inserir(usuarios)

    if opcao == "P": 
       perguntar(usuarios,input("Qual login desejar pesquisar?"))

    if opcao == "E":
        excluir(usuarios,input("Qual login deseja excluir?"))

    if opcao == "L":
       listar(usuarios)
    opcao = perguntar()  

