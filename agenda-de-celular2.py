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
    print("")
    opcao = int(input("Digite uma opcao:    "))

    if opcao == 1:
        os.system("cls")
        email=input("Digite o e-mail:   ")
        nome=input("Digite nome:   ")
        numero=input("Digite numero:   ")
        
        contato_clonado = False

        for contato in agenda:
            if contato['nome'].strip().lower() == nome.strip().lower():
                contato_clonado = True
                break
        if contato_clonado:
            print(f"O contato {nome} já existe!")
        
        else:    

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
            time.sleep(10)
            continue 
        
        print(f"Voce tem {len(agenda)} contatos salvos:  ")
        print("*****LISTA DE CONTATOS*****")
       
        for contato in agenda:
            print(f"Nome: {contato['nome']} --- Telefone: {contato['numero']} --- E-mail: {contato['e-mail']} |")
            
        print("*****FIM DA LISTA DE CONTATOS*****")
        time.sleep(3)          


    elif opcao == 3:
        os.system("cls")
        print("A agenda foi limpa!  ")
        time.sleep(3)
        break
    elif opcao == 0:
        os.system("cls")
        print("Finalizando aplicação...")
        time.sleep(TEMPO)
        break
   
    else:
        os.system("cls")
        print("Opção invalida")
        time.sleep(3)





    