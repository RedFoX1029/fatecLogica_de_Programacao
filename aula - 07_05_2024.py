agenda = []

def cadastrar_contato():
    while True:        
        pessoa = []
        nome = input('Digite o nome da pessoa(0 - Para finalizar): ')
        if nome == '0':
            break
        telefone = input('Digite o telefone da pessoa: ')
        email = input('Digite o email da pessoa: ')
        pessoa.append(nome)
        pessoa.append(telefone)
        pessoa.append(email)
        agenda.append(pessoa)
        print('Contato cadastrado com sucesso! ')

def listar_todos_contatos():
    print('Lista de Contatos: ')
    for i, contato in enumerate(agenda):
        print(f'{i + 1}.    Nome: {contato[0]},    Telefone: {contato[1]},    E-mail: {contato[2]}')

def consultar_contato_por_nome():
    nome_procurado = input('Digite o nome da pessoa que deseja buscar: ')
    for contato in agenda:
        if contato[0].lower() == nome_procurado.lower():
            print('Contato encontrado: ')
            print('Nome: ', contato[0])
            print('Telefone: ', contato[1])
            print('E-mail: ', contato[2])
            return
    print('Contato não encontrado.')

def remover_contato():
    nome_procurado = input('Digite o nome da pessoa que deseja remover: ')
    for contato in agenda:
        if contato[0].lower() == nome_procurado.lower():
            agenda.remove(contato)
            print('Contato removido com sucesso.')
            return
    print('Contato não encontrado.')

def atualizar_contato():
    nome_procurado = input('Digite o nome da pessoa que deseja atualizar: ')
    for contato in agenda:
        if contato[0].lower() == nome_procurado.lower():
            novo_telefone = input('Digite o novo telefone: ')
            novo_email = input('Digite o novo email: ')
            contato[1] = novo_telefone
            contato[2] = novo_email
            print('Contato atualizado com sucesso.')
            return
    print('Contato não encontrado.')

def gravar_agenda_em_arquivo(agenda):
    with open("agenda_contatos.txt", "w") as arquivo:
        for contato in agenda:
            arquivo.write(f"Nome: {contato[0]}\n")
            arquivo.write(f"Telefone: {contato[1]}\n")
            arquivo.write(f"E-mail: {contato[2]}\n")
            arquivo.write("--------------------\n")

    print("Agenda de contatos gravada no arquivo 'agenda_contatos.txt'.")

def carregar_agenda_do_arquivo(agenda):
    agenda = []
    with open("agenda_contatos.txt", "r") as arquivo:
        for contato in agenda:
            arquivo.read(f"Nome: {contato[0]}\n")
            arquivo.read(f"Telefone: {contato[1]}\n")
            arquivo.read(f"E-mail: {contato[2]}\n")
            arquivo.read("--------------------\n")

while True:
    print('\nMenu')
    print('1. Cadastrar contato')
    print('2. Listar todos os contatos')
    print('3. Consultar contato por nome')
    print('4. Remover contato')
    print('5. Atualizar contato')
    print('6. Gravar arquivo')
    print('7. Carregar arquivo')
    print('8. Sair')

    opcao = input('\nEscolha uma opção: ')

    if opcao == '1':
        cadastrar_contato()
    elif opcao == '2':
        listar_todos_contatos()
    elif opcao == '3':
        consultar_contato_por_nome()
    elif opcao == '4':
        remover_contato()
    elif opcao == '5':
        atualizar_contato()
    elif opcao == '6':
        gravar_agenda_em_arquivo(agenda)
    elif opcao == '7':
        carregar_agenda_do_arquivo(agenda)
    elif opcao == '8':
        break