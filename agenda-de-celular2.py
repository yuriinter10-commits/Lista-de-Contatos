import time
import os

agenda = []
TEMPO = 5
  
while True:
    os.system("cls")
    print("======AGENDA======")
    print("1- Adicionar: ")
    print("2- Ver Contato: ")
    print("3- SAIR: ")

    opcao = int(input("Digite uma opcao:    "))

    if opcao == 1:
        os.system("cls")
        email=input("Digite o e-mail:   ")
        nome=input("Digite nome:   ")
        numero=input("Digite numero:   ")
    
        contato = {
        "nome": nome,
        "numero":   numero,
        "e-mail":   email 
        }
        agenda.append(contato)
        print(f"{contato['nome']} foi adicionado")
        time.sleep(3)
    
    elif opcao == 2:
        os.system("cls")
        if len(agenda) == 0:
            print("lista de contatos vazia! ")
            time.sleep(3)
            continue 
        len(agenda)
        for contato in agenda:
            print("*****LISTA DE CONTATOS*****")
                
            print(f"Nome: {contato['nome']} --- Telefone: {contato['numero']} --- E-mail: {contato['e-mail']} |")

            print("*****FIM DA LISTA DE CONTATOS*****")
            time.sleep(3)

    elif opcao == 3:
        os.system("cls")
        print("Finalizando aplicação...")
        time.sleep(3)
        break
    
    else:
        os.system("cls")
        print("Opção invalida")
        time.sleep(3)





    