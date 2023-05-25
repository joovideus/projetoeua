from funcoes import limp, aguarde
while True:
    limp()
    print("(0) Sair")
    print("(1) Incluir Alunos")
    print("(2) Mostrar Lista")
    print("(3) Deletar todos os registros")
    opcao = input()
    if opcao == "0":
        break
    elif opcao == "1":
        nome = input("Nome: ")
        email = input("E-mail:")
        arquivo = open("bd.atitus","a") #w  write # r read # a append
        arquivo.write(nome+" "+email+"\n")
        arquivo.close()
        print("Dados Salvos")
        aguarde(5)
    elif opcao == "2":
        try:
            arquivo = open("bd.atitus","r")
            dados = arquivo.read()
            print(dados)
            arquivo.close()
            aguarde(5)
        except:
            print("Banco de Dados não localizado!")
            print("Estamos criando um para vc!")
            arquivo = open("bd.atitus","w")
            arquivo.close()
            aguarde(1)
    else:
        print("Opção Inválida!")
        aguarde(2)

                
    








